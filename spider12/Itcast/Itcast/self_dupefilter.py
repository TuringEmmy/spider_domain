# life is short, you need use python to create something!
# author    TuringEmmy
# time      11/28/18 3:29 PM
# project   spider_study
from __future__ import absolute_import

from copy import deepcopy

from scrapy.utils.request import request_fingerprint
from scrapy.utils.url import canonicalize_url

from scrapy_splash.utils import dict_hash

from scrapy_redis.dupefilter import RFPDupeFilter


def splash_request_fingerprint(request, include_headers=None):
    """ Request fingerprint which takes 'splash' meta key into account """

    fp = request_fingerprint(request, include_headers=include_headers)
    if 'splash' not in request.meta:
        return fp

    splash_options = deepcopy(request.meta['splash'])
    args = splash_options.setdefault('args', {})

    if 'url' in args:
        args['url'] = canonicalize_url(args['url'], keep_fragments=True)

    return dict_hash(splash_options, fp)


class SplashAwareDupeFilter(RFPDupeFilter):
    """
    DupeFilter that takes 'splash' meta key in account.
    It should be used with SplashMiddleware.
    """
    def request_fingerprint(self, request):
        return splash_request_fingerprint(request)

"""对于scrapy_redis和scrapy_splash的dupefilter_class在配置中是冲突的,
所以我们需要分别查看他俩的源代码的不同,把俩个指纹去重类的功能放到一个类当中"""
"""请直接复制粘贴使用"""