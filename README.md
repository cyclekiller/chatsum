# chatsum
群聊总结 做了一半 主要是群聊数据从TIM导出后进行拆分、格式化的逻辑

### 运行
下载仓库，把导出的TIM消息（{群聊名称}.txt）放在`data/{群聊名称}.txt`下，运行`clean_and_annotate_text.py`。将里面的`filename`更换成你的群聊名称。

### 例子
使用必应api进行总结（见`群聊实例1.txt`），不过必应有时会拒绝回答

![image](https://github.com/cyclekiller/chatsum/assets/48796459/3a5773df-2b74-4e54-aa3b-d41651285839)
