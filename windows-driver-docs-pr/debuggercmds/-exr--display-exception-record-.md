---
title: ".exr (Display Exception Record)"
description: "The .exr command displays the contents of an exception record."
keywords: ["Display Exception Record (.exr) command", "exception record", ".exr (Display Exception Record) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .exr (Display Exception Record)
api_type:
- NA
---

# .exr (Display Exception Record)

The **.exr** command displays the contents of an exception record.

```dbgcmd
.exr Address 
.exr -1
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address* - Specifies the address of the exception record. If you specify **-1** as the address, the debugger displays the most recent exception.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

The **.exr** command displays information that is related to an exception that the debugger encountered on the target computer. The information that is displayed includes the exception address, the exception code, the exception flags, and a variable list of parameters to the exception.

You can usually obtain the *Address* by using the [**!pcr**](-pcr.md) extension.

The **.exr** command is often used to debug bug check 0x1E. For more information and an example, see [**Bug Check 0x1E**](../debugger/bug-check-0x1e--kmode-exception-not-handled.md) (KMODE\_EXCEPTION\_NOT\_HANDLED).

## See also

[Changing Contexts](../debugger/changing-contexts.md)

[Register Context](../debugger/changing-contexts.md#register-context)

[.ecxr (Display Exception Context Record)](-ecxr--display-exception-context-record-.md)

[.trap](-trap--display-trap-frame-.md)

