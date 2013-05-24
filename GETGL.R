GETGL(name)·	
s cmda="s a=$order(^"_name_"(a))"
s cmdb="s b=$order(^"_name_"(a,b))"
s cmdc="s c=$order(^"_name_"(a,b,c))"
s cmdr="s record=^"_name_"(a,b,c)"
s a=""
for  x cmda q:a=""  do
. s b=""
. for  x cmdb q:b=""  do
. . s c=""
. . for  x cmdc q:c=""  do
. . . x cmdr
. . . s id=""
. . . for i=1:1:$l(b)  do
. . . . s ascii=$a(b,i)
. . . . s id=id_ascii
. . . s tmp=record
. . . s shift=0
. . . s pos=1
. . . for  s pos=$f(record,"\",pos) q:pos=0  do
. . . . s tmp=$e(tmp,1,pos-2+shift)_"\\"_$e(tmp,pos+shift,$l(tmp))
. . . . s shift=shift+1
. . . s record=tmp
. . . s shift=0
. . . s pos=1
. . . for  s pos=$f(record,"""",pos) q:pos=0  do
. . . . s tmp=$e(tmp,1,pos-2+shift)_"\"""_$e(tmp,pos+shift,$l(tmp))
. . . . s shift=shift+1
. . . w !,"{""par"": {""id"": """_id_""", ""prop"": """_c_"""}, ""val"": """_record_"""}"
