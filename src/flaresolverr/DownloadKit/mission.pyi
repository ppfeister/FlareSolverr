# -*- coding:utf-8 -*-
from pathlib import Path
from typing import Union, List, Optional

from ..DataRecorder import ByteRecorder
from requests import Session
from requests.structures import CaseInsensitiveDict

from .downloadKit import DownloadKit


class MissionData(object):
    """保存任务数据的对象"""
    url: str = ...
    goal_path: Union[str, Path] = ...
    rename: Optional[str] = ...
    suffix: Optional[str] = ...
    file_exists: str = ...
    split: bool = ...
    kwargs: dict = ...
    offset: int = ...

    def __init__(self, url: str, goal_path: Union[str, Path], rename: Optional[str], suffix: Optional[str],
                 file_exists: str, split: bool, kwargs: dict, offset: int = 0): ...


class BaseTask(object):
    """任务类基类"""
    _DONE: str = ...
    RESULT_TEXTS: dict = ...

    _id: str = ...
    state: str = ...
    result: Optional[str, False] = ...
    info: str = ...

    def __init__(self, ID: Union[int, str]): ...

    @property
    def id(self) -> Union[int, str]: ...

    @property
    def data(self): ...

    @property
    def is_done(self) -> bool: ...

    def set_states(self,
                   result: Optional[bool, str] = None,
                   info: str = None,
                   state: str = 'done') -> None: ...


class Mission(BaseTask):
    """任务类"""
    file_name: Optional[str] = ...
    _data: MissionData = ...
    _path: Optional[str, Path] = ...
    _recorder: Optional[ByteRecorder] = ...
    size: Optional[float] = ...
    done_tasks_count: int = ...
    tasks_count: int = ...
    tasks: List[Task] = ...
    download_kit: DownloadKit = ...
    session: Session = ...
    headers: CaseInsensitiveDict = ...
    method: str = ...
    encoding: Optional[str] = ...

    def __init__(self, ID: int, download_kit: DownloadKit, file_url: str, goal_path: Union[str, Path], rename: str,
                 suffix: str, file_exists: str, split: bool, encoding: Optional[str], kwargs: dict): ...

    def __repr__(self) -> str: ...

    def _set_session(self) -> Session: ...

    def _handle_kwargs(self, url: str, kwargs: dict) -> dict: ...

    @property
    def data(self) -> MissionData: ...

    @property
    def path(self) -> Union[str, Path]: ...

    def _set_path(self, path: Optional[str, Path]) -> None: ...

    @property
    def recorder(self) -> ByteRecorder: ...

    @property
    def rate(self) -> Optional[float]: ...

    def _set_done(self, result: Optional[bool, str], info: str) -> None: ...

    def _a_task_done(self, is_success: bool, info: str) -> None: ...

    def _break_mission(self, result: Optional[bool, str], info: str) -> None: ...

    def cancel(self) -> None: ...

    def del_file(self): ...

    def wait(self, show: bool = True, timeout: float = 0) -> tuple: ...


class Task(BaseTask):
    """子任务类"""
    mission: Mission = ...
    range: Optional[list] = ...
    size: Optional[int] = ...
    _downloaded_size: int = 0

    def __init__(self, mission: Mission, range_: Optional[list], ID: str, size: Optional[int]): ...

    def __repr__(self) -> str: ...

    @property
    def mid(self) -> int: ...

    @property
    def data(self) -> MissionData: ...

    @property
    def path(self) -> str: ...

    @property
    def file_name(self) -> str: ...

    @property
    def rate(self) -> Optional[float]: ...

    def add_data(self, data: bytes, seek: int = None) -> None: ...

    def clear_cache(self) -> None: ...

    def _set_done(self, result: Optional[bool, str], info: str) -> None: ...