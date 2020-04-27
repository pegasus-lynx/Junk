#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define TOKEN_BUFFER_SIZE 32

// Function Declarations for builtin shell commands:
int dksh_cd(char **args);
int dksh_help(char **args);
int dksh_exit(char **args);

// Configurations
const char *FILE_HISTORY = "/home/phoenix/Documents/Sem-4/Assignments/OS/Shell/hist";
const char *TOKEN_DELIMS = " \t\n\r\a";
const char *BUILTIN_COMMANDS[] = {
	"cd", "exit", "help"
};
const int (*BUILTIN_FUNCTIONS[]) (char **) = {
	&dksh_cd, &dksh_exit, &dksh_help
};

// Helper methods
int BUILTIN_COMMANDS_LENGTH() {
	return sizeof(BUILTIN_COMMANDS) / sizeof(BUILTIN_COMMANDS[0]);
}

char *readline() {
	ssize_t size = 0;
	char *line = NULL;
	getline(&line, &size, stdin);
	return line;
}

char **splitline(char *line) {
	int bufsize = TOKEN_BUFFER_SIZE, pos = 0;
	char **split = (char **)malloc(sizeof(char *) * bufsize);
	char *token;

	token = strtok(line, TOKEN_DELIMS);
	while (token != NULL) {
		split[pos++] = token;

		if (pos >= bufsize) {
			bufsize += TOKEN_BUFFER_SIZE;
			split = realloc(split, bufsize * sizeof(char *));
		}

		token = strtok(NULL, TOKEN_DELIMS);
	}
	split[pos] = NULL;
	return split;
}

// Shell lifecycle
void initialize() {
	printf("Welcome to DK's Shell.\n");
}

void updateHistory(char *line) {
	FILE *file = fopen(FILE_HISTORY, "a+");
	fprintf(file, "%s", line);
	fclose(file);
}

int launch(char **args) {
	pid_t pid, wpid;
	int status;

	pid = fork();
	if (pid == 0) {
		// Child process.
		if (execvp(args[0], args) == -1)
			perror("dksh");
	} else if (pid < 0) {
		perror("dksh");
	} else {
		// Parent process
		do {
			wpid = waitpid(pid, &status, WUNTRACED);
		} while (!WIFEXITED(status) && !WIFSIGNALED(status));
	}
	return 1;
}

int execute(char **args) {
	int i;
	if (args[0] == NULL)
		return 1;

	for (i = 0; i < BUILTIN_COMMANDS_LENGTH(); i++) {
		if (strcmp(args[0], BUILTIN_COMMANDS[i]) == 0)
			return (*BUILTIN_FUNCTIONS[i])(args);
	}
	return launch(args);
}

void repl() {
	char *line;
	char **args;
	int status;

	do {
		printf("-> ");
		line = readline();
		updateHistory(line);

		args = splitline(line);

		status = execute(args);

		free(line);
		free(args);

	} while (status);
}

// Builtin commands
int dksh_exit(char **args) {
	return 0;
}

int dksh_help(char **args) {
	printf("this is help.\n");
	return 1;
}

int dksh_cd(char **args) {
	if (args[1] == NULL)
		fprintf(stderr, "dksh: Expected argument to \"cd\"\n");
	else {
		if (chdir(args[1]) != 0)
			perror("dksh");
	}
	return 1;
}


int main(int argc, char const *argv[]) {
	initialize();

	repl();

	return 0;
}
