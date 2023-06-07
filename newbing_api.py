import asyncio
from EdgeGPT import Chatbot, ConversationStyle

prompt = """下面是qq群“ChatRWKV技术研发群”的一段聊天记录节选，“@某人”表示对某人说。请总结这段聊天记录的主要内容。
支持向量机说：梦回11年CSDN爆出明文密码
支持向量机说：套壳都套不明白 连prompt都不用 直接str.replace()
支持向量机说：[图片]
星辰说：[表情]
星辰说：还不如我们自己微调开发的
hex说：[图片]
hex说：[表情]
发不出Q1不改名说：@alohachen @alohachen 那CSDN怎么过的
alohachen说：CSDN像黑灰产吗
发不出Q1不改名说：[表情]太tmd像了
发不出Q1不改名说：原地tp卖钱这种屌事也就CSDN做的出来的
发不出Q1不改名说：有一说一，CSDN不被打。这监管了个寂寞
发不出Q1不改名说：先不聊效果
线性层说：csdn脱离fgw直接死掉的企业
线性层说：没啥好关注的
线性层说：great firewall
浮说：csdn确实该死
🐳说：rwkv 7b模型 6G显存 32内存 加载会爆[表情]
狼魂说：@发不出Q1不改名 7b@发不出Q1不改名 一直没弄明白，那个蒸馏是怎么收费的，chatGPT 3.5的API是否收费 ？
多层感知器说：@Dumber @Dumber 那能持续学习的模型国内没上线希望了
线性层说：[图片]
线性层说：随便搞个培训，买显卡的钱就有了
星辰说：这些我觉得我都可以讲
多层感知器说：就这东西
星辰说：最多9.9
多层感知器说：还4000多
线性层说：网课都这个价格，实际10块钱的知识，我也觉得是这样
线性层说：不过对大老板来说，4000块让你拥有一个能和其他老板吹牛的基础知识，也不是很贵？
多层感知器说：网上搜搜都能收到
多层感知器说：虽然他们不会搜索
多层感知器说：哦问chatgpt都能问到
多层感知器说：虽然他们没飞机场问
线性层说：对抗训练呢，正反例都发出来[表情]
Aster说：怎么吹出去，别的老板为什么不以智商税的名义嘲讽
Aster说：还是得看主讲人啥地位，你把open ai的ceo请来，这智商税也不是不能交
狼魂说：昨天群主倡议搞数据的事情，大家能不能贡献点爬虫，从不同的类别去爬，然后搞数据清洗
微雨说：有规划分工吗
支持向量机说：@大胆 负责
左之易说：群里有没有谁成功训练了微调lora模型？传授一下经验吧
海绵宝宝说：首先需要一个网盘
海绵宝宝说：大伙都没传数据
海绵宝宝说：其次需要一个数据清洗工具
海绵宝宝说：剩下的就是搞数据清洗
ewq说：数据清洗是什么意思？
潴:-D硪祥称了、说：取其精华去其糟粕
支持向量机说：@海绵宝宝 @海绵宝宝 有repo了
支持向量机说：别大伙各建各网盘
支持向量机说：各扫门前雪还得再整合
🐳说：端测想跑起模型 还是压力山大呀
左之易说：本来想周末训练lora模型的，你们都没训练过吗？
左之易说：还有其他的训练方法吗？
未来可期的🐶正说：@支持向量机 谁搞个脚本撒，翻译，清洗，上传[表情]
左之易说：推特公布了源代码？
alohachen说：里面有对马斯克的特殊人工处理[表情]
左之易说：@未来可期的正 @alohachen 你们会自己训练对话模型吗？
alohachen说：等卡中[表情]
左之易说：autodl训练啊
左之易说：@alohachen 你用的是什么训练方法？
澹海说：vicuna的办法不错，你可以把自己语料混在里面训练
🐳说：训练模型 有框架 [表情]
未来可期的🐶正说：@左之易 整理好语料格式塞进去微调撒
未来可期的🐶正说：懒人包也出来了
左之易说：@未来可期的正 @未来可期的正 能指一下路吗？
Blealtan说：@线性层 [图片] 这smjbdx
反馈连接说：?
mu?(?ə(说：@左之易 @左之易 是哪个模型的lora版？
反馈连接说：@Blealtan @Blealtan 有病吧？
前馈网络说：[图片]
发不出Q1不改名说：有病吧
前馈网络说：看上去就是骗钱玩意
发不出Q1不改名说：你骗我
发不出Q1不改名说：起码得软件所吧
反馈连接说：草.
前馈网络说：[表情][表情]
Holocene说：“职业教育研究院”
Holocene说：逗我玩呢
发不出Q1不改名说：[图片]
发不出Q1不改名说：监管来了
Holocene说：确实需要监管
大胆说： 有什么办法套出提示词吗
ewq说：[图片]
ewq说：@反馈连接 @反馈连接 这叫光明正大割韭菜
ewq说：@Blealtan @Blealtan
左之易说：@mu?(?ə( @mu?(?ə( 看群公告"""

def get_plain_text(response):
    return response['item']['messages'][1]['text']

async def main():
    bot = Chatbot(cookiePath='./cookie.json', proxy="http://127.0.0.1:7890")
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.balanced, wss_link="wss://sydney.bing.com/sydney/ChatHub")
    print(response)
    print(get_plain_text(response))
    await bot.close()

if __name__ == "__main__":
    input(f'Press enter to send message. The prompt you are going to send is: {prompt}')
    asyncio.run(main())
