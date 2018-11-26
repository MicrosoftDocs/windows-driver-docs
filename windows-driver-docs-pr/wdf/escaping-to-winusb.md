---
title: Calling WinUSB from UMDF
description: Calling WinUSB from UMDF
ms.assetid: 33455d61-0eb3-47ef-998a-6e1b5d7db24e
keywords:
- WinUSB WDK UMDF
- WinUSB WDK UMDF , escaping to WinUSB
- user-mode drivers WDK UMDF , escaping to WinUSB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling WinUSB from UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A UMDF driver can call [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) directly if the driver cannot use the USB-specific UMDF interfaces to perform a specific operation. To call WinUSB Functions, the driver must first obtain a WinUSB interface handle by calling [**IWDFUsbTargetDevice::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560369) or [**IWDFUsbInterface::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560337). A WinUSB interface handle is used to define the first interface in the selected configuration.

For more information, see [How to Access a USB Device by Using WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540174).

 

 





