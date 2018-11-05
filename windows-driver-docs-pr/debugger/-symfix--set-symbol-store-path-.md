---
title: .symfix (Set Symbol Store Path)
description: The .symfix command automatically sets the symbol path to point to the Microsoft symbol store.
ms.assetid: 9ad80217-e2d1-4776-a620-f2735b2c8f84
keywords: ["Set Symbol Store Path (.symfix) command", "SymSrv, Set Symbol Store Path (.symfix) command", ".symfix (Set Symbol Store Path) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .symfix (Set Symbol Store Path)
api_type:
- NA
ms.localizationpriority: medium
---

# .symfix (Set Symbol Store Path)


The **.symfix** command automatically sets the symbol path to point to the Microsoft symbol store.

```dbgcmd
.symfix[+] [LocalSymbolCache]
```

## <span id="ddk_meta_set_symbol_store_path_dbg"></span><span id="DDK_META_SET_SYMBOL_STORE_PATH_DBG"></span>Parameters


<span id="______________"></span> **+**   
Causes the Microsoft symbol store path to be appended to the existing symbol path. If this is not included, the existing symbol path is replaced.

<span id="_______LocalSymbolCache______"></span><span id="_______localsymbolcache______"></span><span id="_______LOCALSYMBOLCACHE______"></span> *LocalSymbolCache*   
Specifies the directory to be used as a local symbol cache. If this directory does not exist, it will be created when the symbol server begins copying files. If *LocalSymbolCache* is omitted, the sym subdirectory of the debugger installation directory will be used.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details, see [Using Symbol Servers and Symbol Stores](symbol-stores-and-symbol-servers.md).

Remarks
-------

The following example shows how to use **.symfix** to set a new symbol path that points to the Microsoft symbol store.

```dbgcmd
3: kd> .symfix c:\myCache
3: kd> .sympath
Symbol search path is: srv*
Expanded Symbol search path is: cache*c:\myCache;SRV*https://msdl.microsoft.com/download/symbols
```

The following example shows how to use **.symfix+** to append the existing symbol path with a path that points to the Microsoft symbol store.

```dbgcmd
3: kd> .sympath
Symbol search path is: c:\someSymbols
Expanded Symbol search path is: c:\somesymbols
3: kd> .symfix+ c:\myCache
3: kd> .sympath
Symbol search path is: c:\someSymbols;srv*
Expanded Symbol search path is: c:\somesymbols;cache*c:\myCache;SRV*https://msdl.microsoft.com/download/symbols
```

 

 





