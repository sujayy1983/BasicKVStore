"""
    Author: Sujayyendhiren
    Overview: A wrapper (boiler plate) around simplkv library for quicker 
              friction free integration and code reuse.
"""

import os
import json
import traceback

from simplekv.fs import FilesystemStore
from pathlib import Path


class KVStore():

    __CACHEPATH__ = str(Path(__file__).resolve().parent) + "/../cache/"

    def __init__(self, kvname):
        """
            Description: Initialize cache and directory paths

            Parameters:
                @kvname: Name the key value store.
        """

        #Attempt at creating the path only if it doesnt exist
        if not os.path.exists(KVStore.__CACHEPATH__):
            Path(KVStore.__CACHEPATH__).mkdir(parents=True, exist_ok=True)

        self.kvobj = FilesystemStore(f"{KVStore.__CACHEPATH__}{kvname}")


    def add(self, key, value):
        """
            Description:
                Simple key and value parameters are gathered as input and added
                to the simple kv store.

            Parameters:
                @key: Key that will be used commonly to lookup this kv pair.
                @value: Value that maybe string, list or dictionary.
        """

        if type(value) is str:
            self.kvobj.put(key, value.encode('utf-8'))

        else:
            self.kvobj.put(key, json.dumps(value).encode('utf-8'))


    def get(self, key):
        """
            Description: Method that assists with O(1) lookup

            Parameter(s):
                @key: Key that needs to be looked up in O(1) time
        """
        try:
            value = self.kvobj.get(key).decode('utf-8')

            if (value.startswith('[') and value.endswith(']')) or \
                    (value.startswith('{') and value.endswith('}')):
                return json.loads(value)
            else:
                return value

        except Exception as exc:
            print(f"DEBUG: {exc}")
            print(traceback.format_exc())
            return None
