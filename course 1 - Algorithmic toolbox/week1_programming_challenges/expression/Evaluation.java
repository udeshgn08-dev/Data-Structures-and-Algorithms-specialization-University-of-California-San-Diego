
/**
 * Evaluation 
 * @see oracle 
 * @see order of precendence
 */
public class Evaluation
{
    public static void main(String[] args) { 
       int a = 9, b = 6, c = -3, d = 4, x = 2, y = 5; 
       System.out.print("Expression1: ");
       System.out.println(a+b-c*d/x%y); 
       // 12 / 2 % 5 = 1 + 9 + 6 = 16 
       System.out.print("Expression2: ");
       /* 12 + 6 / 5 % 2 + 9 = 22 
        */
       System.out.print(a-(c*d)+(b/y%x)+ "," +(a-c*d+b/y%x));
    }
}
