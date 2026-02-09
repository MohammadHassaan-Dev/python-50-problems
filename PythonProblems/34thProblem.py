def func(ransomNote, magazine):
    for i in ransomNote: #a
        if ransomNote.count(i) > magazine.count(i):
            return False

    return True
        


ransomNote = "aab"
magazine = "ab"    
print(func(ransomNote, magazine))