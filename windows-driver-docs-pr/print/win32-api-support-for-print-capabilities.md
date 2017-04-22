---
title: Win32 API Support for Print Capabilities
author: windows-driver-content
description: Win32 API Support for Print Capabilities
ms.assetid: 1b40cc3e-c6f6-460f-b514-4ef3a001f563
keywords:
- Print Capabilities WDK , Win32 API support
- DrvDeviceCapabilities
- Win32 applications WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Win32 API Support for Print Capabilities


The Windows Vista print subsystem provides compatibility support that enables Windows Presentation Foundation (WPF) applications to use GDI-based print drivers and enables Microsoft Win32-based applications to use XPSDrv print drivers. This compatibility is provided through a layer of software shims. Shims are software modules that perform transformation operations on the data so that otherwise incompatible software can interoperate. The following figure shows the data paths of this implementation for Print Capabilities.

![diagram illustrating print capabilities data flows](images/ptpccomp.gif)

Both [XPSDrv print drivers](xpsdrv-printer-drivers.md) and GDI-based, version 3 print drivers support the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function. When a Win32 application calls **DrvDeviceCapabilities** or the **GetDevCap** function, the print subsystem will call **DrvDeviceCapabilities** to collect the device capability information from the print driver.

When a WPF application requests a PrintCapabilities document from a print driver, the print subsystem will do one of the following:

-   If the print driver supports the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375), the print subsystem will query the print driver for the PrintCapabilities document by using the [**IPrintTicketProvider::GetPrintCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff554365) method.

-   If the print driver does not support the **IPrintTicketProvider** interface, the Print Ticket Manager will query the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function of the print driver and use the returned information to create a PrintTicket document that is returned to the application.

For more information about how the **IPrintTicketProvider** interface is supported by Microsoft print drivers, see [Printer Driver and Plug-in Interface Design in Windows Vista](printer-driver-and-plug-in-helper-interfaces.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Win32%20API%20Support%20for%20Print%20Capabilities%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


