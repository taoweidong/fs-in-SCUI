# Django 学习项目


# 创建Django的应用
在 Django 中创建一个新的应用程序（APP）需要以下几个步骤：

1. 打开终端或命令提示符，并导航到你的 Django 项目的根目录。

2. 运行以下命令来创建新的 APP：
```
python manage.py startapp <app_name>
```
这里，`<app_name>` 是你想要给你的应用程序取的名字。

3. 在创建应用程序后，你会在项目的根目录中看到一个新的目录，该目录名与你的应用程序名相同。

4. 接下来，你需要将新创建的应用程序添加到项目的主配置文件 `settings.py` 中。打开这个文件，并找到 `INSTALLED_APPS` 列表。在这个列表中，将你的 APP 的名称添加到列表末尾，类似这样：
```
INSTALLED_APPS = [
    ...
    '<app_name>',
]
```
确保用你实际的应用程序名替换 `<app_name>`。

5. 配置数据库（可选）。如果你的应用程序需要使用数据库，你需要在 `settings.py` 文件中配置数据库连接。

6. 运行数据库迁移，以创建必要的数据库表和模式。在终端或命令提示符中运行以下命令：
```
python manage.py makemigrations
python manage.py migrate
```

现在，你已经成功创建了一个新的 Django 应用程序。你可以在新创建的应用程序目录中定义和编写模型、视图和模板来实现你的应用程序逻辑。


# 根据模型创建数据库和数据表

在终端或命令提示符中，运行以下命令以创建数据库表和模式：

python manage.py makemigrations
python manage.py migrate