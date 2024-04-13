---
title: "!wsle (WinDbg)"
description: "The !wsle extension displays all working set list entries (WSLEs)."
keywords: ["!wsle Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wsle
api_type:
- NA
---

# !wsle

The **!wsle** extension displays all working set list entries (WSLEs).

Syntax

```dbgcmd
!wsle [Flags [Address]] 
```

## Parameters

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the information to include in the display. This can be any combination of the following bits. The default is zero. If this is used, only basic information about the working set is displayed.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to include information about each WSLE's address, age, lock status, and reference count. If a WSLE has an invalid page table entry (PTE) or page directory entry (PDE) associated with it, this is also displayed.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include the total number of valid WSLEs, the index of the last WSLE, and the index of the first free WSLE.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to include the total number of free WSLEs, as well as the index of each free WSLE. If bit 1 is also set, then a check is done to make sure that the number of free WSLEs plus the number of valid WSLEs is actually equal to the total number of WSLEs.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the working set list. If this is omitted, the default working set list is used. Specifying zero for *Address* is the same as omitting it.

## DLL

Kdexts.dll

## Additional Information

For information about working sets, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

This extension can take a significant amount of time to execute.

Here is an example from an x86 target computer running Windows Server 2003:

```dbgcmd
kd> !wsle 3

Working Set @ c0503000
    FirstFree:       a7  FirstDynamic:          4
    LastEntry      23d  NextSlot:         4  LastInitialized      259
    NonDirect       65  HashTable:        0  HashTableSize:         0

Reading the WSLE data...

Virtual Address           Age  Locked  ReferenceCount
        c0300203          0        1        1
        c0301203          0        1        1
        c0502203          0        1        1
        c0503203          0        1        1
        c01ff201          0        0        1
        77f74d19          3        0        1
        7ffdfa01          2        0        1
        c0001201          0        0        1

.....

Reading the WSLE data...
Valid WSLE entries = 0xa7
found end @ wsle index 0x259

.....
```
