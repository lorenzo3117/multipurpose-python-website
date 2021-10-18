def gather_file_information(file):
    file_information = {
        "fileName": file.filename,
        "fileType": file.content_type,
        "lineCount": 0,
        "emptyLineCount": 0,
        "wordFrequency": {},
        "wordCount": 0,
        "mostUsedWord": ""
    }

    for line in file.readlines(1024):
        line = bytes.decode(line.strip())
        
        # Line count
        file_information["lineCount"] += 1

        # Empty line count
        if len(line) == 0:
            file_information["emptyLineCount"] += 1

        # Words
        words_temp = line.split(" ")
        for word in words_temp:
            if word is not "":
                file_information["wordFrequency"][word] = file_information["wordFrequency"].get(word, 0) + 1

        # Word count
        file_information["wordCount"] = len(file_information["wordFrequency"].keys())

        # Most used word
        file_information["mostUsedWord"] = list(file_information["wordFrequency"].keys())[-1]

    return file_information