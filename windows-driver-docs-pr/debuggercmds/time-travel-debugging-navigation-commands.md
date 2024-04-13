---
title: "Time travel navigation commands"
description: "This section describes the time travel navigation commands."
keywords: ["Time travel navigation commands", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 09/23/2017
---

# Time travel navigation commands

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

This section describes the time travel navigation commands.

## </span><span id="P"></span> p- (Step Back)

The *p-* command executes the previous single instruction or source line. When subroutine calls or interrupts occur, they are treated as a single step. You can invoke this command using the **Step Over Back**  button on the **Home** ribbon in WinDbg.

## </span><span id="T"></span> t- (Trace Back)

The *t-* command executes the previous single instruction or source line. When subroutine calls or interrupts occur, each of their steps is also traced. You can invoke this command using the **Step Into Back**  button on the **Home** ribbon in WinDbg.

## </span><span id="Go"></span> g- (Go Back)

The *g-* command starts executing the current process in reverse. Execution will halt at the end of the program, when BreakAddress is hit, or when another event causes the debugger to stop. You can invoke this command using the **Go Back**  button on the **Home** ribbon in WinDbg.

## </span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The time travel navigation commands only work with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[Time Travel Debugging - Replay a trace](time-travel-debugging-replay.md)

