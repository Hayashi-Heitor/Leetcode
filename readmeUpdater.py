import os

DIRECTORYS = {
    "C" : "Scripts/C",
    "Python" : "Scripts/Python",
    "Shell" : "Shell"
}

def message(string):
    print("readmeLeetcodeUpdater >", string)

def readsAllFiles():
    problem = {}

    for language, path in DIRECTORYS.items():
        if not os.path.exists(path):
            continue
        
        for file in os.listdir(path):
            questionNumber = file.split('.')[0]
            problem[questionNumber] = {
                "questionNumber" : questionNumber,
                "questionName" : file.split('.')[1].strip(),
                "language" : language
            }
            message(f"\033[32madded: \033[37m{problem[questionNumber]["questionNumber"]}")
    
    return dict(sorted(problem.items(), key = lambda x: int(x[0])))

if __name__ == "__main__":
    print("\033[33mReadme Leetcode Updater V0.0.1\033[0m", end="\n\n")
    readsAllFiles()