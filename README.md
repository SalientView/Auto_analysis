# Auto_analysis
自动化分析脚本，更快的速度得到数据结论。

|	方法名	|	功能	|	输入	|	输出	|
|	----	|	----	|	----	|	----	|
|	transition	|	过度行	|	methods.transition('infomation')	|	![](https://imgkr.cn-bj.ufileos.com/2b1cbca6-537a-4b02-a981-5fb4fa36f96a.png)	|
|	variable_show	|	展示每列特征的取值个数和占比	|	methods.variable_show(data)	|		![](https://imgkr.cn-bj.ufileos.com/92d2aa11-206e-4c42-9b0c-c3cf2c562272.png)|
|	show_info	|	展示数据的基本信息	|	methods.show_info(data)	|		![](https://imgkr.cn-bj.ufileos.com/c8568df8-cd84-4409-8a51-3050039dc528.png)|
|	discrete_show	|	所有离散变量的取值分布	|	methods.discrete_show(data)	|	![](https://imgkr.cn-bj.ufileos.com/4417ba64-8c47-4a20-aaca-ea8c1238821c.png)	|
|	num_show	|	所有连续变量的取值分布	|	methods.num_show(data,figsize=(14,4),titlesize=14)	|	![](https://imgkr.cn-bj.ufileos.com/167bec53-cbc9-4833-b3e3-1a591f3e564b.png)	|
|	cross_show	|	离散变量和连续变量的交叉分析	|	methods.cross_show(data,x='size',y='total_bill',figsize=(14,6))	|	![](https://imgkr.cn-bj.ufileos.com/0f73b178-5890-4f76-91cc-c729a192b204.png)	|
|	total_cross	|	与cross_show类似，但不同是在一张图里展示	|	methods.total_cross(data,x='day',y='total_bill')	|	![](https://imgkr.cn-bj.ufileos.com/7246ae2e-ac7b-494f-aef4-afb1ca79f4da.png)	|
|	discrete_group	|	所有离散变量两两交叉组合	|	methods.discrete_group(data)	|	![](https://imgkr.cn-bj.ufileos.com/cfd4e3c2-6d5c-4f30-9636-308a3a74d0dd.png)	|
|	corr_tril	|	获取相关矩阵，去上三角矩阵	|	methods.corr_tril(data)	|	![](https://imgkr.cn-bj.ufileos.com/d24f10d6-3a70-4640-bef6-65f9a561c7d0.png)	|
|	mode	|	查看所有变量众数及占比	|	methods.mode(data)	|	![](https://imgkr.cn-bj.ufileos.com/35c6e172-aff9-4b85-bf30-4a50b9f21133.png)	|
|	type_count	|	统计每个变量的数据类型个数	|	count,___ = methods.type_count(data)	|	![](https://imgkr.cn-bj.ufileos.com/9773d0b0-0a79-4f84-87c3-a91067af25c9.png)	|




