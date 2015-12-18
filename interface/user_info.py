author__ = 'lyi'



import MySQLdb,time, re



class UserInfo():

    def __init__(self):

        self.conn = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd ="123456",  db="test", charset="utf8")

        self.cursor = self.conn.cursor()



    #查询账号信息

    def SelectUserInfo(self, uid):

        res = {'errno':0,'errmsg':'','data':[]}

        if len(str(uid)) == 0:        #传的uid 为空

            res['errno'] = 101

            res['errmsg'] = "uid is None"

            return res

        sql = "select uid,name,mobile,mail,gender,addtime,modtime,status from user_info where uid = " + str(uid).strip()

        try:

            n = self.cursor.execute(sql)

            self.conn.commit()

            if n >= 1:              # 查询到数据

                res['data'] = self.cursor.fetchall()

            else:                   #没有查询到数据

                res['errno'] = 102

                res['errmsg'] = "not exist user"

        except:                     #查询时出现错误

            res['errno'] = 103

            res['errmsg'] = "select data error"

        finally:

            return res



    #修改账号信息

    def UpdateUserInfo(self, uid, i_param):

        res = {'errno':0,'errmsg':''}



        if (uid=='' or len(i_param)==0):

            res['errno'] = 201

            res['errmsg'] = "param is error"

            return res



        if self.SelectUserInfo(uid)['errno'] <> 0:  #没有这个账号的情况

            res['errno'] = 202

            res['errmsg'] = "not exist user"

            return res



        sql = "update user_info" +  " set "

        set = ""

        if 'name' in i_param.keys():

            set += "name = " +"'" + str(i_param.get('name')).strip() + "', "

        if 'mobile' in i_param.keys():

            set += "mobile = " + "'" + str(i_param.get('mobile')).strip() + "', "

        if 'mail' in i_param.keys():

            set += "mail = " + "'" + str(i_param.get('mail')).strip() + "', "

        if 'gender' in i_param.keys():

            set += "gender = " +  "'" + str(i_param.get('gender')) + "', "

        if 'status'in i_param.keys():

            set += "status = " + "'" + str(i_param.get('status')) + "', "



        check_mobile = re.compile('^1[3578]\d{9}$')

        n_mobile = len(check_mobile.findall(str(i_param.get('mobile'))))



        check_mail = re.compile('^\w+@\w+(\.com\.cn|\.com|\.cn)$')

        n_mail = len(check_mail.findall(str(i_param.get('mail'))))



        if (i_param.get('name') is not None and len(i_param.get('name').strip()) >= 33) or

                (i_param.get('mobile') is not None and n_mobile ==0) or

                (i_param.get('mail') is not None and n_mail ==0) or

                (i_param.get('gender') is not None and i_param.get('gender') not in (0,1)) or

                (i_param.get('status') is not None and i_param.get('status') not in (0,1,2)):   #参数错误

            res['errno'] = 201

            res['errmsg'] = "param is error"

            return res



        set += "modtime = " + "'" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "' "

        where = " where uid = " + str(uid)

        sql = sql + set + where



        try:

            n = self.cursor.execute(sql)

            self.conn.commit()

        except:

            self.conn.rollback()

            res['errno'] = 203

            res['errmsg'] = "update data failed"

        finally:

            return res



    def __del__(self):

        self.cursor.close()

        self.conn.close()



if __name__=="__main__":

    test = UserInfo()

    print test.SelectUserInfo(1)

    print test.UpdateUserInfo(1,{'name':'cm1 ','mail':'cm1@cm1.com'})
