---
title: Debugging Spooler Components
description: Debugging Spooler Components
keywords:
- debugging spooler components WDK printer
- spooler component debugging WDK print
- trace messages WDK printer
ms.date: 06/04/2020
ms.localizationpriority: medium
---

# Debugging Spooler Components

This section provides information about how you can enable debug messages in spooler components. The first part of this section lists the debug variables used in spooler components. You can use these debug variables to cause debug messages originating in spooler components to be displayed. Note that you must be working with checked builds of these components.

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

The second part of this section details the steps need to display trace messages in a spooler component.

> [!NOTE]
> There are special considerations for [debugging XPSDrv printer drivers](debugging-xpsdrv-printer-drivers.md).

## Displaying Trace Messages in a Spooler Component

The following procedure lists the steps necessary for you to be able to see trace messages in checked builds of winspool.drv. The steps for displaying trace messages are similar for other spooler components.

To display trace messages in a spooler component:

1. Attach a debugger.

1. Break into the process you want to debug.

1. Find the debug variable, winspool!ClientDebug.

1. Set the DBG\_TRACE bit (0x0008) in the low WORD of the winspool!ClientDebug variable.

1. Click Go.
