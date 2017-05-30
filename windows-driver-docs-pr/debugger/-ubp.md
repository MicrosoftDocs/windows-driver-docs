---
title: ubp
description: The ubp extension sets a breakpoint in user space.
ms.assetid: 1aaa6bec-59d3-4e37-a1c6-af3554da809f
keywords: ["ubp Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ubp
api_type:
- NA
---

# !ubp


The **!ubp** extension sets a breakpoint in user space.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ubp%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





