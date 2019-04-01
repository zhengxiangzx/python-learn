-- 俄罗斯方块环游记|SERVER
CREATE DATABASE IF NOT EXISTS elsfkhyj_server_original COMMENT '俄罗斯方块环游记|SERVER'
  LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj';

use elsfkhyj_server_original;

--1. 服务器事件(serverevent) 一级日志
--日志名称：serverevent.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_serverevent`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `sdkversion` string COMMENT 'SDK版本号',
  `system` string COMMENT '系统',
  `gamechannel` string COMMENT '推广渠道id',
  `deviceid` string COMMENT '设备唯一标识',
  `userid` string COMMENT '账号id',
  `code` string COMMENT '_行为号',
  `version` string COMMENT '客户端版本号'
)
 COMMENT '服务器事件(serverevent) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/serverevent';

--2. [1010]心跳日志(heart) 一级日志
--日志名称：heart.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_heart`(
  `servertime` string COMMENT '时间戳',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverId` string COMMENT '游戏服务器id',
  `onlineuser` int COMMENT '在线用户数',
  `paidui` int COMMENT '排队人数'
)
 COMMENT '[1010]心跳日志(heart) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/heart';

--3. [2050]游戏服务器登录(login) 一级日志
--日志名称：login.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_login`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `rolename` string COMMENT '角色名',
  `ip` string COMMENT '登录ip',
  `valueamount` int COMMENT '价值虚拟币总量',
  `leaguename` string COMMENT '联盟名称',
  `lives` int COMMENT '体力',
  `coin` int COMMENT '金币',
  `paycount` double COMMENT '玩家的总付费(人民币)',
  `max_paycont` double COMMENT '玩家单次最大充值额(人民币)',
  `lastpaydays` int COMMENT '玩家最近一次付费间隔',
  `Lastlogindays` int COMMENT '玩家最近一次登录间隔',
  `model` string COMMENT '设备型号',
  `regtime` string COMMENT '玩家注册时间'
)
 COMMENT '[2050]游戏服务器登录(login) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/login';

--4. [3025]创建角色(rolebuild) 一级日志
--日志名称：rolebuild.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_rolebuild`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `rolename` string COMMENT '角色名',
  `gender` int COMMENT '角色性别'
)
 COMMENT '[3025]创建角色(rolebuild) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/rolebuild';

--5. [3030]角色登录(rolelogin) 一级日志
--日志名称：rolelogin.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_rolelogin`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `rolename` string COMMENT '角色名',
  `valueamount` int COMMENT '价值虚拟币总量'
)
 COMMENT '[3030]角色登录(rolelogin) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/rolelogin';

--6. [4010-4990]新手引导(newstages)
--日志名称：newstages.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_newstages`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `eventid` string COMMENT '引导步大类'
)
 COMMENT '[4010-4990]新手引导(newstages)'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/newstages';

--7. [9999]登出(logout) 一级日志
--日志名称：logout.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_logout`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `rolename` string COMMENT '角色名称',
  `valueamount` int COMMENT '价值虚拟币总量',
  `onlinetimes` int COMMENT '在线时长(单位S)',
  `vip` string COMMENT 'Vip等级'
)
 COMMENT '[9999]登出(logout) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/logout';

--8. [5000-5999]充值(recharge) 一级日志
--日志名称：recharge.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_recharge`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `amount` double COMMENT '充值额度(RMB元)',
  `rechargechannel` string COMMENT '充值渠道id',
  `valuequantity` int COMMENT '价值虚拟币数量',
  `currency` string COMMENT '币种',
  `ip` string COMMENT '用户进行充值时设备的ip',
  `valueamount` int COMMENT '价值虚拟币总量',
  `vip` string COMMENT 'Vip等级',
  `goods_id` string COMMENT '商品id',
  `orderid` string COMMENT '订单号'
)
 COMMENT '[5000-5999]充值(recharge) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/recharge';

--9. [6010]升级(levelup) 一级日志
--日志名称：levelup.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_levelup`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `rolename` string COMMENT '角色名',
  `rolelevelaf` int COMMENT '升级后等级',
  `rolelevelbf` int COMMENT '升级前等级',
  `time` int COMMENT '升级时长(单位S)'
)
 COMMENT '[6010]升级(levelup) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/levelup';

--10. [7010]商城日志(shoptrade) 一级日志
--日志名称：shoptrade.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_shoptrade`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `itemtypeid` string COMMENT '商品类型id',
  `itemid` string COMMENT '商品id',
  `itemcount` int COMMENT '商品数量',
  `moneytypeid` string COMMENT '消耗货币id',
  `moneycount` int COMMENT '消耗货币数量',
  `shopid` string COMMENT '商城id',
  `vip` string COMMENT 'vip等级',
  `Leagueid` string COMMENT '联盟Id'
)
 COMMENT '[7010]商城日志(shoptrade) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/shoptrade';

--11. [8010]货币获得与消耗(money) 一级日志
--日志名称：money.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_money`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `causeid` string COMMENT '获得或消耗方式id',
  `quantity` int COMMENT '获得或消耗数量',
  `total` int COMMENT '获得或消耗后总量',
  `typeid` string COMMENT '货币id',
  `vip` string COMMENT 'Vip等级',
  `subcauseid` string COMMENT '获得与消耗位置',
  `action` int COMMENT '行为'
)
 COMMENT '[8010]货币获得与消耗(money) 一级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/money';

--12. [B2110]物品获得与消耗(item) 二级日志
--日志名称：item.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_item`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `itemtypeid` string COMMENT '物品类型id',
  `itemid` string COMMENT '物品id',
  `causeid` string COMMENT '获得或消耗方式id',
  `quantity` int COMMENT '获得或消耗数量',
  `vip` string COMMENT 'Vip等级',
  `subcauseid` string COMMENT '获得或消耗位置',
  `action` int COMMENT '行为',
  `total` int COMMENT '剩余总量',
  `timelimit` int COMMENT '物品使用时效'
)
 COMMENT '[B2110]物品获得与消耗(item) 二级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/item';

--13. [B3110&3120]任务(task) 二级日志
--日志名称：task.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_task`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `taskid` string COMMENT '任务id',
  `result` string COMMENT '结果',
  `tasktype` string COMMENT '任务类型'
)
 COMMENT '[B3110&3120]任务(task) 二级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/task';

--14. [B4100-B4199]关卡战斗(pvefight) 二级日志
--日志名称：pvefight.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_pvefight`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `stageid` string COMMENT '关卡id',
  `type` string COMMENT '战斗类型',
  `npcid` string COMMENT 'npcid',
  `result` string COMMENT '战斗结果',
  `mapid` string COMMENT '地图id',
  `star` string COMMENT '评价星级',
  `stagetype` string COMMENT '关卡类型',
  `time` int COMMENT '关卡用时(单位S)',
  `score` string COMMENT '通关时分数',
  `speed` int COMMENT '通关时速度'
)
 COMMENT '[B4100-B4199]关卡战斗(pvefight) 二级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/pvefight';

--15. [B6110]运营活动(activity) 二级日志(只有七日签到)
--日志名称：activity.log.yyyy-mm-dd
--注意: 标记的日志名不一致请检查！
CREATE EXTERNAL TABLE IF NOT EXISTS `server_activity`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `activityid` string COMMENT '活动id',
  `subid` string COMMENT '档位id'
)
 COMMENT '[B6110]运营活动(activity) 二级日志(只有七日签到)'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/activity';

--16. [B8110] 段位日志(grade) 二级日志
--日志名称：grade.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_grade`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `gradebf` string COMMENT '升级前段位',
  `result` string COMMENT '结果',
  `time` string COMMENT '停留时长(单位S)'
)
 COMMENT '[B8110] 段位日志(grade) 二级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/grade';

--17. [B8200-B8299] pvp战斗日志(pvpfight) 二级日志
--日志名称：pvpfight.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_pvpfight`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `battletype` string COMMENT '战斗类型',
  `battleid` string COMMENT '战斗模式id',
  `battlelevel` string COMMENT '战斗难度',
  `orderid` string COMMENT '战斗流水id',
  `teamid` string COMMENT '队伍id',
  `result` string COMMENT '战斗结果',
  `time` int COMMENT '耗时(s)',
  `targettype` string COMMENT '对手类型',
  `heroid` string COMMENT '卡牌id',
  `kotime` int COMMENT 'KO次数',
  `attacktime` int COMMENT '攻击行次数',
  `ischange` int COMMENT '约战配置更改'
)
 COMMENT '[B8200-B8299] pvp战斗日志(pvpfight) 二级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/pvpfight';

--18. [B8300-B8399] 匹配日志(pickup) 二级日志
--日志名称：pickup.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_pickup`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `battletype` string COMMENT '战斗类型',
  `battleid` string COMMENT '战斗模式id',
  `battlelevel` string COMMENT '战斗难度',
  `orderid` string COMMENT '战斗流水id',
  `teamid` string COMMENT '队伍id',
  `result` string COMMENT '匹配结果',
  `time` int COMMENT '匹配耗时(s)'
)
 COMMENT '[B8300-B8399] 匹配日志(pickup) 二级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/pickup';

--19. [C1200-C1299]好友(friends) 三级日志
--日志名称：friends.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_friends`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `friendsnum` int COMMENT '好友数量',
  `targetroleid` string COMMENT '对方id',
  `Online` string COMMENT '对方是否在线',
  `addtype` string COMMENT '好友操作'
)
 COMMENT '[C1200-C1299]好友(friends) 三级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/friends';

--20. [C1800]操作设置(operationset)三级日志
--日志名称：operationset.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_operationset`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `operationset` int COMMENT '操作方式',
  `agile` int COMMENT '灵敏度'
)
 COMMENT '[C1800]操作设置(operationset)三级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/operationset';

--21. [C1900]皮肤&印花&音乐包设置(skinset)三级日志
--日志名称：skinset.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_skinset`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `skintype` int COMMENT '使用皮肤类型',
  `skinid` int COMMENT '使用皮肤ID'
)
 COMMENT '[C1900]皮肤&印花&音乐包设置(skinset)三级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/skinset';

--22. [C2000]奖牌竞赛(medal)三级日志
--日志名称：medal.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_medal`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `stageid` string COMMENT '关卡id',
  `failtime` int COMMENT '当次的累计失败次数'
)
 COMMENT '[C2000]奖牌竞赛(medal)三级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/medal';

--23. [C2100]宠物事件(petevent)三级日志
--日志名称：petevnet.log.yyyy-mm-dd
CREATE EXTERNAL TABLE IF NOT EXISTS `server_petevnet`(
  `servertime` string COMMENT '时间',
  `appkey` string COMMENT '游戏标识',
  `version` string COMMENT '客户端版本',
  `modelname` string COMMENT '日志模块名',
  `normversion` string COMMENT '服务器日志规范版本号',
  `stepnumid` string COMMENT '步骤号',
  `serverid` string COMMENT '游戏服务器id',
  `gamechannel` string COMMENT '推广渠道id',
  `userid` string COMMENT '账号id',
  `roleid` string COMMENT '角色id',
  `rolelevel` int COMMENT '角色等级',
  `grade` string COMMENT '段位',
  `deviceid` string COMMENT '设备唯一标识',
  `petid` int COMMENT '触发的宠物id',
  `eventid` int COMMENT '触发的事件id',
  `eventtype` int COMMENT '事件类型',
  `charm` int COMMENT '触发时魅力值'
)
 COMMENT '[C2100]宠物事件(petevent)三级日志'
PARTITIONED BY (
  `dt` string COMMENT 'date' 
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001' 
STORED AS INPUTFORMAT 'com.hadoop.mapred.DeprecatedLzoTextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' 
LOCATION 'hdfs://WH-BI-NS/ydbi/original/server/elsfkhyj/petevnet';
