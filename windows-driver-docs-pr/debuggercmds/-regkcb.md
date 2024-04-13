---
title: "!regkcb (WinDbg)"
description: "The !regkcb extension displays a registry key control block."
keywords: ["!regkcb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- regkcb
api_type:
- NA
---

# !regkcb

The **!regkcb** extension displays a registry key control block.

```dbgcmd
!regkcb Address 
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the key control block.

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
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For information about the registry and its components, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

In Windows 2000, **!regkcb** displays a specific registry key control block.

In Windows XP and later versions of Windows, the [**!reg**](-reg.md) extension command should be used instead.

Every registry key has a control block that contains properties, such as its permissions.

