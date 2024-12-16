"""

В текстовом файле in.txt записан некоторый текст. Требуется в файл out.txt
переписать его так, чтобы в каждой строке выходного файла находилось ровно одно предложение,
начиная от последнего и заканчивая первым. В рамках задачи считать, что предложения оканчиваются точками,
и других точек, кроме тех, которые обозначают конец предложения, в тексте нет. С файлом in.txt работать построчно
так, чтобы в памяти единовременно находилось не более одного предложения.

"""

file2 = open("out.txt", "w")
sentence = ""
char = ""
with open("in.txt", encoding='utf-8') as file1:
    position = file1.seek(0, 2)
    while position - 1 >= 0:
        position -= 1

        file1.seek(position)
        char = file1.read(1)

        if char == "." and sentence.count(".") == 1:
            file2.write((sentence+"\n").strip(" "))
            sentence = "."
        elif position - 1 == 0:
            if char != "\n":
                sentence = char + sentence
            file1.seek(position - 1)
            char = file1.read(1)
            if char != "\n":
                sentence = char + sentence
            file2.write((sentence+'\n').strip(" "))
            sentence = ""
        else:
            if char != "\n":
                sentence = char + sentence
