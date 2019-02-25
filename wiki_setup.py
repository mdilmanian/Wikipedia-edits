##############################
### Setting up the network ###
##############################

from datetime import datetime

### Main function ###

def main():
    # Get Wikipedia data
    data = get_data('rowiki_2006.txt')
    # Parse Wiki data and construct network list
    network = parse_append(data)
    # Construct set of nodes
    nodes = get_nodes(network)

### Individual functions ###

def get_data(fname, header = True, encoding = 'utf-8'):
    '''Opens Wikipedia edit data in file fname and returns
    list of formatted values. Assumes first row is headers.
    Assumes utf-8 encoding.'''
    with open(fname, mode = 'r', encoding = encoding) as f:
        data = [] # Create empty list for values

        if header == True:
            f.readline() # Skip first row

        # Split up each line and save as list of lists
        for edit in f.readlines():
            title, dt, rev, version, user = edit.strip().split('\t')
            data.append([title.strip(),
                         datetime.strptime(dt, "%Y-%m-%d %H:%M:%S"),
                         int(rev),
                         int(version),
                         user])
    return data

def parse_append(data):
    '''Parses list of Wikipedia edit data.
    Appends reverter, reverted user and time to a list
    of lists called "network". '''
    network = []

    for index, item in enumerate(data):
        # Add reverts to 'network'
        if item[2]==1: # Select only reverts
            i = index + 1 # Start search with next entry
            # Find restored version
            while (data[i][3] != item[3]):
                i += 1
            # If no self-revert or non-edit...
            if (item[4] != data[i-1][4] and
                item[3] != data[index+1][3]):
                # ... Add reverter, reverted user and timestamp to network
                network.append([item[4], data[i-1][4], item[1]])

    return network

def get_nodes(network):
    '''Extracts nodes (reverters and reverted users)
    from Wikipedia network list. Returns set of nodes.'''
    # Add reverters
    nodes = {i[0] for i in network}

    # Add reverted users
    for i in network:
        nodes.add(i[1])

    return nodes

if __name__ == '__main__':
    main()
