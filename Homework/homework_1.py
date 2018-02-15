"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    temp_string = ''
    for s in dna:
        if s == 'C':
            temp_string += 'G'
        elif s == "A":
            temp_string += 'T'
        elif s == "T":
            temp_string += 'A'
        elif s == "G":
            temp_string += 'C'
        else:
            print('invalid')

    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    return temp_string
print(fast_complement('CTAG'))


def remove_interval(s, start , stop):
    t=s[:start]+s[stop+1:]
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    return t
print(remove_interval('ABCDEFGHI',2,5))

def kmer_list(s, k):
    kmers = []
    n = len(s)

    for i in range(0, n - k + 1):
        kmers.append(s[i:i + k])

    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    return kmers
print(kmer_list('mohith',2))


def kmer_set(s, k):
    kmers = set()
    n = len(s)

    for i in range(0, n - k + 1):
        kmers.add(s[i:i + k])

    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    return kmers
print(kmer_set('Mohith',2))

def kmer_dict(s, k):
    kmers = {}
    n = len(s)

    for i in range(0, n - k + 1):
        kmers[(s[i:i + k])] = 1


    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    return kmers
print(kmer_dict('mohith',2))

#Reading Files
def head(file_name):
    f = open("proper_fasta.fasta","r")
    for x in range(1,10):
        contents = f.readline()
        print(contents)
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    # return
head('')
def tail(file_name):
    with open("tricky_fasta.fasta", "r") as file:
        contents = file.readlines()
        print(contents[len(contents)-10:len(contents)])

    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    #return

tail(' ')

def print_even(file_name):
    with open('tricky_fasta.fasta', 'r') as infile:
        seqs = infile.read()
        x = seqs.split('\n')
        for s in range(0,len(x),2):
            print(x[s])

    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
print_even(' ')


def csv_list(file_name):
    with open('mohith.fasta', 'r') as infile:
        x = infile.readlines()
        list=[]
        for s in x:
            y = s.split(',')
            list.append(y)

    """``
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    return list
print(csv_list(''))

def get_csv_column(file_name, column):
    with open('mohith.fasta', 'r') as infile:
            x = infile.readlines()
            list = []
            for s in x:
                y = s.split(',')
                list.append(y[column])
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    return list
print (get_csv_column('', 1 ))

def fasta_seqs(file_name):
    with open('tricky_fasta.fasta','r') as infile:
        sequence = []
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            x = seq.split('\n', 1)
    sequence = x[1].replace('\n', '')

    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    return sequence
print(fasta_seqs('tricky_fasta.fasta'))

def fasta_headers(file_name):
    with open('tricky_fasta.fasta','r') as infile:
        header = set()
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            x = seq.split('\n', 1)
            header.add(x[0])


    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    return header
print(fasta_headers('tricky_fasta.fasta'))

def fasta_dict(file_name):
    with open('tricky_fasta.fasta','r') as infile:
        dict = {}
        text = infile.read ()
        seqs = text.split('>')
        for seq in seqs:
            if seq != '':
                x = seq.split('\n', 1)
                dict[x[0]] = x[1]

    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    return dict
print(fasta_dict('tricky_fasta.fasta'))

def fastq_to_fasta(file_name, new_name=None):


    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    return

# Transcription and Translation
def reverse_complement(dna):
    temp_string = ''
    for s in dna:
        if s == 'C':
            temp_string += 'G'
        elif s == "A":
            temp_string += 'T'
        elif s == "T":
            temp_string += 'A'
        elif s == "G":
            temp_string += 'C'
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    return temp_string[::-1]
print(reverse_complement('CTAGGATC'))

def transcribe(dna):
    temp_string = ''
    for s in dna:
        if s == 'C':
            temp_string += 'G'
        elif s == "A":
            temp_string += 'U'
        elif s == "T":
            temp_string += 'A'
        elif s == "G":
            temp_string += 'C'

    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    return temp_string
print(transcribe('CTAGFFFCTAGJBKJKCTAG'))

def translate(rna):


    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


    return

def reading_frames(dna):

    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """

    temporary = []

    a = dna[1:]
    b = dna[2:]

    temporary.append(dna)
    temporary.append(reverse_complement(dna))
    temporary.append(a)
    temporary.append(reverse_complement(a))
    temporary.append(b)
    temporary.append(reverse_complement(b))



    return temporary

print(reading_frames('TAGGTACTAGC'))