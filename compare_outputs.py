import sys

argument_list = str(sys.argv)
plus_file = str(sys.argv[1])
moins_file = str(sys.argv[2])
true_labels_file = str(sys.argv[3])


with open(plus_file) as f:
    plus = f.read().splitlines()

with open(moins_file) as f:
    moins = f.read().splitlines()
            
with open(true_labels_file) as f:
    true_labels = f.read().splitlines()
    
assert len(plus) == len(true_labels)
assert len(moins) == len(true_labels)
    
number_of_lines = len(true_labels)
count_plus = 0.0
count_moins = 0.0
for i in range(number_of_lines):
    if plus[i] == true_labels[i]:
	count_plus += 1.0
    if moins[i] == true_labels[i]:
	count_moins += 1.0

count_plus =  count_plus / number_of_lines * 100
count_moins = count_moins / number_of_lines * 100
            
print("Plus performante: %.4f" % count_plus)
print("Moins performante: %.4f" % count_moins)
