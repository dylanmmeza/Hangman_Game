from sys import argv

""" Creates a list,the size of argv[2], and fills each index with "_" """
def First_Progress(len_word):
  blanks=[]
  for x in range(len_word):
    blanks.append("_")
  return blanks

""" Creates a list of lists, with the individual list being ex: [a__l_,apple] (only for 1st time)"""
def List_Words(words_txt,length,letter):
  poss_words=[]
  combo_words=[]
  for w in words_txt:
    if len(w)==length:
      poss_words.append(w)

  for w in poss_words:
    show_word=[]
    one_word=[]
    for c in range(len(w)):
      if w[c]==letter:
        show_word.append(letter)
      else:
        show_word.append("_")
      one_word=[''.join(show_word),w]
    combo_words.append(one_word)

  return combo_words

""" Creates a list of lists, with the individual list being ex: [a__l_,apple] """
def Check_word(words,letter,len_word):
  all_words=[]
  for w in words:
    string=list(w[1])
    show_word=list(w[0])
    for c in range(len_word):
      if string[c]==letter:
        show_word[c]=(letter)
      elif show_word[c]==("_") and string[c]!=letter:
        show_word[c]=="_"
    all_words.append([''.join(show_word),''.join(string)])
  return all_words

""" Creates the dictionary of blanks and repititions ex:{'a__l_':1}"""
def Dict_words(list_words):
  d={}
  for x in list_words:
    if x[0] in d:
      d[x[0]]+=1
    else:
      d[x[0]]=1

  return dict(sorted(d.items(),key=lambda x:x[1])) 

""" returns a dictionary with the new set of words to look for. ex: returns {'____':628}"""
def remove_dic(words,letter,d,b):
  max_val=max(d.values())
  new_dic={}
  new_new_dic={}
  old=0
  old_temp=0

  for key in d:
    temp_list=[]
    if d.get(key)==max_val:
      new_dic[key]=max_val

    if len(new_dic)>1:
      for key in new_dic:
        new_new_dic={}
        count_blank=key.count("_")

        if count_blank>old:
          old=count_blank
          new_new_dic[key]=max_val

        if count_blank==old:
          for w in words:
            sub=w[0]
            if sub==key:
              temp_list.append(w[1])

          for temp in temp_list:
            count_temp=0
            for c in temp:
              count_temp+=ord(c)
            if count_temp>old_temp:
              old_temp=count_temp
              final_word=temp

          for w in words:
            if w[1]==final_word:
              new_new_dic[w[0]]=max_val

        if len(new_new_dic)>=1:
          new_dic={}
          new_dic=new_new_dic

  return new_dic

""" removes words not in the new dictionary key from possible words"""
def remove_words_list(new_dic,word_combo):
  new_words=[]
  for key in new_dic:
    for w in word_combo:
      if w[0]==key:
        new_words.append(w)
  return new_words

""" Creates a list of all the missed letters for words.txt, since you are looking at more then one word at a time"""
def wrong_letters(Dict_words,letter,blanks,list_words,m):
  for key in Dict_words:
    if key==blanks:
      m.append(letter)
    else:
      for w in list_words:
        substring=w[1]
        if key==w[0]:
          if substring.count(letter)==0:
            m.append(letter)
            break

  return m

""" prints the dictionaries to show computer cheating"""
def debug_print(s):
  if len(argv) > 4:
    for key in s:
      print(f"{key}:{s[key]}")     

def run():
  guesses=int(argv[3])
  len_word=int(argv[2])
  txt_file=open(argv[1],'r').read().splitlines()
  words_rows=sorted(txt_file, key=lambda sub: ord(max(sub))) 
  letter=''
  words=List_Words(words_rows,len_word,letter)
  show=''.join(First_Progress(len_word))
  blank=''.join(First_Progress(len_word))
  missed=[]
  new_guesses=guesses

  """ Lets game keep running while user still has guesses reamaning """
  while new_guesses>0:
    if len(argv)>4:
      print(f"{len(words)} words left.")
    print(show)
    print(f"missed letters: {' '.join(missed)} ({new_guesses} chances left)")
    letter=input("Enter your guess: ")

    words=Check_word(words,letter,len_word)
    if len(words)==0:
      print()
      print(f"No words with length {len_word}")
      exit()
    DictWords=Dict_words(words)
    Debug=debug_print(DictWords)    
    DictWords=remove_dic(words,letter,DictWords,blank)
    missed=wrong_letters(DictWords,letter,blank,words,missed)
    words=remove_words_list(DictWords,words)  
    for key in DictWords:
      show=key
    new_guesses=guesses-(len(missed)) 
    print()

    """ determines if game should keep playing or print final message """
    if new_guesses<=0:
      print(f"You lost after {argv[3]} wrong guesses.")    
    if len(words)==1:
      for c in words:
        if c[0]==c[1]:
          print(f"You guessed the word: {c[1]}")
          new_guesses=-1

  return

if __name__ == '__main__':
  run()

#python3 hangman.py w1.txt 7 10
#python3 hangman.py w1.txt 6 4
#python3 hangman.py words.txt 7 10 
#python3 hangman.py words.txt 3 5 debug
#python3 hangman.py words.txt 19 10 debug 
#python3 hangman.py w1.txt 8 7 debug
#python3 hangman.py w1.txt 8 7 
#python3 hangman.py words.txt 19 10

