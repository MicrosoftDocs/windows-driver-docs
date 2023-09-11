---
title: .enable_long_status (Enable Long Integer Display)
description: The .enable_long_status command specifies whether the debugger displays long integers in decimal format or in the default radix.
keywords: ["Enable Long Integer Display (.enable_long_status) command", ".enable_long_status (Enable Long Integer Display) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .enable_long_status (Enable Long Integer Display)
api_type:
- NA
---

# .enable\_long\_status (Enable Long Integer Display)


The **.enable\_long\_status** command specifies whether the debugger displays long integers in decimal format or in the default radix.

```dbgcmd
.enable_long_status 0 
.enable_long_status 1
```

## <span id="ddk_meta_enable_long_integer_display_dbg"></span><span id="DDK_META_ENABLE_LONG_INTEGER_DISPLAY_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Displays all long integers in decimal format. This is the default behavior of the debugger.

<span id="_______1______"></span> **1**   
Displays all long integers in the default radix.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **.enable\_long\_status** command affects the output of the [**dt (Display Type)**](dt--display-type-.md) command.

In WinDbg, **.enable\_long\_status** also affects the display in the [Locals window](locals-window.md) and the

Watch window. These windows are automatically updated after you issue **.enable\_long\_status**.

This command affects only the display of long integers. To control whether standard integers are displayed in decimal format or the default radix, use the [**.force\_radix\_output (Use Radix for Integers)**](-force-radix-output--use-radix-for-integers-.md) command.

**Note**   The [**dv (Display Local Variables)**](dv--display-local-variables-.md) command always displays long integers in the current number base.

 

To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command.

 

 





