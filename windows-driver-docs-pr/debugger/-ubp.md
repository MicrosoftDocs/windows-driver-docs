---
title: ubp
description: The ubp extension sets a breakpoint in user space.
ms.assetid: 1aaa6bec-59d3-4e37-a1c6-af3554da809f
keywords: ["ubp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ubp
api_type:
- NA
ms.localizationpriority: medium
---

# !ubp


The **!ubp** extension sets a breakpoint in user space.

```dbgcmd
!ubp Address 
```

## <span id="ddk__ubp_dbg"></span><span id="DDK__UBP_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal virtual address of the location in user space where the breakpoint is to be set.

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

The **!ubp** extension sets a breakpoint in user space. The breakpoint is set on the actual physical page, not just the virtual page.

Setting a physical breakpoint will simultaneously modify every virtual copy of a page, with unpredictable results. One possible consequence is corruption of the system state, possibly followed by a bug check or other system crash. Therefore, these breakpoints should be used cautiously, if at all.

This extension cannot be used to set breakpoints on pages that have been swapped out of memory. If a page is swapped out of memory after a breakpoint is set, the breakpoint ceases to exist.

It is not possible to set a breakpoint inside a page table or a page directory.

Each breakpoint is assigned a *breakpoint number*. To find out the breakpoint number assigned, use [**!ubl**](-ubl.md). Breakpoints are enabled upon creation. To step over a breakpoint, you must first disable it by using [**!ubd**](-ubd.md). To clear a breakpoint, use [**!ubc**](-ubc.md).

## <span id="see_also"></span>See also


[**!ubc**](-ubc.md)

[**!ubd**](-ubd.md)

[**!ube**](-ube.md)

[**!ubl**](-ubl.md)

[User Space and System Space](user-space-and-system-space.md)

 

 






