# python-learn
python 学习
### 学习一些算法
### python的学习


# Game Prophet System(GPS)

游戏先知系统子项目用于数据前处理（分句、分词）及词向量训练。


## 新加作业（job）步骤

这里以新加xxx作业为例说明：

1. jobs包下新建 `xxx_job.py` - 作业的入口及处理逻辑，公共的模块可以放到`dependencies`包
2. configs目录新建 `xxx_config.json` - 配置参数 
3. tests包 `test_xxx_job.py`  - 测试

详细说明见下面。

## 环境

项目使用Python3.6（与spark2.2保持一致）并集成了:

- pyspark=2.2.0
- jieba
- pyltp
- gensim

注：
1. PyCharm + PySpark + Anaconda 开发环境配置，参考[6]

2.  pyltp需使用whl单独安装，编译需要c11（gcc-4.8支持）环境，linux打包的时候需要注意(模块就是一个so文件)，使用的时候要手动加载，见[3]。

    linux版pyltp运行时需要更新`/usr/lib64/libstdc++.so.6`（Centos 6.4默认的版本低）
    ```shell
    $ll /usr/lib64/libstdc++.so.6*
    lrwxrwxrwx 1 root root      30 Nov  1 19:23 /usr/lib64/libstdc++.so.6 -> /usr/lib64/libstdc++.so.6.0.19
    -rwxr-xr-x 1 root root  989840 Mar 22  2017 /usr/lib64/libstdc++.so.6.0.13
    -rwxr-xr-x 1 root root 6466427 Nov  1 19:21 /usr/lib64/libstdc++.so.6.0.19
    ```

## 项目结构

项目基本结构如下:

```bash
root/
 |-- dependencies/
 |   |-- logging.py
 |   |-- spark.py
 |-- jobs/
 |   |-- etl_job.py
 |-- configs/
 |   |-- etl_config.json
 |   tests/
 |   |-- test_data/
 |   |-- | -- employees/
 |   |-- | -- employees_report/
 |   |-- test_etl_job.py
 |   build_dependencies.sh
 |   packages.zip
```

包含ETL作业（将发送到Spark集群）的主要Python模块是`jobs/etl_job.py`。 `etl_job.py`所需的任何外部配置参数都以JSON格式存储在`configs/etl_config.json`中。 支持此作业的其他模块可以保存在`dependencies`文件夹中（稍后将详细介绍）。 在项目的根目录中，我们包含`build_dependencies.sh`，这是一个bash脚本，用于将这些依赖项构建到一个zip文件中以发送到集群（`packages.zip`）。 单元测试模块保存在`tests`文件夹中，用于测试的小块代表性输入和输出数据保存在`tests/test_data`文件夹中。

## 运行ETL作业

假设`$SPARK_HOME`环境变量指向您的本地Spark安装文件夹，那么可以使用终端中的以下命令从项目的根目录运行ETL作业，如果你使用了CDH组件可以使用`spark2-submit`命令提交任务

```bash
$SPARK_HOME/bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--py-files dependencies.zip \
--files configs/etl_config.json \
jobs/etl_job.py
```

简而言之，提供的选项有以下用途：

- `--master yarn` - 用于启动作业的Spark集群地址。集群使用Spark on Yarn模式，所以这里只能是yarn模式。本地测试可以为`local`
- `--deploy-mode client` - 部署模式
    - `client`	表示作业的 AM 会放在 Master 节点上运行。要注意的是，如果设置这个参数，那么需要同时指定上面 master 为 yarn。
    - `cluster`	表示 AM 会随机的在 worker 节点中的任意一台上启动运行。要注意的是，如果设置这个参数，那么需要同时指定上面 master 为yarn。
- `--files configs/etl_config.json` - （可选）ETL作业可能需要的任何配置文件的路径，这些文件放在每个executor的工作目录下面。
- `--py-files packages.zip` - 逗号分隔的”.zip”,”.egg”或者“.py”文件，这些文件放在python app的PYTHONPATH下面。
- `jobs/etl_job.py` - 包含要执行的ETL作业的Python模块文件。

完整详细的可能选项在[这里](http://spark.apache.org/docs/latest/submitting-applications.html)。注意，我们在作业中保留了一些选项（实际上是Spark应用程序） - 例如 `spark.cores.max`和`spark.executor.memory`在Python脚本中定义，因为它认为作业应明确包含对所需群集资源的请求。

## 将配置参数传递给ETL作业

尽管可以将参数传递给`etl_job.py`，就像运行作为“主”程序的任何通用Python模块一样，这里我们的方案项spark发送一个单独的配置文件 - 使用带有`spark2-submit`的`--files configs/etl_config.json`参数-包含JSON格式的配置，可以使用`json.loads（config_file_contents）`将其解析为一行代码中的Python字典。
eg:

```python
import json

config = json.loads("""{"field": "value"}""")
```

有关配置文件如何定位，打开和解析的具体细节，请参阅`dependencies/spark.py`中的`start_spark()`函数。

## 使用 `start_spark`测试和调试Spark作业

使用spark-submit将它们发送到集群来测试和调试Spark作业和检查堆栈跟踪以找出出错的线索有些不切实际，这里我们使用`start_spark`函数 - 可以在`dependencies/spark.py`中找到 - 以便于开发者知道正在执行它们的上下文的Spark作业 - 即作为spark-submit作业或在IPython控制台中。作业所需的Spark和作业配置参数的位置取决于检测到的执行上下文。 `start_spark`的doscstring给出了精确的细节，详细见[dependencies/spark.py](./dependencies/spark.py)。

```python
def start_spark(app_name='my_spark_app', master='local[*]', jar_packages=[],
                files=[], spark_config={}):
    """Start Spark session, get Spark logger and load config files.

    :param app_name: Name of Spark app.
    :param master: Cluster connection details (defaults to local[*].
    :param jar_packages: List of Spark JAR package names.
    :param files: List of files to send to Spark cluster (master and
        workers).
    :param spark_config: Dictionary of config key-value pairs.
    :return: A tuple of references to the Spark session, logger and
        config dict (only if available).
    """

    # ...

    return spark_sess, spark_logger, config_dict
```

下面是使用时候的代码片段,

```python
spark, log, config = start_spark(
    app_name='my_etl_job',
    jar_packages=['com.somesparkjar.dependency:1.0.0'],
    files=['configs/etl_config.json'])
```

如果从交互式控制台会话或调试器执行，将使用提供给`start_spark`的参数来设置Spark作业，但是如果这是作业执行的方式，将查找通过`spark-submit`发送的相同参数。

## 测试

为了使用Spark进行测试，我们使用`pyspark`Python包，它与基于每个test-suite的编程start-up和tear-down本地Spark实例，他与Spark JAR捆绑在一起（我们建议在`unittest.TestCase`中使用`setUp`和`tearDown`方法，每个test-suite执行一次）。 注意，使用`pyspark`运行Spark是使用Spark开发的另一种方法，而不是使用PySpark shell或`spark-submit`。

运行此项目的单元测试,

```bash
python -m unittest tests/test_*.py
```

## 打包ETL作业依赖项

在此项目中，可以跨不同ETL作业使用的函数保存在名为dependencies的模块中，并在特定作业(job)模块中引用，例如，

```python
from dependencies.spark import start_spark
```

此包以及其中引用的任何其他依赖项必须复制到每个Spark节点，以用于运行`dependencies`的所有作业。 这可以通过以下几种方式之一实现：

1. 在spark提交时使用`--py-files`将依赖项打包成`zip`和作业一起发送，容易控制依赖包的版本，不需要没法发包同步数据，推荐。
2. 提前在每个节点安装或者把依赖项复制到各个节点

依赖的三方模块使用`参考[7][8]`的方式，用于解决worker节点找不到模块问题。

Python环境安装：
```shell
# create conda environment for distribution
conda create -n nlp_env --copy -y -q python=3.6
source activate nlp_env

# install third module
pip install -r requirements.txt

cd ~/.conda/envs/
zip -r ../../nlp_env.zip nlp_env
```

提交Job应用，eg: [start_etl.sh](./bin/start_etl.sh)：
```shell
PYTHON_ROOT=./NLP/nlp_env
PYSPARK_PYTHON=${PYTHON_ROOT}/bin/python
 
spark-submit 
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=$PYSPARK_PYTHON \
--conf spark.yarn.appMasterEnv.PYSPARK_DRIVER_PYTHON=$PYSPARK_PYTHON \
--master yarn-cluster 
--files configs/etl_config.json \
--py-files dependencies.zip \
--archives nlp_env.zip#NLP \
jobs/etl_job.py
```

##参考：
1. [pyspark-example-project](https://github.com/AlexIoannides/pyspark-example-project)
2. [Best Practices Writing Production-Grade PySpark Jobs](https://developerzen.com/best-practices-writing-production-grade-pyspark-jobs-cb688ac4d20f)
3. [spark-submit 参数设置说明](https://www.alibabacloud.com/help/zh/doc-detail/28124.htm)
4. [如何在PySpark中调用C/C++代码](https://zhujun1980.github.io/2016/08/pyspark-cplusplus)
5. [pyltp在windows下的编译安装](https://mlln.cn/2018/01/31/pyltp%E5%9C%A8windows%E4%B8%8B%E7%9A%84%E7%BC%96%E8%AF%91%E5%AE%89%E8%A3%85/)
6. [Running PySpark on Anaconda in PyCharm](https://dimajix.de/running-pyspark-on-anaconda-in-pycharm/?lang=en)
7. [Running PySpark with Conda Env](https://henning.kropponline.de/2016/09/24/running-pyspark-with-conda-env/)
8. [Use your favorite Python library on PySpark cluster - Cloudera](https://blog.cloudera.com/blog/2017/04/use-your-favorite-python-library-on-pyspark-cluster-with-cloudera-data-science-workbench/)