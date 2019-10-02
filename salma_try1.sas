libname salma 'C:\Users\sshaik2\projects\criminal_justice\us-crime-analytics';run;

data temp;
set Old_crime_90_01;
*where year < 1994;
run;

proc means sum data=temp (where = (fips_state = 6));
var robbery_sum;
class year;
run;

/*proc import datafile="C:\Users\sshaik2\projects\criminal_justice\us-crime-analytics\data\crime\Crime_National_UCR_offenses_1960_2015.csv"
     out=cr_ucr_60_15
     dbms=csv
     replace;
run;
*/
data updated_cr_60_15;
set cr_ucr_60_15;
ori = ori_code;
drop division;
run;


proc sort data = temp; by ori year; run;
proc sort data = updated_cr_60_15; by ori year; run;

data combo_temp_new;
merge temp(in=a) updated_cr_60_15(in=b); by ori year;
if a and b;
run;

data robbery_diff;
set combo_temp_new;
rob_diff = robbery_sum - robbery;
*if year = 1993;
keep ori year population govt_level VIOLENT_SUM agg_assault_sum murder_sum rape_sum robbery_sum simple_assault_sum 
murder robbery rape aggravated_assault simple_assault rob_diff;
run;

proc sort data = robbery_diff; by rob_diff; run;

data salma.crime_outliers;
set robbery_diff;
where rob_diff < -1;
run;

proc freq data = crime_outliers;
tables year;
run;
