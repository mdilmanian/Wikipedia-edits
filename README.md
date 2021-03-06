## Time-scale of interactions for bots and humans in Wikipedia edits

This project was my final assignment for the postgraduate Computer Programming course at the LSE.

The objective was to use `Python` to determine the distribution of times between successive “reverts” for bot-bot and human-human interactions on Wikipedia (a revert occurs when an editor undoes the changes made by another editor). This required constructing a network from the raw data and classifying each node in the network as one of three types &ndash; bot, human or vandal. 

The main dataset for this assignment was a `.txt` file containing information about every article edit made on Romanian Wikipedia since it began until the end of 2006 (roughly 470,000 edits). 

---

Files in this repository:
-	[final_assignment.ipynb](final_assignment.ipynb): this is the main Jupyter Notebook containing the assignment and results.
-	[utils.py](utils.py), [wiki_classify.py](wiki_classify.py), [wiki_interactions.py](wiki_interactions.py), [wiki_setup.py](wiki_setup.py): the files ending in `.py` contain code for helping functions used in the assignment.

