//to compile:
//g++ -I /home/sebasmuro1/verano/pythia8309/include/ higgsv2.cc -o higgsv2 -lpythia8 -L /home/sebasmuro1/verano/pythia8309/lib/
//before runing type where linux should look for the installed libraries:
//export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/sebasmuro1/verano/pythia8309/lib/
#include <iostream>
#include <fstream>
#include <Pythia8/Pythia.h>
#include <Pythia8Plugins/ResonanceDecayFilterHook.h>

using namespace Pythia8;

int main(){
  std::ofstream datafull2;
  std::ofstream dataon2;

  datafull2.open("datafull2.csv");
  datafull2 << "i" << "," << "j" << "," << "id" << "," << "m" << "," << "pabs" << "," << "e" << "\n";
  dataon2.open("dataon2.csv");
  dataon2 << "i" << "," << "j" << "," << "id" << "," << "m" << "," << "px" << "," << "py" << "," << "pz" << "\n";

  int nevents = 15000;
  Pythia pythia;

  auto myUserHooks = make_shared<ResonanceDecayFilterHook>(pythia.settings);
  pythia.setUserHooksPtr( myUserHooks);


  pythia.readString("Beams:idA = 2212");
  pythia.readString("Beams:idB = 2212");
  pythia.readString("Beams:eCM = 13.6e3");
  // pythia.readString("SoftQCD:all = on");
  // pythia.readString("HardQCD:all = on");
  pythia.readString("HiggsSM:all = on");

  pythia.readString("ResonanceDecayFilter:filter = on");
  pythia.readString("ResonanceDecayFilter:exclusive = off");
  pythia.readString("ResonanceDecayFilter:eMuTauAsEquivalent = on");
  pythia.readString("ResonanceDecayFilter:mothers = 25,23");
  pythia.readString("ResonanceDecayFilter:daughters = 23,11");
  pythia.init();

  //iterating over each event
  for(int i = 0; i < nevents; i++){
    if(!pythia.next()) continue;//necessary
    int entries = pythia.event.size();

    std::cout << "Event: " << i << std::endl;
    std::cout << "Event size: " << entries << std::endl;

    //for iterating over each particle in the ith event
    for(int j = 0; j < entries; j++){
      int id = pythia.event[j].id();
      double m = pythia.event[j].m();
      double px = pythia.event[j].px();
      double py = pythia.event[j].py();
      double pz = pythia.event[j].pz();
      double pabs = sqrt(pow(px,2)+pow(py,2)+pow(pz,2));
      double e = pythia.event[j].e();

      // appen all particles
      if(id == 25 or id == 23 or id == 11 or id == -11 or id == 13 or id == -13 or id == 15 or id == -15){
        // std::cout << id << " " << m << " " << pabs << " " << e << std::endl;
        datafull2 << i << "," << j << "," << id << "," << m << "," << pabs << "," << e << "\n";
      }// if close

      // append on-shell particles
      if(id == 11 or id == -11 or id == 13 or id == -13 or id == 15 or id == -15){
        // std::cout << px << " " << py << " " << pz << std::endl;
        dataon2 << i << "," << j << "," << id << "," << m << "," << px << "," << py << "," << pz << "\n";
      }// if close

    }// for j close
  }// for i close


  datafull2.close();
  dataon2.close();
  return 0;
}// main close
