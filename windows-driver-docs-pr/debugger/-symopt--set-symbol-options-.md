---
title: .symopt (Set Symbol Options)
description: The .symopt command sets or displays the symbol options.
keywords: [".symopt (Set Symbol Options) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .symopt (Set Symbol Options)
api_type:
- NA
---

# .symopt (Set Symbol Options)


The **.symopt** command sets or displays the symbol options.

```dbgcmd
.symopt+ Flags 
.symopt- Flags 
.symopt 
```

## <span id="ddk_meta_set_symbol_options_dbg"></span><span id="DDK_META_SET_SYMBOL_OPTIONS_DBG"></span>Parameters


<span id="______________"></span> **+**   
Causes the symbol options specified by *Flags* to be set. If **.symopt** is used with *Flags* but no plus or minus sign, a plus sign is assumed.

<span id="_______-______"></span> **-**   
Causes the symbol options specified by *Flags* to be cleared.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the symbol options to be changed. *Flags* must be the sum of the bit flags of these symbol options.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For a list and description of each symbol option, its bit flag, and other methods of setting and clearing these options, see [Setting Symbol Options](symbol-options.md).

## Remarks

Without any arguments, **.symopt** displays the current symbol options.

 

 





