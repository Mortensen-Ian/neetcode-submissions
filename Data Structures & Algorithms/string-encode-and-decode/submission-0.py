class Solution:
    def encode(self, strs: List[str]) -> str:
        ListOfLists = []
        for l in strs:
            miniList = []
            for c in l:
                miniList.append(str(ord(c)))
            miniList.append(",")
            ListOfLists.append(",".join(miniList))
            #H,e,l,l,o|W,o,r,l,d
        if len(ListOfLists) > 0:
            ListOfLists[-1] += ("|")
        return "|".join(ListOfLists)

    def decode(self, s: str) -> List[str]:
        WordList = []
        Word = []
        character = ""
        for c in s:
            if c == '|':
                WordList.append("".join(Word))
                Word = []
            elif c == ',':
                if character == "":
                    Word.append("")
                else:
                    Word.append(chr(int(character)))
                character = ""
            else:
                character += c
        return WordList