---
title: vadump
description: The vadump extension displays all virtual memory ranges and their corresponding protection information.
ms.assetid: b13aa852-7333-41fc-ad66-4386040522d8
keywords: ["vadump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- vadump
api_type:
- NA
ms.localizationpriority: medium
---

# !vadump


The **!vadump** extension displays all virtual memory ranges and their corresponding protection information.

```dbgcmd
    !vadump [-v] 
```

## <span id="ddk__vadump_dbg"></span><span id="DDK__VADUMP_DBG"></span>Parameters


<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Causes the display to include information about each original allocation region as well. Because individual addresses within a region can have their protection altered after memory is allocated (by **VirtualProtect**, for example), the original protection status for this larger region may not be the same as that of each range within the region.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To view memory protection information for a single virtual address, use [**!vprot**](-vprot.md). For information about memory protection, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

Remarks
-------

Here is an example:

```dbgcmd
0:000> !vadump
BaseAddress:       00000000
RegionSize:        00010000
State:             00010000  MEM_FREE
Protect:           00000001  PAGE_NOACCESS

BaseAddress:       00010000
RegionSize:        00001000
State:             00001000  MEM_COMMIT
Protect:           00000004  PAGE_READWRITE
Type:              00020000  MEM_PRIVATE
.........
```

In this display, the State line shows the state of the memory range beginning at the specified BaseAddress. The possible state values are MEM\_COMMIT, MEM\_FREE, and MEM\_RESERVE.

The Protect line shows the protection status of this memory range. The possible protection values are PAGE\_NOACCESS, PAGE\_READONLY, PAGE\_READWRITE, PAGE\_EXECUTE, PAGE\_EXECUTE\_READ, PAGE\_EXECUTE\_READWRITE, PAGE\_WRITECOPY, PAGE\_EXECUTE\_WRITECOPY, and PAGE\_GUARD.

The Type line shows the memory type. The possible values are MEM\_IMAGE, MEM\_MAPPED, and MEM\_PRIVATE.

Here is an example using the **-v** parameter:

```dbgcmd
0:000> !vadump -v
BaseAddress:       00000000
AllocationBase:    00000000
RegionSize:        00010000
State:             00010000  MEM_FREE
Protect:           00000001  PAGE_NOACCESS

BaseAddress:       00010000
AllocationBase:    00010000
AllocationProtect: 00000004  PAGE_READWRITE
RegionSize:        00001000
State:             00001000  MEM_COMMIT
Protect:           00000004  PAGE_READWRITE
Type:              00020000  MEM_PRIVATE
.........
```

When **-v** is used, the AllocationProtect line shows the default protection that the entire region was created with. The Protect line shows the actual protection for this specific address.

 

 





