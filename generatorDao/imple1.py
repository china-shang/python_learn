#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Generator():
    
    def __init__(self,tablesName,fields,type_dict):

        self.isBase=["Lession","User","Agency","Subscription","Comment","Administration"]
        self.type_dict=type_dict
        self.fields=fields
        self.tablesName=tablesName
        self.className=tablesName.title()
        if(self.className not in self.isBase):
            self.daoClassName="DaoImp" + self.className
        else:
            self.daoClassName="DaoImp" + self.className+"Base"


        self.createVO()
        self.createImple()


    def createVO(self):

        header="""
package vo;
import java.sql.Date;
import java.sql.Timestamp;

        """
        header+="\npublic class {0}{{".format(self.className)
        text=""

        print(header)
        text += header

        for field in self.fields:
            if(type_dict[field]=="Int"):
                f_type="Integer"
            else:
                f_type=type_dict[field]

            init=""" 
                private {1} {0}=null; """.format(field,f_type)

            print(init)
            text += init

        for field in self.fields:
            if(type_dict[field]=="Int"):
                f_type="Integer"
            else:
                f_type=type_dict[field]
            get="""
                public {2} get{0}(){{
                    return this.{1};
                }}
            """.format(field.title(),field,f_type)
            print(get)
            text += get

        for field in self.fields:

            if(type_dict[field]=="Int"):
                f_type="Integer"
            else:
                f_type=type_dict[field]
            set="""
                public void set{0}({2} {1}){{
                    this.{1}={1};
                }}
            """.format(field.title(),field,f_type)
            print(set)
            text += set;
        text += "}"


        with open(self.className+".java","w") as f:
            f.write(text)

    def createImple(self):

        header="""
    package dao;
    import java.sql.PreparedStatement;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Connection;
    import java.sql.Statement;
    import vo.{2};
    import daoInterface.DAOabstractInterface;


    public class {0} extends AbstractDao<{1}> {{

        """.format(self.daoClassName,self.className,self.tablesName.title())

    #     tail="""
    #         public Connection getConnection() {
    #             return connection;
    #         }
    #
    #         public void setConnection(Connection connection) {
    #             this.connection = connection;
    #         }
    #
    #         @Override
    #         public void close() {
    #             try {
    #                 this.getConnection().close();
    #             } catch (SQLException e) {
    #                  e.printStackTrace();
    #                  }
    #         }
    # }
    #     """
        tail="}"
        append_method=self.appendMethod()
        delete_method=self.deleteMethod()
        find_method=self.findMethod()
        update_method=self.updateMethod()
        fetch_method=self.fetchMethod()
        fetch_method_ord=self.fetchMethodOrder()

        text=header+append_method+delete_method+update_method+find_method+fetch_method+fetch_method_ord+tail


        print(text)
        with open(self.daoClassName+".java","w") as f:
            f.write(text)

    def updateParameterWarp(self):

        body=""
        for field in self.fields:
            if(field != "id"):
                body += "`" + field + "`" + "=?,"

        body = body[:-1]

        end=" WHERE  id =?;"

        return body+end

    def updateSetParameter(self):

        i=1
        t="\n"
        for field in self.fields:
            if(field != "id"):
                t += "\t\tstatment.set{3}({0},{1}.get{2}());\n".format(i,self.tablesName,field.title(),type_dict[field])
                i += 1

        t += "\t\tstatment.setInt({0},{1}.getId());\n".format(i,self.tablesName)
        t += "\t\tstatment.execute();\n"

        return t
        
    def insertParameterWarp(self):

        field_start='('
        value_start='VALUES ('
        for field in self.fields:
            if(field != "id"):
                field_start += "`" + field + "`" + ","
                value_start += "?" + ","

        field_start = field_start[:-1]
        value_start = value_start[:-1]

        return ( field_start + ")" + value_start + ")" )

    def insertSetParameter(self):

        i=1
        t="\n"
        for field in self.fields:

            if(field!="id"):
                t += "\t\tstatment.set{3}({0},{1}.get{2}());\n".format(i,self.tablesName,field.title(),type_dict[field])
                i += 1

        t += "\t\tstatment.execute();\n"

        return t
        
    def findMethod(self):

        header="""
            @Override
            public {0} findById(int id)  {{
                try{{
                PreparedStatement stat = getConnection().prepareStatement("SELECT {2} FROM {1}  WHERE  id =?");
                stat.setInt(1, id);
                ResultSet result = stat.executeQuery();
                if(!result.next()){{
                    return null;
                    }}
                
                {3} {4}=new {3}();
                
            """.format(self.className,self.tablesName,self.findParameterWarp(),self.tablesName.title(),self.tablesName)

        i=1
        t="\n"
        for field in self.fields:
            t += "\t\t{2}.set{0}(result.get{3}({1}));\n".format(field.title(),i,self.tablesName,self.type_dict[field])
            i += 1

        result=header+t+"return {0};\n}}catch(Exception e){{e.printStackTrace();return null;}}".format(self.tablesName) + "}"

        return result

    def findParameterWarp(self):
        t=""
        for field in self.fields:
            t += "`"+field + "`,"

        t = t[:-1]
        return t

    def updateMethod(self):

        header="""
            @Override
            public void update({0} {3})  {{
                try{{
                    
                PreparedStatement statment = getConnection().prepareStatement("UPDATE   {1}  SET {2}");
        """.format(self.className,self.tablesName,self.updateParameterWarp(),self.tablesName)
        mid=self.updateSetParameter()

        end="}catch(Exception e){e.printStackTrace();\n}\t}"

        result=header + mid + end

        return result

    
    def deleteMethod(self):

        t="""
            @Override
            public void delete({0} {1}) {{
                try{{
                PreparedStatement stat = getConnection().prepareStatement("DELETE FROM  {1}  WHERE  id =?");
                stat.setInt(1, {1}.getId());
                stat.execute();
                }}catch(Exception e){{
                e.printStackTrace();
                }}
            }}
        """.format(self.className,self.tablesName)

        result = t
        return result
    def fetchMethod(self):
        header = """
                   @Override
                   public {0}[] fetchAll()  {{
                       try{{
                       PreparedStatement stat = getConnection().prepareStatement("SELECT {2} FROM {1}  ");
                       ResultSet result = stat.executeQuery();
                       int rows=0;
                      
		if (result.last()) {{
		    rows = result.getRow();
		    System.out.println(rows);
		    // Move to beginning
		    result.beforeFirst();
		}}
		int i=0;

                       {3}[] {4}s=new {3}[rows];
                       while(result.next()){{
                       {4}s[i] =new {3}();\n

                   """.format(self.className, self.tablesName, self.findParameterWarp(), self.tablesName.title(),
                              self.tablesName)

        i = 1
        t = "\n"
        for field in self.fields:
            t += " \t\t{2}s[i].set{0}(result.get{3}({1}));\n".format(field.title(), i, self.tablesName,
                                                                self.type_dict[field])
            i += 1

        result = header + t + "i++;}}return {0}s;\n}}catch(Exception e){{e.printStackTrace();return null;}}".format(self.tablesName) + "}"

        return result
    def fetchMethodOrder(self):
        header = """
                   @Override
                   public {0}[] fetchAll(String col, boolean desc, int start, int len){{
                        String s="SELECT {2} FROM {1} ORDER BY ? ";
                        if (desc) {{
                        s += "DESC";
                        }}
                       try{{
                       PreparedStatement stat = getConnection().prepareStatement(s);
                       stat.setString(1,col);
                       ResultSet result = stat.executeQuery();
                       int rows=0;
                      
        if (result.last()) {{
            rows = result.getRow();
            // Move to beginning
            result.beforeFirst();
        }}
        int size = (rows - start + 1) >= len ? len : (rows - start + 1);
        int i = 0;

                       {3}[] {4}s=new {3}[size];
                       while(result.next()&&i<size){{
                       {4}s[i] =new {3}();\n

                   """.format(self.className, self.tablesName, self.findParameterWarp(), self.tablesName.title(),
                              self.tablesName)

        i = 1
        t = "\n"
        for field in self.fields:
            t += " \t\t{2}s[i].set{0}(result.get{3}({1}));\n".format(field.title(), i, self.tablesName,
                                                                self.type_dict[field])
            i += 1

        result = header + t + "i++;}}return {0}s;\n}}catch(Exception e){{e.printStackTrace();return null;}}".format(self.tablesName) + "}"

        return result

    def appendMethod(self):

        header="""
            @Override
            public int insert({0} {1})  {{
                try{{
                    
                PreparedStatement statment = getConnection().prepareStatement("INSERT INTO {1} {2}",Statement.RETURN_GENERATED_KEYS);
        """.format(self.className,self.tablesName,self.insertParameterWarp())

        mid=self.insertSetParameter()+"""
        ResultSet   result = statment.getGeneratedKeys();result.next();int id = result.getInt(1);
        return id;
        
        """

        end="}catch(Exception e){e.printStackTrace();return -1;}}"

        result=header + mid + end

        return result
        

if __name__=="__main__":

    tablesName=sys.argv[1]
    t=sys.argv[2:]
    type_dict={}
    fields=[ t[i] for i in range(0,len(t),2)]
    types=[ t[i] for i in range(1,len(t),2)]
    for i in range(0,len(fields)):
        if(types[i]=="bool" or types[i]=="tinyint"):
            f_type="Boolean"
        elif(types[i].endswith("char")):
            f_type="String"
        elif(types[i].endswith("float")):
            f_type="Float"
        elif(types[i]=="timestamp" or types[i]=="time"):
            f_type="Timestamp"
        elif(types[i].endswith("int") or types[i]=="int"):
            f_type="Int"
        else:
            f_type="Date"

        type_dict[fields[i]]=f_type
    print(type_dict)

    Generator(tablesName,fields,type_dict)







