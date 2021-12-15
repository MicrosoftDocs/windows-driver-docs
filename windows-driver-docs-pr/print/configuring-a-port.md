---
title: Configuring a Port
description: Configuring a Port
keywords:
- port management WDK print , configuring ports
- ConfigurePort
ms.date: 04/20/2017
---

# Configuring a Port





Configuring a port consists of modifying a port monitor server DLL's stored configuration information for a previously-added port.

When an application calls the print spooler's [**ConfigurePort**](/previous-versions/ff546286(v=vs.85)) function (described in the Microsoft Windows SDK documentation), the **ConfigurePort** function calls the [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function contained in the port monitor UI DLL of the appropriate port monitor.

The port monitor UI DLL's [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function should perform the following operations:

1.  Call the print spooler's OpenPrinter function (described in the Windows SDK documentation), which causes the [**XcvOpenPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvopenport) function in the port monitor server DLL to be called.

2.  Call the print spooler's [**XcvData**](/previous-versions/ff564255(v=vs.85)) function one or more times, to transfer configuration information between the UI DLL and the server DLL. The **XcvData** function calls the server DLL's [**XcvDataPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvdataport) function. The [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) function typically obtains configuration information from the user by displaying dialog boxes.

3.  Call the print spooler's ClosePrinter function (described in the Windows SDK documentation), which causes the [**XcvClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvcloseport) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui). Also see [Storing Port Configuration Information](storing-port-configuration-information.md).

 

