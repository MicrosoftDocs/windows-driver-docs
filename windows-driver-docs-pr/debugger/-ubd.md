---
title: ubd
description: The ubd extension temporarily disables a user-space breakpoint.
ms.assetid: a639c5e0-111c-45c7-ac7d-6b7e70c1de4f
keywords: ["ubd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ubd
api_type:
- NA
ms.localizationpriority: medium
---

# !ubd


The **!ubd** extension temporarily disables a user-space breakpoint.

```dbgcmd
!ubd BreakpointNumber 
```

## <span id="ddk__ubd_dbg"></span><span id="DDK__UBD_DBG"></span>Parameters


<span id="_______BreakpointNumber______"></span><span id="_______breakpointnumber______"></span><span id="_______BREAKPOINTNUMBER______"></span> *BreakpointNumber*   
Specifies the number of the breakpoint to be disabled. An asterisk (\*) indicates all breakpoints.

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

Disabled breakpoints will be ignored. Use [**!ube**](-ube.md) to re-enable the breakpoint.

## <span id="see_also"></span>See also


[**!ubc**](-ubc.md)

[**!ube**](-ube.md)

[**!ubl**](-ubl.md)

[**!ubp**](-ubp.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






