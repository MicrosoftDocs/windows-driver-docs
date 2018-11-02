---
title: ube
description: The ube extension re-enables a user-space breakpoint.
ms.assetid: caa13c30-e03a-44fd-9221-66e44eec88af
keywords: ["ube Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ube
api_type:
- NA
ms.localizationpriority: medium
---

# !ube


The **!ube** extension re-enables a user-space breakpoint.

```dbgcmd
!ube BreakpointNumber 
```

## <span id="ddk__ube_dbg"></span><span id="DDK__UBE_DBG"></span>Parameters


<span id="_______BreakpointNumber______"></span><span id="_______breakpointnumber______"></span><span id="_______BREAKPOINTNUMBER______"></span> *BreakpointNumber*   
Specifies the number of the breakpoint to be enabled. An asterisk (\*) indicates all breakpoints.

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

This is used to re-enable a breakpoint that was disabled by [**!ubd**](-ubd.md).

## <span id="see_also"></span>See also


[**!ubc**](-ubc.md)

[**!ubd**](-ubd.md)

[**!ubl**](-ubl.md)

[**!ubp**](-ubp.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






