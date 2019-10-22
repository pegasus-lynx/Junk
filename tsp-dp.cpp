#include<iostream>
using namespace std;

#define int         long long
#define ull 		unsigned long long
#define ll 			long long
#define M 			1000000007
#define pb 			push_back
#define p_q 		priority_queue
#define pii         pair<ll,ll>
#define vi          vector<ll>
#define vii         vector<pii>
#define mi          map<ll,ll>
#define mii         map<pii,ll>
#define all(a)      (a).begin(),(a).end()
#define sz(x)       (ll)x.size()
#define ios	    	ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define lb 			lower_bound
#define ub			upper_bound
#define F           first
#define S           second
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define ini(a,n,b)	for(ll int i=0;i<n;i++) a[i]=0;
#define hell 		(ull)1e9

int dp[15][1<<15],b[15][1<<15],n,v[15][15];
int solve(int cur,int mask)
{

	int &ans=dp[cur][mask];
	if(mask==((1<<n)-1))
	{
		b[cur][mask]=0;
		return ans=v[cur][0];
	}
	if(ans!=-1)
		return ans;
	ans=(ll)1e6+1;
	b[cur][mask]=-1;
	rep(i,0,n)
	{
		if(mask&(1<<i)) continue;
		int nmask=mask|(1<<i);
		int x=solve(i,nmask)+v[cur][i];
		if(x<ans)
			ans=x,b[cur][mask]=i;
	}
	return ans;
}


signed main(void)
{ios
	cin>>n;
	rep(i,0,n)
	rep(j,0,n)
	cin>>v[i][j];
	rep(i,0,15)
	rep(j,0,1<<15)
	dp[i][j]=-1;
	cout<<"Cost = "<<solve(0,1)<<endl;
	int t=0,m=1;
	cout<<"Path : "<<0<<" ";
	while(m!=((1<<n)-1))
	{
		t=b[t][m];
		cout<<t<<" ";
		m|=(1<<t);
	}
	cout<<0;
}
/*
4
0 4 1 3
4 0 2 1
1 2 0 5 
3 1 5 0
*/
