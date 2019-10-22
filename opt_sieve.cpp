// C++ program to generate all prime numbers less than N in O(N).

#include<bits/stdc++.h>
#define ll long long 

using namespace std; 
const ll MAX_SIZE = 10000001; 

// isPrime[] : isPrime[i] is true if number is prime 
// prime[] : stores all prime number less than N 
// SPF[] : stores the smallest prime factor of a number 

vector<ll> isprime(MAX_SIZE , true); 
vector<ll> prime; 
vector<ll> SPF(MAX_SIZE); 

// Function to generate all prime numbers less than N in O(n).
void optimized_sieve(ll N) 
{ 
	isprime[0] = isprime[1] = false ; 
	
	for (ll i=2; i<N ; i++) 
	{ 
		if (isprime[i]) 
		{ 
			prime.push_back(i); 
			SPF[i] = i; 
		} 

		// Remove all multiples of i*prime[j] which are not prime by making isPrime[i*prime[j]] = false 
		// and put smallest prime factor of i*Prime[j] as prime[j].
		// [ for example :let i = 5 , j = 0 , prime[j] = 2 [ i*prime[j] = 10 ] 
		// so smallest prime factor of '10' is '2' that is prime[j] ] 
		// This loop runs only once for numbers which are not prime.
		for (ll j=0; j < (ll)prime.size() && i*prime[j] < N && prime[j] <= SPF[i]; j++) 
		{ 
			isprime[i*prime[j]]=false; 

			// put smallest prime factor of i*prime[j] 
			SPF[i*prime[j]] = prime[j] ; 
		} 
	} 
} 

// driver program to test above function 
int main() 
{ 
	ll N = 1e4 ; // Must be less than MAX_SIZE 
	//cin>>N;
	optimized_sieve(N); 

	// Print all prime number less then N.
	for (ll i=0; i<prime.size() && prime[i] <= N ; i++) 
		cout << prime[i] << " "; 

	return 0; 
} 

