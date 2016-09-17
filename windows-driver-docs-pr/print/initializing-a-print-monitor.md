---
title: Initializing a Print Monitor
author: windows-driver-content
description: Initializing a Print Monitor
MS-HAID:
- 'provider\_4b65082e-c7bb-4b42-a352-7b21c64796a2.xml'
- 'print.initializing\_a\_print\_monitor'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 006727dd-aa0f-451c-b1c9-983d0c6401df
keywords: ["print monitors WDK , initializing", "initializing print monitors", "LoadLibrary"]
---

# Initializing a Print Monitor


## <a href="" id="ddk-initializing-a-print-monitor-gg"></a>


When the spooler calls LoadLibrary to load a print monitor DLL, the system immediately calls the DLL's **DllEntryPoint** function. It is generally a good idea for the entry point function to call DisableThreadLibraryCalls, described in the Microsoft Windows SDK documentation, so the DLL is not unnecessarily notified when threads are created and deleted.

Each DLL exports an initialization function, which the spooler calls after calling LoadLibrary. Language monitor DLLs and port monitor server DLLs export an [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function. Port monitor UI DLLs export an [**InitializePrintMonitorUI**](https://msdn.microsoft.com/library/windows/hardware/ff551608) function.

These two initialization functions are responsible for returning pointers to the rest of the [functions defined by print monitors](functions-defined-by-print-monitors.md), so the spooler can call them. The initialization functions can also perform load-time initialization operations. The monitor's [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function returns a monitor instance handle. The monitor should allocate local memory to store instance-specific information, and use the monitor handle as an identifier for the allocated memory.

When the spooler is first started, it loads all of the monitor DLLs that have been installed. After calling all monitor initialization functions, the spooler calls each port monitor's [**EnumPorts**](https://msdn.microsoft.com/library/windows/hardware/ff548754) function, which enumerates the ports supported by the monitor. (A monitor supports a port if the port has been added to the monitor's database, as described in [Adding a Port](adding-a-port.md).) Each supported port is then opened, as described in [Opening and Closing a Port](opening-and-closing-a-port.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Initializing%20a%20Print%20Monitor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


