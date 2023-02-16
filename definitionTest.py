'''
함수란?
f(x) => x값을 넣었을 때 x -> f(x) => y


장점 :
    1. 코드의 재사용 가능하다. 용이하다.
    2. 코드의 가독성이 좋다.
단점 :
    1. 무분별한 함수사용은 속도를 더 늦추게 하는 원인이 될 수 있다.



def add(): 내가 반복해서 시키고 싶은 문장들을 하나로 뭉쳐놓은 곳
    문장1
    문장2
    문장3

def minus(): 값을 돌려주고 싶다.
    계산 
    return 계산 < 이런 식으로 값을 돌려줄 수 있다. 
    
tkinter

GUI => graphic user interface

모듈

from tkinter import*
import tkinter

geometry(가로크기x세로크기) 
title('문자열')

component => 요소

1. Label(띄울 프레임창,옵션) => 하나의 문자열 
2. Entry(띄울 프레임창,옵션 ~~) => 입력칸 ******
3. Button(띄울 프레임창,command=add) => 버튼
4. Radiobutton(띄울 프레임창, 옵션~) => 
5. Checkbutton(띄울 프레임창,옵션~) => 

옵션 종류:
text = 'OK'
height , width
bg , fg bg='red' fg='white'
show='*'
command=


위젯을 배치
1. pack(side=RIGHT) => 수직,수평 정렬
    옵션 LEFT,RIGHT,TOP,BOTTOM
2. place 절대 배치
    place(x,y) x와 y의 좌표에 그냥 배치
3. grid
    격자 테이블 형식으로 배치
    grid(row=0,column=1)


from tkinter import messagebox
'''
from tkinter import *
def register(): #마우스 이벤트 처리
    #1. 내가 입력한 아이디 가져오기
    #2. 내가 입력한 비밀번호 가져오기
    #3. 1번에 해당하는 비밀번호가 맞는지 확인한다.
    #맞으면? 로그인 성공
    #틀리면? 로그인 실패 5번의 기회
    # 똑같은 아이디로 5번 실패했을 시 시도할 수 없도록
    id_string = Id.get()
    paswword_string=Password.get()
    
root = Tk() #하나의 프레임창 만들기 
root.geometry('500x350')
root.title('간단한 프로그램')
login_information = {'123':'321'}  #(key : value) 
#key => id
#value => password 
l1 = Label(root,text='라벨 1') #만들기만 한다.
l2 = Label(root,text='라벨 2')
l3 = Label(root,text='라벨 3')
b1 = Button(root,text='확인',command=register)

Id = Entry(root)
Password = Entry(root)

l1.pack(side=LEFT) 
l2.place(x=30,y=30)
l3.pack(side=LEFT)
b1.pack(side=LEFT)

Id.pack(side=LEFT)
Password.pack(side=LEFT)

root.mainloop() #프레임 창 꺼지지 않도록 막는다.