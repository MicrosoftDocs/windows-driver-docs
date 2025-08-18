---
title: "Time travel debugging extensions"
description: "This section describes how to use the time travel debugger extension commands."
keywords: ["Time travel debugging extensions", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 11/12/2024
ms.topic: reference
---

# Time travel debugging extension commands

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

This section introduces the time travel debugger extension commands.

## In this section

|Topic              | Description |
|------------------ |------------ |
|!tt (time travel)  |The [!tt (time travel)](time-travel-debugging-extension-tt.md) debugger extension that allows you to navigate forward and backwards in time.|
|!positions         |The [!positions](time-travel-debugging-extension-positions.md) extension displays all the active threads, including their current positions in the time travel trace.|
|!index             |The [!index](time-travel-debugging-extension-index.md) extension indexes time travel traces or displays index status information.|
 

### Additional Information

These extensions only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

### DLL

The time travel debugger extension commands are implemented in ttdext.dll. The time travel command dll is loaded automatically in WinDbg. You don't need to use the load command to manually load the ttdext.dll.
 
## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

