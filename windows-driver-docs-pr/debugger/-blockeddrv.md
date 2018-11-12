---
title: blockeddrv
description: The blockeddrv extension displays the list of blocked drivers on the target computer.
ms.assetid: 38331ff6-1957-4b28-90c0-10b2c77339fb
keywords: ["blocked drivers", "blockeddrv Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- blockeddrv
api_type:
- NA
ms.localizationpriority: medium
---

# !blockeddrv


The **!blockeddrv** extension displays the list of blocked drivers on the target computer.

```dbgcmd
    !blockeddrv
```

## <span id="ddk__blockeddrv_dbg"></span><span id="DDK__BLOCKEDDRV_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example:

```dbgcmd
kd> !blockeddrv
Driver:      Status    GUID
afd.sys      0:        {00000008-0206-0001-0000-000030C964E1}
agp440.sys   0:        {0000005C-175A-E12D-5000-010020885580}
atapi.sys    0:        {0000005C-B04A-E12E-5600-000020885580}
audstub.sys  0:        {0000005C-B04A-E12E-5600-000020885580}
Beep.SYS     0:        {0000005C-B04A-E12E-5600-000020885580}
Cdfs.SYS     0:        {00000008-0206-0001-0000-000008F036E1}
.....
```

 

 





