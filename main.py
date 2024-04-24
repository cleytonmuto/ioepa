import os


def main():
    ocr_output = ["#/bin/bash"]
    with open("somente_pdfs.txt", "rt", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            line = "'" + line[:-1] + "'"
            ocr_output.append("ocrmypdf webfiles/" + line + " output/" + line + " --skip-text")
    with open("ocr_script.sh", "wt", encoding="UTF-8") as file:
        for line in ocr_output:
            file.write(line + "\n")
    
    
if __name__ == "__main__":
    main()