#include "menu.h"

void printMenu(AndroidComm& And, UbuntuComm& Ubu) {
  And.print("--> Piksi Integration Software\n"
    "1. Run Console\n"
    "2. Choose CSV to read\n"
    "3. Delete all CSV files\n"
    "4. Start Streamming\n"
    "9. Reset Python Code\n"
    "0. Shut down ODROID\n");

  menuEngine(And, Ubu); 
}

void clearBuffer(UbuntuComm& Ubu) {
    String msg = Ubu.readString();
    while(!((msg = Ubu.readString()) == NULL));  
}

void menuEngine(AndroidComm& And, UbuntuComm& Ubu) {
  int opt;
  String msg = NULL;

  while(msg == NULL) {
    while((msg = And.readString()) == NULL);
    if(msg.equals("menu")) printMenu(And, Ubu);
    char myChar = msg[0];

    if(isDigit(myChar)) {
      opt = msg.toInt();
      String chosenFile[2];
      
      switch(opt) {
        case 1:
          clearBuffer(Ubu);
          Ubu.print(String(opt));
          And.println("Console running...");
          clearBuffer(Ubu);
          And.println("-----------------------------");         
          break;          
        
        case 2:
          clearBuffer(Ubu);
          Ubu.print(String(opt));
          getChosenFile(chosenFile, And, Ubu);
          Ubu.print(chosenFile[0]);
          Ubu.print(chosenFile[1]);            
          And.println("-----------------------------");         
          break;
          
        case 3:
          clearBuffer(Ubu);
          Ubu.print(String(opt));
          And.println("Deleting CSV files...");
          And.println("-----------------------------");
          break;
  
        case 4:
          clearBuffer(Ubu);
          Ubu.print(String(opt));
          while((msg = Ubu.readString()) == NULL);
          if(msg == "false") And.println("No file has been opened yet.");
          else if(msg == "true") {
            And.println("Starting to stream... type in 'stop'.");
            while(!((And.readString()) == "stop")) {
              msg = Ubu.readString();
              if(msg != NULL) And.println(msg);
            };
            Ubu.print("stop");
            And.println("-----------------------------");
            printMenu(And, Ubu);
          }
          break;
          
        case 9:
          clearBuffer(Ubu);
          Ubu.print(String(opt));
          And.println("---------------------------------");
          And.println("|   Resetting Python Code   |");
          And.println("---------------------------------");
          menuEngine(And, Ubu);
          break;
          
        case 0:
          Ubu.print(String(opt));
          And.println("---------------------------------");
          And.println("|   Shutting down Odroid    |");
          And.println("---------------------------------");
          menuEngine(And, Ubu);
          break;
  
        default:
          And.println("Invalid option! Try again.");
          msg = NULL;  
      }      
    } else {
      msg = NULL;
      And.println("Invalid option! Try again.");
    }  
  }
}

void getChosenFile(String files[2], AndroidComm& And, UbuntuComm& Ubu) {
  int nFiles;
  String msg = NULL;

  // Receiving number of files 
  while(msg == NULL) msg = Ubu.readString();
  if(!(nFiles = msg.toInt())) {
    And.println("No CSV files found.");
    And.println("---------------------------------");
    menuEngine(And, Ubu);
  }

  And.println("----------------- File list");

  // Gets file names from Python
  String fileNames[nFiles];
  for(int i=0; i < nFiles; i++) {
    while((fileNames[i] = Ubu.readString()) == NULL);
    And.println(fileNames[i]);
  }

  // Gets chosen file and send it to Python
  int fChoice[2];
  int fileChoice[2];
  for(int j=0; j<2; j++) {
    if(j==0) And.print("Choose your baseline file: ");
    else if(j==1) And.print("Choose your position file: ");   

    msg = NULL;
    while((msg = And.readString()) == NULL);

    if(!(fileChoice[j] = msg.toInt()) && msg.toInt() != 0) printMenu(And, Ubu);

    if(fileChoice[j] > nFiles || fileChoice[j] < 0) {
      And.println("Invalid file number.");
      printMenu(And, Ubu);
    }
  }

  if(fileChoice[0] != 0 || fileChoice[0] != 0) And.println("Files successfully chosen.\n");
  
  if(fileChoice[0] != 0) files[0] = fileNames[fileChoice[0]-1];
  else files[0] = "0";
  
  if(fileChoice[1] != 0) files[1] = fileNames[fileChoice[1]-1];  
  else files[1] = "0";
}



