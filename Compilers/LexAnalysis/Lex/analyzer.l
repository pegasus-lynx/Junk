NUM   -?(([0-9]+)|([0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?)
WS   [ \n\t\r]+
KEY  if|else|int|main|void|return
ID   ^[a-zA-Z_][a-zA-Z0-9_]*
OP   \=|\(|\)|\{|\}|\;

%{
	#include<stdio.h>
	#include<math.h>
%}

%%
{NUM} 	{
	printf("NUMBER : %s\n", yytext);
	}

{WS} 	{
	printf("WHITESPACE\n");
	}

{KEY} 	{
	printf("KEYWORD : %s\n", yytext);
	}

{ID}  	{
	printf("IDENTIFIER : %s\n", yytext);
	}

{OP}  	{
	printf("OPERATOR : %s\n", yytext);
	}
%%

int yywrap() {
	return 1;
}

int main()
{
	yylex();
}
