---
title: Configuring a Port
author: windows-driver-content
description: Configuring a Port
ms.assetid: f5996e94-aa48-4aa0-82f5-331a57d2fb6b
keywords:
- port management WDK print , configuring ports
- ConfigurePort
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuring a Port


## <a href="" id="ddk-configuring-a-port-gg"></a>


Configuring a port consists of modifying a port monitor server DLL's stored configuration information for a previously-added port.

When an application calls the print spooler's [**ConfigurePort**](https://msdn.microsoft.com/library/windows/hardware/ff546286) function (described in the Microsoft Windows SDK documentation), the **ConfigurePort** function calls the [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290) function contained in the port monitor UI DLL of the appropriate port monitor.

The port monitor UI DLL's [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290) function should perform the following operations:

1.  Call the print spooler's OpenPrinter function (described in the Windows SDK documentation), which causes the [**XcvOpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff564259) function in the port monitor server DLL to be called.

2.  Call the print spooler's [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function one or more times, to transfer configuration information between the UI DLL and the server DLL. The **XcvData** function calls the server DLL's [**XcvDataPort**](https://msdn.microsoft.com/library/windows/hardware/ff564258) function. The [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290) function typically obtains configuration information from the user by displaying dialog boxes.

3.  Call the print spooler's ClosePrinter function (described in the Windows SDK documentation), which causes the [**XcvClosePort**](https://msdn.microsoft.com/library/windows/hardware/ff564254) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**ConfigurePortUI**](https://msdn.microsoft.com/library/windows/hardware/ff546290). Also see [Storing Port Configuration Information](storing-port-configuration-information.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Configuring%20a%20Port%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


