---
title: TTD Calls Objects
description: This section describes the calls model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Calls Objects
## Description
*TTD Calls* objects are used to give information about function calls that occur over the course of a trace.

## Properties
| Property | Description |
| --- | --- |
| Function | The symbolic name of the function. |
| FunctionAddress | The function's address in memory. |
| ReturnValue | The return value of the function. If the function has a void type, this property will not be present. |

## Children
| Object | Description |
| --- | --- |
| Parameters[] | An array containing the parameters passed to the function. The number of elements varies based on the type signature of the function. |
| TimeStart | A [position object](time-travel-debugging-position-objects.md) that describes the position at the start of the call. |
| TimeEnd | A [position object](time-travel-debugging-position-objects.md) that describes the position at the end of the call. |

## Remarks
Time travel debugging uses symbol information provided in the PDBs to determine the number of parameters for a function and their types, the return value type, and the calling convention. In the event that symbol information is not available or the symbols have been restricted to public symbol information, it is still possible to do queries. The time travel query engine will make some assumptions in this scenario:
* There are four 64-bit unsigned integer parameters to the function
* The return value is a 64-bit unsigned integer
* The function name is set to a fixed string: “UnknownOrMissingSymbols”

These assumptions allow queries to be made in the absence of adequate symbol information. However, for best results use full PDB symbols when possible.


## Example Usage
Coming soon.

## See Also
Coming soon.