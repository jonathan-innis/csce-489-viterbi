import math

class Sentence:
    def __init__(self, vb, sentence):
        self.PARTS_OF_SPEECH = ["noun", "verb", "inf", "prep"]
        self.vb = vb
        self.viterbi_net_str = ""
        self.backptr_net_str = ""
        self.sentence = sentence
        self.prob = [{tag:(1 if i == 0 else 0) for tag in self.PARTS_OF_SPEECH} for i in range(len(sentence))]
        self.bp = [{tag:(1 if i == 0 else 0) for tag in self.PARTS_OF_SPEECH} for i in range(len(sentence))]
        self.pos = ["" for x in range(len(self.sentence))]
        self.tag()

    def get_final_tags(self):
        for k in range(len(self.sentence) - 2, -1, -1):
            self.pos[k] = self.bp[k+1][self.pos[k+1]]

    def print_final_tags(self):
        for i in range(len(self.sentence)):
            print("%s -> %s" % (self.sentence[i], self.pos[i]))
    
    def get_probability(self, k, v, w):
        return self.prob[k-1][w] + math.log(self.vb.get_transition(v,w)) + math.log(self.vb.get_emission(self.sentence[k], v))
    
    def tag_sentence_start(self):
        for v in self.PARTS_OF_SPEECH:
            max_prob = 1 + math.log(self.vb.get_transition(v, 'phi')) + math.log(self.vb.get_emission(self.sentence[0], v))
            max_arg = v
            self.bp[0][v] = max_arg
            self.prob[0][v] = max_prob
            self.viterbi_net_str += "P(%s=%s) = %s\n" % (self.sentence[0], v, '{0:0.10f}'.format(math.e**max_prob))
    
    def tag_sentence_end(self):
        last_probs = self.prob[len(self.sentence) - 1]
        max_prob = last_probs[self.PARTS_OF_SPEECH[0]]
        max_tag = self.PARTS_OF_SPEECH[0]
        for v in self.PARTS_OF_SPEECH:
            if last_probs[v] > max_prob:
                max_prob = last_probs[v]
                max_tag = v      
        self.pos[len(self.sentence) - 1] = max_tag
        print ("BEST TAG SEQUENCE HAS PROBABILITY = %s" % ('{0:0.10f}'.format(math.e**max_prob)))

    def tag(self):
        #Doing initial tagging with the startng tags
        self.viterbi_net_str += "FINAL VITERBI NETWORK\n\n"
        self.backptr_net_str += "FINAL BACKPTR NETWORK\n\n"

        self.tag_sentence_start()
            
        for k in range(1, len(self.sentence)):
            for v in self.PARTS_OF_SPEECH:
                max_prob = self.get_probability(k,v,v)
                max_arg = v
                for w in self.PARTS_OF_SPEECH:
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
