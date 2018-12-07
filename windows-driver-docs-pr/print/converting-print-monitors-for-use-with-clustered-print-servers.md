---
title: Converting Print Monitors for Use with Clustered Print Servers
description: Converting Print Monitors for Use with Clustered Print Servers
ms.assetid: 6b374d61-bb2b-42a4-9609-3cde9b82bb2b
keywords:
- print monitors WDK , clustered print servers
- clustered print servers WDK
- print server clustering WDK
- converting print monitors for clustered print servers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting Print Monitors for Use with Clustered Print Servers





Clustering of print servers is a new feature of Windows 2000. Any printer port monitor that is intended to run on Windows 2000 (or later) clusters must be modified so it can be called from multiple spooler instances (the node's spooler and a cluster spooler). The following steps must be taken:

-   The monitor's [**InitializePrintMonitor**](https://msdn.microsoft.com/library/windows/hardware/ff551600) function must be replaced with an [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function. The latter function returns a monitor instance handle.

-   Globally stored variables must be moved to locally allocated memory, and this memory must be associated with the monitor handle returned by [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605).

-   Calls to the Win32 registry API must be replaced with calls to the spooler's registry functions, addresses of which are passed to the monitor in a [**MONITORREG**](https://msdn.microsoft.com/library/windows/hardware/ff557537) structure. (See [Storing Port Configuration Information](storing-port-configuration-information.md).)

-   Port monitors must be divided into a port monitor UI DLL and a port monitor server DLL. The UI DLL must communicate with the server DLL by calling the spooler's [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function.

-   A [**Shutdown**](https://msdn.microsoft.com/library/windows/hardware/ff562646) function must be added.

Print monitors that are not converted can be used only in a nonclustered environment. They cannot be used with clustered servers.

Once a printer port monitor running on a clustered node of a machine running Windows 2000 or later has made a connection (either across the network or locally), the port monitor should return from calls made by the spooler within a reasonable amount of time. (The default value of the spooler resource time-out is 180 seconds. See [Setting Port Time-Out Values](setting-port-time-out-values.md) for more information.)

When a failover from one cluster node to another occurs, the spooler must wait for all current printing jobs to complete or fail. If a pending print job is held up in a port monitor for longer than the spooler resource time-out, the spooler may come back online in an incomplete state, with printers temporarily missing. This may affect users who have connections to those missing printers.

 

 




