---
title: "!bcb (WinDbg)"
description: "The !bcb extension displays the specified buffer control block."
keywords: ["cache manager", "!bcb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bcb
api_type:
- NA
---

# !bcb


The **!bcb** extension displays the specified buffer control block.

```dbgcmd
!bcb Address
```

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the buffer control block.

## DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable (see Remarks section)</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

For information about other cache management extensions, use the [**!cchelp**](-cchelp.md) extension.

## Remarks

This extension is available for Windows 2000 only. In Windows XP or later, use the [**dt nt!\_BCB Address**](dt--display-type-.md) command to display the buffer control block directly.

