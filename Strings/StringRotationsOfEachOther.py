s1 = input()
s2 = input()

class StringRotationsOfEachOther:
    def areRotations(self,s1,s2):
        if len(s1)==len(s2) and s2 in (s1+s1):
            return True
        return False

print(StringRotationsOfEachOther().areRotations(s1,s2))


## "abcd" "cdab"
## true