import os
import io
import math
import random
pathWS='dataws_test'
file_name='dictionary.txt'
file_input='input.txt'
#=============
def dictionary_write_out(wso):
    f=open(file_name,'w',encoding='utf-8')
    li=wso.keys()
    x=''
    for i in li:
        x=x+str(i)+' '
    f.write(x)
    f.close()
#==============
def dictionary_read():
    f=open(file_name,'r',encoding='utf-8')
    st=f.read()
    st=st.split()
    wso={}
    s=''
    for i in range(len(st)):
        if st[i] not in wso:
            wso[st[i]]=1
    return wso
#==============
def tokenize(st):
    list=['. ',', ','\'','"',':','!','?','\\',' .',' ,','-','/',')','(','}','{']
    for i in range(len(list)):
        st=st.replace(list[i],' '+list[i]+' ')
    while(st.find('  ')>-1):
        st=st.replace('  ',' ')
    return st
#===============
def words_seg_dictionary():
    wso={}
    p_dir=os.listdir(pathWS)
    for i in range(len(p_dir)):
        file_name_dir=pathWS+'/'+p_dir[i]
        print(file_name_dir)
        st=open(file_name_dir,'r',encoding='utf-8').read()
        st=st.lower()
        st=tokenize(st)
        words=st.split()
        for j in range(len(words)):
            if (words[j][0]!='<')and(words[j] not in wso):
                wso[words[j]]='1'
                lt=wso.keys()
                #print(len(lt))
    return wso
#==============
def words_seg(st):
    st_out=''
    save=''
    st=tokenize(st)
    print(st)
    st=st.split()
    print(st)
    while len(st)>0:
        for i in range(len(st)):
            if i==0:
                s=st[i]
            else:
                s=s+'_'+st[i]
            if s in wso:
                vt=i
                save=s
        if save!='':
            st_out=st_out+' '+save
            st=st[vt+1:len(st)]
        else:
            st_out=st_out+' '+st[0]
            st=st[1:len(st)]
        save=''
    return st_out[1:len(st_out)]
#===========
#ws=words_seg_dictionary()
#dictionary_write_out(ws)
wso=dictionary_read()
st=open(file_input,'r',encoding='utf-16').read()
st=st.lower()
print(words_seg(st))
