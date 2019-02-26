## Time-scale of interactions for bots and humans in Wikipedia edits

This project was my submission for the final assignment in Computer Programming (MY470), a postgraduate course at the LSE taught by Professor Milena Tsvetkova.

The objective was to determine the distribution of times between successive “reverts” for bot-bot and human-human interactions on Wikipedia. (A revert occurs when an editor undoes the changes made by another editor.) This required constructing a network from the raw data and classifying each node in the network as one of three types (bot, human or vandal). 

The main dataset for this assignment – provided by the professor as a `.txt` file – includes every article edit made on Romanian Wikipedia since it began until the end of 2006 (roughly 470,000 edits). 

Files in this repository:
-	[MY470_final_assignment.ipynb](MY470_final_assignment.ipynb): main Jupyter Notebook containing the assignment and results
-	`.py` files: contain code for helping functions used in the assignment

For Milena’s published work on this topic, see: 
-	Tsvetkova M, García-Gavilanes R, Floridi L, Yasseri T (2017). Even good bots fight: The case of Wikipedia. _PLoS ONE 12_(2): e0171774. https://doi.org/10.1371/journal.pone.0171774.
-	[Milena’s website](http://tsvetkova.me/)
