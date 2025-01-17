#!/usr/bin/python3

# ibus-typing-booster - A completion input method for IBus
#
# Copyright (c) 2019 Mike FABIAN <mfabian@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

'''
This file implements test cases for finding similar emojis
'''

import sys
import logging
import unittest

from gi import require_version # type: ignore
require_version('IBus', '1.0')
from gi.repository import IBus # type: ignore

LOGGER = logging.getLogger('ibus-typing-booster')

sys.path.insert(0, "../engine")
import itb_util
import itb_emoji
sys.path.pop(0)

# Set the domain name to something invalid to avoid using
# the translations for the doctest tests. Translations may
# make the tests fail just because some translations are
# added, changed, or missing.
itb_emoji.DOMAINNAME = ''

@unittest.skipIf(
    '..' not in itb_emoji.find_cldr_annotation_path('en'),
    'Using external emoji annotations: %s '
    % itb_emoji.find_cldr_annotation_path('en')
    + 'Testing with older emoji annotations instead '
    'of those included in the ibus-typing-booster source is likely '
    'to create meaningless test failures.')
class EmojiSimilarTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        LOGGER.info("itb_emoji.find_cldr_annotation_path('en')->%s",
                    itb_emoji.find_cldr_annotation_path('en'))

    def tearDown(self) -> None:
        pass

    def test_dummy(self) -> None:
        self.assertEqual(True, True)

    def test_similar_query_is_not_an_emoji(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['en_US', 'it_IT', 'es_MX', 'es_ES', 'de_DE', 'ja_JP'])
        self.assertEqual(
            mq.similar('this is not an emoji', match_limit=5),
            [])

    def test_similar_white_smiling_face_en_US(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['en_US', 'it_IT', 'es_MX', 'es_ES', 'de_DE', 'ja_JP'])
        self.assertEqual(
            mq.similar('☺', match_limit=5),
            [('☺️', 'white smiling face [☺️, So, people, face, outlined, relaxed, smile, uc1, smiling face]', 9), ('😙', 'kissing face with smiling eyes [So, people, face, smile]', 4), ('😍', 'smiling face with heart-shaped eyes [So, people, face, smile]', 4), ('😋', 'face savouring delicious food [So, people, face, smile]', 4), ('😇', 'smiling face with halo [So, people, face, smile]', 4)])

    def test_similar_white_smiling_face_it_IT(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['it_IT', 'en_US', 'es_MX', 'es_ES', 'de_DE', 'ja_JP'])
        self.assertEqual(
            mq.similar('☺', match_limit=5),
            [('☺️', 'faccina sorridente [☺️, delineata, faccina, rilassata, sorridente]', 5), ('😗', 'faccina che bacia [faccina]', 1), ('😚', 'faccina che bacia con occhi chiusi [faccina]', 1), ('😘', 'faccina che manda un bacio [faccina]', 1), ('😙', 'faccina che bacia con occhi sorridenti [faccina]', 1)])

    def test_similar_camel_en_US(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['en_US', 'it_IT', 'es_MX', 'es_ES', 'de_DE', 'ja_JP'])
        self.assertEqual(
            [('🐫', 'bactrian camel [🐫, So, nature, bactrian, camel, hump, uc6, two-hump camel]', 8), ('🐪', 'dromedary camel [So, nature, hump, uc6, camel]', 5), ('🐐', 'goat [So, nature, uc6]', 3), ('🐑', 'sheep [So, nature, uc6]', 3), ('🐘', 'elephant [So, nature, uc6]', 3)],
            mq.similar('🐫', match_limit=5))

    def test_similar_camel_it_IT(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['it_IT', 'en_US','es_MX', 'es_ES', 'de_DE', 'ja_JP'])
        self.assertEqual(
            mq.similar('🐫', match_limit=5),
            [('🐫', 'cammello [🐫, animale, cammello, gobba]', 4), ('🐪', 'dromedario [animale, cammello, gobba]', 3), ('🐐', 'capra [animale]', 1), ('🐑', 'pecora [animale]', 1), ('🐘', 'elefante [animale]', 1)])

    def test_similar_camel_de_DE(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['de_DE', 'it_IT', 'en_US','es_MX', 'es_ES', 'ja_JP'])
        self.assertEqual(
            mq.similar('🐫', match_limit=5),
            [('🐫', 'Kamel [🐫, Kamel, Tier, zweihöckrig]', 4), ('🐪', 'Dromedar [Kamel, Tier]', 2), ('🐐', 'Ziege [Tier]', 1), ('🐑', 'Schaf [Tier]', 1), ('🐘', 'Elefant [Tier]', 1)])

    def test_similar_camel_es_MX(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['es_MX', 'it_IT', 'de_DE', 'en_US', 'es_ES', 'ja_JP'])
        self.assertEqual(
            mq.similar('🐫', match_limit=5),
            [('🐫', 'camello [🐫, animal, camélido, camello, joroba]', 5), ('🐪', 'dromedario [animal, camélido, joroba]', 3), ('\U0001f999', 'llama [camélido]', 1), ('🐐', 'cabra [animal]', 1), ('🐑', 'oveja [animal]', 1)])

    def test_similar_camel_es_ES(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['es_ES',  'it_IT', 'es_MX', 'de_DE', 'en_US', 'ja_JP'])
        self.assertEqual(
            mq.similar('🐫', match_limit=5),
            [('🐫', 'camello [🐫, bactriano, camello, desierto, dromedario, jorobas]', 6), ('🐪', 'dromedario [camello, desierto, dromedario]', 3), ('🏜️', 'desierto [desierto]', 1), ('🐫', 'cammello [🐫, animale, cammello, gobba]', 4), ('🐪', 'dromedario [animale, cammello, gobba]', 3)])

    def test_similar_euro_sign_es_ES(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['es_ES',  'it_IT', 'es_MX', 'de_DE', 'en_US', 'ja_JP'])
        self.assertEqual(
            mq.similar('€', match_limit=5),
            [('€', 'euro [€, divisa, EUR, euro, moneda]', 5), ('£', 'libra esterlina [divisa, moneda]', 2), ('₽', 'rublo [divisa, moneda]', 2), ('₹', 'rupia india [divisa, moneda]', 2), ('¥', 'yen [divisa, moneda]', 2)])

    def test_similar_surfer_es_ES(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['es_ES',  'it_IT', 'es_MX', 'de_DE', 'en_US', 'ja_JP'])
        self.assertEqual(
            mq.similar('🏄‍♂', match_limit = 2),
            [('🏄\u200d♂️', 'hombre haciendo surf [🏄\u200d♂️, hombre, hombre haciendo surf, surf, surfero, surfista]', 6), ('🏄🏻\u200d♂️', 'hombre haciendo surf: tono de piel claro [hombre, hombre haciendo surf, surf, surfero, surfista]', 5)])

    def test_similar_de_DE_versus_de_CH(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['de_DE'])
        self.assertEqual(
            mq.similar('🤐', match_limit = 3),
            [('🤐', 'Gesicht mit Reißverschlussmund [🤐, Gesicht, Gesicht mit Reißverschlussmund, Mund, Reißverschluss]', 5), ('🫡', 'salutierendes Gesicht [Gesicht]', 1), ('🤔', 'nachdenkendes Gesicht [Gesicht]', 1)])
        mq = itb_emoji.EmojiMatcher(
            languages = ['de_CH'])
        self.assertEqual(
            mq.similar('🤐', match_limit = 3),
            [('🤐', 'Smiley mit Reissverschlussmund [🤐, Gesicht, Mund, Reissverschluss, Smiley mit Reissverschlussmund]', 5), ('🫡', 'grüssendes Gesicht [Gesicht]', 1), ('😅', 'Lachender Smiley mit kaltem Schweiss [Gesicht]', 1)])

    def test_similar_show_keywords_option_en_US(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['en_US'])
        self.assertEqual(
            [('🐌', 'snail [🐌, So, nature, snail, uc6]', 5), ('🐛', 'bug [So, nature, uc6]', 3), ('🐚', 'spiral shell [So, nature, uc6]', 3)],
            mq.similar('🐌', match_limit = 3))
        self.assertEqual(
            [('🐌', 'snail', 5), ('🐛', 'bug', 3), ('🐚', 'spiral shell', 3)],
            mq.similar('🐌', match_limit = 3, show_keywords=False))

    @unittest.skipIf(
        itb_emoji.IMPORT_PINYIN_SUCCESSFUL,
        "Skipping because import pinyin worked.")
    def test_similar_horse_racing_pinyin_missing_zh_CN(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['zh_CN'])
        self.assertEqual(
            mq.similar('🏇', match_limit = 3),
            [('🏇', '赛马 [🏇, 赛马, 马]', 3), ('🏇🏻', '赛马: 较浅肤色 [赛马, 马]', 2), ('🏇🏼', '赛马: 中等-浅肤色 [赛马, 马]', 2)])

    @unittest.skipUnless(
        itb_emoji.IMPORT_PINYIN_SUCCESSFUL,
        "Skipping because import pinyin failed.")
    def test_similar_horse_racing_pinyin_available_zh_CN(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['zh_CN'])
        self.assertEqual(
            mq.similar('🏇', match_limit = 3),
            [('🏇', '赛马 [🏇, 赛马, sàimǎ, 马, mǎ]', 5), ('🏇🏻', '赛马: 较浅肤色 [赛马, sàimǎ, 马, mǎ]', 4), ('🏇🏼', '赛马: 中等-浅肤色 [赛马, sàimǎ, 马, mǎ]', 4)])

    @unittest.skipIf(
        itb_emoji.IMPORT_PINYIN_SUCCESSFUL,
        "Skipping because import pinyin worked.")
    def test_similar_horse_racing_pinyin_missing_zh_TW(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['zh_TW'])
        self.assertEqual(
            mq.similar('🏇', match_limit = 1),
            [('🏇', '賽馬 [🏇, 賽馬, 騎馬]', 3)])

    @unittest.skipUnless(
        itb_emoji.IMPORT_PINYIN_SUCCESSFUL,
        "Skipping because import pinyin failed.")
    def test_similar_horse_racing_pinyin_available_zh_TW(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['zh_TW'])
        self.assertEqual(
            mq.similar('🏇', match_limit = 1),
            [('🏇', '賽馬 [🏇, 賽馬, sàimǎ, 騎馬, qímǎ]', 5)])

    @unittest.skipIf(
        itb_emoji.IMPORT_PYKAKASI_SUCCESSFUL,
        "Skipping because import pykakasi worked.")
    def test_candidates_pykakasi_missing_ja_JP(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['ja_JP'])
        self.assertEqual(
            [('🐤', 'ひよこ [🐤, ひな, ひよこ, 動物, 横を向いているひよこ, 顔, 鳥]', 7), ('🐣', '卵からかえったひよこ [ひな, ひよこ, 動物, 顔, 鳥]', 5), ('🐥', '前を向いているひよこ [ひな, ひよこ, 動物, 鳥]', 4), ('🐦', '鳥 [動物, 顔, 鳥]', 3), ('🐔', 'にわとり [動物, 顔, 鳥]', 3)],
            mq.similar('🐤', match_limit=5))
        self.assertEqual(
            [('🐌', 'かたつむり [🐌, かたつむり, でんでん虫, 虫]', 4), ('🦋', 'チョウ [虫]', 1), ('🐛', '毛虫 [虫]', 1), ('🐜', 'アリ [虫]', 1), ('🐝', 'ミツバチ [虫]', 1)],
            mq.similar('🐌', match_limit=5))
        self.assertEqual(
            [('😱', '恐怖 [😱, がーん, ショック, 叫び, 恐怖, 顔]', 6), ('🙀', '絶望する猫 [がーん, ショック, 顔]', 3), ('😨', '青ざめ [がーん, 顔]', 2), ('🤯', '頭爆発 [ショック, 顔]', 2), ('🫨', '震えている顔 [ショック, 顔]', 2)],
            mq.similar('😱', match_limit=5))

    @unittest.skipUnless(
        itb_emoji.IMPORT_PYKAKASI_SUCCESSFUL,
        "Skipping because import pykakasi failed.")
    def test_candidates_pykakasi_available_ja_JP(self) -> None:
        mq = itb_emoji.EmojiMatcher(
            languages = ['ja_JP'])
        self.assertEqual(
            [('🐤', 'ひよこ [🐤, ひな, ひよこ, 動物, どうぶつ, 横を向いているひよこ, よこをむいているひよこ, 顔, かお, 鳥, とり, hina, hiyoko, doubutsu, yokowomuiteiruhiyoko, kao, tori]', 17), ('🐣', '卵からかえったひよこ [ひな, ひよこ, 動物, どうぶつ, 顔, かお, 鳥, とり, hina, hiyoko, doubutsu, kao, tori]', 13), ('🐥', '前を向いているひよこ [ひな, ひよこ, 動物, どうぶつ, 鳥, とり, hina, hiyoko, doubutsu, tori]', 10), ('🐦', '鳥 [動物, どうぶつ, 顔, かお, 鳥, とり, doubutsu, kao, tori]', 9), ('🐔', 'にわとり [動物, どうぶつ, 顔, かお, 鳥, とり, doubutsu, kao, tori]', 9)],
            mq.similar('🐤', match_limit=5))
        self.assertEqual(
            [('🐌', 'かたつむり [🐌, かたつむり, でんでん虫, でんでんむし, 虫, むし, katatsumuri, dendenmushi, mushi]', 9), ('🦋', 'チョウ [虫, むし, mushi]', 3), ('🐛', '毛虫 [虫, むし, mushi]', 3), ('🐜', 'アリ [虫, むし, mushi]', 3), ('🐝', 'ミツバチ [虫, むし, mushi]', 3)],
            mq.similar('🐌', match_limit=5))
        self.assertEqual(
            [('😱', '恐怖 [😱, がーん, ショック, しょっく, 叫び, さけび, 恐怖, きょうふ, 顔, かお, gaan, shokku, sakebi, kyoufu, kao]', 15), ('🙀', '絶望する猫 [がーん, ショック, しょっく, 顔, かお, gaan, shokku, kao]', 8), ('🤯', '頭爆発 [ショック, しょっく, 顔, かお, shokku, kao]', 6), ('🫨', '震えている顔 [ショック, しょっく, 顔, かお, shokku, kao]', 6), ('😨', '青ざめ [がーん, 顔, かお, gaan, kao]', 5)],
            mq.similar('😱', match_limit=5))


if __name__ == '__main__':
    LOG_HANDLER = logging.StreamHandler(stream=sys.stderr)
    LOGGER.setLevel(logging.DEBUG)
    LOGGER.addHandler(LOG_HANDLER)
    unittest.main()
