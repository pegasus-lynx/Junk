package q3;
import java.util.*; 
public class Q3
{
	static class Graph
	{
		public int v;
		public int[][] adj=new int[15][15];
		
		public Graph(int x)
		{
			this.v=x;
			for(int i=0;i<x;i++)
				for(int j=0;j<x;j++)
					adj[i][j]=Integer.MAX_VALUE;
				
		}
		
	}
	public static void depth_first(Graph g,int s,int d,String str)
	{
		str=str+Integer.toString(s);
		if(s==d)
			System.out.println(str);
		for(int j=0;j<g.v;j++)
			if(g.adj[s][j]!=Integer.MAX_VALUE)
				{
					g.adj[s][j]=Integer.MAX_VALUE;
					depth_first(g,j,d,str);
				}
			return;
		
	}
	public static void bellman_ford(Graph g,int s,int d)
	{
		int []dist=new int[g.v];
		Arrays.fill(dist,Integer.MAX_VALUE);
		dist[s]=0;
		for(int i=1;i<=g.v-1;i++)
		{
			for(int j=0;j<g.v;j++)
				for(int k=0;k<g.v;k++)
				{
					if(dist[j]!=Integer.MAX_VALUE&&g.adj[j][k]!=Integer.MAX_VALUE)
					if(dist[j]+g.adj[j][k]<dist[k])
						dist[k]=dist[j]+g.adj[j][k];
				}
		}
		int x=dist[d];
		for(int j=0;j<g.v;j++)
				for(int k=0;k<g.v;k++)
				{
					if(dist[j]!=Integer.MAX_VALUE&&g.adj[j][k]!=Integer.MAX_VALUE)
					if(dist[j]+g.adj[j][k]<dist[k])
						dist[k]=dist[j]+g.adj[j][k];
				}
				if(x==dist[d])
					{
						System.out.println("No negative cycle");
						System.out.print("Distance across shortest path is ");
						System.out.println(dist[d]);
					}
				else
					System.out.println("Negative cycle exists");
	}
	public static void add_edge(Graph g,int src,int dest,int wt)
	{
		g.adj[src][dest]=wt;
	}

	public static void main(String[] args)
	{
		System.out.println("Enter the number of vertices");
		Scanner sc=new Scanner(System.in);
		int v=sc.nextInt();
		Graph g=new Graph(v);
		System.out.println("Enter the edges as src to dest, first enter source then destination");
		while(true)
		{
			System.out.println("Enter src");
			int src=sc.nextInt();
			System.out.println("Enter dest");
			int dest=sc.nextInt();
			System.out.println("Enter weight");
			int wt=sc.nextInt();
			add_edge(g,src,dest,wt);
			System.out.println("To continue adding edges, press 1 else 0");
			int flag=sc.nextInt();
			if(flag==0)
				break;
			else
				continue;

		}
		System.out.println("Enter the node which is to be taken as source");
		int src=sc.nextInt();
		System.out.println("Enter the node which is to be taken as destination");
		int dest=sc.nextInt();
		bellman_ford(g,src,dest);
		System.out.println("All the paths are");
		depth_first(g,src,dest,"");

	}
}