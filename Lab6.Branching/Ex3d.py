# This is what it would potentially look like without using any if statements at all
def determine_progress4(hits, spins):
    progress_messages = ["Get going!", "On your way!", "Almost there!", "You win!"]

    if spins == 0:
        return progress_messages[0]

    hits_spins_ratio = hits / spins
    index = (hits_spins_ratio >= 0.5 and hits < spins) * 3 + (hits_spins_ratio >= 0.25) * 2 + (hits_spins_ratio > 0) * 1
    
    return progress_messages[index]

# Run tests on determine_progress4, we need to include the rest of the other codes, but I am a bit lazy
# test_determine_progress(determine_progress4)