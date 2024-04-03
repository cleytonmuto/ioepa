import os


def main():
    wget_output = ["#/bin/bash"]
    ocr_output = ["#/bin/bash"]
    year = "2022"
    pwd = os.getcwd()
    path = os.path.join(pwd, "input", year)
    mode = 0o775
    os.mkdir(path, mode)
    with open(year + ".html", "rt", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line[:-1]
            if line.find("pdf") > 0:
                tokens = line.split("\"")
                for token in tokens:
                    if token.find("arquivos") > 0:
                        pieces = token.split("/")
                        wget_output.append("wget https://www.ioepa.com.br" + token)
                        ocr_output.append("ocrmypdf input/" + year + "/" + pieces[3] + " output/" + year + "/" + pieces[3])
    with open("input/" + year + "/script.sh", "wt", encoding="UTF-8") as file:
        for line in wget_output:
            file.write(line + "\n")
    with open("ocr_script.sh", "wt", encoding="UTF-8") as file:
        for line in ocr_output:
            file.write(line + "\n")
    
    
if __name__ == "__main__":
    main()