# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Union

from .._elements.chromium_element import ChromiumElement
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_frame import ChromiumFrame
from .._pages.chromium_page import ChromiumPage
from .._pages.mix_page import MixPage
from .._pages.tabs import ChromiumTab, MixTab


class Scroller(object):
    _t1: str = ...
    _t2: str = ...
    _owner: Union[ChromiumBase, ChromiumElement] = ...
    _wait_complete: bool = ...

    def __init__(self, owner: Union[ChromiumBase, ChromiumElement]): ...

    def _run_js(self, js: str): ...

    def to_top(self) -> None: ...

    def to_bottom(self) -> None: ...

    def to_half(self) -> None: ...

    def to_rightmost(self) -> None: ...

    def to_leftmost(self) -> None: ...

    def to_location(self, x: int, y: int) -> None: ...

    def up(self, pixel: int = 300) -> None: ...

    def down(self, pixel: int = 300) -> None: ...

    def left(self, pixel: int = 300) -> None: ...

    def right(self, pixel: int = 300) -> None: ...

    def _wait_scrolled(self) -> None: ...


class ElementScroller(Scroller):

    def to_see(self, center: Union[bool, None] = None) -> ChromiumElement: ...

    def to_center(self) -> ChromiumElement: ...

    def to_top(self) -> ChromiumElement: ...

    def to_bottom(self) -> ChromiumElement: ...

    def to_half(self) -> ChromiumElement: ...

    def to_rightmost(self) -> ChromiumElement: ...

    def to_leftmost(self) -> ChromiumElement: ...

    def to_location(self, x: int, y: int) -> ChromiumElement: ...

    def up(self, pixel: int = 300) -> ChromiumElement: ...

    def down(self, pixel: int = 300) -> ChromiumElement: ...

    def left(self, pixel: int = 300) -> ChromiumElement: ...

    def right(self, pixel: int = 300) -> ChromiumElement: ...


class PageScroller(Scroller):
    def __init__(self, owner: Union[ChromiumBase, ChromiumElement]): ...

    def to_see(self,
               loc_or_ele: Union[str, tuple, ChromiumElement],
               center: Union[bool, None] = None) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def to_top(self) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def to_bottom(self) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def to_half(self) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def to_rightmost(self) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def to_leftmost(self) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def to_location(self, x: int, y: int) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def up(self, pixel: int = 300) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def down(self, pixel: int = 300) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def left(self, pixel: int = 300) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def right(self, pixel: int = 300) -> Union[ChromiumTab, MixTab, ChromiumPage, MixPage]: ...

    def _to_see(self, ele: ChromiumElement, center: Union[bool, None]) -> None: ...


class FrameScroller(PageScroller):
    def __init__(self, frame: ChromiumFrame): ...

    def to_top(self) -> ChromiumFrame: ...

    def to_bottom(self) -> ChromiumFrame: ...

    def to_half(self) -> ChromiumFrame: ...

    def to_rightmost(self) -> ChromiumFrame: ...

    def to_leftmost(self) -> ChromiumFrame: ...

    def to_location(self, x: int, y: int) -> ChromiumFrame: ...

    def up(self, pixel: int = 300) -> ChromiumFrame: ...

    def down(self, pixel: int = 300) -> ChromiumFrame: ...

    def left(self, pixel: int = 300) -> ChromiumFrame: ...

    def right(self, pixel: int = 300) -> ChromiumFrame: ...

    def to_see(self, loc_or_ele, center=None) -> ChromiumFrame: ...
