import os
import shutil
import pyodbc
import xml.etree.ElementTree as ET
if __name__ == '__main__':
    pathfile = "./数据库/数据表/病害数据集.accdb"
    connStr = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s;' % pathfile
    pyodbc.lowercase = False  # 是否将字段名转为小写

    conn = pyodbc.connect(connStr)
    cur = conn.cursor()
    # file = "G:/GPRlabel/1_0_1-01200.zol192.xml"
    # # filePath, fileName = os.path.split(file)
    # filePath, fileName = os.path.split(file)
    # # print(file)
    # # print(filePath)
    # # print(fileName)
    # # print('./数据库/雷达图像/' + fileName)
    # # shutil.copyfile(file, './数据库/雷达图像/' + fileName)
    # root = ET.parse(file).getroot()
    # objects = root.findall('object')
    # for obj in objects:
    #     difficult = obj.find('difficult').text.strip()
    #     bbox = obj.find('bndbox')
    #     defectClass = obj.find('name').text.lower().strip()
    #     print(defectClass)
    #     if defectClass == 'subgrade settlement':
    #         defectClass = '路基下沉'
    #     if defectClass == 'mud':
    #         defectClass = '翻浆冒泥'
    #     if defectClass == 'cavity':
    #         defectClass = '空洞'
    #     if defectClass == 'separate':
    #         defectClass = '脱空'
    #     if defectClass == 'loose':
    #         defectClass = '疏松'
    #     insertImageSQL = "INSERT INTO 病害标签(文件名,病害类型,附件路径) VALUES('" + fileName + "', '" + defectClass + "', '" + file + "'" + ")"
    #     print(insertImageSQL)
    #     cur.execute(insertImageSQL)
    #     conn.commit()
    # # cur, conn = self.initDatabase()
    # # insertImageSQL = "INSERT INTO 雷达图谱(文件名,附件路径) VALUES(" + str(fileName) + "," + str(file) + ")"
    # # insertImageSQL = "INSERT INTO 病害标签(文件名,附件路径) VALUES('" + fileName + "', '" + file + "'" + ")"
    # # print(insertImageSQL)
    # cur.execute("SELECT DISTINCT 病害类型, COUNT(*) AS 病害数量 FROM 病害标签 GROUP BY 病害类型")
    defectClass = '空洞'

    print("SELECT  病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.文件名=雷达图谱.文件名 WHERE [病害标签.病害类型] = " + defectClass)
    SQL = "SELECT  病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签  WHERE [病害标签.病害类型] = " + defectClass
    # cur.execute(SQL)
    print(       "SELECT DISTINCT 文件名, 病害类型, 附件路径 FROM 病害标签 WHERE 病害类型 = '" + defectClass + "'")
    cur.execute("SELECT 病害标签.id, 病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.文件名=雷达图谱.文件名 WHERE [病害类型]= '" + defectClass + "'")

    adminInfor = (cur.fetchall())
    print(adminInfor)
    cur.close()
    conn.close()
    # print(file)
    # # print(filePath)
    # # print(fileName)
    # print('./数据库/病害标签/' + fileName)
    # insertImageSQL = "INSERT INTO 雷达图谱(文件名,附件路径) VALUES('" + fileName + "', '" + file + "'" + ")"
    #
    # # insertImageSQL = "INSERT INTO 病害类型(病害类型) VALUES('" + fileName + "')"
    # print(insertImageSQL)
    # # cur.execute(insertImageSQL)
    # # conn.commit()
    # # cur.execute("SELECT * FROM 病害类型")
    # # adminInfor = (cur.fetchall())
    # # print(adminInfor)
    # cur.close()
    # conn.close()