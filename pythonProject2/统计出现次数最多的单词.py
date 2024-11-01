word_counts= {}


with open('./word.txt')as f:
    for line  in f:
        line=line.strip()
        words=line.split()
        for word in words:
            if word  not in word_counts:
                word_counts[word]=0
            word_counts[word] +=1




print((sorted(word_counts.items(),key=lambda x:x[-1],reverse=True))[:10])