## Random Walks And Phonetic Drif   t

# Overall Design:

right now the UI is a non-function bit of Tkinter. Don't worry about that at the moment. Looking at this, the important part is the CSVhandler.py, and the ipadirectional.py. What the CSV handler can do is take language names, and either display their information, or find their intersection with other languages, i.e. what phonemes do they not share. This is what we will hook up to the language tree to compare between languages as development goes. All we need to do is implement the order of languages, and run each pair through that function to get the individual vector. Storing those in series we get a good picture of how the sounds drifted from one to antoher. 

the next part is the ipa directional.py. This is what is supposed to model different random walks for drift. Vowels are implemented via a graph database in a csv file. feed a vowel address (there is a function to find this already in the code) into the function and it will output a drifted vowel, based on what that vowel is close to on the traditional IPA vowel chart. I am currently working on this for consonants as well, but in 2D array form b/c it is easier and more intuitive on the way consonants can drift. currently the different random walk generators are un-implemented, but are pretty self-explanatory. 

As for what we do after that, all we need to do is run the trees through the first part I described to get a good model on that, and then run our RW models and compare them statistically. Pretty straigtforward.
