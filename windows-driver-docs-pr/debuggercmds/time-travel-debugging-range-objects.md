---
title: "TTD Range Objects"
description: "This section describes the range model objects associated with time travel debugging."
keywords: ["TTD Range Objects", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 11/15/2024
---

# TTD Range Objects

## Description

*TTD Range* objects are used to give information about a range of time in a trace. These are generally used to describe the lifetime of a [TTD thread object](time-travel-debugging-thread-objects.md) during a TTD session.

## Children

| Object | Description |
| ------ | ----------- |
| MinPosition | A [position object](time-travel-debugging-position-objects.md) that describes the earliest position relevant to the range. |
| MaxPosition | A [position object](time-travel-debugging-position-objects.md) that describes the latest position relevant to the range. |


## Example Usage

In this example the MinPosition and MaxPosition objects are shown for Lifetime and ActiveTime associated with a thread.

```dbgcmd
0:003> dx -r1 @$curprocess.TTD.Threads[5]
@$curprocess.TTD.Threads[5]                 : UID: 7, TID: 0x2580
    UniqueId         : 0x7
    Id               : 0x2580
    Lifetime         : [BAF:0, FFFFFFFFFFFFFFFE:0]
    ActiveTime       : [BB2:0, C6A:0]
    GatherMemoryUse  [Gather inputs, outputs and memory used by a range of execution within a thread]

0:003> dx -r1 @$curprocess.TTD.Threads[5].Lifetime
@$curprocess.TTD.Threads[5].Lifetime                 : [BAF:0, FFFFFFFFFFFFFFFE:0]
    MinPosition      : BAF:0 [Time Travel]
    MaxPosition      : FFFFFFFFFFFFFFFE:0 [Time Travel]

0:003> dx -r1 @$curprocess.TTD.Threads[5].ActiveTime
@$curprocess.TTD.Threads[5].ActiveTime                 : [BB2:0, C6A:0]
    MinPosition      : BB2:0 [Time Travel]
    MaxPosition      : C6A:0 [Time Travel]
```

## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)
