---
title: TTD Event Objects
description: This section describes the event model objects associated with time travel debugging.
ms.author: domars
ms.date: 09/22/2017
ms.localizationpriority: medium
---



# TTD Event Objects
## Description
*TTD Event* objects are used to give information about important events that happened during a time travel trace.

## Properties

| Property | Description |
| --- | --- |
| Type | Describes the type of event that happened. Possible values are: ThreadCreated, ThreadTerminated, ModuleLoaded, ModuleUnloaded, Exception |

## Children

| Object | Description |
| --- | --- |
| Position | A [position object](time-travel-debugging-position-objects.md) that describes the position the event occurred. |
| Module* | A [module object](time-travel-debugging-module-objects.md) containing information about the module that was loaded or unloaded. |
| Thread* | A [thread object](time-travel-debugging-thread-objects.md) containing information about the thread that was created or terminated. |
| Exception* | An [exception object](time-travel-debugging-exception-objects.md) containing information about the exception that was hit. |

\* - Existence of these child objects depends on the type of event

## Example Usage



```dbgcmd
0:000> dx -r2 @$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)
@$curprocess.TTD.Events.Where(t => t.Type == "Exception").Select(e => e.Exception)                
    [0x0]            : Exception of type CPlusPlus at PC: 0X777663B0
        Position         : 13B7:0 [Time Travel]
        Type             : CPlusPlus
        ProgramCounter   : 0x777663b0
        Code             : 0xe06d7363
        Flags            : 0x1
        RecordAddress    : 0x0
    [0x1]            : Exception of type Hardware at PC: 0XF1260D0
        Position         : BC0F:0 [Time Travel]
        Type             : Hardware
        ProgramCounter   : 0xf1260d0
        Code             : 0x80000003
        Flags            : 0x0
        RecordAddress    : 0x0
```


## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


