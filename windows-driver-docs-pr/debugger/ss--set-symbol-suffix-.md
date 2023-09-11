---
title: ss (Set Symbol Suffix)
description: The ss command sets or displays the current suffix value that is used for symbol matching in numeric expressions.
keywords: ["ss (Set Symbol Suffix) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ss (Set Symbol Suffix)
api_type:
- NA
---

# ss (Set Symbol Suffix)


The **ss** command sets or displays the current suffix value that is used for symbol matching in numeric expressions.

```dbgcmd
ss [a|w|n] 
```

## <span id="ddk_cmd_set_symbol_suffix_dbg"></span><span id="DDK_CMD_SET_SYMBOL_SUFFIX_DBG"></span>Parameters


<span id="_______a______"></span><span id="_______A______"></span> **a**   
Specifies that the symbol suffix should be "A", matching many ASCII symbols.

<span id="_______w______"></span><span id="_______W______"></span> **w**   
Specifies that the symbol suffix should be "W", matching many Unicode symbols.

<span id="_______n______"></span><span id="_______N______"></span> **n**   
Specifies that the debugger should not use a symbol suffix. (This parameter is the default behavior.)

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about symbol matching, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

## Remarks

If you specify the **ss** command together with no parameters, the current state of the suffix value is displayed.

 

 





