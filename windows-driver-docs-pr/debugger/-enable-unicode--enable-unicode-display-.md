---
title: .enable_unicode (Enable Unicode Display)
description: The .enable_unicode command specifies whether the debugger displays USHORT pointers and arrays as Unicode strings.
ms.assetid: bb029ff4-1802-4d91-ba4b-9db10fa7c055
keywords: ["Enable Unicode Display (.enable_unicode) command", "UNICODE_STRING structure", ".enable_unicode (Enable Unicode Display) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .enable_unicode (Enable Unicode Display)
api_type:
- NA
ms.localizationpriority: medium
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

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.enable\_unicode** command affects the output of the [**dt (Display Type)**](dt--display-type-.md) command.

In WinDbg, the **.enable\_unicode** command also affects the display in the [Locals window](locals-window.md) and the Watch window. These windows are automatically updated after you issue **.enable\_unicode**.

You can also select or clear **Display 16-bit values** as Unicode on the shortcut menu of the Locals or Watch window to specify the display for USHORT arrays and pointers.

## <span id="see_also"></span>See also


[**ds, dS (Display String)**](ds--ds--display-string-.md)

 

 






