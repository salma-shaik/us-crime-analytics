* setting up work directory to read, write files

libname salma 'C:\Users\sshaik2\projects\us-crime-analytics';
run;


* import Final_Main_Var_1990_2001 file
proc import datafile = "C:\Users\sshaik2\projects\us-crime-analytics\data\Final_Main_Var_1990_2001.csv"
out = fnl_main_90_01
dbms = csv
replace;
run;


* import ucr crime file Crime_National_UCR_offenses_1960_2015.csv
proc import datafile = "C:\Users\sshaik2\projects\us-crime-analytics\data\Crime_National_UCR_offenses_1960_2015.csv"
out = cr_ucr_60_15
dbms = csv
replace;
run;
