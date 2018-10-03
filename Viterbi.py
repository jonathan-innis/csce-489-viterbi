import sys

class Viberbi:
    def __init__(self, prob_file, sents_file):
        self.tags = ["noun", "verb", "inf", "prep", "phi", "fin"]
        self.emissions = {}
        self.transitions = {}
        self.sentences = []

        #Initializing based on the files
        self.parse_prob_file(prob_file)
        self.parse_sents_file(sents_file)

    def read_file(self, file_name):
        contents = []
        f = open(file_name)
        for line in f:
            contents.append(line)
        f.close()
        return contents

    def parse_prob_file(self, file):
        contents = self.read_file(file)
        for line in contents:
            self.parse_prob_line(line)

    def parse_prob_line(self, line):
        parsed_line = line.strip().split(" ")
        if len(parsed_line) == 3:
            if parsed_line[0] in self.tags and parsed_line[1] in self.tags:
                self.transitions[(parsed_line[0], parsed_line[1])] = float(parsed_line[2])
            else:
                self.emissions[(parsed_line[0], parsed_line[1])] = float(parsed_line[2])

    def parse_sents_file(self, file):
        contents = self.read_file(file)
        for line in contents:
            self.parse_sents_line(line)
    
    def parse_sents_line(self, line):
        parsed_line = line.strip().split(" ")
        parsed_line.insert(0, "phi")
        parsed_line.append("fin")
        self.sentences.append(parsed_line)

    def remove_pseudotags(self, sentence):
        return sentence[1:-1]

    def train(self):
        for sentence in self.sentences:
            print("PROCESSING SENTENCE: %s" % (' '.join(self.remove_pseudotags(sentence))))
    
def main():
    try:
        if (len(sys.argv) != 3):
            raise ReferenceError("You did not include the correct number of files as arguments")
        else:
            prob_file = sys.argv[1]
            sentence_file = sys.argv[2]
            vb = Viberbi(prob_file, sentence_file)
            vb.train()

    except ReferenceError as e:
        print(e)


if __name__ == '__main__':
    main()

