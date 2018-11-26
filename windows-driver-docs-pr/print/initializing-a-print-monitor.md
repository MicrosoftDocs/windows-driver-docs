---
title: Initializing a Print Monitor
description: Initializing a Print Monitor
ms.assetid: 006727dd-aa0f-451c-b1c9-983d0c6401df
keywords:
- print monitors WDK , initializing
- initializing print monitors
- LoadLibrary
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Print Monitor





When the spooler calls LoadLibrary to load a print monitor DLL, the system immediately calls the DLL's **DllEntryPoint** function. It is generally a good idea for the entry point function to call DisableThreadLibraryCalls, described in the Microsoft Windows SDK documentation, so the DLL is not unnecessarily notified when threads are created and deleted.

Each DLL exports an initialization function, which the spooler calls after calling LoadLibrary. Language monitor DLLs and port monitor server DLLs export an [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function. Port monitor UI DLLs export an [**InitializePrintMonitorUI**](https://msdn.microsoft.com/library/windows/hardware/ff551608) function.

These two initialization functions are responsible for returning pointers to the rest of the [functions defined by print monitors](functions-defined-by-print-monitors.md), so the spooler can call them. The initialization functions can also perform load-time initialization operations. The monitor's [**InitializePrintMonitor2**](https://msdn.microsoft.com/library/windows/hardware/ff551605) function returns a monitor instance handle. The monitor should allocate local memory to store instance-specific information, and use the monitor handle as an identifier for the allocated memory.

When the spooler is first started, it loads all of the monitor DLLs that have been installed. After calling all monitor initialization functions, the spooler calls each port monitor's [**EnumPorts**](https://msdn.microsoft.com/library/windows/hardware/ff548754) function, which enumerates the ports supported by the monitor. (A monitor supports a port if the port has been added to the monitor's database, as described in [Adding a Port](adding-a-port.md).) Each supported port is then opened, as described in [Opening and Closing a Port](opening-and-closing-a-port.md).

 

 




