---
title: Initialize a Print Monitor
description: Provides information about how to initialize a print monitor.
keywords:
- print monitors WDK, initializing
- initializing print monitors
- LoadLibrary
ms.date: 09/14/2022
---

# Initialize a print monitor

When the spooler calls LoadLibrary to load a print monitor DLL, the system immediately calls the DLL's [**DllEntryPoint**](/windows/win32/dlls/dllmain) function. It is generally a good idea for the entry point function to call [**DisableThreadLibraryCalls**](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls), so the DLL is not unnecessarily notified when threads are created and deleted.

Each DLL exports an initialization function, which the spooler calls after calling [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya). Language monitor DLLs and port monitor server DLLs export an [**InitializePrintMonitor2**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor2) function. Port monitor UI DLLs export an [**InitializePrintMonitorUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitorui) function.

These two initialization functions are responsible for returning pointers to the rest of the [functions defined by print monitors](functions-defined-by-print-monitors.md), so the spooler can call them. The initialization functions can also perform load-time initialization operations. The monitor's [**InitializePrintMonitor2**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor2) function returns a monitor instance handle. The monitor should allocate local memory to store instance-specific information, and use the monitor handle as an identifier for the allocated memory.

When the spooler is first started, it loads all of the monitor DLLs that have been installed. After calling all monitor initialization functions, the spooler calls each port monitor's [**EnumPorts**](/previous-versions/ff548754(v=vs.85)) function, which enumerates the ports supported by the monitor. (A monitor supports a port if the port has been added to the monitor's database, as described in [Adding a port](adding-a-port.md).) Each supported port is then opened, as described in [Opening and closing a port](opening-and-closing-a-port.md).
