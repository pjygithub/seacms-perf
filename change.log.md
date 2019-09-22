#### 时间：2019年9月22日
###### 要点：
- [x] 修复：非域名根目录安装时，默认模板访问不正常的一些问题；

###### 细节：
1. 改变./templets/default/html/foot.html第32行为：`<a href="{seacms:indexlink}/gbook.php"`；
2. 改变./templets/default/html/head.html第6行为：`<a class="logo" href="{seacms:indexlink}">`；
3. 第12行：`<li class=" {if:{seacms:currenttypeid}=-444}active{end if} hidden-sm hidden-xs"><a href="{seacms:indexlink}">首页</a></li>`；
4. templets/default/html/login.html
5. templets/default/html/newshead.html
6. templets/default/html/reg.html
7. templets/default/html/tophead.html 
8. templets/default/html/content.html 
9. 补充了以上模板文件的`{seacms:indexlink}`
10. include/mkhtml.func.php 第1706行：`<url>".$GLOBALS['cfg_basehost']."./../pic/logo.gif</url>\n`


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

