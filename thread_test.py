#!/usr/bin/env python
# coding=utf-8
import threading


def fun1():
    i = 5
    while i > 0:
        print("this fun1 ")
        i = i - 1


def fun2():
    i = 5
    while i > 0:
        print("this fun2 ")
        i = i - 1


run_fun1 = threading.Thread(target=fun1, name="fun1_run")
run_fun2 = threading.Thread(target=fun2, name="fun2_run")
run_fun1.start()
run_fun2.start()
run_fun1.join()
print("fun1 end")
run_fun2.join()

g = 0
lock = threading.Lock()


def change1():
    global g
    i = 5
    lock.acquire()
    while i > 0:
        g = g - 1
        g = g + 1
        print(g)
        i = i - 1
    lock.release()


def change2():
    global g
    i = 5
    while i > 0:
        g = g - 5
        g = g + 5
        print(g)
        i = i - 1


fun_change1 = threading.Thread(target=change1, name='change1_run')
fun_change2 = threading.Thread(target=change2, name='change2_run')
fun_change1.start()
fun_change2.start()
fun_change1.join()
fun_change2.join()
print("end")
localvar = threading.local()


def startthread(var):
    localvar.var = var
    do()
    localvar.var = "none"
    do()


def do():
    var = localvar.var
    print(var)
    print("Thread is %s" % (threading.current_thread().name))


run1 = threading.Thread(target=startthread, args=("var1",), name="first")
run2 = threading.Thread(target=startthread, args=("var2",), name="second")
run1.start()
run2.start()
run1.join()
run2.join()
