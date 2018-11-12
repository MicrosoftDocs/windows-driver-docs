---
title: TTD Calls Objects
description: This section describes the calls model objects associated with time travel debugging.
ms.author: domars
ms.date: 09/25/2017
ms.localizationpriority: medium
---


# TTD Calls Objects
## Description
*TTD Calls* objects are used to give information about function calls that occur over the course of a trace.

## Parameters

| Property | Description |
| --- | --- |
| Function!SymbolName | One or more contained in double quotes, separated by a comma. For example dx @$cursession.TTD.Calls("module!symbol1", "module!symbol2", ...) |

## Properties

| Property | Description |
| --- | --- |
| EventType  |  The type of event. This is "Call" for all TTD Calls objects. |
| ThreadId   |  The OS thread ID of thread that made the request. |
| UniqueThreadId |   A unique ID for the thread across the trace. Regular thread IDs can get reused over the lifetime of a process but UniqueThreadIds cannot. |
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

Note that the Calls function does computation, and depending on the size of the trace, it can take a while to run. CPU usage will spike during the computation and watching CPU usage in task manager, gives an indication that the computation is progressing.  The query results are cached in memory so subsequent queries against previously queried calls are significantly faster.



## Example Usage

This example shows the calls object for ucrtbase!initterm.

```dbgcmd
0:000> dx -r2 @$cursession.TTD.Calls("ucrtbase!initterm")
@$cursession.TTD.Calls("ucrtbase!initterm")
    [0x0]
        EventType        : Call
        ThreadId         : 0x2074
        UniqueThreadId   : 0x2
        TimeStart        : 1E:5D0
        TimeEnd          : 2D:E
        Function         : ucrtbase!_initterm
        FunctionAddress  : 0x7ffb345825d0
        ReturnAddress    : 0x7ff6a521677e
        Parameters
```




## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


