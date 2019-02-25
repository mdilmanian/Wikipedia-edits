# Load packages
import pickle
from matplotlib import pyplot

def main():
    pass

####################
### Pickle utils ###
####################

def unpickle(pickled_fname):
    '''Loads and returns pickled file into python.'''
    with open (pickled_fname, 'rb') as fr:
        return pickle.load(fr)

######################
### Plotting utils ###
######################

def set_plot_params(title, leg_loc, xlow, xhigh, xlab, ylab):
    '''Set most-needed parameters for pyplot histogram.'''
    pyplot.title(title)
    pyplot.legend(loc = leg_loc) # Legend location
    pyplot.xlim((xlow, xhigh)) # Range of x-axis
    pyplot.xlabel(xlab)
    pyplot.ylabel(ylab)

if __name__ == '__main__':
    main()
