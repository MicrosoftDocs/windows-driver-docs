---
title: "!vprot (WinDbg)"
description: "The !vprot extension displays virtual memory protection information."
keywords: ["memory, memory protection", "!vprot Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- vprot
api_type:
- NA
---

# !vprot

The **!vprot** extension displays virtual memory protection information.

```dbgcmd
!vprot [Address]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address whose memory protection status is to be displayed.

## DLL

Uext.dll

## Additional Information

To view memory protection information for all memory ranges owned by the target process, use [**!vadump**](-vadump.md). For information about memory protection, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

The **!vprot** extension command can be used for both live debugging and dump file debugging.

Here is an example:

```dbgcmd
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
