class Game :

      def __init__(self):
            while True:
                  print (''' welcome to our Game

                  press 1 to play Multipcation Table game
                  press 2 to play Remove Duplicates Game
                  press 3 to play Divede Numbers Game
                  press 4 to Exit
      ''')
                  
                  user_chois=int(input('Enter your number Game'))
                  if user_chois >4 :
                        print (' pleace inter number between 1 , 4' )

                  elif user_chois ==1 :
                        self.game1()

                  elif user_chois==2:
                        self.game2()
                  elif user_chois ==3:
                        self.game3()

                  elif user_chois==4:
                        print('GodBey')
                        return
                  play_again = input('when you play again press any key , press n to Exit')
                  if play_again =='n' :
                        print ('Godbey')
                        break

      def game1 (self):
            start=int(input('enter Your Start Numbers'))
            end=int(input('enter Your End Numbers'))
            for x in range (start,end):
                  for y in range (1,13):
                        print (f'{x} X {y} ≈ {x*y}')

      def game2 (x):
            word=x.split('   ')
            new_word=[]
            for w in word:
                  if w in new_word:
                        continue
                  else:
                        new_word.append(w)
            print(new_word)
                  
                  

      def game3(self):
            print(list(x for x in range (1,101) if x%2 ==0 ))


g=Game()
g.game2('my my name name name name is is is ehsa ehsan ehsan')



















