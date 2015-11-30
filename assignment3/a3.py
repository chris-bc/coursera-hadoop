fileA = sc.textFile("input/join1_fileA.txt")
#fileA.collect()
fileB=sc.textFile("input/join1_fileB.txt")
#fileB.collect()

def split_fileA(line):
    line = line.split(",")
    word = line[0]
    count = line[1]
    count = int(count)
    return(word,count)

# def test_line="able,991"
# split_fileA(test_line)

fileA_data = fileA.map(split_fileA)
#fileA_data.collect()

def split_fileB(line):
    line = line.split(",")
    count_string = line[1]
    line = line[0].split(" ")
    date = line[0]
    count = line[1]
    return(word,data + " " + count_string)

fileB_data = fileB.map(split_fileB)
#fileB_data.collect()

fileB_joined_fileA = fileB_data.join(fileA_data)
fileB_joined_fileA.collect()

