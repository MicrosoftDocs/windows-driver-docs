---
title: Calling WinUSB from UMDF
author: windows-driver-content
description: Calling WinUSB from UMDF
ms.assetid: 33455d61-0eb3-47ef-998a-6e1b5d7db24e
keywords: ["WinUSB WDK UMDF", "WinUSB WDK UMDF , escaping to WinUSB", "user-mode drivers WDK UMDF , escaping to WinUSB"]
---

# Calling WinUSB from UMDF


\[This topic applies to UMDF 1.*x*.\]

A UMDF driver can call [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) directly if the driver cannot use the USB-specific UMDF interfaces to perform a specific operation. To call WinUSB Functions, the driver must first obtain a WinUSB interface handle by calling [**IWDFUsbTargetDevice::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560369) or [**IWDFUsbInterface::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560337). A WinUSB interface handle is used to define the first interface in the selected configuration.

For more information, see [How to Access a USB Device by Using WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540174).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Calling%20WinUSB%20from%20UMDF%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




