def detect_anagrams(word, candidates):
    viable_candidates = []
    length = len(word)
    temp_word = word.lower()
    for candidate in candidates:
        candidate_case_preserve = candidate
        candidate = candidate.lower()
        word = temp_word
        if len(word) != len(candidate) or word == candidate:
            continue
        for char in candidate:
            if word.find(char) != -1:
                pos = word.find(char)
                word = word[0:pos] + word[pos+1:length]
            else: break
        if word == '':
            viable_candidates.append(candidate_case_preserve)
    return viable_candidates

str1 = 'corn'
print(detect_anagrams('corn', ["corn", "dark", "Corn", "rank", "CORN", "cron", "park"]))
