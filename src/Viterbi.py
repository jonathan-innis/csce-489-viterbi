import sys
import Sentence

class Viberbi:
    def __init__(self, prob_file, sents_file):
        self.PARTS_OF_SPEECH = ["noun", "verb", "inf", "prep", "phi", "fin"]
        self.emissions = {}
        self.transitions = {}
        self.sentences = []

        #Initializing based on the files
        self.parse_prob_file(prob_file)
        self.parse_sents_file(sents_file)

    def get_transition(self, transition1, transition2):
        if (transition1, transition2) not in self.transitions:
            return 0.0001
        return self.transitions[(transition1, transition2)]

    def get_emission(self, emission1, emission2):
        if (emission1, emission2) not in self.emissions:
            return 0.0001
        return self.emissions[(emission1, emission2)]

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
        parsed_line = [x.lower() for x in line.strip().split(" ")]
        if len(parsed_line) == 3:
            if parsed_line[0] in self.PARTS_OF_SPEECH and parsed_line[1] in self.PARTS_OF_SPEECH:
                self.transitions[(parsed_line[0], parsed_line[1])] = float(parsed_line[2])
            else:
                self.emissions[(parsed_line[0], parsed_line[1])] = float(parsed_line[2])

    def parse_sents_file(self, file):
        contents = self.read_file(file)
        for line in contents:
            self.parse_sents_line(line)
    
    def parse_sents_line(self, line):
        parsed_line = [x.lower() for x in line.strip().split(" ")]
        self.sentences.append(parsed_line)

    def train(self):
        for sentence in self.sentences:
            print("PROCESSING SENTENCE: %s\n" % (' '.join(sentence)))
            Sentence.Sentence(self, sentence)
    
def main():
    try:
        assert len(sys.argv) == 3
        prob_file = sys.argv[1]
        sentence_file = sys.argv[2]
        vb = Viberbi(prob_file, sentence_file)
        vb.train()

    except ReferenceError as e:
        print(e)


if __name__ == '__main__':
    main()

