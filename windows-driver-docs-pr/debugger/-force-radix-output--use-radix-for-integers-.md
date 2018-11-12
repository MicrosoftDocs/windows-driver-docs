---
title: .force_radix_output (Use Radix for Integers)
description: The .force_radix_output command specifies whether integers are displayed in decimal format or in the default radix.
ms.assetid: 9ce79919-69fd-426f-8de1-34d0721c35a5
keywords: ["Use Radix for Integers (.force_radix_output) command", ".force_radix_output (Use Radix for Integers) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .force_radix_output (Use Radix for Integers)
api_type:
- NA
ms.localizationpriority: medium
---

# .force\_radix\_output (Use Radix for Integers)


The **.force\_radix\_output** command specifies whether integers are displayed in decimal format or in the default radix.

```dbgcmd
.force_radix_output 0 
.force_radix_output 1 
```

## <span id="ddk_meta_use_radix_for_integers_dbg"></span><span id="DDK_META_USE_RADIX_FOR_INTEGERS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Displays all integers (except for long integers) in decimal format. This is the default behavior for the Debugger.

<span id="_______1______"></span> **1**   
Displays all integers (except for long integers) in the default radix.

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

The **.force\_radix\_output** command affects the output of the [**dt (Display Type)**](dt--display-type-.md) command.

In WinDbg, **.force\_radix\_output** also affects the display in the [Locals window](locals-window.md) and the Watch window. You can select or clear **Always display numbers in default radix** on the shortcut menu of the Locals or Watch window to have the same effect as **.force\_radix\_output**. These windows are automatically updated after you issue this command.

The **.force\_radix\_output** command affects only the display of standard integers. To specify whether long integers are displayed in decimal format or the default radix, use the [**.enable\_long\_status (Enable Long Integer Display)**](-enable-long-status--enable-long-integer-display-.md) command.

To change the default radix, use the [**n (Set Number Base)**](n--set-number-base-.md) command.

 

 





