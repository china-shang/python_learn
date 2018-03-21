#!/bin/bash


begin(){
echo $1
mysql -u root -p'123456' -e "select COLUMN_NAME,DATA_TYPE from information_schema.COLUMNS
where table_name = '$1' and table_schema='database'"
}
run(){
#begin $1 2>/dev/null |grep "\| \<\.*\>" |grep -vi "column_name" |xargs   python3 dao.py 
begin $1 2>/dev/null |grep "\| \<\.*\>" |grep -vi "column_name" |xargs   python3 imple1.py 
}


start (){
    
    for i in $@;
    do
        echo "begin $i "
        run $i
        echo "end $i "
    done
    echo "Sucess all "
    
}

start $@








