###########################
### Classifying editors ###
###########################

### Main function ###

def main():
    # Get bots data and transform to set
    bots = set(get_bots_data('botlist_final.txt'))
    # Construct dictionary of reverted users
    reverteds_dict = get_reverteds_dict(network)
    # Construct dictionary of editors
    edits_dict = get_edits_dict(network, data)
    # Construct set of vandals
    vandals = get_vandals(reverteds_dict, edits_dict)
    # Construct classification dictionary
    class_dict = classify_users(nodes, bots, vandals)

### Individual functions ###

def get_bots_data(fname, header = False, encoding = 'utf-8'):
    '''Opens Wikipedia botlist in file fname and returns
    list of bots as strings. Default assumes no header row.
    Default assumes utf-8 encoding.'''
    with open(fname, mode = 'r', encoding = encoding) as f:
        data = [] # Create empty list for values

        if header == True:
            f.readline() # Skip first row

        # Strip trailing newline
        for row in f.readlines():
            bot = row.rstrip('\n')
            data.append(bot)

    return data

def get_reverteds_dict(network):
    '''Constructs and returns dict of reverteds. Keys are
    reverted users, values are reverters for each reverted user.'''
    # Construct dictionary
    reverteds_dict = {i[1]:[] for i in network}

    # Add reverted users
    for i, j, k in network:
        reverteds_dict[j].append(i)

    return reverteds_dict

def get_edits_dict(network, data):
    '''Constructs and returns dict of {editors: [edit times]}.
    Includes only users who have been reverted.'''
    # Construct dictionary
    edits_dict = {i[1]:[] for i in network}

    # Add edits
    for entry in data:
        if entry[4] in edits_dict: edits_dict[entry[4]].append(entry[1])

    return edits_dict

def get_vandals(reverteds_dict, edits_dict):
    '''Constructs and returns set of vandals based on dict
    of reverted users and dict of editors.'''
    vandals = []

    for user in reverteds_dict:
        # If number of edits equals number of reversions...
        if len(edits_dict[user]) == len(reverteds_dict[user]):
            # ... Append user to list
            vandals.append(user)

    # Return as set to improve runtime in membership tests
    return set(vandals)

def classify_users(nodes, bots, vandals):
    '''Constructs and returns dictionary that classifies each
    Wikipedia user contained in nodes. Requires pre-defined
    bots and vandals. Arguments are iterables, ideally sets.'''
    # Construct dictionary to classify each user
    class_dict = {i:[] for i in nodes}

    for user in class_dict:
        if user in bots:
            class_dict[user] = 'bot'
        elif user in vandals:
            class_dict[user] = 'vandal'
        else: class_dict[user] = 'human'

    return class_dict

if __name__ == '__main__':
    main()
