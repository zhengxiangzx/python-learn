#!/usr/bin/env python
# encoding: utf-8


from dependencies.process_data import split_sentence, wordtokenizer

raw_sentences = [
    ' 游戏氪金内容不多，而且即使不氪金，也能玩的很愉快，不存在什么RMB玩家碾压',
    '1，卡顿，卡顿还是很明显的。 2，希望出一个屏蔽其他玩家的功能，一堆犬夜叉太影响走剧情了。 3，希望后续能出奈落等反派主角。 4，希望主角的技能能根据剧情发展更新，开局铁碎牙什么的太违和了。 目前就这么多，等在玩一段时间再评论。希望这个游戏好好做，我觉得可以赶超崩坏（前提是没有崩坏那么肝😂'
]

print(split_sentence(raw_sentences))

sentences =[]

wordtokenizer(raw_sentences,sentences)
print(sentences)
