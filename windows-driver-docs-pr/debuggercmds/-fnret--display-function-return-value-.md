---
title: ".fnret (Display Function Return Value)"
description: "The .fnret command displays information about a function's return value."
keywords: [".fnret (Display Function Return Value) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .fnret (Display Function Return Value)
api_type:
- NA
---

# .fnret (Display Function Return Value)


The **.fnret** command displays information about a function's return value.

```dbgcmd
.fnret [/s] Address [Value] 
```

## Parameters


<span id="________s______"></span><span id="________S______"></span> **/s**   
Sets the **$callret** pseudo-register equal to the return value that is being displayed, including type information.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the function.

<span id="_______Value______"></span><span id="_______value______"></span><span id="_______VALUE______"></span> *Value*   
Specifies the return value to display. If you include *Value*, **.fnret** casts *Value* to the return type of the specified function and displays it in the format of the return type. If you omit *Value*, the debugger obtains the return value of the function from the return value registers.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

If you include the *Value* parameter, the **.fnret** command only casts this value to the proper type and displays the results.

If you omit *Value*, the debugger uses the return value registers to determine this value. If a function has returned more recently than the function that the *Address* parameter specifies, the value that is displayed will probably not be a value that this function returned.

