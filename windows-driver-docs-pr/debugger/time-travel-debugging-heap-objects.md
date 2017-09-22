---
title: TTD Heap Objects
description: This section describes the heap model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
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
| BaseAddress | TODO |
| Flags | Meaning depends on the API |
| Result | The result of the heap API call. Non-zero means success and zero means failure. |
| ReserveSize | Amount of memory to reserve for the heap. |
| CommitSize | Initial committed size for the heap. |
| MakeReadOnly | A non-zero value indicates a request to make the heap read-only; A zero value indicates the heap should be read-write. |

## Children
| Object | Description |
| --- | --- |
| TimeStart | A [position object](time-travel-position-objects.md) that describes the position at the start of the allocation. |
| TimeEnd | A [position object](time-travel-position-objects.md) that describes the position at the end of the allocation. |


## Example Usage
Coming soon.

## See Also
Coming soon.