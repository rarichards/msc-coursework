import statistics

open('lessthan30.fastq', 'w')
open('atleast30.fastq', 'w')

with open('seq_sample.fastq') as openfile:
	inlist = openfile.readlines()			                                    #read file in

sample_list = [i.rstrip('\n') for i in inlist]			                        #remove \n

for count in range(0, len(inlist), 8):
  
    sample_id1 = sample_list[count]
    q_val1 = sample_list[count+3]
    
    sample_id2 = sample_list[count+4]
    q_val2 = sample_list[count+7]

#find ascii vales using ord command

    Q1 = []
    for q in q_val1:
        val = ord(q) - 64
        Q1.append(val)

    mQ1 = statistics.mean(Q1)

    Q2 = []
    for q in q_val2:
        val = ord(q) - 64
        Q2.append(val)
		
    mQ2 = statistics.mean(Q2)

    if (mQ1 < 30) or (mQ2 < 30):
        with open('lessthan30.fastq', 'a') as openfile:
            for l in range(count, count+7):
                openfile.write(inlist[l])
                
    elif (mQ1 >= 30) or (mQ2 >= 30):
        with open('atleast30.fastq', 'a') as openfile:
            for l in range(count, count+7):
                openfile.write(inlist[l])