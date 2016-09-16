---
title: Converting Print Monitors for Use with Clustered Print Servers
author: windows-driver-content
description: Converting Print Monitors for Use with Clustered Print Servers
MS-HAID:
- 'provider\_42484e98-b94e-49a9-82b3-b683ee592ec5.xml'
- 'print.converting\_print\_monitors\_for\_use\_with\_clustered\_print\_servers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6b374d61-bb2b-42a4-9609-3cde9b82bb2b
keywords: ["print monitors WDK , clustered print servers", "clustered print servers WDK", "print server clustering WDK", "converting print monitors for clustered print servers"]
---

# Converting Print Monitors for Use with Clustered Print Servers


## <a href="" id="ddk-converting-print-monitors-for-use-with-clustered-print-servers-gg"></a>


Clustering of print servers is a new feature of Windows 2000. Any printer port monitor that is intended to run on Windows 2000 (or later) clusters must be modified so it can be called from multiple spooler instances (the node's spooler and a cluster spooler). The following steps must be taken:

-   The monitor's [**InitializePrintMonitor**](https://msdn.microsoft.com/library/windows/hardware/ff551600) function must be replaced with an [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function. The latter function returns a monitor instance handle.

-   Globally stored variables must be moved to locally allocated memory, and this memory must be associated with the monitor handle returned by [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605).

-   Calls to the Win32 registry API must be replaced with calls to the spooler's registry functions, addresses of which are passed to the monitor in a [**MONITORREG**](https://msdn.microsoft.com/library/windows/hardware/ff557537) structure. (See [Storing Port Configuration Information](storing-port-configuration-information.md).)

-   Port monitors must be divided into a port monitor UI DLL and a port monitor server DLL. The UI DLL must communicate with the server DLL by calling the spooler's [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function.

-   A [**Shutdown**](https://msdn.microsoft.com/library/windows/hardware/ff562646) function must be added.

Print monitors that are not converted can be used only in a nonclustered environment. They cannot be used with clustered servers.

Once a printer port monitor running on a clustered node of a machine running Windows 2000 or later has made a connection (either across the network or locally), the port monitor should return from calls made by the spooler within a reasonable amount of time. (The default value of the spooler resource time-out is 180 seconds. See [Setting Port Time-Out Values](setting-port-time-out-values.md) for more information.)

When a failover from one cluster node to another occurs, the spooler must wait for all current printing jobs to complete or fail. If a pending print job is held up in a port monitor for longer than the spooler resource time-out, the spooler may come back online in an incomplete state, with printers temporarily missing. This may affect users who have connections to those missing printers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Converting%20Print%20Monitors%20for%20Use%20with%20Clustered%20Print%20Servers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


