import java.io.*;
import java.util.*;

public class Lagrange
{
	public static void main(String[] args)
	{
		double suma = 0;
		double mnozenia = 1;
		int szukana = 1;
		
		ArrayList<Double> X = new ArrayList<>();
		ArrayList<Double> Y = new ArrayList<>();
		
		X.add(-4.0);
		X.add(-2.0);
		X.add(0.0);
		X.add(2.0);
		X.add(4.0);
		
		Y.add(354.0);
		Y.add(24.0);
		Y.add(-2.0);
		Y.add(-12.0);
		Y.add(90.0);
		
		for(int i = 0; i < X.size(); i++)
		{
			
			for(int j = 0; j < Y.size(); j++)
			{
				if(i!=j)
				{
					mnozenia *= (szukana - X.get(j))/(X.get(i) - X.get(j));
				}
			}
			suma += Y.get(i)*mnozenia;
			mnozenia = 1;
		}
		
		System.out.println(suma);
	}
}
