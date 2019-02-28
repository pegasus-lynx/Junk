#include<stdio.h>
#include<pthread.h>
#include<time.h>
#include<stdlib.h>
#define BUFFER_SIZE 10
#define THRDS 5

#define MUTEX 0
#define EMPTY 1
#define FULL  2

int no_buf = BUFFER_SIZE;
int semaphores[3] = { 1, BUFFER_SIZE, 0};
int buffer[BUFFER_SIZE]; 
int cnt =0;

void init(){
	for(int i=0;i<BUFFER_SIZE;i++) buffer[i]=0;
}

void print(){
	for(int i=0;i<BUFFER_SIZE;i++){ printf("%d ", buffer[i]);}
	printf("\n");
}

void print_semaphores(){
	printf("E %d F %d\n", semaphores[1], semaphores[2]);
	// fflush( stdout );
}

void _wait(int ind){
	while(semaphores[ind]<=0) ;
	semaphores[ind]--;
}

void _signal(int ind){
	semaphores[ind]++;
}

void* consumer_process(void* iter){
	int i = (int)iter;
	do{
		_wait(MUTEX);
		_wait(FULL);
		buffer[semaphores[EMPTY]] = 0;
		printf("%d Consuming %d\n",i, semaphores[EMPTY]);
		_signal(EMPTY);
		_signal(MUTEX);
	}while(--i);
}

void* producer_process(void* iter){
	int  i= (int)iter;
	do{
		_wait(MUTEX);
		_wait(EMPTY);
		printf("%d Producing %d\n",i, semaphores[EMPTY]);
		buffer[semaphores[EMPTY]] = 1;
		_signal(FULL);
		_signal(MUTEX);
	}while(--i);
}

int main(){
	init();

	// Creating threads:
	pthread_t threads[THRDS];
	pthread_attr_t attr;
	pthread_attr_init(&attr);
	pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);

	int process_type[THRDS];
	int iters[THRDS];
	
	printf("Enter the process type for %d threads: ", THRDS);
	for(int i=0;i<THRDS;i++){
		scanf("%d", &process_type[i]);
	}

	printf("Enter the  number of buffers each process will produce/consume: ");
	for(int i=0;i<THRDS;i++){
		scanf("%d", &iters[i]);
	}

	int stat;
	for(int i=0;i<THRDS;i++){
		if(process_type[i]){
			stat = pthread_create(&threads[i], NULL, producer_process, (void*)iters[i]);
		}
		else{
			stat = pthread_create(&threads[i], NULL, consumer_process, (void*)iters[i]);
		}
		if(stat!=0) printf("Thread %d not created.\n", i);
	}

	//Joining threads
	for(int i=0;i<THRDS;i++){
		pthread_join(threads[i], NULL);
	}

	return 0;
}