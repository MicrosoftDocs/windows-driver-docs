---
title: "TTD Heap Objects"
description: "This section describes the heap model objects associated with time travel debugging."
keywords: ["TTD Heap Objects", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 09/24/2017
---

# TTD Heap Objects

## Description
*TTD Heap* objects are used to give information about heap calls that occur over the course of a trace.

## Properties
Every heap object will have these properties.

| Property | Description |
| --- | --- |
| Action | Describes the action that occurred. Possible values are: Alloc, ReAlloc, Free, Create, Protect, Lock, Unlock, Destroy. |
| Heap | The handle for the Win32 heap. |

### Conditional properties
Depending on the heap object, it may have some of the properties below.

| Property | Description |
| --- | --- |
| Address | The address of the allocated object. |
| PreviousAddress | The address of the allocated object before it was reallocated. If Address is not the same as PreviousAddress then the reallocation caused the memory to move. |
| Size | The size and/or requested size of an allocated object. |
| BaseAddress | The address of an allocated object in the heap.  It can represent the address which will be freed (Free) or the address of the object before it is reallocated (ReAlloc.) |
| Flags | Meaning depends on the API. |
| Result | The result of the heap API call. Non-zero means success and zero means failure. |
| ReserveSize | Amount of memory to reserve for the heap. |
| CommitSize | Initial committed size for the heap. |
| MakeReadOnly | A non-zero value indicates a request to make the heap read-only; A zero value indicates the heap should be read-write. |

## Children

| Object | Description |
| --- | --- |
| TimeStart | A [position object](time-travel-debugging-position-objects.md) that describes the position at the start of the allocation. |
| TimeEnd | A [position object](time-travel-debugging-position-objects.md) that describes the position at the end of the allocation. |


## Example Usage

Use this dx command to display the heap memory in a grid using the -g option.

```dbgcmd
0:0:000> dx -g @$cursession.TTD.Data.Heap()
=======================================================================================================================================================
=                          = Action     = Heap          = Address       = Size      = Flags  = (+) TimeStart = (+) TimeEnd = Result = PreviousAddress =
=======================================================================================================================================================
= [0x0] : [object Object]  - Alloc      - 0xaf0000      - 0xb0cfd0      - 0x4c      - 0x0    - FAB:17B1      - FAD:40      -        -                 =
= [0x1] : [object Object]  - Alloc      - 0xaf0000      - 0xb07210      - 0x34      - 0x8    - FB1:9         - FB3:74      -        -                 =
= [0x2] : [object Object]  - Alloc      - 0xaf0000      - 0xb256d8      - 0x3c      - 0x8    - E525:174      - E526:E1     -        -                 =
```


The output can be described as “normalized data” because there is a chosen set of APIs that represent heap operations. The data that is extracted from the appropriate parameters, is presented in a uniform manner.

Clicking on TimeStart or TimeEnd will navigate you to that point in the trace.  

Click on the parameters field next to a specific entry, to display available parameter information.

```dbgcmd
dx -r1 @$cursession.TTD.Data.Heap()[2].@"Parameters"
@$cursession.TTD.Data.Heap()[2].@"Parameters"                
    [0x0]            : 0x16c7d780000
    [0x1]            : 0x280000
    [0x2]            : 0x20
    [0x3]            : 0x0
```

## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

