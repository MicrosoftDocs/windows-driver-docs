---
title: Configuring a Port
description: Configuring a Port
ms.assetid: f5996e94-aa48-4aa0-82f5-331a57d2fb6b
keywords:
- port management WDK print , configuring ports
- ConfigurePort
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring a Port





Configuring a port consists of modifying a port monitor server DLL's stored configuration information for a previously-added port.

When an application calls the print spooler's [**ConfigurePort**](https://msdn.microsoft.com/library/windows/hardware/ff546286) function (described in the Microsoft Windows SDK documentation), the **ConfigurePort** function calls the [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290) function contained in the port monitor UI DLL of the appropriate port monitor.

The port monitor UI DLL's [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290) function should perform the following operations:

1.  Call the print spooler's OpenPrinter function (described in the Windows SDK documentation), which causes the [**XcvOpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff564259) function in the port monitor server DLL to be called.

2.  Call the print spooler's [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function one or more times, to transfer configuration information between the UI DLL and the server DLL. The **XcvData** function calls the server DLL's [**XcvDataPort**](https://msdn.microsoft.com/library/windows/hardware/ff564258) function. The [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290) function typically obtains configuration information from the user by displaying dialog boxes.

3.  Call the print spooler's ClosePrinter function (described in the Windows SDK documentation), which causes the [**XcvClosePort**](https://msdn.microsoft.com/library/windows/hardware/ff564254) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290). Also see [Storing Port Configuration Information](storing-port-configuration-information.md).

 

 




