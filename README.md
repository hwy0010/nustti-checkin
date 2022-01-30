## 使用步骤

1. 点击 use this template 选择 private 创建自己的仓库

2. 编辑 getid.py 在 stuid 中填入学号 如 

   ```
   stuid = "1909660000"
   ```

   

3. 打开 Actions 执行 getid 点开运行结果 获取 id （5位数字）

4. 在此查询地区编码 http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html 编辑 checkin.py 填好参数 如

   

  ```
  stuid = "1909660000"
  id = "35900"
  province = "江苏省"
  city = "泰州市"
  district = "海陵区"
  street = '梅兰东路8号'
  areacode = "321202"
  ```

  | Key      | Value             |
  | -------- | ----------------- |
  | stuid    | 学号              |
  | id       | 使用getid获取的id |
  | province | 省份              |
  | city     | 城市              |
  | district  | 区县              |
  | street   | 街道地址          |
  | areacode  | 地区编码        |


  


5. 运行一次 Actions 中的 CI 查看打卡是否成功 按照设置 每天11点左右会自动执行一次 
打卡成功时 Actions 运行结果中会出现 "Serv_Outp:good_ok! "
   
