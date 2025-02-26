# Function in order to help determine the progress based on hits or spins. 
def determine_progress1(hits, spins):
    # If no spins, this will get a message saying "Get going" which will try to encourage players to start
    if spins == 0:
        return "Get going!"
    # Calculating the hits to spins ratio
    hits_spins_ratio = hits / spins
    # default progress message
    if hits_spins_ratio > 0:
        progress = "On your way!"
        # If it is at least 25 percent of spins have hitted, progress will update
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            # if it's at least 50 percent of spins are hits, and the hits are less than spins
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        # No hits, will get us this
        progress = "Get going!"

    return progress

# Function in order to test determine_progress1 using assertions
def test_determine_progress(progress_function):
   # Test case 1: spins = 0 returns “Get going!”
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed"
    assert progress_function(2, 5) == "Almost there!", "Test case 2 failed"
    assert progress_function(1, 5) == "On your way!", "Test case 3 failed"
    assert progress_function(5, 10) == "You win!", "Test case 4 failed"  

# Without using nested IFs or elifs and else
def determine_progress2(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    progress = "Get going!"
    if hits_spins_ratio > 0:
        progress = "On your way!"
    if hits_spins_ratio >= 0.25:
        progress = "Almost there!"
    if hits_spins_ratio >= 0.5 and hits < spins:
        progress = "You win!"

    return progress

test_determine_progress(determine_progress2)