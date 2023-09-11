---
title: .srcnoisy (Noisy Source Loading)
description: The .srcnoisy command controls the verbosity level for source file loading.
keywords: [".srcnoisy (Noisy Source Loading) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .srcnoisy (Noisy Source Loading)
api_type:
- NA
---

# .srcnoisy (Noisy Source Loading)


The **.srcnoisy** command controls the verbosity level for source file loading.

```dbgcmd
.srcnoisy [Options]
```

## <span id="ddk_meta_noisy_source_loading_dbg"></span><span id="DDK_META_NOISY_SOURCE_LOADING_DBG"></span>Parameters


*Options*
Can be any one of the following options:

<span id="0"></span>0  
Disables the display of extra messages.

<span id="1"></span>1  
Displays information about the progress of source file loading and unloading.

<span id="2"></span>2  
Displays information about the progress of symbol file loading and unloading.

<span id="3"></span>3  
Displays all information displayed by options 1 and 2.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

With no parameters, **.srcnoisy** will display the current status of noisy source loading.

Noisy source loading should not be confused with noisy symbol loading -- that is controlled by the [**!sym noisy**](-sym.md) extension and by other means of controlling the [SYMOPT\_DEBUG](symbol-options.md#symopt-debug) setting.

 

 





