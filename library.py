class users:
    def check_details_librarian(self,name,pw):
        with open ('users_data.txt') as f:
            f.seek(0)
            a=f.readline()
            b=a.split(',')
            if b[0]==name and b[2]==pw+'\n':
                print('You have access to library management system!')
                return True
            else:
                print('Incorrect password')
                return False
    def verify_useraccount(self,name):
        self.n=name
        with open ('users_data.txt') as f:
            f.seek(0)
            f.readline()
            a=f.readlines()
            for i in range(len(a)):
                b=a[i]
                c=b.split(',')       
            for j in c:
                if c[0]==self.n:
                    print(c)
                    print('Access granted!')
                    return True
                else:
                    print('No user found:(')
                    return None
    def create_useraccount(self,name,email,pw):
        self.n=name
        self.e=email
        self.password=pw
        self.account=self.n+','+self.e+','+self.password+'\n'
        print(self.account)
        with open ('users_data.txt','a') as f:
            f.write(self.account)
        print("Your membership has been approved!")      
    def cancel_membership(self,record):
        with open("users_data.txt", "r") as f:
            b= f.readlines()
        with open("users_data.txt", "w") as f:
            for line in b:
                if line.strip("\n") != record:
                    f.write(line)
class librarian(users):
    def add_book(self,ID,t,a,p,q,l):
        self.book_id=ID
        self.title=t
        self.author=a
        self.pub_date=p
        self.quantity=q
        self.lending_fees=l
        self.new_book=str(self.book_id)+','+self.title+','+self.author+','+self.pub_date+','+str(self.quantity)+','+str(self.lending_fees)+'\n'
        print(self.new_book)
        with open ('books.txt','a') as f:
            f.write(self.new_book)
        print("Book added successfully")
    def remove_book(self,br):
        with open("books.txt", "r") as f:
            f.seek(0)
            a=f.readlines()
            for i in a:
                i.strip('\n')
                #print(i)
            self.book_to_remove=br    
            new_lst=[]
            for book in a:
                if self.book_to_remove in book:
                    continue
                else:
                    new_lst.append(book) 
        with open("books.txt", "w") as f:
            for item in new_lst:
                    f.write(item)
        print("Book removed successfully")       
class features(users):
    def display_books(self):
        with open ('books.txt') as f:
            f.seek(0)
            a=f.readlines()
            temp_lst=[]
            for i in range(len(a)):
                b=a[i]
                c=b.split(',') 
                temp_lst.append(c)
            print ("{:<5} {:<35} {:<30}{:<20}{:<15}{:<15}".format('BOOK_ID','TITLE','AUTHOR','PUBLICATION_DATE','QUANTITY','LENDING_PRICE'))
            for v in temp_lst:
                book_id,title,author,publication_date,quantity,lending_price = v
                print ("{:<5} {:<35} {:<30}{:<20}{:<15}{:<15}".format(book_id,title,author,publication_date,quantity,lending_price))
    def search_book(self,br):
        with open("books.txt", "r") as f:
            f.seek(0)
            a=f.readlines()
            for i in a:
                i.strip('\n')
                #print(i)
            self.book_to_search=br   
            new_lst=[]
            for book in a:
                if self.book_to_search in book:
                    new_lst.append(book)
                else:
                    continue
            print("{:<5} {:<35} {:<30}{:<20}{:<15}{:<15}".format('BOOK_ID','TITLE','AUTHOR','PUBLICATION_DATE','QUANTITY','LENDING_PRICE'))
            for j in new_lst:
                k=j.split(',')
                print(f'\n{k[0]:5}{k[1]:35}{k[2]:30}{k[3]:20}{k[4]:15}{k[5]:15}',end='')  
    def return_book(self):
        book_name=input('Enter book you want to return:')
        with open ('books.txt') as f:
            f.seek(0)
            a=f.readlines()
            temp_lst=[]
            for i in range(len(a)):
                b=a[i]
                c=b.split(',')
                if book_name in c:
                    c[4]=int(c[4])
                    c[4]+=1
                    print (c)
                    print('Thank you for returning the book!')    
    def renew_book(self):
        book_name=input('Enter book you want to renew:')
        with open ('books.txt') as f:
            f.seek(0)
            a=f.readlines()
            temp_lst=[]
            for i in range(len(a)):
                b=a[i]
                c=b.split(',')
                if book_name in c:
                    print('Book renewed!You have 10 more days to return the book')

    
    # Sorting using bubble sort        
    def sort_books(self): #This function sorts the books alphabetically.
        with open("books.txt", "a+") as f:
            f.seek(0)
            liness = f.readlines()
            new_lst = []
            for item in liness:
                item = item.split(",")
                lt = item.pop()
                new_lt = ""
                for character in lt:
                    if character == "\n":
                        continue
                    else:
                        new_lt += character
                item.append(new_lt)
                new_lst.append(item)
            alpha_list = []
            for item in new_lst:
                a = item[0]
                b = item[1]
                alpha_item = [b,a]
                alpha_list.append(alpha_item)
            length= len(alpha_list)
            for i in range(length-1):
                for j in range(0, length-i-1):
                    if alpha_list[j] > alpha_list[j + 1] :
                        alpha_list[j], alpha_list[j + 1] = alpha_list[j + 1], alpha_list[j]
            for item in alpha_list:
                print("Book Name: ", item[0])
                print("Book ID: ", item[1])
                print("^"*80)

import datetime as dt 
class date:
    def __init__(self):
        self.due_day = 0
        self.creation_date = dt.datetime.now()
        self.today = self.creation_date.strftime('%d')
        self.due_date()
    def issue_date(self):
        self.creation_date = dt.datetime.now()
        print('the book issued on', self.creation_date)
    def due_date(self):
        self.month =self.creation_date.strftime('%m')
        if int(self.today) > 20 :
            if int(self.month)%2 == 0:
                due = 30 - int(self.today)
                self.due_day = 10 - due
            elif int(self.month)%2 != 0:
                due = 31 - int(self.today)
                self.due_day = 10 - due
        else:
            self.due_day = int(self.today) + 10
            # print('you have 10 days to return the book')
        return self.due_day
    def check_fine(self):
        print('Welcome Again <3 Now you can return the book')
        day = input('Enter today date in local format dd/mm/yy')
        self.d = day[:2]
        self.m = day[3:5]
        print(self.month)
        if int(self.today)<= int(self.d) <=self.due_day:
            print('no fine')
        elif int(self.month) != self.m:
            print('You\'re a month late , fine is applicable for you' )
        else:
            print('you run out of day , You have to pay of 50 Rs for fine')
            
class BookReservation(date):
    def fetch_reservation_details(self):#gets the details regarding reservation
        reserve = input('enter the name of book you want to reserve')
        if reserve not in BookItem.book:#sees if the mentioned book is in the book dictionary
            print('Book is not available to reserve')
        else:
            print('your book is reserved now, you can lend it whenever you want')

class BookItem:
    book = {'A Thousand Splendid Sun': '1','One Hundred Years of Solitude':'2', 'Where the Crawdads Sing':'3' ,'Celestial Bodies':'4','Charlotte\'s Web':'5','The Heart of the Matter':'6','Silent Patient':'7',
             'Harry Potter':'8','Ulysses':'9' ,'Hamlet':'10','Right Under Our Nose':'11','When Breath Becomes Air':'12',
             'The Phantom Tollbooth':'13','Fear of Flying':'14','The Adventures of Tom Sawyer':'15','In the Heart of the Sea':'16','Mind-Master':'17','Alchemist':'18','Cheque book':'19','Lolita':'20',
             'The Overstory':'21','In Search of Lost Time':'22','War and Peace':'23','Vahana Masterclass':'24','Letting Go':'25','Educated':'26','Encyclopedia Brown Boy Detective':'27','Little Women':'28','The Great Gatsby':'29','The Handmaid\'s Tale':'30'}

class BookLending(BookItem,date):
  def __init__(self):
    super().__init__()
    self.d=date()
  def lend_book(self):
    user_input = input('Enter the name of book you want to lend:')
    if user_input in BookItem.book:
        print(f'the book{user_input} is issued')
        print(f'the issued date is {self.d.creation_date}')
        print(f'the due date is {self.d.due_day}')
    else:
        print('Book is not available')



#DRIVER CODE        
print('********************************')
print('WELCOME IN THE LIBRARY INFINITE')
print('(1)Log in as a librarian\n'\
     '(2)Log in as a member\n'\
     '(3)Create account\n'\
     '(4)Cancel membership:',end='')
x=int(input())    
                      
if x==1:
    name = input('Enter your name: ')
    email=input('Enter email: ')
    pw=input('Enter password: ')
    object=users()
    check=object.check_details_librarian(name,pw)
    while check==True:
        print()
        print ('*-*-*-*-*-*-*-*-*-*-*-* SELECT THE OPTIONS BELOW *-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print('1. Add a book')
        print('2. Display books')
        print('3. Lend a book')
        print('4. Reserve a book')
        print('5. Return a book')
        print('6. Remove book')
        print('7. Search a book')
        print('8. Sort books alphabetically')
        print('9. Renew a book')  
        print('press any other number to exit')

        y=int(input('Enter your choice: '))
        obj=librarian()
        fet=features()
        obj1=BookLending()
        obj2=BookReservation()
        if y==1:
            book_id=input('Enter book_id: ')
            title=input('Enter title of the book: ')
            author=input('Enter name of the author: ')
            pub_date=input("Enter publication Date in the format DD/MM/YYYY: ")
            quantity=int(input('Enter quantity: '))
            lending_fees=int(input('Enter Lending Price: '))
            obj.add_book(book_id,title,author,pub_date,quantity,lending_fees)
        elif y==2:
            fet.display_books()
        elif y==3:    
            obj1.lend_book()
        elif y==4:
            obj2.fetch_reservation_details()
        elif y==5:
            fet.return_book()
        elif y==6:
            book_to_remove=input('Enter book title inorder to remove it: ')   
            obj.remove_book(book_to_remove)        
        elif y==7:
            search_by=int(input('Search by (1)Title (2)Author or (3)Publication date:'))
            if search_by==1:
                search_title=input('Enter title of the book: ')                  
                fet.search_book(search_title)
            elif  search_by==2:
                search_author=input('Enter author of the book: ')  
                fet.search_book(search_author) 
            elif  search_by==3:
                search_pubdate=input('Enter publication date of the book: ')  
                fet.search_book(search_pubdate)
            else:
                print("You are requested to enter the correct option.")            
        elif y==8:
            fet.sort_books()
        elif y==9:
            fet.renew_book()    
        else:
            break
elif x==2:
    name = input('Enter your name: ')
    email=input('Enter email: ')
    pw=input('Enter password: ')
    obj=users()
    check=obj.verify_useraccount(name)
    while check==True:
        print()
        print ('*-*-*-*-*-*-*-*-*-*-*-* SELECT THE OPTIONS BELOW *-*-*-*-*-*-*-*-*-*-*-*-*-*\n' )
        print('1. Display books')
        print('2. Lend a book')
        print('3. Reserve a book')
        print('4. Return a book')
        print('5. Renew a book')
        print('6. Search a book')
        print('7. Sort books alphabetically') 
        print('press any other number to exit') 
        y=int(input('Enter your choice: '))
        obj=librarian()
        fet=features()
        obj1=BookLending()
        obj2=BookReservation()
        if y==1:
            fet.display_books()
        elif y==2:    
            obj1.lend_book()
        elif y==3:
            obj2.fetch_reservation_details()
        elif y==4:
            fet.return_book()
        elif y==5:
            fet.renew_book()           
        elif y==6:
            search_by=int(input('Search by (1)Title (2)Author or (3)Publication date:'))
            if search_by==1:
                search_title=input('Enter title of the book: ')                  
                fet.search_book(search_title)
            elif  search_by==2:
                search_author=input('Enter author of the book: ')  
                fet.search_book(search_author) 
            elif  search_by==3:
                search_pubdate=input('Enter publication date of the book: ')  
                fet.search_book(search_pubdate)
            else:
                print("You are requested to enter the correct option.")            
        elif y==7:
            fet.sort_books()
        else:
            break
elif x==3:
    name = input('Enter your name: ')
    email=input('Enter email: ')
    pw=input('Enter password: ')
    obj=users()
    check=obj.create_useraccount(name,email,pw)    
    while check==True:
        print()
        print ('*-*-*-*-*-*-*-*-*-*-*-* SELECT THE OPTIONS BELOW *-*-*-*-*-*-*-*-*-*-*-*-*-*\n' )
        print('1. Display books')
        print('2. Lend a book')
        print('3. Reserve a book')
        print('4. Return a book')
        print('5. Renew a book')
        print('6. Search a book')
        print('7. Sort books alphabetically') 
        print('press any other number to exit') 

        y=int(input('Enter your choice: '))
        obj=librarian()
        fet=features()
        obj1=BookLending()
        obj2=BookReservation()
        if y==1:
            fet.display_books()
        elif y==2:    
            obj1.lend_book()
        elif y==3:
            obj2.fetch_reservation_details()
        elif y==4:
            fet.return_book()
        elif y==5:
            fet.renew_book()           
        elif y==6:
            search_by=int(input('Search by (1)Title (2)Author or (3)Publication date:'))
            if search_by==1:
                search_title=input('Enter title of the book: ')                  
                fet.search_book(search_title)
            elif  search_by==2:
                search_author=input('Enter author of the book: ')  
                fet.search_book(search_author) 
            elif  search_by==3:
                search_pubdate=input('Enter publication date of the book: ')  
                fet.search_book(search_pubdate)
            else:
                print("You are requested to enter the correct option.")            
        elif y==7:
            fet.sort_books()
        else:
            break
elif x==4:
    name = input('Enter your name: ')
    email=input('Enter email: ')
    pw=input('Enter password: ')
    l=name+','+email+','+pw
    obj=users()
    obj.cancel_membership(l)
else:
    print('Thank you for visiting!!')