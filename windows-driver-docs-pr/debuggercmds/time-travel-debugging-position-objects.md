---
title: "TTD Position Objects"
description: "This section describes the position model objects associated with time travel debugging."
keywords: ["TTD Position Objects", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 06/23/2025
ms.topic: concept-article
---

# TTD Position Objects

## Description

*Position* objects are used to describe a position in a time travel trace. A position object is normally described by two hexadecimal numbers separated by a colon. The first of the hexadecimal numbers is the *Sequence* and the second is the *Steps*.

A position of FFFFFFFFFFFFFFFE:0 indicates the end of the trace.

## Properties

| Property | Description |
| -------- | ----------- |
| Percent  | Percentage into trace (to the nearest Sequence).<br>Note: The exact percentage can differ from what is requested in !tt command due to rounding to the nearest Sequence. |
| Sequence | The sequencing point relevant to the position. |
| Steps    | The number of steps from the sequence point in this thread to get to this position. |

## Methods

| Method   | Description |
| -------- | ----------- |
| SeekTo() | Time travels to this position in the trace. |
| ToSystemTime() | Returns the approximate wall clock time for the position (UTC). |

## Example Usage

```dbgcmd
0:003> dx -r1 @$create("Debugger.Models.TTD.Position", 14006, 0)
@$create("Debugger.Models.TTD.Position", 14006, 0)                 : 36B6:0 [Time Travel]
    Sequence         : 0x36b6
    Steps            : 0x0
    SeekTo           [Method which seeks to time position]
    ToSystemTime     [Method which obtains the approximate system time at a given position]
```

## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md)

