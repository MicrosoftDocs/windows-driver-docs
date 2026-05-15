---
title: "TTD Exception Objects"
description: "This section describes the exception model objects associated with time travel debugging."
keywords: ["TTD Exception Objects", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 11/14/2024
ms.topic: reference
---

# TTD Exception Objects

## Description

*TTD Exception* objects are used to provide information about event exceptions that happened during a trace session.

## Properties

| Property | Description |
| -------- | ----------- |
| Type | Describes the type of exception. Possible values are "Software" and "Hardware". |
| ProgramCounter | The instruction where the exception was thrown.  |
| Code | The code of the exception.  |
| Flags | The exception flags. |
| RecordAddress | Where in memory you can find the record of the exception.  |

## Children

| Object   | Description |
| -------- | ----------- |
| Position | A [position object](time-travel-debugging-position-objects.md) that describes the position the exception occurred. |

## Example Usage

```dbgcmd
0:003> dx -r1 @$curprocess.TTD.Events.Where(t => t.Type == "Exception")[0].Exception
@$curprocess.TTD.Events.Where(t => t.Type == "Exception")[0].Exception                 : Exception 0x80010012 of type Software at PC: 0X7FF9F6DC8670
    Position         : 36A7:0 [Time Travel]
    Type             : Software
    ProgramCounter   : 0x7ff9f6dc8670
    Code             : 0x80010012
    Flags            : 0x1
    RecordAddress    : 0x0
```

## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

