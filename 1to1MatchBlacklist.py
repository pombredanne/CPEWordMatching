# from fuzzywuzzy import fuzz

f = open("matchingDescriptions.txt", "a")

def fuzz_compare(descWord, CPELib, fullDesc):
    if descWord.lower() == CPELib.lower():
        # print("exact match between "+descWord+" and "+CPELib)
        f.write(CPELib+"    :"+fullDesc+"\n")

def read_cpe_items(filename):
    cpeList = []
    with open(filename, encoding="utf8") as file:
        for line in file:
            splitLine = line.split(" --> ")
            appendLine = splitLine[0]
            cpeList.append(appendLine)
    return cpeList

def read_descriptions(filename):
    descList = []
    with open(filename, encoding="utf8") as file:
        for line in file:
            line = line.strip()
            # splitLine = line.split(";;")
            # appendLine = splitLine[1]
            # descList.append(appendLine)
            descList.append(line)
    return descList

def compare_all_results(cpeList, descList, blackList):
    prevLib = ""
    for fullDesc in descList:
        descWordList = fullDesc.split(" ")
        for descWord in descWordList:
            if descWord.lower() not in blackList:
                for CPELib in cpeList:
                    if prevLib != CPELib:
                        fuzz_compare(descWord, CPELib, fullDesc)
                        prevLib = CPELib

cpeList = read_cpe_items("filteredCPEItems.txt")
descList = read_descriptions("2020descriptions.txt")
blackList = read_descriptions("blackList.txt")
compare_all_results(cpeList, descList, blackList)

f.close()