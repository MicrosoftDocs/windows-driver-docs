---
title: "!vadump (WinDbg)"
description: "The !vadump extension displays all virtual memory ranges and their corresponding protection information."
keywords: ["!vadump Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- vadump
api_type:
- NA
---

# !vadump

The **!vadump** extension displays all virtual memory ranges and their corresponding protection information.

```dbgcmd
!vadump [-v] 
```

## Parameters

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Causes the display to include information about each original allocation region as well. Because individual addresses within a region can have their protection altered after memory is allocated (by **VirtualProtect**, for example), the original protection status for this larger region may not be the same as that of each range within the region.

## DLL

Uext.dll

## Additional Information

To view memory protection information for a single virtual address, use [**!vprot**](-vprot.md). For information about memory protection, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

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
