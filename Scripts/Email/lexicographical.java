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
    public static int stringCompare(String str1, 
                                    String str2) 
    { 
        for (int i = 0; i < str1.length() &&  
                    i < str2.length(); i++) { 
            if ((int)str1.charAt(i) ==  
                (int)str2.charAt(i)) { 
                continue; 
            }  
            else { 
                return (int)str1.charAt(i) -  
                    (int)str2.charAt(i); 
            } 
        } 
  
        // Edge case for strings like 
        // String 1="Geeky" and String 2="Geekyguy" 
        if (str1.length() < str2.length()) { 
            return (str1.length()-str2.length()); 
        }  
        else if (str1.length() > str2.length()) { 
            return (str1.length()-str2.length()); 
        } 
          
        // If none of the above conditions is true, 
        // it implies both the strings are equal 
        else { 
            return 0; 
        } 
    } 
    
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.print("Enter a string : ");
        Scanner s1 = new Scanner(System. in);
        String s = s1. next();
        System.out.print("Enter another string : ");
        Scanner s2 = new Scanner(System. in);
        String p = s2. next();
        System.out.println(stringCompare(s,p));
    }
    
}
