def solve(str1: str, str2: str):
    LCS = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
    max_value = 0
    for i in range(1, len(LCS)):
        for j in range(1, len(LCS[i])):
            if str1[i-1] == str2[j-1]:
                LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            if LCS[i][j] > max_value:
                max_value = LCS[i][j]
    for row in LCS:
        print(row)
    print(max_value)

def main():
    solve("stone", "longest")

if __name__ == "__main__":
    main()