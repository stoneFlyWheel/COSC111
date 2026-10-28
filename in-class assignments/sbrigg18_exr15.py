def build_word_counts(text):
    #1) set up a blank dictionary
    
    #2) split text into words (this will be a list because the split() method returns a list

   #3) using a for loop, go through the words list
          #a) convert each word to lower-case (so "Cat" and "cat" get counted as the same term) - use the lower() method
          #b) remove punctuation - (".,!?;:\"'()") -  using the strip() method

          #c) if word is in counts (the dictionary we're building): counts[word] = counts[word] +1
          # otherwise: counts[word] =1

   #4) after the for loop is done running, don't forget to return counts - this will enable the driver code to print out top 10 terms
 



# ----- Driver code (no need to modify)  -----

infile = open("input.txt", "r")
text = infile.read()
infile.close()

word_counts = build_word_counts(text)

# Sort the (word, count) pairs by count, highest first
sorted_counts = sorted(word_counts.items(), key=lambda pair: pair[1],reverse=True)

print("Top 10 most common words:")
for word, count in sorted_counts[:10]:
    print(word, ":", count)