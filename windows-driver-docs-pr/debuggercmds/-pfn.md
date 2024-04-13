---
title: "!pfn (WinDbg)"
description: "The !pfn extension displays information about a specific page frame or the entire page frame database."
keywords: ["page frame", "!pfn Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pfn
api_type:
- NA
---

# !pfn

The **!pfn** extension displays information about a specific page frame or the entire page frame database.

```dbgcmd
!pfn PageFrame
```

## Parameters

<span id="_______PageFrame______"></span><span id="_______pageframe______"></span><span id="_______PAGEFRAME______"></span> *PageFrame*   
Specifies the hexadecimal number of the page frame to be displayed.

### DLL

Kdexts.dll

## Additional Information

For information about page tables, page directories, and page frames, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

The page frame number for a virtual address can be obtained by using the [**!pte**](-pte.md) extension.

Here is an example of the output from this extension:

```dbgcmd
kd> !pte 801544f4
801544F4  - PDE at C0300800        PTE at C0200550
          contains 0003B163      contains 00154121
        pfn 3b G-DA--KWV    pfn 154 G--A--KRV

kd> !pfn 3b
    PFN 0000003B at address 82350588
    flink       00000000  blink / share count 00000221  pteaddress C0300800
    reference count 0001                                 color 0
    restore pte 00000000  containing page        000039  Active   
 

kd> !pfn 154
    PFN 00000154 at address 82351FE0
    flink       00000000  blink / share count 00000001  pteaddress C0200550
    reference count 0001                                 color 0
    restore pte 00000060  containing page        00003B  Active     M     
    Modified          
```
