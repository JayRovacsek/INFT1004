###  Programmer : Jay Rovacsek & Aaron Smith
###  Date: 12 April - 25 May
###  This program should be able to parse a text file in a list, 
###  remove punctuation that is not valid and create a list and frequency count
###  of these words which then paints a very simple graph with all words 
###  which scales the bar to show the frequencies.
###  Use case of this program is:
###  >>> readAndPlot(fileStub, widthVertical, widthHorizontal, heightHorizontal)

def readAndPlot(fileStub, widthVertical, widthHorizontal, heightHorizontal): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      ### Top-level function: read the text, do the vertical plot,
      ### read the keywords, and do the horizontal plot.
      ### This complete function was provided with the assignment specification.
      
      ### ---------- TASK 2 ----- (Part 1) ---------------------------------------------
      ### Read the text file and form the list of words and frequencies
      frequencyList = readText(getMediaPath(fileStub + ".txt"))
       
      ### ---------- TASK 2 ----- (Part 1) ---------------------------------------------
      ### Make a vertical plot, widthVertical pixels wide, of the frequency list, and explore it
      verticalPlot = plotVertical(frequencyList, widthVertical)
      #explore(verticalPlot)
  
      ### ---------- TASK 3 ----- (Part 2) ---------------------------------------------
      ### Read the keywords into their own list
      keywords = readKeywords(getMediaPath(fileStub + "Keywords.txt"))
  
      ### ---------- TASK 4 ----- (Part 2) ---------------------------------------------
      ### Get the frequencies of the keywords from the full frequency list
      keywordFrequencies = calculateFrequencies(keywords, frequencyList)
      
      ### ---------- TASK 5 ----- (Part 2) ---------------------------------------------  
      ### Make a horizontal plot, widthHorizontal, heightHorizontal, of the keyword frequencies
      horizontalPlot = plotHorizontal(keywordFrequencies, widthHorizontal, heightHorizontal)
      
      ### Explore the picture and save it, after changing YourName to your own name
      explore(horizontalPlot)
      writePictureTo(horizontalPlot, getMediaPath("AaronSmithJayRovacsek.jpg"))                    # I feel this should have more of a distinct name, say, add the filestub to the name? Alas I will follow the requirements
  
def readText(filename): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      fileContents = open(filename, "r")                     # Open the file
      listA = []                                             # Create some empty lists 
      listB = []                                             # Create some empty lists 
      freqList = []                                          # More empty lists for other uses
      fileContents.close                                     # Close the file
  
      removeNewLine(listA,fileContents)                      # Remove new line chars, pass a list and the filefoutput to make a rough list. (OUTPUT listA)

      listCleanup(listA,listB)                               # Remove characters that will never exist within the English language as a feature of a word other than gramatically by default ---- ( Exclaimation marks, Questions marks, Periods, Quotation marks etc)
                                                             # Also perform actions that test for single char entries and/or small exceptions that may slip through if a hyphen exists, which still may exist within a word validly in the English language.
      frequencyList = listFrequencyCount(listB,freqList)     # Take the now formatted list of words, sort it, kill duplicates and append the required frequency counts that are suggested in the assignment outline including the list-in-list structure style. 

      return frequencyList
  
def removeNewLine(listA,fileContents): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
      for line in fileContents:                                    # I really have to give you credit for this snippet Keith, as outlined in Lecture code from week 6; function: readPrintFile() which was the best way I could find to remove the annoying '\n'
            words = line.split()                                   # We split the line of text to now have multiple entries inside a list
            for word in words:                                     # Iterate through the entries in that list
                  characters = len(word)                           # Figure the length of the word entries in the list so we can look at the n-1 char
                  if word[characters-1] == "\n":                   # If the char is \n let's nuke it
                        removedNewline =  line[0:characters-1]     # Nuke successful
                  else:                                            # If it isn't the \n we hate so much
                        removedNewline =  line[0:characters]       # We shall leave it in peace
                        listA.append(word)                         # Append the good entry to the list (Yet to be cleaned properly)

def listCleanup(listA,listB): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
      for i in range(0,len(listA)):                                # Check all entries created earlier
            if listA[i].isalpha():                                 # If the entry isalpha, add it to the new list after moving it to lover case.
                  tempA = listA[i].lower()
                  listB.append(tempA)
            elif not listA[i].isalpha() and len(listA[i]) > 1:     # If it does not adhere to isaplha == true and it is an entry larger than length 1 let's cull some chars and then check validity
                  tempA = listA[i]
                  tempB = tempA.replace(",","")                    # I know this is uninspiring however I was uncertain of how to replace via any other methods
                  tempA = tempB.replace("?","")                    # I intend on improving this soon to instead look at a list of undesirable chars instead                   
                  tempB = tempA.replace('"',"")                    # that would mean I could extend this code out to cover any char that doesn't naturally occur
                  tempA = tempB.replace("!","")                    # in the English language, as unless I am mistaken the only chars that should be left would
                  tempB = tempA.replace(")","")                    # include the chars of: ' OR -
                  tempA = tempB.replace(".","")                    #
                  tempB = tempA.replace("(","")                    #
                  tempA = tempB.replace(";","")                    #
                  tempB = tempA.replace(":","")                    #
                  tempA = tempB.lower()                            # Create lowercase entries as required by the assignment
                  if len(tempA) != 1:                              # If the entry we just processed is not a single char - typically hyphens without homes, we want to kill it and only append legitimate alpha chars.
                        listB.append(tempA)                        # I tried to find an exception to the logic placed here but couldn't, at-least it didn't seem to exist within the four files HOWEVER something like: "--a" would break this I am pretty certain
                                                                   # Will suggested a function that would seek an entry and find any alpha char to return a true/false logic, however I am yet to code that
        
def listFrequencyCount(listB,freqList): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      words = listB
      i=0                                                          # I used a counter despite knowing when the iteration would cancel but not knowing how to catch it before an out of bounds error
      uniqWords = sorted(set(words))                               # Sorting the words
      for word in uniqWords:                                       # Call the iteration for testing if we have reached the end, if not we want to append those entries to a new list
            if i != len(uniqWords):
                  freqList.append([])                              # If we are not at the end we need to create an empty entry for the incoming freq count
        
            freqList[i].append(str(words.count(word)))             # Now we append the counts of the words in an entry along-side the word in a list
            freqList[i].append(word)                               # Append word
            i=i+1                                                  # Increase the counter
  
      frequencyList = sorted(freqList, key=getKey,reverse=True)    # While sorting it earlier was nice, we want to now sort so we can list it later via frequency, reading up on the key to sorted() led me to write the function getKey() which allows us to sort by the 
      return frequencyList                                         # frequency in which the word turns up, NIFTY! I chose to also set it to decrease in frequency by setting reverse=True.
  
def getKey(item): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
      return int(item[0])                                          # Pulled my hair out for almost a whole day trying to figure why sorted would put "66" before "7" - alas, dr DuckDuckGo told me all items within the lists are strings,which I should have known
                                                                   # Convert to int and BAM! I now have the ability to sort via a call for the frequency entry in each list
                                                                   
def plotVertical(frequencyList, widthVertical): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
      buffer = 10                                                                                                                      # So I know this is a messy bit of coding, firstly I set a buffer of 10 pixels
      verticalPlot = makeEmptyPicture(widthVertical,((len(frequencyList)*14)+buffer*3),white)                                          # We create an empty picture in which to plot all our words and whatnot
      maxFreqRatio = float(getWidth(verticalPlot)-(13*buffer))/(float(frequencyList[0][0]))                                            # We want a ratio to consider how to best scale each entry not only against the max freq but also to best display on the graph.
      for i in range(0,len(frequencyList)):                                                                                            # We now iterate through the list of words, the variable "i" is very useful to use to move our text and relevent bars down the graph
            freq = int(frequencyList[i][0])                                                                                            # We request the frequency that the word occured, variable thanks to "i"
            addText(verticalPlot,1+buffer,1+(buffer+(buffer+(i*14))),str(frequencyList[i][1]),black)                                   # We add the text that is listed at the current entry we are looking at, variable again thanks to "i"
            addRectFilled(verticalPlot,12*buffer,1+(buffer+(i*14)),int(round(maxFreqRatio,3)*freq),buffer+2,blue)                      # We add the base color blue for the graph, draw starts at 12*buffer(120) to ensure space for the words plus a bit (and as it was suggested)
            addRect(verticalPlot,12*buffer,1+(buffer+(i*14)),int(round(maxFreqRatio,3)*freq),buffer+2,black)                           # We now re-draw over the original rectangle, give it a pretty little outline in black
  
      addText(verticalPlot,1+buffer,2+(buffer+(buffer+(int(len(frequencyList))*14))),"Highest count: "+str(frequencyList[0][0]),black) # We add the text at the bottom of the graph as stipulated in the assignment outline.
      return verticalPlot

def readKeywords(filename): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
      fileContents = open(filename, "r")                 #Open the file
      listA = []                                         #Create some empty lists 
      listB = []                                         #Create some empty lists  
      fileContents.close                                 #Close the file
  
      removeNewLine(listA,fileContents)                  #Remove new line chars, pass a list and the filefoutput to make a rough list. (OUTPUT listA)

      listCleanup(listA,listB)                           #Remove characters that will never exist within the English language as a feature of a word other than gramatically by default ---- ( Exclaimation marks, Questions marks, Periods, Quotation marks etc)
                                                         #Also perform actions that test for single char entries and/or small exceptions that may slip through if a hyphen exists which still may exist within a word validly in the English language.
      return listB

def calculateFrequencies(keywords, frequencyList): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      i=0                                                                        # Set a counter
      keywordFrequencies = []                                                    # Create an empty list
      for x in range(0,len(keywords)):                                           # Start iteration through list
            for y in range(0,len(frequencyList)):                                # Iterate through main frequency list
                  if str(frequencyList[y][1]) == str(keywords[x]):               # Pair items that occur in the frequency list and the keyword list
                        keywordFrequencies.append([])                            # Append an empty entry to the current list
                        keywordFrequencies[i].append(str(frequencyList[y][0]))   # Append the count
                        keywordFrequencies[i].append(keywords[x])                # Append the relevent word we're looking at
                        i=i+1                                                    # Make sure the count reflects the next entry point
                              
      keywordFrequencies = sorted(keywordFrequencies,key=getKey,reverse=True)    # Sort the entries
      return(keywordFrequencies)                                                 # Return the list to the original caller

def plotHorizontal(keywordFrequencies, widthHorizontal, heightHorizontal): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      buffer = 10                                                                                                                            # Buffers are beautiful
      horizontalPlot = makeEmptyPicture(widthHorizontal,heightHorizontal,white)                                                              # Creating an empty picture
      rotatedStrings = rotateStrings(keywordFrequencies)                                                                                     # Create the picture of the keywords side-ways
      spacingRatioWords = ((getWidth(horizontalPlot))-((8*buffer)+(len(keywordFrequencies)*14)))/(len(keywordFrequencies)-1)                 # Create some useful spacing variables
      spacingRatioNumbers = (getHeight(horizontalPlot)-(120+(2*buffer))-(int(keywordFrequencies[0][0])*10))/int(keywordFrequencies[0][0])    # Create some useful spacing variables - based on the expected max size of a list
      spacingRatioBars = float((getHeight(horizontalPlot)-(120+(buffer))))/int(keywordFrequencies[0][0])                                     # Create some useful spacing variables - This time for the bars to display the frequency

      for i in range(0,len(keywordFrequencies)):                                                                                             # Set a loop for the number of keywords
            for x in range(0,14):                                                                                                            # Set a loop for every 14 pixels - used as opposed to "10" as the words seemed to have issues with "y" "g" and other characters that may 
                        for y in range(0,getHeight(rotatedStrings)):                                                                         # push for space beyond that 10 pixel area
                              aPixel = getPixel(rotatedStrings,(getWidth(rotatedStrings)-((1+i)*14)+x), (getHeight(rotatedStrings)-y)-1)     # We grab the pixels from the rotated text
                              aColor = getColor(aPixel)                                                                                      # We set the color to a variable to avoid messing with colors and other niceties 
                              bPixel = getPixel(horizontalPlot,(6*buffer+(spacingRatioWords*i)+x),(getHeight(horizontalPlot)-y)-1)           # We set the new pixels, dependent on the before mentioned spacing ratio, we convert back from float to keep the process more accurate
                              bColor = setColor(bPixel, aColor)                                                                              # We set the next pixel color
      
      for i in range(0,int(keywordFrequencies[0][0])):                                                                                       # We only iterate to the highest count of the keyword frequencies
            addText(horizontalPlot,0,2*buffer+((spacingRatioNumbers*i)+(i*10)),str(int(keywordFrequencies[0][0])-i))                         # We add some sexy numbers up the size
            addLine(horizontalPlot,4*buffer,2*buffer+((spacingRatioNumbers*i)+(i*10))-3,2*buffer,2*buffer+((spacingRatioNumbers*i)+(i*10))-3)# We set up the "ticks", here we also slightly offset the tick from the numbers as otherwise they're ugly and don't allign well at all.

      for i in range(0,len(keywordFrequencies)):                                                                                                           # We iterate through the keywords
            maxFreq = int(keywordFrequencies[0][0])                                                                                                        # Set a max frequency - later this is useful to offset the rectangles draw start as they require the lowest y value
            freq = int(keywordFrequencies[i][0])                                                                                                           # We grab the frequency count of the entry we're currently looking at
            addRectFilled(horizontalPlot,6*buffer+(spacingRatioWords*i),int(buffer+((maxFreq-freq)*spacingRatioBars)),14,int(spacingRatioBars*freq),green) # We draw a green rectangle showing how frequent a word shows up, as suggested above, based on the comparison between
            addRect(horizontalPlot,6*buffer+(spacingRatioWords*i),int(buffer+((maxFreq-freq)*spacingRatioBars)),14,int(spacingRatioBars*freq),black)       # max frequency and the actual frequency of the word
      
      addLine(horizontalPlot,4*buffer,getHeight(horizontalPlot)-120,getWidth(horizontalPlot)-buffer,getHeight(horizontalPlot)-120,black)                   # We draw an X and Y axis to avoiud eye-aids.
      addLine(horizontalPlot,4*buffer,getHeight(horizontalPlot)-120,4*buffer,buffer,black)                                                                 # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      return(horizontalPlot)                                                                                                                               # Return the image to the readAndPlot() function

def rotateStrings(strings): #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      textPicture = makeEmptyPicture(120,(len(strings)*14),white)                        # Using 14 as it worked nicely with the graph to print something readable, can be edited later
      for i in range(0,len(strings)):                                                    # We add text based on all the words that occur with a frequency other than "0"
            addText(textPicture,10,10+(i*14),str(strings[i][1]))                         # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      
      rotatedText = makeEmptyPicture(getHeight(textPicture),getWidth(textPicture),white) # We create a new picture to rotate the one just made into
      for x in range(0,getWidth(rotatedText)):                                           # Start iteration
            for y in range(0,getHeight(rotatedText)):                                    # ^^^^^^^^^^^^^^^
                  aPixel = getPixel(textPicture, y, x)                                   # Grab some of the original pixels
                  aColor = getColor(aPixel)                                              # Get the colour of said pixels
                  bPixel = getPixel(rotatedText,(getWidth(rotatedText)-1)-x,y)           # Set a target pixel on the rotated image
                  bColor = setColor(bPixel, aColor)                                      # Fire on the pixel with out lovely aColour variable.
                  
      return(rotatedText)                                                                # Return the rotated text to the caller function
                                                                                                                                                                                                                                                                                      