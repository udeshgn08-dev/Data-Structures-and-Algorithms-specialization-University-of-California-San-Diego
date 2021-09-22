/**
* To determine leap year: 
* if the year evenly divisible by 4, go to step 2. Otherwise, go to step 5 
* if the year evenly divisible by 100, got to step 3. Otherwise, got to step 4 
* if the year evenly divisible by 400, go to step 4. Otherwise, go to step 5
* The year is a leap year. It has 366 days 
* The year is not a leap year. It has 365 days 
* Condition 1: The year should be divisible by 4 
* Condition 2: The year divisible by 100 should also be divisible by 400 
* Year that does meet both the conditions,is a leap year. 
* Year that does not meet any of the two conditions,it is not a leap year 
*/

public class LeapYear { 
   
      static boolean determineYear(int year) {
          if (((year % 4 == 0) && (year % 100 != 0)) || (year%400 == 0))
         return true; 
        return false;
      }
     public static void main(String[] args) { 
      
          int argYear = Integer.parseInt(args[0]); 
          System.out.println(determineYear(argYear)? "The year is a leap year,it has 366 days " : "The year is not a leap year,it has 365 days");
     }
     
     }

 
