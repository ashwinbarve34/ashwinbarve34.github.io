import sys
import os
import random

final = []
count = 0;
count1 = 0;
count2 = 0;
count3 = 0;
count4 = 0;
count5 = 0;
inter = 0;
maid = 0;
te = 0;
swe = 0;
mea = 0;
nut = 0;
spi = 0;
tri = 0;
par = 0;
tw = 0;
th = 0;
fia = 0;
aud = 0;
sco = 0;
m = 0;
f = 0;
b = 0;
p = 0;
s = 0;
g = 0;
r = 0;
mo = 0;
t = 0;
pa = 0;
re = 0;
mor = 0;

#create dictionary for following fields:

#profession, age, marital_status, spouse, children, gross annual income,

#gross monthly income, saving types,

def tax(gai, mi):
    global nmi
    global ft
    global mft
    if int(gai) >= 500000:
        ft = percentage(20, int(gai));
        mft = ft / 12;
        print ("\nYour Federal Income Tax is 20% of your gross annual income");
        print ("\nFederal Income Tax : Rs", ft);
        print ("\nTotal Monthly Tax : Rs", mft);
        nmi = int(mi) - mft;
        print ("\nNet Monthly Income : Rs", nmi);
        return [int(ft), int(mft), int(nmi)]
    else:
        ft = percentage(5, int(gai));
        mft = ft / 12;
        print ("\nYour Federal Income Tax is 5% of your gross annual income");
        print ("\nFederal Income Tax : Rs", ft);
        print ("\nTotal Monthly Tax : Rs", mft);
        nmi = int(mi) - mft;
        print ("\nNet Monthly Income : Rs", nmi);
        return [int(ft), int(mft), int(nmi)]

def percentage(percent, whole):
  return (percent * whole) / 100.0

def hnmi():
    global nmi
    return (int(nmi))

def annual():
    global ai
    return (int(ai))

def month():
    global monthly
    return (int(monthly))

def nmi():
    global nmi
    global save4
    global bi
    global a
    bi = int(nmi) - int(save4)
    a = nmi - save4
    return (bi)

def remain():
    global bi
    if bi != 0:
        return (bi)
    else:
        return "Congratulations!"

def left():
    global bi
    global save4
    total = int(bi) + int(save4)
    return (total)

def listed():
    global nmi
    global ft
    global mft
    return [int(ft), int(mft), int(nmi)]

#--------------------------------------------GROCERY--------------------------------------------------------GROCERY----------------------------|

def grocery(gro):
    global bi
    answer = 2;
    if int(gro) == int(answer):
        return "Correct answer. Well Done!"
    else:
        return "Sorry. Your answer is wrong. Please try again."

def grocery1(option):
    global bi
    global count
    global m
    global f
    global te
    global nut
    global spi
    global swe
    global mea
    global final
    if count == 0:
        if 'milk' in option:
            bi = bi - 120;
            m = 1;
            count = count + 1;
            final.append('milk')
        else:
            m = 0;
        if 'fruits' in option:
            bi = bi - 100;
            count = count + 1;
            f = 1;
            final.append('fruits')
        else:
            f = 0;
        if 'tea' in option:
            bi = bi - 120;
            count = count + 1;
            te = 1;
            final.append('tea')
        else:
            te = 0;
        if 'sweet' in option:
            bi = bi - 120;
            count = count + 1;
            swe = 1;
            final.append('sweet')
        else:
            swe = 0;
        if 'meat' in option:
            bi = bi - 120;
            count = count + 1;
            mea = 1;
            final.append('meat')
        else:
            mea = 0;
        if 'nuts' in option:
            bi = bi - 120;
            count = count + 1;
            nut = 1;
            final.append('nuts')
        else:
            nut = 0;
        if 'spices' in option:
            bi = bi - 120;
            count = count + 1;
            spi = 1;
            final.append('spices')
        else:
            spi = 0;
        return 'Amount left to allocate is Rs.', bi
    else:
        if 'milk' in option:
            if m == 1:
                bi = bi;
            elif m == 0:
                bi = bi - 120;
                m = 1;
                final.append('milk')
        else:
            if m == 1:
                bi = bi + 120;
                m = 0;
                final.remove('milk')
        if 'fruits' in option:
            if f == 1:
                bi = bi;
            elif f == 0:
                bi = bi - 100;
                f = 1;
                final.append('fruits')
        else:
            if f == 1:
                bi = bi + 100;
                f = 0;
                final.remove('fruits')
        if 'tea' in option:
            if te == 1:
                bi = bi;
            elif te == 0:
                bi = bi - 120;
                te = 1;
                final.append('tea')
        else:
            if te == 1:
                bi = bi + 120;
                te = 0;
                final.remove('tea')
        if 'sweet' in option:
            if swe == 1:
                bi = bi;
            elif swe == 0:
                bi = bi - 120;
                swe = 1;
                final.append('sweet')
        else:
            if swe == 1:
                bi = bi + 120;
                swe = 0;
                final.remove('sweet')
        if 'meat' in option:
            if mea == 1:
                bi = bi;
            elif mea == 0:
                bi = bi - 120;
                mea = 1;
                final.append('meat')
        else:
            if mea == 1:
                bi = bi + 120;
                mea = 0;
                final.remove('meat')
        if 'nuts' in option:
            if nut == 1:
                bi = bi;
            elif nut == 0:
                bi = bi - 120;
                nut = 1;
                final.append('nuts')
        else:
            if nut == 1:
                bi = bi + 120;
                nut = 0;
                final.remove('nuts')
        if 'spices' in option:
            if spi == 1:
                bi = bi;
            elif spi == 0:
                bi = bi - 120;
                spi = 1;
                final.append('spices')
        else:
            if spi == 1:
                bi = bi + 120;
                spi = 0;
                final.remove('spices')
        return 'Amount left to allocate is Rs.', bi


#-----------------------------------FITNESS-----------------------------------FITNESS-----------------------------------------|

def fitness(pho):
    global bi
    answer = 2;
    if int(pho) == int(answer):
        return "Correct answer. Well Done!"
    else:
        return "Sorry. Your answer is wrong. Please try again."

def fitness1(option):
    global bi
    global count2
    global s
    global g
    global final
    print (final)
    if count2 == 0:
        if 'sports' in option:
            bi = bi - 700;
            s = 1;
            count2 = count2 + 1;
            final.append('sports')
        else:
            s = 0;
        if 'gym' in option:
            bi = bi - 1400;
            count2 = count2 + 1;
            g = 1;
            final.append('gym')
        else:
            g = 0;
        return 'Amount left to allocate is Rs.', bi
    else:
        if 'sports' in option:
            if s == 1:
                bi = bi;
            elif s == 0:
                bi = bi - 700;
                s = 1;
                final.append('sports')
        else:
            if s == 1:
                bi = bi + 700;
                s = 0;
                final.remove('sports')
        if 'gym' in option:
            if g == 1:
                bi = bi;
            elif g == 0:
                bi = bi - 1400;
                g = 1;
                final.append('gym')
        else:
            if g == 1:
                bi = bi + 1400;
                g = 0;
                final.remove('gym')
        return 'Amount left to allocate is Rs.', bi

#--------------------------------------HOUSING-------------------------------HOUSING------------------------------------------|

def housing(hou):
    global bi
    answer = 2;
    if int(hou) == int(answer):
        return "Correct answer. Well Done!"
    else:
        return "Sorry. Your answer is wrong. Please try again."

def housing1(option):
    global bi
    global count5
    global re
    global mor
    global tw
    global th
    global final
    if count5 == 0:
        if 'rent' in option:
            bi = bi - 11000;
            re = 1;
            count5 = count5 + 1;
            final.append('rent')
        else:
            re = 0;
        if 'mortgage' in option:
            bi = bi - 20000;
            count5 = count5 + 1;
            mor = 1;
            final.append('mortgage')
        else:
            mor = 0;
        if 'two' in option:
            bi = bi - 35000;
            count5 = count5 + 1;
            tw = 1;
            final.append('two')
        else:
            tw = 0;
        if 'three' in option:
            bi = bi - 50000;
            count5 = count5 + 1;
            th = 1;
            final.append('three')
        else:
            th = 0;
        return 'Amount left to allocate is Rs.', bi
    else:
        if 'rent' in option:
            if re == 1:
                bi = bi;
            elif re == 0:
                bi = bi - 12000;
                re = 1;
                final.append('rent')
        else:
            if re == 1:
                bi = bi + 12000;
                re = 0;
                final.remove('rent')
        if 'mortgage' in option:
            if mor == 1:
                bi = bi;
            elif mor == 0:
                bi = bi - 20000;
                mor = 1;
                final.append('mortgage')
        else:
            if mor == 1:
                bi = bi + 20000;
                mor = 0;
                final.remove('mortgage')
        if 'two' in option:
            if tw == 1:
                bi = bi;
            elif tw == 0:
                bi = bi - 35000;
                tw = 1;
                final.append('two')
        else:
            if tw == 1:
                bi = bi + 35000;
                tw = 0;
                final.remove('two')
        if 'three' in option:
            if th == 1:
                bi = bi;
            elif th == 0:
                bi = bi - 50000;
                th = 1;
                final.append('three')
        else:
            if th == 1:
                bi = bi + 50000;
                th = 0;
                final.remove('three')
        return 'Amount left to allocate is Rs.', bi
    
#---------------------------------------------TRANSPORT-----------------------------TRANSPORT---------------------------------------|

def transportation(tra):
    global bi
    answer = 2;
    if int(tra) == int(answer):
        return "Correct answer. Well Done!"
    else:
        return "Sorry. Your answer is wrong. Please try again."

def transportation1(option):
    global bi
    global count4
    global t
    global pa
    global fia
    global aud
    global sco
    global final
    if count4 == 0:
        if 'taxi' in option:
            bi = bi - 1700;
            t = 1;
            count4 = count4 + 1;
            final.append('taxi')
        else:
            t = 0;
        if 'pass' in option:
            bi = bi - 1400;
            count4 = count4 + 1;
            pa = 1;
            final.append('pass')
        else:
            pa = 0;
        if 'fiat' in option:
            bi = bi - 20000;
            count4 = count4 + 1;
            fia = 1;
            final.append('fiat')
        else:
            fia = 0;
        if 'audi' in option:
            bi = bi - 40000;
            count4 = count4 + 1;
            aud = 1;
            final.append('audi')
        else:
            aud = 0;
        if 'scooty' in option:
            bi = bi - 10000;
            count4 = count4 + 1;
            sco = 1;
            final.append('scooty')
        else:
            sco = 0;
        return 'Amount left to allocate is Rs.', bi
    else:
        if 'taxi' in option:
            if t == 1:
                bi = bi;
            elif t == 0:
                bi = bi - 1700;
                t = 1;
                final.append('taxi')
        else:
            if t == 1:
                bi = bi + 1700;
                t = 0;
                final.remove('taxi')
        if 'pass' in option:
            if pa == 1:
                bi = bi;
            elif pa == 0:
                bi = bi - 1400;
                pa = 1;
                final.append('pass')
        else:
            if pa == 1:
                bi = bi + 1400;
                pa = 0;
                final.remove('pass')
        if 'fiat' in option:
            if fia == 1:
                bi = bi;
            elif fia == 0:
                bi = bi - 20000;
                fia = 1;
                final.append('fiat')
        else:
            if fia == 1:
                bi = bi + 20000;
                fia = 0;
                final.remove('fiat')
        if 'audi' in option:
            if aud == 1:
                bi = bi;
            elif aud == 0:
                bi = bi - 40000;
                aud = 1;
                final.append('audi')
        else:
            if aud == 1:
                bi = bi + 40000;
                aud = 0;
                final.remove('audi')
        if 'scooty' in option:
            if sco == 1:
                bi = bi;
            elif sco == 0:
                bi = bi - 10000;
                sco = 1;
                final.append('scooty')
        else:
            if sco == 1:
                bi = bi + 10000;
                sco = 0;
                final.remove('scooty')
        return 'Amount left to allocate is Rs.', bi


#------------------------------ENTERTAINMENT-----------------------------ENTERTAINMENT-------------------------------------------|


def entertainment(ent):
    global bi
    answer = 2;
    if int(ent) == int(answer):
        return "Correct answer. Well Done!"
    else:
        return "Sorry. Your answer is wrong. Please try again."

def entertainment1(option):
    global bi
    global count3
    global r
    global mo
    global tri
    global par
    global final
    if count3 == 0:
        if 'restaurant' in option:
            bi = bi - 3000;
            r = 1;
            count3 = count3 + 1;
            final.append('restaurant')
        else:
            r = 0;
        if 'movies' in option:
            bi = bi - 2000;
            count3 = count3 + 1;
            mo = 1;
            final.append('movies')
        else:
            mo = 0;
        if 'trip' in option:
            bi = bi - 4000;
            count3 = count3 + 1;
            tri = 1;
            final.append('trip')
        else:
            tri = 0;
        if 'party' in option:
            bi = bi - 3500;
            count3 = count3 + 1;
            par = 1;
            final.append('party')
        else:
            par = 0;
        return 'Amount left to allocate is Rs.', bi
    else:
        if 'restaurant' in option:
            if r == 1:
                bi = bi;
            elif r == 0:
                bi = bi - 3000;
                r = 1;
                final.append('restaurant')
        else:
            if r == 1:
                bi = bi + 3000;
                r = 0;
                final.remove('restaurant')
        if 'movies' in option:
            if mo == 1:
                bi = bi;
            elif mo == 0:
                bi = bi - 2000;
                mo = 1;
                final.append('movies')
        else:
            if mo == 1:
                bi = bi + 2000;
                mo = 0;
                final.remove('movies')
        if 'trip' in option:
            if tri == 1:
                bi = bi;
            elif tri == 0:
                bi = bi - 4000;
                tri = 1;
                final.append('trip')
        else:
            if tri == 1:
                bi = bi + 4000;
                tri = 0;
                final.remove('trip')
        if 'party' in option:
            if par == 1:
                bi = bi;
            elif par == 0:
                bi = bi - 3500;
                par = 1;
                final.append('party')
        else:
            if par == 1:
                bi = bi + 3500;
                par = 0;
                final.remove('party')
        return 'Amount left to allocate is Rs.', bi

#------------------------------UTILITIES-----------------------------UTILITIES-----------------------------------------|

def utilities(ele):
    global bi
    answer = 4;
    if int(ele) == int(answer):
        return "Correct answer. Well Done!"
    else:
        return "Sorry. Your answer is wrong. Please try again."

def utilities1(option):
    global bi
    global count1
    global b
    global p
    global inter
    global maid
    global final
    if count1 == 0:
        if 'basic' in option:
            bi = bi - 1200;
            b = 1;
            count1 = count1 + 1;
            final.append('basic')
        else:
            b = 0;
        if 'phone' in option:
            bi = bi - 600;
            count1 = count1 + 1;
            p = 1;
            final.append('phone')
        else:
            p = 0;
        if 'internet' in option:
            bi = bi - 2500;
            count1 = count1 + 1;
            inter = 1;
            final.append('internet')
        else:
            inter = 0;
        if 'maid' in option:
            bi = bi - 2000;
            count1 = count1 + 1;
            maid = 1;
            final.append('maid')
        else:
            maid = 0;
        return 'Amount left to allocate is Rs.', bi
    else:
        if 'basic' in option:
            if b == 1:
                bi = bi;
            elif b == 0:
                bi = bi - 1200;
                b = 1;
                final.append('basic')
        else:
            if b == 1:
                bi = bi + 1200;
                b = 0;
                final.remove('basic')
        if 'phone' in option:
            if p == 1:
                bi = bi;
            elif p == 0:
                bi = bi - 600;
                p = 1;
                final.append('phone')
        else:
            if p == 1:
                bi = bi + 600;
                p = 0;
                final.remove('phone')
        if 'internet' in option:
            if inter == 1:
                bi = bi;
            elif inter == 0:
                bi = bi - 2500;
                inter = 1;
                final.append('internet')
        else:
            if inter == 1:
                bi = bi + 2500;
                inter = 0;
                final.remove('internet')
        if 'maid' in option:
            if maid == 1:
                bi = bi;
            elif maid == 0:
                bi = bi - 2000;
                maid = 1;
                final.append('maid')
        else:
            if maid == 1:
                bi = bi + 2000;
                maid = 0;
                final.remove('maid')
        return 'Amount left to allocate is Rs.', bi


def savings(save, save1, save2, save3):
    global save4
    save4 = int(save);
    total = int(save1) + int(save2) + int(save3);
    #print (total);
    if (total == save4):
        return "Congratulations! Now you can start your budget"
    else:
        return "Improper Allocation"

def main(name):
    global ai
    global monthly
    global final
    doctor = "As a General Surgeon my responsibilities are to perform operations involving the major parts of the human body."
    engineer = "As a software developer my responsibilities are to develop new enterprise software solutions and optimize existing solutions."
    athlete = "As a professional badminton player, I undergo rigorous training every day. Winning the olympic gold medal is my ultimate goal."
    businessman = "As the owner of a fast food chain, I am responsible for the daily operations of the chain."
    teacher = "As a chemistry teacher at a junior college, I am responsible to provide quality education to my students."
    d = {'Doctor':3000000, 'Engineer':400000, 'Athlete':1000000, 'Teacher':600000, 'Businessman':4000000};
    d1 = {'Doctor':39, 'Engineer':27, 'Athlete':24, 'Teacher':32, 'Businessman':40}; #age
    d2 = {'Doctor':doctor, 'Engineer':engineer, 'Athlete':athlete, 'Teacher':teacher, 'Businessman':businessman};
    name = name;
    option = random.choice(list(d.keys()));
    final.append(option);
    salary = d[option];
    final.append(salary);
    job = d2[option];
    ai = int(salary);
    age = d1[option];
    gmi = int(salary) / 12;
    monthly = int(gmi);
    return [option, salary, int(gmi), name, job, int(age)];

#Start of code
if __name__ == '__main__':
	main()
