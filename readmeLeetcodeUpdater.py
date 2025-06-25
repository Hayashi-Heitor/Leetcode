import os

DIRECTORYS = {
    "C" : "Scripts/C",
    "Python" : "Scripts/Python",
    "Shell" : "Shell",
    "MySQL" : "Sql"
}

EXTENSIONS = {
    "C" : ".c",
    "Python" : ".py",
    "Shell" : ".sh",
    "MySQL" : ".sql"
}

TABLE_START = "|---|-------|----------|"

def message(string):
    print("readmeLeetcodeUpdater >", string)

def readsAllFiles():
    question = {}

    for language, path in DIRECTORYS.items():
        
        # Checks if the path exists
        if not os.path.exists(path): 
            message(f"\033[31mcan't find path passed on DIRECTORYS: {path}\033[37m")
            break
        
        # Passes all files informations to questions dictionarys
        for file in os.listdir(path): 
            questionNumber = file.split('.')[0]
            question[questionNumber] = {
                "questionNumber" : questionNumber,
                "questionName" : file.split('.')[1].strip(),
                "questionLanguage" : language,
                "questionPath" : path + '/' + questionNumber + '.' + file.split('.')[1].replace(' ', "%20") + EXTENSIONS[language],
                "questionLink" : "https://leetcode.com/problems/" + file.split('.')[1].strip().replace(' ', '-').lower()
            }
            message(f"\033[32mread: \033[37m{question[questionNumber]["questionNumber"]}. {question[questionNumber]["questionName"]}")
    
    # Returns the sorted dictonary
    return dict(sorted(question.items(), key = lambda x: int(x[0]))) 

def writesReadme(question):
    with open("README.md", 'r') as ReadmeFile:
        content = ReadmeFile.readlines()

    with open("README.md", 'w') as ReadmeFile:
        for line in content: #reads all lines
            ReadmeFile.write(line)

            # Compares the current line with the start of the table
            if TABLE_START == line.strip(): 

                # Checks if there is a line break after the start of the table
                if line[-1] == TABLE_START[-1]: 
                    ReadmeFile.write("\n")

                # Writes all the questions on the readme
                for num, data in question.items(): 
                        ReadmeFile.writelines(f"| {num} | [{data["questionName"]}]({data["questionLink"]}) | [{data["questionLanguage"]}]({data["questionPath"]}) |\n")
                        message(f"\033[32mwritten: \033[37m{data["questionNumber"]}. {data["questionName"]}")
                break
                

if __name__ == "__main__":
    print("\033[33mReadme Leetcode Updater V1.0.2\033[0m", end="\n\n")
    writesReadme(readsAllFiles())