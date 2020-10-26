/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package q1;
import java.util.*; 
/**
 *
 * @author Bhavya Malhotra
 */
public class Q1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.print("Enter a string : ");
        Scanner s1 = new Scanner(System. in);
        String s = s1. next();
        System.out.print("Enter a substring : ");
        Scanner s2 = new Scanner(System. in);
        String p = s2. next();
        
        List<Integer> indexes = new ArrayList<>();
	if(s.isEmpty() || p.length()>s.length()) 
            System.out.println("Substring doesn't exist in string");
        else
        {
	Map<Character,Integer> pHash = new HashMap<>();
	for(char c: p.toCharArray()) {
		if(pHash.containsKey(c)) {
			pHash.put(c, pHash.get(c)+1);
		} else {
			pHash.put(c, 1);
		}
	}
	
	int numberOfCharsToBeZero = pHash.keySet().size();
	
	for(int i=0;i<p.length();i++) {
		char c = s.charAt(i);
		if(pHash.containsKey(c)) {
			int value = pHash.get(c)-1;
			pHash.put(c, value);
			if(value==0) numberOfCharsToBeZero--;
		}
	}
	if(numberOfCharsToBeZero==0) indexes.add(0);
	int start=0;
	int end=p.length()-1;
	while(end<s.length()-1) {
		char startChar = s.charAt(start++);
		char endChar = s.charAt(++end);
		if(pHash.containsKey(startChar)) {
			if(pHash.get(startChar)==0) numberOfCharsToBeZero++;
			pHash.put(startChar, pHash.get(startChar)+1);
		}
		if(pHash.containsKey(endChar)) {
			pHash.put(endChar, pHash.get(endChar)-1);
			if(pHash.get(endChar)==0) numberOfCharsToBeZero--;
		}
		if(numberOfCharsToBeZero==0) indexes.add(start);
	}
	
        System.out.println(indexes.size());
        }
    }
    
}
