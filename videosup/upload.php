<?php
ini_set('track_errors', 1);
//禁用错误报告
error_reporting(0);

session_start();
// include_once('./composer.json');
// 连接数据库
include('./../data/common.inc.php');
$uid=$_SESSION['sea_user_id'];
// $uid = 1;
$conn = new mysqli($cfg_dbhost, $cfg_dbuser, $cfg_dbpwd,$cfg_dbname);
// 检测连接
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
// echo "连接成功";
//查询数据
$sql_user = "SELECT * FROM ".$cfg_dbprefix."member WHERE `id` = ".$uid;
$result = mysqli_query($conn,$sql_user);
$row_user=mysqli_fetch_assoc($result);
// echo $row_user['username'];
$sql_add = "";
$a = $_POST['nameee'];
echo $a;
//引入包
include('./src/Upload/Upload.php');
include_once('./vendor/autoload.php');
// include('./vendor/*');


$upload = new \Dj\Upload('form-name-file');
$filelist = $upload->save('./upload', [
    'ext'=>'jpg,jpeg,png,gif,mp4',
    'size'=> 4294967296
], 'localhost');
if(is_array($filelist)){
    # 返回数组，文件就上传成功了
    // print_r($filelist);
    $r = array("code" => 200, 
    "data" => null);
    $r_json = json_encode($r+$filelist);
    echo $r_json;
    return $r_json;

}else{
    # 如果返回负整数(int)就是发生错误了
    // echo $error_msg;
    $error_msg = [0=>'不允许上传空文件',-1=>'上传失败',-2=>'文件存储路径不合法',-3=>'上传非法格式文件',-4=>'文件大小不合符规定',-5=>'token验证错误'];
    echo $error_msg[$filelist];
    $r = array("code" => 400, 
    "data" => null);
    $r_json = json_encode($r+$filelist);
    echo $r_json;
    
    return $r_json;
}

?>