---
title: Port monitor server DLL functions
description: Provides information about required and optional port monitor server DLL functions.
keywords:
- port monitors WDK print, functions
- server DLL port monitor functions WDK
ms.date: 09/08/2022
---

# Port monitor server DLL functions

The following table lists the functions that a port monitor server DLL must define:

| Function name | Description |
|--|--|
| **DllEntryPoint** | DLL entry point, typically called [**DllMain**](/windows/win32/dlls/dllmain). |
| [**ClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeport) | Closes a port if there are no printers connected to it. |
| [**EndDocPort**](/previous-versions/ff548742(v=vs.85)) | Performs end-of-print-job tasks on a port. |
| [**EnumPorts**](/previous-versions/ff548754(v=vs.85)) | Enumerates the ports available for printing on a server. |
| [**InitializePrintMonitor2**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor2) | Initializes the print monitor and returns an instance handle. |
| [**OpenPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-openport) | Opens a printer port. |
| [**OpenPortEx**](/previous-versions/ff559596(v=vs.85)) | Opens a printer port. (Language monitor only) |
| [**ReadPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-readport) | Reads data from a printer port. |
| [**StartDocPort**](/previous-versions/ff562710(v=vs.85)) | Performs the tasks required to start a print job on a port. |
| [**WritePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-writeport) | Writes data to a printer port. |
| [**XcvClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvcloseport) | Closes a port after port management is complete. |
| [**XcvDataPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvdataport) | Handles port management tasks. |
| [**XcvOpenPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvopenport) | Opens a port for management purposes. |

The following port monitor server DLL functions are optional:

| Function name | Description |
|--|--|
| [**GetPrinterDataFromPort**](/previous-versions/ff550506(v=vs.85)) | Sends an I/O control code to a port driver and returns the result. |
| [**SendRecvBidiDataFromPort**](/previous-versions/ff562071(v=vs.85)) | Supports bidirectional communication between an application and a printer or print server. |
| [**SetPortTimeOuts**](/previous-versions/ff562630(v=vs.85)) | Sets a time-out value on an open port. |
| [**Shutdown**](/previous-versions/ff562646(v=vs.85)) | Deletes a monitor instance. This function is required for cluster support. |
