# PySpark

> JAVA 安装与环境配置

1. [JAVA Download](https://www.oracle.com/java/technologies/javase-downloads.html)
2. 环境变量
    1. 新建系统变量
        1. JAVA_HOME: path\jdkwersion
        2. classpath: %JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar
    3. 新增系统Path变量
        4. Path: %JAVA_HOME%\bin
    5. CMD java -version

> PySpark 安装

1. 安装pyspark: pip install pyspark
2. CMD pyspark

> 配置Jupyter notebook启动PySpark的用户变量

1. pip install --upgrade jupyter notebook
1. PYSPARK_DRIVER_PYTHON：ipython
1. PYSPARK_DRIVER_PYTHON_OPTS：notebook