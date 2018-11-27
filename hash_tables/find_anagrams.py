def find_anagrams(dictionary):
    sorted_string_to_anagram = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagram[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagram.values() if len(group) >= 2]
