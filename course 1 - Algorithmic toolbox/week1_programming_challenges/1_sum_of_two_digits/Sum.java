/*
 * Arguments to sum three integers values 
 */
public class Sum {

	public static void main(String[] args) {
		// put some code 
		try {
		int a = Integer.parseInt(args[0]),b = Integer.parseInt(args[1]),c = Integer.parseInt(args[2]);
		int add = a + b + c;
		System.out.println("Additive :" + add);
		}
		// catch exception 
		catch(ArrayIndexOutOfBoundsException aib){
			System.err.print("Error  ");
			System.err.println("Argument " +aib.getMessage()+ " is < array of index");
		}
	}
}
