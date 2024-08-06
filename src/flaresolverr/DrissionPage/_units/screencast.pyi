# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from pathlib import Path
from typing import Union

from .._pages.chromium_base import ChromiumBase


class Screencast(object):
    def __init__(self, owner: ChromiumBase):
        self._owner: ChromiumBase = ...
        self._path: Path = ...
        self._tmp_path: Path = ...
        self._running: bool = ...
        self._enable: bool = ...
        self._mode: str = ...

    @property
    def set_mode(self) -> ScreencastMode: ...

    def start(self, save_path: Union[str, Path] = None) -> None: ...

    def stop(self, video_name: str = None) -> str: ...

    def set_save_path(self, save_path: Union[str, Path] = None) -> None: ...

    def _run(self) -> None: ...

    def _onScreencastFrame(self, **kwargs) -> None: ...


class ScreencastMode(object):
    def __init__(self, screencast: Screencast):
        self._screencast: Screencast = ...

    def video_mode(self) -> None: ...

    def frugal_video_mode(self) -> None: ...

    def js_video_mode(self) -> None: ...

    def frugal_imgs_mode(self) -> None: ...

    def imgs_mode(self) -> None: ...
