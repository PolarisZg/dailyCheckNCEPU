# dailyCheckNCEPU
this is a automation script about wechat daily check of NCEPU

## 所需参数

### 饼干

`SECKEY_ABVK` , `BMAP_SECKEY` , `_WEU` , `JSESSIONID` <br>
这些参数需要使用者自己补充道代码之中

### 数据

`formData` 传给服务器的数据, 这个也需要使用者自己补充

## 参数获取方式

1. 
   * 在电脑浏览器上登录学校微信上报网页
   这一步需要抓包工具 [`Fiddler`](http://fiddler2.com/docs/default-source/public-downloads/fiddler2setup.exe?sfvrsn=16)  以及该工具插件 [`free cookies`](https://raw.githubusercontent.com/lulianqi/FreeCookies/master/bin/Debug/FreeCookies.dll)<br>
   * 下载安装 `Fiddler` 一路下一步, 遇到情况按 **是** 直到安装完成<br>
   * 复制 `free cookies` 的 `dll` 文件至 `Fiddler安装目录 / Scrpts  ` 文件夹下, 现在该 `dll` 文件的目录为 `Fiddler安装目录 / Scrpts / FreeCookies.dll`
   * 打开 `Fiddler` 可以看到右侧多出 `free cookies` 标签
  
2. * 配置 PC 端 Fiddler 及 Android 端网络
   * 配置Fiddler允许监听https <br>
     打开Fiddler菜单项Tools->Options->HTTPS，选中decrypt https traffic和ignore server certificate errors两项
   * 配置Fiddler允许远程连接<br>
     菜单中点击connections，选中allow remote computers to connect，默认监听端口为8888，若被占用也可以设置，配置好后需要重启Fiddler
   * 配置手机端<br>
     Pc端命令行ipconfig查看Fiddler所在机器ip<br>
     打开手机连接到同一局域网的wifi，并修改该wifi网络详情(长按wifi选择->修改网络)->显示高级选项，选择手动代理设置，主机名填写Fiddler所在机器ip，端口填写Fiddler端口，默认8888<br>
     这时，手机上的网络访问在Fiddler就可以查看了

3. * 手机端访问 *每日上报* 并分享链接至 PC 端, `Fiddler` 点击最早的对每日上报的请求, 然后点击 `free cookies` 再点击 `Get cookies` 得到所有cookies
   * 浏览器输入上报链接地址, 回车访问,  `Fiddler` 点击相应请求, `free cookies` 选项卡下 `Url Filer` 内填入上报链接, 勾选 `Injext Cookies`, 浏览器再输入上报链接访问, 此时应该能打开相应的网页
   * `F12 -> 应用 -> cookies` 可看到所有饼干, `F12 -> 网络 -> Fetch/XHR` 可查看所有网络请求
   * 点击 *编辑* -> *提交* 
   * `checkData.do` 请求的 `载荷` 选项卡下可获得参数 `formData`
   * `cookies` 下可获得所有需要的饼干

4. 完善 `python` 代码, 运行获得以下结果即可成功

```
{"datas":{"T_STU_DAILYREPORT_INFO_SAVE":1},"code":"0"}
```

5. 注册腾讯云账号, 新建云函数, `python` 版本选 2.6 , 复制所有代码, 部署即可