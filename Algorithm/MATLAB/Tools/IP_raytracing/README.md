## 文件结构以及说明
### 生成的文件说明
<code>radio_map_20_15.mat</code> 生成的“RSS仿真环境数据集”,(1999, 1499, 6)的数组,比如fingerprint(1000, 1000, 2)代表的是仿真环境中位置（100,100）上接收到的第2个AP的RSS.

<code>offline_data_rss.mat</code>离线数据RSS,每行为一个RSS向量

<code>offline_data_location.mat</code>离线数据位置点,每行为一个位置点x,y

<code>online_data_trace.mat</code>生成测试数据的运动轨迹,10000*2的数组,比如trace(10,:)代表的是第10个时刻目标的位置x和y

<code>online_data_rss.mat</code>生成测试数据中与运行轨迹对应的RSS,10000*6的数组,比如trace(10, :)代表的是第10个时刻时目标测得的各个RSS.

### 代码文件目录以及说明
<details>
<summary>展开查看</summary>
<pre><code>
├── generate_radio_map.m 生成“RSS仿真环境数据集”.
├── get_offline_data.m 
├── get_offline_data_random.m 模拟随机数据采集,生成位置指纹库.
├── get_offline_data_uniform.m 模拟均匀数据采集,生成位置指纹库.
├── get_online_data.m 模拟在线阶段,生成测试数据.
├── get_random_trace.m 生成一条随机轨迹.
├── get_rss_by_ray_tracing.m 简化场景下（空旷房间）的射线跟踪.
├── main_raytracing.m 主程序
└── README.md
</code></pre>
</details>