import datetime
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
    file = "G:/GPRlabel/1_0_1-01200.zol192.xml"
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
    # # cur.execute("SELECT DISTINCT 病害类型, COUNT(*) AS 病害数量 FROM 病害标签 GROUP BY 病害类型")
    # defectClass = '空洞'
    #
    # print("SELECT  病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.文件名=雷达图谱.文件名 WHERE [病害标签.病害类型] = " + defectClass)
    # SQL = "SELECT  病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签  WHERE [病害标签.病害类型] = " + defectClass
    # # cur.execute(SQL)
    # print(       "SELECT DISTINCT 文件名, 病害类型, 附件路径 FROM 病害标签 WHERE 病害类型 = '" + defectClass + "'")
    # # cur.execute("SELECT 病害标签.id, 病害标签.文件名, 病害标签.病害类型, 病害标签.附件路径, 雷达图谱.附件路径 FROM 病害标签 LEFT JOIN 雷达图谱 ON 病害标签.文件名=雷达图谱.文件名 WHERE [病害类型]= '" + defectClass + "'")
    # resarchNumSQL = "SELECT COUNT(*) FROM 雷达图谱"
    # cur.execute(resarchNumSQL)
    # adminInfor = (cur.fetchall())
    # print(adminInfor[0][0])
    # cur.close()
    # conn.close()
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
    # # # print(adminInfor)
    # # cur.close()
    # # conn.close()
    # file = 'G:/GPR_detect_pipline/data/VOC/2007_trainval/Annotations/1.xml'
    # filePath, fileName = os.path.split(file)
    # # resarchNumSQL = "SELECT COUNT(*) FROM 雷达图谱"
    # cur.execute(resarchNumSQL)
    # countNum = (cur.fetchall())
    # dataNum = countNum[0][0] + 1
    # print(dataNum)
    # print("INSERT INTO 雷达图谱(文件名,路径,num) VALUES('" + str(dataNum) + fileName[-4:] + "', '" + "./数据库/雷达图像/" + str(dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "')")
    # insertImageSQL = "INSERT INTO 雷达图谱(文件名,路径,num) VALUES('" + str(dataNum) + fileName[-4:] + "', '" + "./数据库/雷达图像/" + str(dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "')"
    # shutil.copyfile(file, './数据库/雷达图像/' + str(dataNum) + fileName[-4:])
    # print(insertImageSQL)
    # cur.execute(insertImageSQL)
    # conn.commit()
    # filePath, fileName = os.path.split(file)
    # root = ET.parse(file).getroot()
    # objects = root.findall('object')
    # resarchNumSQL = "SELECT COUNT(*) FROM 病害标签"
    # # cur.execute(resarchNumSQL)
    # countNum = (cur.fetchall())
    # dataNum = countNum[0][0] + 1
    # for obj in objects:
    #     difficult = obj.find('difficult').text.strip()
    #     bbox = obj.find('bndbox')
    #     defectClass = obj.find('name').text.lower().strip()
    #     print(defectClass)
    #     if defectClass == 'subgrade settlement':
    #         defectClass = '路基下沉'
    #     if defectClass == 'settlement':
    #         defectClass = '路基下沉'
    #     if defectClass == 'mud':
    #         defectClass = '翻浆冒泥'
    #     if defectClass == 'mud pumping':
    #         defectClass = '翻浆冒泥'
    #     if defectClass == 'cavity':
    #         defectClass = '空洞'
    #     if defectClass == 'separate':
    #         defectClass = '脱空'
    #     if defectClass == 'loose':
    #         defectClass = '疏松'
    # insertImageSQL = "INSERT INTO 病害标签(文件名,病害数,路径,num) VALUES('" + str(dataNum) + fileName[
    #                                                                               -4:] + "', " + "'" + str(
    #     len(objects)) + "', " + "'" + "./数据库/病害标签/" + str(
    #     dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "')"
    # print(insertImageSQL)
    # cur.execute(insertImageSQL)
    # conn.commit()
    # shutil.copyfile(file, './数据库/病害标签/' + fileName)
    # cur.close()
    # conn.close()
    filePath, fileName = os.path.split(file)
    root = ET.parse(file).getroot()
    size = root.findall('size')
    width = size[0].find('width').text.strip()
    height = size[0].find('height').text.strip()
    print(width, height)
    objects = root.findall('object')
    resarchNumSQL = "SELECT COUNT(*) FROM 病害标签"
    cur.execute(resarchNumSQL)
    countNum = (cur.fetchall())
    dataNum = countNum[0][0] + 1
    for obj in objects:
        difficult = obj.find('difficult').text.strip()
        bbox = obj.find('bndbox')
        xmin = bbox.find('xmin').text.strip()
        xmax = bbox.find('xmax').text.strip()
        ymin = bbox.find('ymin').text.strip()
        ymax = bbox.find('ymax').text.strip()
        print(xmin, xmax, ymin, ymax)
        defectClass = obj.find('name').text.lower().strip()
        print(defectClass)
        if defectClass == 'subgrade settlement':
            defectClass = '路基下沉'
        if defectClass == 'settlement':
            defectClass = '路基下沉'
        if defectClass == 'mud':
            defectClass = '翻浆冒泥'
        if defectClass == 'mud pumping':
            defectClass = '翻浆冒泥'
        if defectClass == 'cavity':
            defectClass = '空洞'
        if defectClass == 'separate':
            defectClass = '脱空'
        if defectClass == 'loose':
            defectClass = '疏松'
        # insertImageSQL = "INSERT INTO 病害表(文件名, 病害, 病害分辨率,病害坐标, 标签) VALUES('" + str(
        #     dataNum) + "', '" + defectClass + "', '" + "左下坐标: " + xmin + " " + ymin + " 右上坐标: " + xmax + " " + ymax + "', '" + fileName + "')"
        insertImageSQL = "INSERT INTO 病害表(文件名, 病害, 病害图分辨率,病害坐标, 标签) VALUES('" + str(
            dataNum) + "', '" + defectClass + "', '(" + width + "," + height + ")', '" + defectClass + "左下坐标: (" + xmin + ", " + ymin + ") 右上坐标: (" + xmax + ", " + ymax + ")', '" + fileName + "')"
        print(insertImageSQL)
        cur.execute(insertImageSQL)
        conn.commit()
    # now = datetime.datetime.now()
    # insertImageSQL = "INSERT INTO 病害标签(文件名,病害数,路径,num,上传时间) VALUES('" + str(dataNum) + fileName[
    #                                                                                    -4:] + "', " + "'" + str(
    #     len(objects)) + "', " + "'" + "./数据库/病害标签/" + str(
    #     dataNum) + fileName[-4:] + "'" + ", '" + str(dataNum) + "', '" + str(now.isoformat()) + "')"
    # print(insertImageSQL)
    # cur.execute(insertImageSQL)
    # conn.commit()
