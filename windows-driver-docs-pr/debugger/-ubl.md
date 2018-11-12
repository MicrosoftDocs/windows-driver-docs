---
title: ubl
description: The ubl extension lists all user-space breakpoints and their current status.
ms.assetid: c2c40fa5-888f-49bb-a616-a139d7d2874d
keywords: ["breakpoints, user-space breakpoints", "ubl Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ubl
api_type:
- NA
ms.localizationpriority: medium
---

# !ubl


The **!ubl** extension lists all user-space breakpoints and their current status.

```dbgcmd
!ubl
```

## <span id="ddk__ubl_dbg"></span><span id="DDK__UBL_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example of the use and display of user-space breakpoints:

```dbgcmd
kd> !ubp 8014a131
This command is VERY DANGEROUS, and may crash your system!
If you don't know what you are doing, enter "!ubc *" now!

kd> !ubp 801544f4

kd> !ubd 1

kd> !ubl
 0: e ffffffff`8014a131 (ffffffff`82deb000) 1 ffffffff
 1: d ffffffff`801544f4 (ffffffff`82dff000) 0 ffffffff
```

Each line in this listing contains the breakpoint number, the status (**e** for enabled or **d** for disabled), the virtual address used to set the breakpoint, the physical address of the actual breakpoint, the byte position, and the contents of this memory location at the time the breakpoint was set.

## <span id="see_also"></span>See also


[**!ubc**](-ubc.md)

[**!ubd**](-ubd.md)

[**!ube**](-ube.md)

[**!ubp**](-ubp.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






