#######################################
### Analyzing pairwise interactions ###
#######################################

from math import log10
from datetime import datetime, timedelta

### Main function ###

def main():
    # Construct dicts of bot-bot and human-human interactions;
    # Keys are bot-bot / human-human pairs, values are interaction times.
    botbot_dict, humhum_dict = pairs_dict(network, class_dict)

    # Sort interaction times chronologically,
    # and converts them to time-differences
    time_difs(botbot_dict)
    time_difs(humhum_dict)

    # Extract interactions data and convert to log10 seconds.
    botsdata = get_hist_data(botbot_dict)
    humsdata = get_hist_data(humhum_dict)

### Individual functions ###

def pairs_dict(network, class_dict):
    '''Constructs dictionary where keys are pairs of bot-bot or
    human-human users, and values are interaction times.
    Takes network and classification dict as arguments.'''
    # Create empty dictionaries
    botbot_dict = {}
    humhum_dict = {}

    # Iterate through reverts...
    for revert in network:
        reverter, reverted, time = (revert[0], revert[1], revert[2])
        # ... If both are humans, add entry to humhum.
        if class_dict[reverter] == 'human' and class_dict[reverted] == 'human':
            humhum_dict.setdefault(frozenset((reverter, reverted)),[]).append(time)
        # ... If both are bots, add entry to botbot.
        if class_dict[reverter] == 'bot' and class_dict[reverted] == 'bot':
            botbot_dict.setdefault(frozenset((reverter, reverted)),[]).append(time)

    return botbot_dict, humhum_dict

def time_difs(dic):
    '''Sorts dic values and transforms them from interaction
    times to time-differences between successive interactions.
    Operations done in-place.'''
    # Sort dictionary values chronologically
    [ls.sort() for ls in dic.values()]

    # Replace times with time-differences
    for i in dic:
        dic[i] = [t - s for s, t in zip(dic[i], dic[i][1:])]

def get_hist_data(pairs_dict):
    '''Constructs dataset of interaction time-differences
    in log10 seconds, based on the dictionary pairs_dict.
    For use in distributional analysis and graphing.'''
    # Convert interaction times into list of lists
    data = list(pairs_dict.values())

    # Flatten lists, transform to log10 seconds,
    # and remove interactions with zero time-difference.
    data = [log10(i.total_seconds())
            for sublist in data
            for i in sublist
            if i.total_seconds() > 0.0]

    return data

if __name__ == '__main__':
    main()
