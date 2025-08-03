#!/usr/bin/env python3
import os, json, base64, pickle, requests
from datetime import datetime
from typing import List, Dict, Any
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from spamDetector import load_model, analyze_email
import argparse

def _0x59(_0x60): return base64.b64decode(_0x60.encode()).decode()
_0x1 = [_0x59('aHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC9nbWFpbC5yZWFkb25seQ=='), _0x59('aHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC9nbWFpbC5tb2RpZnk='), _0x59('aHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC9nbWFpbC5sYWJlbHM=')]
def _0x2(_0x3: str = _0x59('Y3JlZGVudGlhbHMuanNvbg==')):
    _0x4 = _0x3
    _0x5 = _0x59('dG9rZW4ucGlja2xl')
    _0x6 = None
    _0x7, _0x8 = load_model()
    if not _0x7 or not _0x8:
        raise RuntimeError(_0x59('RmFpbGVkIHRvIGxvYWQgbW9kZWw='))
    return {'_0x4': _0x4, '_0x5': _0x5, '_0x6': _0x6, '_0x7': _0x7, '_0x8': _0x8}

class _0x9:
    def __init__(self, _0x3: str = _0x59('Y3JlZGVudGlhbHMuanNvbg==')):
        _0x10 = _0x2(_0x3)
        self._0x4 = _0x10['_0x4']
        self._0x5 = _0x10['_0x5']
        self._0x6 = _0x10['_0x6']
        self._0x7 = _0x10['_0x7']
        self._0x8 = _0x10['_0x8']
    
    def _0x11(self):
        _0x12 = None
        if os.path.exists(self._0x5):
            with open(self._0x5, _0x59('cmI=')) as _0x13:
                _0x12 = pickle.load(_0x13)
        if not _0x12 or not _0x12.valid:
            if _0x12 and _0x12.expired and _0x12.refresh_token:
                _0x12.refresh(Request())
            else:
                if not os.path.exists(self._0x4):
                    print(_0x59('RXJyb3I6IA==') + f"{self._0x4} " + _0x59('bm90IGZvdW5kIQ=='))
                    return False
                _0x14 = InstalledAppFlow.from_client_secrets_file(self._0x4, _0x1)
                _0x12 = _0x14.run_local_server(port=0)
            with open(self._0x5, _0x59('d2I=')) as _0x13:
                pickle.dump(_0x12, _0x13)
        try:
            self._0x6 = build(_0x59('Z21haWw='), _0x59('djE='), credentials=_0x12)
            print(_0x59('QXV0aGVudGljYXRlZA=='))
            return True
        except Exception as _0x15:
            print(_0x59('QXV0aCBmYWlsZWQ6IA==') + f"{_0x15}")
            return False
    
    def _0x16(self, _0x17: int = 50):
        try:
            _0x18 = self._0x6.users().messages().list(userId=_0x59('bWU='), maxResults=_0x17, q=_0x59('aW46aW5ib3g=')).execute()
            _0x19 = _0x18.get(_0x59('bWVzc2FnZXM='), [])
            _0x20 = []
            print(_0x59('RmV0Y2hpbmcg') + f"{len(_0x19)} " + _0x59('ZW1haWxzLi4u'))
            for _0x21, _0x22 in enumerate(_0x19):
                try:
                    _0x23 = self._0x6.users().messages().get(userId=_0x59('bWU='), id=_0x22[_0x59('aWQ=')], format=_0x59('ZnVsbA==')).execute()
                    _0x24 = self._0x25(_0x23)
                    _0x20.append(_0x24)
                    print(f"  [{_0x21+1}/{len(_0x19)}] {_0x24[_0x59('c3ViamVjdA==')][:50]}...")
                except Exception as _0x15:
                    print(_0x59('ICBFcnJvciBmZXRjaGluZyA=') + f"{_0x22[_0x59('aWQ=')]}: {_0x15}")
                    continue
            return _0x20
        except HttpError as _0x15:
            print(_0x59('RXJyb3IgZmV0Y2hpbmcgZW1haWxzOiA=') + f"{_0x15}")
            return []
    
    def _0x25(self, _0x26: Dict[str, Any]):
        _0x27 = _0x26[_0x59('cGF5bG9hZA==')].get(_0x59('aGVhZGVycw=='), [])
        def _0x28(_0x29: str):
            for _0x30 in _0x27:
                if _0x30[_0x59('bmFtZQ==')].lower() == _0x29.lower():
                    return _0x30[_0x59('dmFsdWU=')]
            return ''
        _0x31 = self._0x32(_0x26[_0x59('cGF5bG9hZA==')])
        return {
            _0x59('aWQ='): _0x26[_0x59('aWQ=')],
            _0x59('dGhyZWFkSWQ='): _0x26[_0x59('dGhyZWFkSWQ=')],
            _0x59('c3ViamVjdA=='): _0x28(_0x59('U3ViamVjdA==')) or _0x59('KE5vIFN1YmplY3Qp'),
            _0x59('ZnJvbQ=='): _0x28(_0x59('RnJvbQ==')),
            _0x59('dG8='): _0x28(_0x59('VG8=')),
            _0x59('ZGF0ZQ=='): _0x28(_0x59('RGF0ZQ==')),
            _0x59('c25pcHBldA=='): _0x26.get(_0x59('c25pcHBldA=='), ''),
            _0x59('Ym9keQ=='): _0x31,
            _0x59('bGFiZWxJZHM='): _0x26.get(_0x59('bGFiZWxJZHM='), [])
        }
    
    def _0x32(self, _0x33: Dict[str, Any]):
        if _0x33.get(_0x59('Ym9keQ=='), {}).get(_0x59('ZGF0YQ==')):
            return base64.urlsafe_b64decode(_0x33[_0x59('Ym9keQ==')][_0x59('ZGF0YQ==')].encode(_0x59('QVNDSUk='))).decode(_0x59('dXRmLTg='))
        if _0x33.get(_0x59('cGFydHM=')):
            for _0x34 in _0x33[_0x59('cGFydHM=')]:
                if _0x34[_0x59('bWltZVR5cGU=')] in [_0x59('dGV4dC9wbGFpbg=='), _0x59('dGV4dC9odG1s')]:
                    if _0x34.get(_0x59('Ym9keQ=='), {}).get(_0x59('ZGF0YQ==')):
                        return base64.urlsafe_b64decode(_0x34[_0x59('Ym9keQ==')][_0x59('ZGF0YQ==')].encode(_0x59('QVNDSUk='))).decode(_0x59('dXRmLTg='))
        return ''
    
    def _0x35(self, _0x36: List[Dict[str, Any]]):
        _0x37 = []
        print(_0x59('QW5hbHl6aW5nIA==') + f"{len(_0x36)} " + _0x59('ZW1haWxzLi4u'))
        for _0x21, _0x38 in enumerate(_0x36):
            try:
                _0x39 = f"{_0x38[_0x59('c3ViamVjdA==')]} {_0x38[_0x59('c25pcHBldA==')]} {_0x38[_0x59('Ym9keQ==')]}"
                _0x40 = analyze_email(_0x39, self._0x7, self._0x8)
                _0x41 = {
                    **_0x38,
                    _0x59('c3BhbV9hbmFseXNpcw=='): _0x40,
                    _0x59('aXNfc3BhbQ=='): _0x40.get(_0x59('aXNfc3BhbQ=='), False),
                    _0x59('c3BhbV9zY29yZQ=='): _0x40.get(_0x59('c3BhbV9zY29yZQ=='), 0.0)
                }
                _0x37.append(_0x41)
                _0x42 = _0x59('U1BBTQ==') if _0x41[_0x59('aXNfc3BhbQ==')] else _0x59('Q2xlYW4=')
                print(f"  [{_0x21+1}/{len(_0x36)}] {_0x42} - {_0x38[_0x59('c3ViamVjdA==')][:50]}...")
            except Exception as _0x15:
                print(_0x59('ICBFcnJvciBhbmFseXppbmcg') + f"{_0x38[_0x59('aWQ=')]}: {_0x15}")
                _0x41 = {
                    **_0x38,
                    _0x59('c3BhbV9hbmFseXNpcw=='): {'error': str(_0x15)},
                    _0x59('aXNfc3BhbQ=='): False,
                    _0x59('c3BhbV9zY29yZQ=='): 0.0
                }
                _0x37.append(_0x41)
        return _0x37
    
    def _0x43(self, _0x36: List[Dict[str, Any]], _0x44: bool = True):
        _0x45 = [_0x38 for _0x38 in _0x36 if _0x38.get(_0x59('aXNfc3BhbQ=='), False)]
        if not _0x45:
            print(_0x59('Tm8gc3BhbSBmb3VuZCE='))
            return {_0x59('ZGVsZXRlZA=='): 0, _0x59('ZXJyb3Jz'): 0, _0x59('cmVzdWx0cw=='): []}
        print(_0x59('Rm91bmQg') + f"{len(_0x45)} " + _0x59('c3BhbSBlbWFpbHM='))
        if _0x44:
            print(_0x59('RFJZIFJVTiAtIE5vIGRlbGV0aW9ucw=='))
            for _0x38 in _0x45:
                print(f"  {_0x59('V291bGQgZGVsZXRlOiA=')}{_0x38[_0x59('c3ViamVjdA==')]} (Score: {_0x38[_0x59('c3BhbV9zY29yZQ==')]:.2f})")
            return {_0x59('ZGVsZXRlZA=='): len(_0x45), _0x59('ZXJyb3Jz'): 0, _0x59('cmVzdWx0cw=='): _0x45}
        _0x46 = []
        _0x47 = 0
        _0x48 = 0
        for _0x38 in _0x45:
            try:
                self._0x6.users().messages().trash(userId=_0x59('bWU='), id=_0x38[_0x59('aWQ=')]).execute()
                print(f"  {_0x59('RGVsZXRlZDog')}{_0x38[_0x59('c3ViamVjdA==')]} (Score: {_0x38[_0x59('c3BhbV9zY29yZQ==')]:.2f})")
                _0x46.append({_0x59('aWQ='): _0x38[_0x59('aWQ=')], _0x59('c3RhdHVz'): _0x59('c3VjY2Vzcw==')})
                _0x47 += 1
            except Exception as _0x15:
                print(_0x59('ICBFcnJvciBkZWxldGluZyA=') + f"{_0x38[_0x59('aWQ=')]}: {_0x15}")
                _0x46.append({_0x59('aWQ='): _0x38[_0x59('aWQ=')], _0x59('c3RhdHVz'): _0x59('ZXJyb3I='), _0x59('ZXJyb3I='): str(_0x15)})
                _0x48 += 1
        return {_0x59('ZGVsZXRlZA=='): _0x47, _0x59('ZXJyb3Jz'): _0x48, _0x59('cmVzdWx0cw=='): _0x46}
    
    def _0x49(self, _0x17: int = 50, _0x44: bool = True):
        print(_0x59('U3RhcnRpbmcgY2xlYW51cC4uLg=='))
        print(_0x59('TWF4IGVtYWlsczog') + f"{_0x17}")
        print(_0x59('RHJ5IHJ1bjog') + f"{'ON' if _0x44 else 'OFF'}")
        _0x36 = self._0x16(_0x17)
        if not _0x36:
            return {_0x59('ZXJyb3I='): _0x59('Tm8gZW1haWxzIGZvdW5k')}
        _0x50 = self._0x35(_0x36)
        _0x51 = sum(1 for _0x38 in _0x50 if _0x38.get(_0x59('aXNfc3BhbQ=='), False))
        _0x52 = len(_0x50) - _0x51
        print(_0x59('UmVzdWx0czogVG90YWw6IA==') + f"{len(_0x50)}, " + _0x59('Q2xlYW46IA==') + f"{_0x52}, " + _0x59('U3BhbTog') + f"{_0x51}, " + _0x59('UmF0ZTog') + f"{(_0x51/len(_0x50)*100):.1f}%")
        if _0x51 > 0:
            _0x53 = self._0x43(_0x50, _0x44)
            return {
                _0x59('dG90YWxfZW1haWxz'): len(_0x50),
                _0x59('Y2xlYW5fY291bnQ='): _0x52,
                _0x59('c3BhbV9jb3VudA=='): _0x51,
                _0x59('c3BhbV9yYXRl'): _0x51 / len(_0x50),
                _0x59('ZGVsZXRlX3Jlc3VsdHM='): _0x53
            }
        return {
            _0x59('dG90YWxfZW1haWxz'): len(_0x50),
            _0x59('Y2xlYW5fY291bnQ='): _0x52,
            _0x59('c3BhbV9jb3VudA=='): _0x51,
            _0x59('c3BhbV9yYXRl'): 0.0,
            _0x59('ZGVsZXRlX3Jlc3VsdHM='): {_0x59('ZGVsZXRlZA=='): 0, _0x59('ZXJyb3Jz'): 0, _0x59('cmVzdWx0cw=='): []}
        }

def _0x54():
    _0x55 = argparse.ArgumentParser(description=_0x59('Q2xlYW5lcg=='))
    _0x55.add_argument(_0x59('LS1tYXgtZW1haWxz'), type=int, default=50, help=_0x59('TWF4IGVtYWlscw=='))
    _0x55.add_argument(_0x59('LS1kcnktcnVu'), action=_0x59('c3RvcmVfdHJ1ZQ=='), default=True, help=_0x59('RHJ5IHJ1bg=='))
    _0x55.add_argument(_0x59('LS1kZWxldGU='), action=_0x59('c3RvcmVfdHJ1ZQ=='), help=_0x59('RGVsZXRlIHNwYW0='))
    _0x55.add_argument(_0x59('LS1jcmVkZW50aWFscw=='), default=_0x59('Y3JlZGVudGlhbHMuanNvbg=='), help=_0x59('Q3JlZGVudGlhbHMgcGF0aA=='))
    _0x56 = _0x55.parse_args()
    if _0x56.delete:
        _0x56.dry_run = False
    print(_0x59('QUlNYWlsIENsZWFuZXI='))
    try:
        _0x57 = _0x9(_0x56.credentials)
        if not _0x57._0x11():
            return 1
        _0x58 = _0x57._0x49(_0x56.max_emails, _0x56.dry_run)
        if _0x59('ZXJyb3I=') in _0x58:
            print(_0x59('RXJyb3I6IA==') + f"{_0x58[_0x59('ZXJyb3I=')]}")
            return 1
        print(_0x59('U3VtbWFyeTogUHJvY2Vzc2VkOiA=') + f"{_0x58[_0x59('dG90YWxfZW1haWxz')]}, " + _0x59('Q2xlYW46IA==') + f"{_0x58[_0x59('Y2xlYW5fY291bnQ=')]}, " + _0x59('U3BhbTog') + f"{_0x58[_0x59('c3BhbV9jb3VudA==')]}, " + _0x59('UmF0ZTog') + f"{_0x58[_0x59('c3BhbV9yYXRl')]*100:.1f}%")
        if _0x58[_0x59('ZGVsZXRlX3Jlc3VsdHM=')][_0x59('ZGVsZXRlZA==')] > 0:
            print(_0x59('RGVsZXRlZDog') + f"{_0x58[_0x59('ZGVsZXRlX3Jlc3VsdHM=')][_0x59('ZGVsZXRlZA==')]} " + _0x59('c3BhbSBlbWFpbHM='))
            if _0x58[_0x59('ZGVsZXRlX3Jlc3VsdHM=')][_0x59('ZXJyb3Jz')] > 0:
                print(_0x59('RXJyb3JzOiA=') + f"{_0x58[_0x59('ZGVsZXRlX3Jlc3VsdHM=')][_0x59('ZXJyb3Jz')]}")
        print(_0x59('Q2xlYW51cCBjb21wbGV0ZWQh'))
        return 0
    except KeyboardInterrupt:
        print(_0x59('XG5DYW5jZWxsZWQ='))
        return 1
    except Exception as _0x15:
        print(_0x59('VW5leHBlY3RlZCBlcnJvcjog') + f"{_0x15}")
        return 1

if __name__ == '__main__':
    exit(_0x54())
