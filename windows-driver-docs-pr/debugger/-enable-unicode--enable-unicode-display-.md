---
title: .enable_unicode (Enable Unicode Display)
description: The .enable_unicode command specifies whether the debugger displays USHORT pointers and arrays as Unicode strings.
keywords: ["Enable Unicode Display (.enable_unicode) command", "UNICODE_STRING structure", ".enable_unicode (Enable Unicode Display) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .enable_unicode (Enable Unicode Display)
api_type:
- NA
---

# .enable\_unicode (Enable Unicode Display)


The **.enable\_unicode** command specifies whether the debugger displays USHORT pointers and arrays as Unicode strings.

```dbgcmd
.enable_unicode 0 
.enable_unicode 1
```

## <span id="ddk_meta_enable_unicode_display_dbg"></span><span id="DDK_META_ENABLE_UNICODE_DISPLAY_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Displays all 16-bit (USHORT) arrays and pointers as short integers. This is the default behavior of the debugger.

<span id="_______1______"></span> **1**   
Displays all 16-bit (USHORT) arrays and pointers as Unicode strings.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **.enable\_unicode** command affects the output of the [**dt (Display Type)**](dt--display-type-.md) command.

In WinDbg, the **.enable\_unicode** command also affects the display in the [Locals window](locals-window.md) and the Watch window. These windows are automatically updated after you issue **.enable\_unicode**.

You can also select or clear **Display 16-bit values** as Unicode on the shortcut menu of the Locals or Watch window to specify the display for USHORT arrays and pointers.

## <span id="see_also"></span>See also


[**ds, dS (Display String)**](ds--ds--display-string-.md)

 

 






