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

tuling=Tuling(cfg.tuling_key)

print(bot.groups)

tlnbpz_group =[]
company_group=[]
tqyy_group=[]



def main():
    # 设置puid，puid 是 wxpy 特有的聊天对象/用户ID 不同于其他 ID 属性，puid 可始终被获取到，且具有稳定的唯一性
    bot.enable_puid('wxpy_puid.pkl')
    refreshGroups()

#监听消息
@bot.register()
def msg_handler(msg):
    print(msg)

@bot.register(tlnbpz_group, TEXT)
def tlnbpz_auto_reply(msg):
    msg # type: Message
    if tlnbpz_group!=None and  msg.is_at:
        msg_str=str.strip(msg.text)
        if(msg_str.startswith('你是谁') or msg_str.startswith('介绍自己') or msg_str.startswith('who are you')or msg_str.startswith('way')):
            msg.reply("各位弟弟，大家好，我是七哥。欢欢，注意了，不要在装尸体了。还有你老流氓。")
        else:
            tuling.do_reply(msg)
    while tlnbpz_group==None :
        refreshGroups();


@bot.register(company_group, TEXT)
def company_auto_reply(msg):
    if company_group!=None and  msg.is_at:
        tuling.do_reply(msg)
    while company_group==None :
        refreshGroups();
@bot.register(tqyy_group, TEXT)
def tqyy_auto_reply(msg):
    if tqyy_group!=None and  msg.is_at:
        tuling.do_reply(msg)
        msg_str=msg.text;



    while tqyy_group==None :
        refreshGroups();

def refreshGroups():
    try:
        tlnbpz_group = ensure_one(bot.groups().search('屯里那帮骗子'))
    except Exception:
        logger.info("屯里那帮骗子群不活跃，无法获取到")
    try:
        company_group = ensure_one(bot.groups().search('@1555'))
    except Exception:
        logger.info("公司群不活跃，无法获取到")

    try:
        tqyy_group = ensure_one(bot.groups().search('天晴的三湖酒友群'))
    except Exception:
        logger.info("天晴群不活跃，无法获取到")


if __name__ == '__main__':
    main()
    embed()
