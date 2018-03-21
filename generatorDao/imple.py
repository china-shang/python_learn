#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Generator():
    
    def __init__(self,tablesName,fields):

        self.fields=fields
        self.tablesName=tablesName
        self.className=tablesName.title()
        self.daoClassName="DaoImp" + self.className

        self.createVO()
        self.createImple()

    def createVO(self):

        header="\n\n\npublic class {0}{{".format(self.className)
        text=""

        print(header)
        text += header

        for field in self.fields:
            init=""" 
                String {0}=null; """.format(field)

            print(init)
            text += init

        for field in self.fields:
            get="""
                public String get{0}{{
                    return this.{1};
                }}
            """.format(field.title(),field)
            print(get)
            text += get

        for field in self.fields:
            set="""
                public void set{0}(String {1}){{
                    this.{1}={1}
                }}
            """.format(field.title(),field)
            print(set)
            text += set

        with open(self.className+".java","w") as f:
            f.write(text)

    def createImple(self):

        header="""
    package yourpackage;
    import java.sql.PreparedStatement;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Connection;


    public class {0} implements DAOabstractInterface<{1}>{{

            private Connection connection;

        """.format(self.daoClassName,self.className)

        tail="""
            public Connection getConnection() {
                return connection;
            }

            private void setConnection(Connection connection) {
                this.connection = connection;
            }

    }
        """
        append_method=self.appendMethod()
        delete_method=self.deleteMethod()
        find_method=self.findMethod()
        update_method=self.updateMethod()

        text=header+append_method+delete_method+update_method+find_method+tail

        print(text)
        with open(self.daoClassName+".java","w") as f:
            f.write(text)

    def updateParameterWarp(self):

        body=""
        for field in self.fields:
            if(field != "id"):
                body += " " + field + " " + "=?,"

        body = body[:-1]

        end="WHERE  id =?;"

        return body+end

    def updateSetParameter(self):

        i=1
        t="\n"
        for field in self.fields:
            if(field != "id"):
                t += "\t\tstatment.setString({0},{1}.get{2}());\n".format(i,self.tablesName.title(),field)
                i += 1

        t += "\t\tstatment.setString({0},{1}.getId());\n".format(i,self.tablesName)
        t += "\t\tstatment.execute();\n"

        return t
        
    def insertParameterWarp(self):

        field_start='('
        value_start='VALUES ('
        for field in self.fields:
            if(field != "id"):
                field_start += " " + field + " " + ","
                value_start += "?" + ","

        field_start = field_start[:-1]
        value_start = value_start[:-1]

        return ( field_start + ")" + value_start + ")" )

    def insertSetParameter(self):

        i=1
        t="\n"
        for field in self.fields:

            t += "\t\tstatment.setString({0},{1}.get{2}());\n".format(i,self.tablesName,field.title())
            i += 1

        t += "\t\tstatment.execute();\n"

        return t
        
    def findMethod(self):

        header="""
            @Override
            public {0} findById({0} {1}) throws SQLException {{

                PreparedStatement stat = getCon().prepareStatement("SELECT {2} FROM {1}  WHERE  id =?)");
                stat.setString(1, {1}.getId());
                ResultSet result = stat.executeQuery();
                result.next();
            """.format(self.className,self.tablesName,self.findParameterWarp())

        i=1
        t="\n"
        for field in self.fields:
            t += "\t\t{2}.set{0}=result.getString({1})\n".format(field.title(),i,self.tablesName)
            i += 1

        result=header+t+"\n\t}\n"

        return result

    def findParameterWarp(self):
        t=""
        for field in self.fields:
            t += field + ","

        t = t[:-1]
        return t



    def updateMethod(self):

        header="""
            @Override
            public void update({0} {3}) throws SQLException {{
                    
                PreparedStatement statment = getConnection().prepareStatement("UPDATE   {1}  SET {2});
        """.format(self.className,self.tablesName,self.updateParameterWarp(),self.tablesName)
        mid=self.updateSetParameter()

        end="\t}"

        result=header + mid + end

        return result

    
    def deleteMethod(self):

        t="""
            @Override
            public void delete({0} {1}) throws SQLException {{
                    
                PreparedStatement stat = getConnection().prepareStatement("DELETE  {1}  WHERE  id =?)");
                stat.setString(1, {1}.getId());
                stat.execute();
            }}
        """.format(self.className,self.tablesName)

        result = t
        return result

    def appendMethod(self):

        header="""
            @Override
            public void insert({0} {1}) throws SQLException {{
                    
                PreparedStatement statment = getConnection().prepareStatement("INSERT INTO {1} {2}");
        """.format(self.className,self.tablesName,self.insertParameterWarp())

        mid=self.insertSetParameter()

        end="\t}"

        result=header + mid + end

        return result
        

if __name__=="__main__":
    Generator(sys.argv[1],sys.argv[2:])
