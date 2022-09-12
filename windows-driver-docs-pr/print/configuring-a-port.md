---
title: Configure a port
description: Provides information about how to configure a port.
keywords:
- port management WDK print, configuring ports
- ConfigurePort
ms.date: 09/07/2022
---

# Configure a port

Configuring a port consists of modifying a port monitor server DLL's stored configuration information for a previously-added port.

When an application calls the print spooler's [**ConfigurePort**](/windows/win32/printdocs/configureport) function, the **ConfigurePort** function calls the [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function contained in the port monitor UI DLL of the appropriate port monitor.

The port monitor UI DLL's [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function should perform the following operations:

1. Call the print spooler's [**OpenPrinter**](/windows/win32/printdocs/openprinter) function, which causes the [**XcvOpenPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvopenport) function in the port monitor server DLL to be called.

1. Call the print spooler's [**XcvData**](/previous-versions/ff564255(v=vs.85)) function one or more times, to transfer configuration information between the UI DLL and the server DLL. The **XcvData** function calls the server DLL's [**XcvDataPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvdataport) function. The [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function typically obtains configuration information from the user by displaying dialog boxes.

1. Call the print spooler's [**ClosePrinter**](/windows/win32/printdocs/closeprinter) function, which causes the [**XcvClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvcloseport) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui). Also see [Storing Port Configuration Information](storing-port-configuration-information.md).
