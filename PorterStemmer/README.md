# Porter Stemmer for Hindi

The assignment is to make a porter stemmer for hindi language.
Now similar to porter stemmer algorithm we will strip the word at different stages to get the root word. 

For more details on porter stemmer algorithm : [https://tartarus.org/martin/PorterStemmer/def.txt]

## Steps followed for stemming the text:

At first we break the lines of text into words, then we process each word one by one. For processing each word we remove suffiexes from the word and then we remove prefixes from the word only when the measure of the word is at least 2 more then the measure of the prefix. After removing prefixes we remove the `matras` from the words if they are left after removal of the prefix.


 