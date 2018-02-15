---
title: TTD Heap Objects
description: This section describes the heap model objects associated with time travel debugging.
ms.author: domars
ms.date: 09/24/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

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

```
0:0:000> dx -g @$cursession.TTD.Data.Heap()
==================================================================================================================================
=           = (+) Function               = (+) FunctionAddress = (+) ReturnValue  = (+) Parameters = (+) TimeStart = (+) TimeEnd =
==================================================================================================================================
= [0x0]     - UnknownOrMissingSymbols    - 0x7ffbe3daae00      - 0x16c7d7b4050    - {...}          - 50C74:8E      - 50C76:3B    =
= [0x1]     - UnknownOrMissingSymbols    - 0x7ffbe3db0dd0      - 0x1              - {...}          - 50C76:1E9     - 50C78:1D    =
= [0x2]     - UnknownOrMissingSymbols    - 0x7ffbe3daae00      - 0x16c7d7be400    - {...}          - 51C95:21F3    - 51CA6:81    =
```


The output can be described as “normalized data” because there is a chosen set of APIs that represent heap operations. The data that is extracted from the appropriate parameters, is presented in a uniform manner.

Clicking on TimeStart or TimeEnd will navigate you to that point in the trace.  

Click on the parameters field next to a specific entry, to display available parameter information.

```
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

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
