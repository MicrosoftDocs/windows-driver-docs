---
title: Adding a Port
description: Adding a Port
ms.assetid: ec908ddd-761b-4a82-8fc3-ac45c39a0571
keywords: ["port management WDK print , adding ports", "adding ports", "AddPort"]
---

# Adding a Port


## <a href="" id="ddk-adding-a-port-gg"></a>


Adding a port consists of storing the port's name and user-modifiable configuration information inside the port monitor server DLL's local storage or in the registry.

When an application calls the print spooler's AddPort function (described in the Microsoft Windows SDK documentation), it specifies the name of a port monitor as a function argument. The spooler calls the [**AddPortUI**](https://msdn.microsoft.com/library/windows/hardware/ff545026) function contained in the port monitor UI DLL of the specified port monitor.

The port monitor UI DLL's [**AddPortUI**](https://msdn.microsoft.com/library/windows/hardware/ff545026) function should perform the following operations:

1.  Call the print spooler's OpenPrinter function (described in the Windows SDK documentation), which causes the [**XcvOpenPort**](https://msdn.microsoft.com/library/windows/hardware/ff564259) function in the port monitor server DLL to be called.

2.  Call the print spooler's [**XcvData**](https://msdn.microsoft.com/library/windows/hardware/ff564255) function several times, to request the port monitor server DLL to add the port and to transfer configuration information between the UI DLL and the server DLL. The **XcvData** function calls the server DLL's [**XcvDataPort**](https://msdn.microsoft.com/library/windows/hardware/ff564258) function. The [**AddPortUI**](https://msdn.microsoft.com/library/windows/hardware/ff545026) function typically obtains configuration information from the user by displaying dialog boxes.

3.  Call the print spooler's ClosePrinter function (described in the Windows SDK documentation), which causes the [**XcvClosePort**](https://msdn.microsoft.com/library/windows/hardware/ff564254) function in the port monitor server DLL to be called.

For more information about these operations, see the description of [**AddPortUI**](https://msdn.microsoft.com/library/windows/hardware/ff545026). Also see [Storing Port Configuration Information](storing-port-configuration-information.md).

A port monitor's [**EnumPorts**](https://msdn.microsoft.com/library/windows/hardware/ff548754) function must enumerate all ports that have been added. The spooler can call each port monitor's **EnumPorts** function to determine the set of ports supported on a print server.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Adding%20a%20Port%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




