from pickle import load

def test_chain_algorithm(chain_list, solution_path = "test_solution.p"):
    print("Testing type: chain_list a list?")
    if type(chain_list) == type([]):
        print("Passed")
    else:
        print("Failed")
        return False

    print("Testing constituent type: chain_list contains only lists?")
    for x in chain_list:
        if type(x) != type([]):
            print("Failed")
            return False
    print("Passed")
    
    print("Testing uniqueness: no duplicate chains?")
    unique_chains = [list(set_) for set_ in set(tuple(list_) for list_ in chain_list)]
    if len(unique_chains) == len(chain_list):
        print("Passed")
    else:
        print("Failed")
        return False

    print("Testing length: correct number of chains?")
    infile = open(solution_path,'rb')
    solution_chain_list = load(infile)
    infile.close()

    if len(chain_list) == len(solution_chain_list):
        print("Passed")
    else:
        print("Failed. Correct length " +
            str(len(solution_chain_list)) +
            " , chain_list length " +
            str(len(chain_list))
            )
        return False

    chain_list_ord = [x[:] for x in chain_list]
    chain_list_ord.sort()
    print("Testing solution: is solution correct?")
    if solution_chain_list == chain_list_ord:
        print("Passed")
    else:
        print("Failed")
        return False

    print("Passed all tests")

    return True
