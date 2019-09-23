#### 时间：2019年9月22日
###### 要点：
- [x] 修复：非域名根目录安装时，默认模板访问不正常的一些问题；
- [x] 新增：安装向导程序可以选择“新建数据库”和“使用原来已有的数据库”，重装更方便；

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
11. 修改install/index.php


#### 时间：2019年9月21日
###### 要点：
- [x] 新建build.py管理初始化安装状态，便于重新部署程序；
- [x] 新建change.log.md文件管理记录程序优化更新细节；
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

#### 时间：2019年9月12日 v9.99
###### 要点：
- [X] 修复：文章自定义采集实时入库功能
- [X] 修复：采集未入库文章无法编辑
- [X] 修复：采集未入库视频无法编辑
- [X] 修复：留言板界面验证码输入效果

###### 细节：
1. 修改gbook.php
2. 修改/admin/admin_collect_news.php
3. 修改模板文件：admin_co_editnews.htm、admin_co_editvideo.htm、admin_collect_ruleedit.htm、admin_collect_ruleedd.htm

#### 时间：2019年8月25日 v9.98
###### 要点：
- [x] 优化：减少安全过滤误报
- [x] 新增：强制使用 CKplayer
- [x] 新增：强制使用 Dplayer
- [x] 新增：Dplayer增加全屏连播，进度记忆，无缝上下集，p2p加速 
- [x] 新增：播放器参数parent.vid视频id  parent.vfrom当前播放器  parent.vpart当前集数

###### 细节：

#### 时间：2019年8月25日之前
累计更新
