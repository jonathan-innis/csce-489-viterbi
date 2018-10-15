# Viterbi Sentence POS Classification Implementation

## Steps to Compile
- Go into the `src/` directory
- Run the command `python3 Viterbi.py ../data/probs.txt ../data/sents.txt` 

## Results and Analysis
The results given the `probs.txt` and `sents.txt` files are as follows:

```
PROCESSING SENTENCE: mark has fish

FINAL VITERBI NETWORK

P(mark=noun) = 0.1957162916
P(mark=verb) = 0.0163096910
P(mark=inf) = 0.0000000272
P(mark=prep) = 0.0000000272
P(has=noun) = 0.0000012558
P(has=verb) = 0.0038164677
P(has=inf) = 0.0000003588
P(has=prep) = 0.0000058715
P(fish=noun) = 0.0002350944
P(fish=verb) = 0.0000000571
P(fish=inf) = 0.0000000840
P(fish=prep) = 0.0000000954

FINAL BACKPTR NETWORK

Backptr(has=noun) = verb
Backptr(has=verb) = noun
Backptr(has=inf) = verb
Backptr(has=prep) = noun
Backptr(fish=noun) = verb
Backptr(fish=verb) = noun
Backptr(fish=inf) = verb
Backptr(fish=prep) = verb

BEST TAG SEQUENCE HAS PROBABILITY = 0.0002350944
fish -> noun
has -> verb
mark -> noun

PROCESSING SENTENCE: mark bears fish

FINAL VITERBI NETWORK

P(mark=noun) = 0.1957162916
P(mark=verb) = 0.0163096910
P(mark=inf) = 0.0000000272
P(mark=prep) = 0.0000000272
P(bears=noun) = 0.0002511692
P(bears=verb) = 0.0025443118
P(bears=inf) = 0.0000003588
P(bears=prep) = 0.0000058715
P(fish=noun) = 0.0001567296
P(fish=verb) = 0.0000114282
P(fish=inf) = 0.0000000560
P(fish=prep) = 0.0000000636

FINAL BACKPTR NETWORK

Backptr(bears=noun) = verb
Backptr(bears=verb) = noun
Backptr(bears=inf) = verb
Backptr(bears=prep) = noun
Backptr(fish=noun) = verb
Backptr(fish=verb) = noun
Backptr(fish=inf) = verb
Backptr(fish=prep) = verb

BEST TAG SEQUENCE HAS PROBABILITY = 0.0001567296
fish -> noun
bears -> verb
mark -> noun

PROCESSING SENTENCE: mark likes to fish for fish

FINAL VITERBI NETWORK

P(mark=noun) = 0.1957162916
P(mark=verb) = 0.0163096910
P(mark=inf) = 0.0000000272
P(mark=prep) = 0.0000000272
P(likes=noun) = 0.0000012558
P(likes=verb) = 0.0000127216
P(likes=inf) = 0.0000003588
P(likes=prep) = 0.0000058715
P(to=noun) = 0.0000000010
P(to=verb) = 0.0000000001
P(to=inf) = 0.0000027708
P(to=prep) = 0.0000010495
P(fish=noun) = 0.0000000714
P(fish=verb) = 0.0000001455
P(fish=inf) = 0.0000000000
P(fish=prep) = 0.0000000000
P(for=noun) = 0.0000000000
P(for=verb) = 0.0000000000
P(for=inf) = 0.0000000000
P(for=prep) = 0.0000000084
P(fish=noun) = 0.0000000006
P(fish=verb) = 0.0000000000
P(fish=inf) = 0.0000000000
P(fish=prep) = 0.0000000000

FINAL BACKPTR NETWORK

Backptr(likes=noun) = verb
Backptr(likes=verb) = noun
Backptr(likes=inf) = verb
Backptr(likes=prep) = noun
Backptr(to=noun) = verb
Backptr(to=verb) = noun
Backptr(to=inf) = verb
Backptr(to=prep) = verb
Backptr(fish=noun) = prep
Backptr(fish=verb) = inf
Backptr(fish=inf) = inf
Backptr(fish=prep) = noun
Backptr(for=noun) = verb
Backptr(for=verb) = noun
Backptr(for=inf) = verb
Backptr(for=prep) = verb
Backptr(fish=noun) = prep
Backptr(fish=verb) = noun
Backptr(fish=inf) = verb
Backptr(fish=prep) = noun

BEST TAG SEQUENCE HAS PROBABILITY = 0.0000000006
fish -> noun
for -> prep
fish -> verb
to -> inf
likes -> verb
mark -> noun
```

The Viterbi algorithm does an extremely good job at classifying POS tags. There are some instances where the algorithm could interpret the POS tag as another POS tag as any human would, but overall the algorithm does an extremely good job of classifying POS tags as a human would.

## Known Bugs, Problems, or Limitations
There are no known bugs, problems or limitations with the program that I have written.