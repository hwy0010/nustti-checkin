## 使用步骤

1. fork 到自己的 github 记得设置隐私

2. 编辑 getid.py 在 stuid 中填入学号 如 

   ```
   stuid = "1909660000"
   ```

   

3. 打开 Actions 执行 getid 在运行结果里找到获取的 id

4. 编辑 checkin.py 填好参数

   如


  ```
  stuid = "1909660000"
  id = "35900"
  province = "江苏省"
  city = "泰州市"
  distict = "海陵区"
  street = '梅兰东路8号'
  t5_1_id = "320000"
  t5_2_id = "321200"
  t5_3_id = "321202"
  ```

  | Key      | Value             |
  | -------- | ----------------- |
  | stuid    | 学号              |
  | id       | 使用getid获取的id |
  | province | 省份              |
  | city     | 城市              |
  | distict  | 区县              |
  | street   | 街道地址          |
  | t5_1_id  | 地区编码 后4位为0 |
  | t5_2_id  | 地区编码 后2位为0 |
  | t5_3_id  | 地区编码          |

  

t5id是地区编码 可在此查询 http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html


5. 运行一次 Actions 中的 CI 查看打卡是否成功 按照设置 每天10点左右会自动执行一次 
