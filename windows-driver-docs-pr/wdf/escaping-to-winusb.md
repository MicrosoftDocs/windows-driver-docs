---
title: Calling WinUSB from UMDF
description: Calling WinUSB from UMDF
keywords:
- WinUSB WDK UMDF
- WinUSB WDK UMDF , escaping to WinUSB
- user-mode drivers WDK UMDF , escaping to WinUSB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling WinUSB from UMDF


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

A UMDF driver can call [WinUSB Functions](/previous-versions/windows/hardware/drivers/ff540046(v=vs.85)#winusb) directly if the driver cannot use the USB-specific UMDF interfaces to perform a specific operation. To call WinUSB Functions, the driver must first obtain a WinUSB interface handle by calling [**IWDFUsbTargetDevice::GetWinUsbHandle**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-getwinusbhandle) or [**IWDFUsbInterface::GetWinUsbHandle**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getwinusbhandle). A WinUSB interface handle is used to define the first interface in the selected configuration.

For more information, see [How to Access a USB Device by Using WinUSB Functions](../usbcon/using-winusb-api-to-communicate-with-a-usb-device.md).

