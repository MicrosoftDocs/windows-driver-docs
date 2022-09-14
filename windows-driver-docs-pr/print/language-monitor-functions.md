---
title: Language monitor functions
description: Provides a list of functions that a language monitor must define.
keywords:
- language monitors WDK print, functions
ms.date: 09/08/2022
---

# Language monitor functions

The following table lists the functions that a language monitor must define.

| Function name | Description |
|--|--|
| **DllEntryPoint** | A DLL entry point, typically called **DllMain**, which is described in the Microsoft Windows SDK documentation. |
| [**ClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeport) | Closes a port when there are no printers connected to it. |
| [**EndDocPort**](/previous-versions/ff548742(v=vs.85)) | Performs end-of-print-job tasks on a port. |
| [**GetPrinterDataFromPort**](/previous-versions/ff550506(v=vs.85)) | Optional. Polls a port for values that are stored in the registry. |
| [**InitializePrintMonitor2**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitor2) | Initializes the print monitor and returns an instance handle. |
| [**OpenPortEx**](/previous-versions/ff559596(v=vs.85)) | Opens a port for a newly connected printer. |
| [**ReadPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-readport) | Reads data from a printer port. |
| "[**SendRecvBidiDataFromPort**](/previous-versions/ff562071(v=vs.85)) | Optional. Supports bidirectional communication between an application and a printer or print server. |
| [**Shutdown**](/previous-versions/ff562646(v=vs.85)) | Optional. Deletes a monitor instance. This function is required for cluster support. |
| [**StartDocPort**](/previous-versions/ff562710(v=vs.85)) | Performs the tasks required to start a print job on a port. |
| [**WritePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-writeport) | Writes data to a printer port. |
