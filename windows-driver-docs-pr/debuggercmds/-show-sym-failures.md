---
title: .show_sym_failures
description: The .show_sym_failures command enables or disables the display of symbol lookup failures and type lookup failures.
keywords: [".show_sym_failures Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .show_sym_failures
api_type:
- NA
---

# .show\_sym\_failures


The **.show\_sym\_failures** command enables or disables the display of symbol lookup failures and type lookup failures.

```dbgcmd
.show_sym_failures /s 
.show_sym_failures /S
.show_sym_failures /t
.show_sym_failures /T
```

## Parameters


<span id="________s______"></span><span id="________S______"></span> **/s**   
Enables the display of symbol lookup failures.

<span id="________S______"></span><span id="________s______"></span> **/S**   
Disables the display of symbol lookup failures.

<span id="________t______"></span><span id="________T______"></span> **/t**   
Enables the display of type lookup failures.

<span id="________T______"></span><span id="________t______"></span> **/T**   
Disables the display of type lookup failures.

## <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment


|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

 

 





