from test_chain_algorithm import test_chain_algorithm
import pickle
pickle_in = open("test_case.p","rb")
test_list = pickle.load(pickle_in)

#main function
def getListOfChains(two_chains):
    #initialize variables
    sendingNodes = [item[0] for item in two_chains]
    receivingNodes = [item[1] for item in two_chains]
    startingNodes = [] #nodes that send but do not receive
    senderDict = {} #Dictionary of sending nodes 
    full_chains = [] #the desired result to be returned

    #sub-function definition
    def getFullChain(nextNode, full_chain):
        full_chain.append(nextNode)
        if nextNode in senderDict:
            branchList = [item for item in senderDict[nextNode]]
        else:
            branchList = []
        if branchList == []:
            full_chains.append(full_chain)
        else:
            for branch in branchList:
                getFullChain(receivingNodes[branch], [n for n in full_chain])

    #populate senderDict with values of indices
    for index in range(0, len(sendingNodes)):
        if sendingNodes[index] in senderDict:
            senderDict[sendingNodes[index]].append(index)
        else:
            senderDict[sendingNodes[index]] = [index]
    
    #obtain the list of 'starting nodes' that will kick off each full chain
    #this is the majority of the runtime, could probably be optimized further
    for key in senderDict:
        if key in receivingNodes:
            continue
        elif key in startingNodes:
            continue
        else:
            startingNodes.append(key)

    #sub-function call for each starting node
    for startingNode in startingNodes:
        getFullChain(startingNode, [])

    #return result
    return full_chains

#function call
x = getListOfChains(test_list)

#pass into test algorithm
test_chain_algorithm(x)