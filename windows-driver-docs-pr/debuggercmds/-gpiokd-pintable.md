---
title: "!gpiokd.pintable"
description: "The !gpiokd.pintable extension displays information about an array of GPIO pins."
keywords: ["!gpiokd.pintable Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gpiokd.pintable
api_type:
- NA
---

# !gpiokd.pintable


The **!gpiokd.pintable** extension displays information about an array of GPIO pins.

```dbgcmd
!gpiokd.pintable PinBase PinCount [Flags]
```

## Parameters


<span id="_______PinBase______"></span><span id="_______pinbase______"></span><span id="_______PINBASE______"></span> *PinBase*   
Address of an array of [\_GPIO\_PIN\_INFORMATION\_ENTRY](gpio-extensions.md#data-structures-used-by-the-gpio-commands) structures.

<span id="_______PinCount______"></span><span id="_______pincount______"></span><span id="_______PINCOUNT______"></span> *PinCount*   
The number of pins to display.

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
<td align="left"><p>Not used by this command.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="0x2"></span><span id="0X2"></span>0x2</p></td>
<td align="left"><p>Not used by this command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="0x4"></span><span id="0X4"></span>0x4</p></td>
<td align="left"><p>The display includes unconfigured pins.</p></td>
</tr>
</tbody>
</table>

## DLL

Gpiokd.dll

## See also

[GPIO Extensions](gpio-extensions.md)
