import java.util.*; 
public class Sum { 

    public int computeSum(int sumRes) { 
         return sumRes; 
    }
    public int dividend(int divRes) { 
         return divRes; 
    }
    public static void main(String[] args) {
        try { 
        int valOne, valTwo; 
        int sum; 
        Scanner input = new Scanner(System.in); 
        System.out.println("Enter value one: "); 
        valOne = input.nextInt(); 
        System.out.println("Enter value two: "); 
        valTwo = input.nextInt(); 
        String writeMsg = String.valueOf(args[0]);    
        sum = valOne + valTwo;
        // Algorithmic step: Avoid loss of precision of the value // 
        double divisor = (double)sum/2;  
        // Print sum, division // 
        System.out.println(" "); 
        System.out.println(writeMsg); 
        System.out.println("Sum result: " +sum); 
        System.out.println("Division result: " +divisor); 
        }
        catch(ArrayIndexOutOfBoundsException aiobe) {
          // catch exception lines using method printStackTrace() // 
          aiobe.printStackTrace(); 
          System.out.println("Run program correctly:Message enclose in double quotes"); 
         }
         
    }
    }
