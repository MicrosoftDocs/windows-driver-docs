---
title: "!pnpevent (WinDbg)"
description: "The !pnpevent extension displays the Plug and Play device event queue."
keywords: ["!pnpevent Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pnpevent
api_type:
- NA
---

# !pnpevent

The **!pnpevent** extension displays the Plug and Play device event queue.

```dbgcmd
!pnpevent [DeviceEvent]
```

## Parameters

<span id="_______DeviceEvent______"></span><span id="_______deviceevent______"></span><span id="_______DEVICEEVENT______"></span> *DeviceEvent*   
Specifies the address of a device event to display. If this is zero or omitted, the tree of all device events in the queue is displayed.

## DLL

Kdexts.dll

## Additional Information

See [Plug and Play Debugging](../debugger/plug-and-play-debugging.md) for applications of this extension command. For information about Plug and Play drivers, see the Windows Driver Kit (WDK) documentation.

## See also

[Plug and Play and Power Debugger Commands](../debugger/plug-and-play-and-power-debugger-commands.md)
