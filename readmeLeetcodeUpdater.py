import os

DIRECTORYS = {
    "C" : "Scripts/C",
    "Python" : "Scripts/Python",
    "Shell" : "Shell"
}

EXTENSIONS = {
    "C" : ".c",
    "Python" : ".py",
    "Shell" : ".sh"
}

TABLE_START = "|---|-------|----------|"

def message(string):
    print("readmeLeetcodeUpdater >", string)

def readsAllFiles():
    question = {}

    for language, path in DIRECTORYS.items():
        if not os.path.exists(path): #checks if the path exists
            message(f"\033[31mcan't find path passed on DIRECTORYS: {path}\033[37m")
            break
        
        for file in os.listdir(path): #passes all files informations to questions dictionarys
            questionNumber = file.split('.')[0]
            question[questionNumber] = {
                "questionNumber" : questionNumber,
                "questionName" : file.split('.')[1].strip(),
                "questionLanguage" : language,
                "questionPath" : path + '/' + questionNumber + '.' + file.split('.')[1].replace(' ', "%20") + EXTENSIONS[language],
                "questionLink" : "https://leetcode.com/problems/" + file.split('.')[1].strip().replace(' ', '-').lower()
            }
            message(f"\033[32mread: \033[37m{question[questionNumber]["questionNumber"]}. {question[questionNumber]["questionName"]}")
    
    return dict(sorted(question.items(), key = lambda x: int(x[0]))) #returns the sorted dictonary

def writesReadme(question):
    with open("README.md", 'r') as ReadmeFile:
        content = ReadmeFile.readlines()

    with open("README.md", 'w') as ReadmeFile:
        for line in content: #reads all lines
            ReadmeFile.write(line)

            if TABLE_START == line.strip(): #compares the current line with the start of the table

                if line[-1] == TABLE_START[-1]: #checks if there is a line break after the start of the table
                    ReadmeFile.write("\n")

                for num, data in question.items(): #writes all the questions on the readme
                        ReadmeFile.writelines(f"| {num} | [{data["questionName"]}]({data["questionLink"]}) | [{data["questionLanguage"]}]({data["questionPath"]}) |\n")
                        message(f"\033[32mwritten: \033[37m{data["questionNumber"]}. {data["questionName"]}")
                break
                

if __name__ == "__main__":
    print("\033[33mReadme Leetcode Updater V1.0.2\033[0m", end="\n\n")
    writesReadme(readsAllFiles())