class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for word in strs:
            if word == "":
                s += ";"
            for i, w in enumerate(word):
                if i == len(word) - 1:
                    s += w + "`"
                else:
                    s += w


        return s

    def decode(self, s: str) -> List[str]:

        store = ""
        f_ans = []

        for i in s:
            if i == "`":
                f_ans.append(store)
                store = ""
            elif i == ";":
                f_ans.append("")
            else:
                store += i
        
        if store != "":
            f_ans.append(store)

        return f_ans
