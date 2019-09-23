---
title: Adding a Port
description: Adding a Port
ms.assetid: ec908ddd-761b-4a82-8fc3-ac45c39a0571
keywords:
- port management WDK print , adding ports
- adding ports
- AddPort
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding a Port





Adding a port consists of storing the port's name and user-modifiable configuration information inside the port monitor server DLL's local storage or in the registry.

When an application calls the print spooler's AddPort function (described in the Microsoft Windows SDK documentation), it specifies the name of a port monitor as a function argument. The spooler calls the [**AddPortUI**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-addportui) function contained in the port monitor UI DLL of the specified port monitor.

The port monitor UI DLL's [**AddPortUI**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-addportui) function should perform the following operations:

1.  Call the print spooler's OpenPrinter function (described in the Windows SDK documentation), which causes the [**XcvOpenPort**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-xcvopenport) function in the port monitor server DLL to be called.

2.  Call the print spooler's [**XcvData**](https://docs.microsoft.com/previous-versions/ff564255(v=vs.85)) function several times, to request the port monitor server DLL to add the port and to transfer configuration information between the UI DLL and the server DLL. The **XcvData** function calls the server DLL's [**XcvDataPort**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-xcvdataport) function. The [**AddPortUI**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-addportui) function typically obtains configuration information from the user by displaying dialog boxes.

3.  Call the print spooler's ClosePrinter function (described in the Windows SDK documentation), which causes the [**XcvClosePort**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-xcvcloseport) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**AddPortUI**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-addportui). Also see [Storing Port Configuration Information](storing-port-configuration-information.md).

A port monitor's [**EnumPorts**](https://docs.microsoft.com/previous-versions/ff548754(v=vs.85)) function must enumerate all ports that have been added. The spooler can call each port monitor's **EnumPorts** function to determine the set of ports supported on a print server.

 

 




