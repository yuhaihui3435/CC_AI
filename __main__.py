#!/usr/bin/env python
# coding: utf-8
import logging
from wxpy import *
import cfg


logger = logging.getLogger(__name__)

'''
初始化bot ,使用缓存保持登录状态，在控制台输出二维码进行扫码登录
'''
bot = Bot(cache_path=True, console_qr=True) # type: Bot
# 设置puid，puid 是 wxpy 特有的聊天对象/用户ID 不同于其他 ID 属性，puid 可始终被获取到，且具有稳定的唯一性
bot.enable_puid('wxpy_puid.pkl')
# 开启图灵AI
tuling=Tuling(cfg.tuling_key)

tlnbpz_group = None
company_group = None
tqyy_group = None

def refreshGroups():
    try:
        global tlnbpz_group
        tlnbpz_group=ensure_one(bot.groups().search('屯里那帮骗子们'))
    except Exception:
        logger.info("屯里那帮骗子群不活跃，无法获取到")
    try:
        global company_group
        company_group=ensure_one(bot.groups().search('@1555'))
    except Exception:
        logger.info("公司群不活跃，无法获取到")

    try:
        global tqyy_group
        tqyy_group=ensure_one(bot.groups().search('   天晴的三湖酒友群'))
    except Exception:
        logger.info("天晴群不活跃，无法获取到")

refreshGroups()



def main():
    print("程序启动完成")



#监听消息
@bot.register()
def msg_handler(msg):
    print(msg)
    refreshGroups();
@bot.register(tlnbpz_group, TEXT)
def sb_auto_reply(msg):
    print("开始自动回复一帮傻逼那个群",msg.chat)
    msg # type: Message

    if isinstance(msg.chat,Group) and  msg.is_at:
        msg_str=msg.text.split()
        if msg_str.__len__()>1: msg_str=msg_str[1]
        if msg_str.startswith('你是谁') or msg_str.startswith('介绍自己') or msg_str.startswith('who are you')or msg_str.startswith('way'):
            msg.reply("各位弟弟，大家好，我是七哥。欢欢，注意了，不要在装尸体了。还有你老流氓。")
        else:
            tuling.do_reply(msg)
    else:
        refreshGroups();

@bot.register(company_group, TEXT)
def company_auto_reply(msg):
    print("开始自动回复公司群",msg.chat)

@bot.register(tqyy_group, TEXT)
def tq_auto_reply(msg):
    print("开始自动回复天晴渔友的群",msg.chat)

if __name__ == '__main__':
    main()
    embed()
