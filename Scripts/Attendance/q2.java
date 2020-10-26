/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package q2;

import java.util.Scanner;
import java.util.Vector;

public class Q2 {
    public static void main(String[] args) throws java.lang.Exception
    {
        Scanner sc=new Scanner(System.in);
         Vector vec=new Vector();
         /*vec.add("pollution");
         vec.add("environment");
         vec.add("human");*/
         int n;
         System.out.println("Enter the number of words : ");
         n=sc.nextInt();
         System.out.println("Enter "+n+" words : ");
         sc.nextLine();
         for(int i=0 ; i<n ; i++)
         {
             String s=new String();
             s=sc.next();
             vec.add(s);
         }
         sc.nextLine();
         String str=new String();
         System.out.println("Enter a paragraph :");
         
         str=sc.nextLine();
         String s=new String();
         System.out.println("Solution paragraph :");
         for(int i=0 ; i<str.length() ; i++)
         {
             if(str.charAt(i)!=' ' && str.charAt(i)!='.')
             {
                 s=s+str.charAt(i);
             }
             else
             {
                 if(vec.contains(s))
                 {
                     System.out.print(s.charAt(0));
                     for(int j=0 ; j<s.length()-1 ; j++)
                         System.out.print("*");
                     System.out.print(str.charAt(i));
                 }
                 else System.out.print(s+str.charAt(i));
                 
                 s="";
             }
         }
         if(vec.contains(s))
        {
            System.out.print(s.charAt(0));
            for(int j=0 ; j<s.length()-1 ; j++)
                System.out.print("*");
            System.out.print("\n");
        }
        else System.out.println(s);
        
         
    }
}
// Example Paragraph // pollution is caused by human being. it is bad for environment. human should stop pollution.
// Solution // p******** is caused by h**** being. it is bad for e**********. h**** should stop p********.