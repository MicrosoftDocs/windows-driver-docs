---
title: ld (Load Symbols)
description: The ld command loads symbols for the specified module and updates all module information.
keywords: ["ld (Load Symbols) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ld (Load Symbols)
api_type:
- NA
---

# ld (Load Symbols)


The **ld** command loads symbols for the specified module and updates all module information.

```dbgcmd
ld ModuleName [/f FileName]
```

## <span id="ddk_cmd_load_symbols_dbg"></span><span id="DDK_CMD_LOAD_SYMBOLS_DBG"></span>Parameters


<span id="_______ModuleName______"></span><span id="_______modulename______"></span><span id="_______MODULENAME______"></span> *ModuleName*   
Specifies the name of the module whose symbols are to be loaded. *ModuleName* can contain a variety of wildcard characters and specifiers.

<span id="________f_______FileName______"></span><span id="________f_______filename______"></span><span id="________F_______FILENAME______"></span> **/f** *FileName*   
Changes the name selected for the match. By default the module name is matched, but when **/f** is used the file name is matched instead of the module name. *FileName* can contain a variety of wildcard characters and specifiers. For more information on the syntax of wildcard characters and specifiers, see [String Wildcard Syntax](string-wildcard-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The debugger's default behavior is to use *lazy symbol loading* (also known as [deferred symbol loading](../debugger/deferred-symbol-loading.md)). This means that symbols are not actually loaded until they are needed.

The **ld** command, on the other hand, forces all symbols for the specified module to be loaded.

### Additional Information

For more information about deferred (lazy) symbol loading, see [Deferred Symbol Loading](../debugger/deferred-symbol-loading.md). For more information about other symbol options, see [Setting Symbol Options](../debugger/symbol-options.md).

 

 





