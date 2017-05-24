---
title: vprot
description: The vprot extension displays virtual memory protection information.
ms.assetid: 7ee863ef-abfd-4ee7-9bac-34472e60f3fa
keywords: ["memory, memory protection", "vprot Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- vprot
api_type:
- NA
---

# !vprot


The **!vprot** extension displays virtual memory protection information.

``` syntax
!vprot [Address]
```

## <span id="ddk__vprot_dbg"></span><span id="DDK__VPROT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address whose memory protection status is to be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Uext.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To view memory protection information for all memory ranges owned by the target process, use [**!vadump**](-vadump.md). For information about memory protection, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

The **!vprot** extension command can be used for both live debugging and dump file debugging.

Here is an example:

``` syntax
0:000> !vprot 30c191c
BaseAddress: 030c1000
AllocationBase: 030c0000
AllocationProtect: 00000080 PAGE_EXECUTE_WRITECOPY
RegionSize: 00011000
State: 00001000 MEM_COMMIT
Protect: 00000010 PAGE_EXECUTE
Type: 01000000 MEM_IMAGE
```

In this display, the AllocationProtect line shows the default protection that the entire region was created with. Note that individual addresses within this region can have their protection altered after memory is allocated (for example, if **VirtualProtect** is called). The Protect line shows the actual protection for this specific address. The possible protection values are PAGE\_NOACCESS, PAGE\_READONLY, PAGE\_READWRITE, PAGE\_EXECUTE, PAGE\_EXECUTE\_READ, PAGE\_EXECUTE\_READWRITE, PAGE\_WRITECOPY, PAGE\_EXECUTE\_WRITECOPY, and PAGE\_GUARD.

The State line also applies to the specific virtual address passed to **!vprot**. The possible state values are MEM\_COMMIT, MEM\_FREE, and MEM\_RESERVE.

The Type line shows the memory type. The possible values are MEM\_IMAGE, MEM\_MAPPED, and MEM\_PRIVATE.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!vprot%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




