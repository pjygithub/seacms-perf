#### 时间：2019年9月21日
###### 要点：
- [x] 新建build.py管理初始化安装状态，便于重新部署程序；
- [x] 新建change.md文件管理记录程序优化更新细节；
- [x] 优化：安装结果页非根目录安装的显示效果；

###### 细节：
1. 新建change.md文件，并全部输入新内容；
2. 新建build.py文件，并全部输入新内容；
3. 改变./install/templates/step-5.html:第37、38行：$baseurl--> $cbaseurl
4. 改变./install/index.php的第295-303行：
```
	$ newadminname = randomkeys（6）;
  	$jpath='../admin';
	$xpath='../'.$newadminname;
	$cadmin=rename($jpath,$xpath);	
	if($indexUrl=="/"){$cbaseurl=$baseurl;$ccbaseurl=$baseurl.'/';}
	else{$cbaseurl=$baseurl.'/'.$indexUrl;$ccbaseurl=$baseurl.'/'.$indexUrl;}

	if($cadmin==true){$cadmininfo=$ccbaseurl.$newadminname;}
	else{$cadmininfo=$ccbaseurl.'admin';}
```

