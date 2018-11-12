---
title: gpiokd.gpioext
description: The gpiokd.gpioext command displays information about a GPIO controller.
ms.assetid: D5DB5166-A173-409E-A6A1-3872A22D19E1
keywords: ["gpiokd.gpioext Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gpiokd.gpioext
api_type:
- NA
ms.localizationpriority: medium
---

# !gpiokd.gpioext


The **!gpiokd.gpioext** command displays information about a GPIO controller.

```dbgcmd
!gpiokd.gpioext ExtensionAddress [Flags]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______ExtensionAddress______"></span><span id="_______extensionaddress______"></span><span id="_______EXTENSIONADDRESS______"></span> *ExtensionAddress*   
Address of the [\_DEVICE\_EXTENSION](gpio-extensions.md#data-structures-used-by-the-gpio-commands) structure that represents the GPIO controller.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Flags that specify which information is displayed. This parameter is a bitwise OR of one or more of the following flags.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="0x1"></span><span id="0X1"></span>0x1</p></td>
<td align="left"><p>Displays the pin table for each bank.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="0x2"></span><span id="0X2"></span>0x2</p></td>
<td align="left"><p>If bit 0 (0x1) is set and this flag (0x2) is set, the display includes the Enable and Mask registers for each bank.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="0x4"></span><span id="0X4"></span>0x4</p></td>
<td align="left"><p>If bit 0 (0x1) is set and this flag (0x4) is set, the display includes unconfigured pins.</p></td>
</tr>
</tbody>
</table>

 

## <span id="DLL"></span><span id="dll"></span>DLL


Gpiokd.dll

## <span id="see_also"></span>See also


[GPIO Extensions](gpio-extensions.md)

 

 






