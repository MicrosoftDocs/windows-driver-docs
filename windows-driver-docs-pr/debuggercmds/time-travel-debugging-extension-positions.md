---
title: "Time Travel Debugging Extension !positions Command "
description: "The !positions extension displays all the active threads, including their current positions."
keywords: ["positions", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 11/13/2024
ms.topic: concept-article
---

# !positions

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

The **!positions** extension displays all the active threads, including their current positions in the time travel trace.

```dbgcmd
!positions
```

## Parameters

None

## Example

This output shows five threads. Thread 1660 is the current thread indicated by **>** in the left column.

```dbgcmd
0:000> !positions
>*Thread ID=0x1660 - Position: 724:0
  Thread ID=0x3E6C - Position: A8B:0
  Thread ID=0x30EC - Position: A8A:0
  Thread ID=0x1F40 - Position: A8E:0
  Thread ID=0x4170 - Position: C44:0
* indicates an actively running thread
```

## DLL

ttdext.dll

## Additional Information

This extension only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

## See Also

[Time Travel Debugging - Extension Commands](time-travel-debugging-extension-commands.md)

