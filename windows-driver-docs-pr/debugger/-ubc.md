---
title: ubc
description: The ubc extension clears a user-space breakpoint.
ms.assetid: 4BF2C589-A1C4-4714-B712-DD52D04704D1
keywords: ["ubc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ubc
api_type:
- NA
ms.localizationpriority: medium
---

# !ubc


The **!ubc** extension clears a user-space breakpoint.

```dbgcmd
!ubc BreakpointNumber 
```

## <span id="ddk__ubc_dbg"></span><span id="DDK__UBC_DBG"></span>Parameters


<span id="_______BreakpointNumber______"></span><span id="_______breakpointnumber______"></span><span id="_______BREAKPOINTNUMBER______"></span> *BreakpointNumber*   
Specifies the number of the breakpoint to be cleared. An asterisk (\*) indicates all breakpoints.

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

This will permanently delete a breakpoint set with [**!ubp**](-ubp.md).

## <span id="see_also"></span>See also


[**!ubd**](-ubd.md)

[**!ube**](-ube.md)

[**!ubl**](-ubl.md)

[**!ubp**](-ubp.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






