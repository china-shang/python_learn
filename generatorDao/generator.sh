#!/bin/bash
mysql -u root -p'123456' -e "select table_name from information_schema.TABLES where  table_schema = 'database'; " 2>/dev/null | grep "\| \<\.*\>" |grep -vi "column_name\|table_name" |xargs bash c1.sh
