import sys
import math
import decimal

class Example:
    def __init__(self, vb, sentence):
        self.tags = ["noun", "verb", "inf", "prep"]
        self.vb = vb
        self.viterbi_net_str = ""
        self.backptr_net_str = ""
        self.sentence = sentence
        self.prob = [{tag:(1 if i == 0 else 0) for tag in self.tags} for i in range(len(sentence))]
        self.bp = [{tag:(1 if i == 0 else 0) for tag in self.tags} for i in range(len(sentence))]
        self.pos = ["" for x in range(len(self.sentence))]
        self.tag()

    def get_final_tags(self):
        for k in range(len(self.sentence) - 2, -1, -1):
            self.pos[k] = self.bp[k+1][self.pos[k+1]]

    def print_final_tags(self):
        for i in range(len(self.sentence)):
            print("%s -> %s" % (self.sentence[i], self.pos[i]))
    
    def get_probability(self, k, v, w):
        return self.prob[k-1][w] + math.log(self.vb.get_transition(v, w)) + math.log(self.vb.get_emission(self.sentence[k], v))
    
    def tag_sentence_start(self):
        for v in self.tags:
            max_prob = 1 + math.log(self.vb.get_transition(v, 'phi')) + math.log(self.vb.get_emission(self.sentence[0], v))
            max_arg = v
            for w in self.tags:
                pi = 1 + math.log(self.vb.get_transition(w, 'phi')) + math.log(self.vb.get_emission(self.sentence[0], v))
                if pi > max_prob:
                    max_prob = pi
                    max_arg = w
            self.bp[0][v] = max_arg
            self.prob[0][v] = max_prob
            self.viterbi_net_str += "P(%s=%s) = %s\n" % (self.sentence[0], v, '{0:0.10f}'.format(math.e**max_prob))
    
    def tag_sentence_end(self):
        last_probs = self.prob[len(self.sentence) - 1]
        max_prob = last_probs[self.tags[0]]
        max_tag = self.tags[0]
        for v in self.tags:
            if last_probs[v] + math.log(self.vb.get_transition('fin', v)) > max_prob:
                max_prob = last_probs[v] + math.log(self.vb.get_transition('fin', v))
                max_tag = v      
        self.pos[len(self.sentence) - 1] = max_tag
        print "BEST TAG SEQUENCE HAS PROBABILITY = %s" % '{0:0.10f}'.format(math.e**max_prob)

    def tag(self):
        #Doing initial tagging with the startng tags
        self.viterbi_net_str += "FINAL VITERBI NETWORK\n\n"
        self.backptr_net_str += "FINAL BACKPTR NETWORK\n\n"

        self.tag_sentence_start()
            
        for k in range(1, len(self.sentence)):
            for v in self.tags:
                max_prob = self.get_probability(k,v,v)
                max_arg = v
                for w in self.tags:
                    pi = self.get_probability(k,v,w)
                    if pi > max_prob:
                        max_prob = pi
                        max_arg = w
                self.prob[k][v] = max_prob
                self.bp[k][v] = max_arg
                self.viterbi_net_str += "P(%s=%s) = %s\n" % (self.sentence[k], v, '{0:0.10f}'.format(math.e**max_prob))
                self.backptr_net_str += "Backptr(%s=%s) = %s\n" %(self.sentence[k], v, max_arg)


        print(self.viterbi_net_str)
        print(self.backptr_net_str)

        self.tag_sentence_end()
        self.get_final_tags()
        self.print_final_tags()
        print




class Viberbi:
    def __init__(self, prob_file, sents_file):
        self.tags = ["noun", "verb", "inf", "prep", "phi", "fin"]
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
        self.sentences.append(parsed_line)

    def remove_pseudotags(self, sentence):
        return sentence[1:-1]

    def train(self):
        for sentence in self.sentences:
            print("PROCESSING SENTENCE: %s\n" % (' '.join(sentence)))
            ex = Example(self, sentence)
    
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

