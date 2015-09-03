#include "menu.h"

void printMenu(AndroidComm& And, UbuntuComm& Ubu) {
  And.print("--> Piksi Integration Software\n"
    "1. Run Console\n"
    "2. Choose CSV to read\n"
    "3. Delete all CSV files\n"
    "4. Start Streamming\n"
    "5. Save a spot\n"
    "6. Delete spots files\n"
    "7. Toggle manual/automatic\n"
    "9. Reset Python Code\n"
    "0. Shut down ODROID\n");

  menuEngine(And, Ubu); 
}

void clearBuffer(UbuntuComm& Ubu) {
    String msg = Ubu.readString();
    while(!((msg = Ubu.readString()) == NULL));  
}

void menuEngine(AndroidComm& And, UbuntuComm& Ubu) {
  String msg = NULL;
  String chosenFile[2];

  if((msg = And.readString()) != NULL) {   
    if(msg.length() == 1) {
      char opt = msg[0];
          
      // Opens Piksi Console - .../ODG_Rover/piksi_tools
      if(msg.equals("1")) {
        clearBuffer(Ubu); // Clears buffer (from Odroid to Arduino)
        Ubu.print(String(opt)); // Sends instruction to Odroid/Ubuntu
        while((msg = Ubu.readString()) == NULL);
        if(msg == "true") {
          And.println("Console running..."); // Prints to the Android
          And.println("-----------------------------");         
        } else if(msg == "false") {
          And.println("Wrong USB port!");
          And.println("-----------------------------");         
        }
      }         
      
      // Chooses CSV log files
      else if(msg.equals("2")) {
        clearBuffer(Ubu);
        Ubu.print(String(opt));
        if(!(getChosenFile(chosenFile, And, Ubu))) return;
        Ubu.print(chosenFile[0]);
        Ubu.print(chosenFile[1]);            
        And.println("-----------------------------");         
      }
       
      // Deletes all CSV files 
      else if(msg.equals("3")) {
        clearBuffer(Ubu);
        Ubu.print(String(opt));
        And.println("Deleting CSV files...");
        And.println("-----------------------------");
      }
      
      // Streams CSV files
      else if(msg.equals("4")) {
        clearBuffer(Ubu);
        Ubu.print(String(opt));
        while((msg = Ubu.readString()) == NULL);
        if(msg == "false") {
          And.println("No CSV file has been opened yet.");
          And.println("-----------------------------");
        }
        else if(msg == "true") {
          And.println("Starting to stream... type in 'stop'.");
          while(!((And.readString()) == "stop")) {
            msg = Ubu.readString();
            if(msg != NULL) And.println(msg);
          };
          Ubu.print("stop");
          And.println("-----------------------------");
        }
      }
      
      // Saves the current spot to a file  
      else if(msg.equals("5")) {
        clearBuffer(Ubu);
        Ubu.print(String(opt));
        while((msg = Ubu.readString()) == NULL);
        if(msg == "false") { 
          And.println("No CSV file has been opened yet.");          
          And.println("-----------------------------");
        }
        else if(msg == "true") {
          And.println("Spot has been saved.");
          And.println("-----------------------------");            
        }
      }
      
      else if(msg.equals("6")) {
        clearBuffer(Ubu);
        Ubu.print(String(opt));
        while((msg = Ubu.readString()) == NULL);
        if(msg == "true") {
          And.println("Files have been deleted.");
          And.println("-----------------------------");
        } else {
          And.println("No file has been deleted.");
          And.println("-----------------------------");
        } 
      }
      
      else if(msg.equals("7")) {
        clearBuffer(Ubu);
        Ubu.print(String(opt)); 
        if(And._RC == 1) {              
          while((msg = Ubu.readString()) == NULL);          
          if(msg == "true") {
            And._RC = 0;            
            And.println("Robot set to automatic drive.");
            And.println("-----------------------------");           
          } else {
            And.println("No spot has been saved yet.");
            And.println("-----------------------------");                       
          }
        } else {
          And._RC = 1;          
          And.println("Robot set to manual drive.");
          And.println("-----------------------------");                   
        }
      }
      
      // Stops code. It will be reset by ODG_Rover_Python/startup_code.py  
      else if(msg.equals("9")) {
        Ubu.print(String(opt));
        And.println("---------------------------------");
        And.println("|   Resetting Python Code   |");
        And.println("---------------------------------");
        while((msg = Ubu.readString()) == NULL);
      }
      
      // Shutdown Odroid  
      else if(msg.equals("0")) {
        Ubu.print(String(opt));
        And.println("---------------------------------");
        And.println("|   Shutting down Odroid    |");
        And.println("---------------------------------");
      }
      
      else { 
        And.println("Invalid input.");
        And.println("-----------------------------");
      }
    } else {
      // For more than 1 character input
      if(msg.equals("menu")) {
        And.println("-----------------------------");
        printMenu(And, Ubu);
      } else {            
        And.println("Invalid input.");
        And.println("-----------------------------");       
      }
    }
  }
}

int getChosenFile(String files[2], AndroidComm& And, UbuntuComm& Ubu) {
  int nFiles;
  String msg = NULL;

  // Receiving number of files 
  while(msg == NULL) msg = Ubu.readString();
  if(!(nFiles = msg.toInt())) {
    And.println("No CSV files found.");
    And.println("---------------------------------");
    return 0;
  }

  And.println("- File list (type in file number):");

  // Gets file names from Python and prints to Android
  String fileNames[nFiles];
  And.println("0None");
  for(int i=0; i < nFiles; i++) {
    while((fileNames[i] = Ubu.readString()) == NULL);
    String temp = String(i+1) + fileNames[i];
    And.println(temp);
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
      And.println("---------------------------------");
      return 0;
    }
  }

  if(fileChoice[0] != 0 || fileChoice[0] != 0) And.println("Files successfully chosen.\n");
  
  if(fileChoice[0] != 0) files[0] = fileNames[fileChoice[0]-1];
  else files[0] = "0";
  
  if(fileChoice[1] != 0) files[1] = fileNames[fileChoice[1]-1];  
  else files[1] = "0";
  
  return 1;
}



