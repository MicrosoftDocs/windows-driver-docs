---
title: Deleting a Port
description: Deleting a Port
keywords:
- port management WDK print , deleting ports
- deleting print ports
- removing print ports
- DeletePort
ms.date: 04/20/2017
---

# Deleting a Port





Deleting a port consists of removing the port's stored name and user-modifiable configuration information from the port monitor server DLL's local storage or from the registry.

When an application calls the print spooler's **DeletePort** function (described in the Microsoft Windows SDK documentation), the **DeletePort** function calls the [**DeletePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-deleteportui) function contained in the port monitor UI DLL of the appropriate port monitor.

The port monitor UI DLL's **DeletePortUI** function should perform the following operations:

1.  Call the print spooler's **OpenPrinter** function (described in the Windows SDK documentation), which causes the [**XcvOpenPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvopenport) function in the port monitor server DLL to be called.

2.  Call the print spooler's [**XcvData**](/previous-versions/ff564255(v=vs.85)) function one or more times, to request the port monitor server DLL to delete the port. The **XcvData** function calls the server DLL's [**XcvDataPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvdataport) function.

3.  Call the print spooler's **ClosePrinter** function (described in the Windows SDK documentation), which causes the [**XcvClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-xcvcloseport) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**DeletePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-deleteportui).

 

