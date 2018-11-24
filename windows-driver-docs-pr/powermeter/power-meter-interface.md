---
title: Power Meter Interface
description: Power Meter Interface
ms.assetid: be3ffb33-f1da-403d-b888-378ffd5cac8a
keywords:
- Power Metering and Budgeting WDK , interface
- Power Meter Interface WDK
- PMI WDK Power Meter
ms.date: 10/09/2017
ms.localizationpriority: medium
---

# Power Meter Interface


The Power Meter Interface (PMI) is provided through a WDM driver that services I/O request packets (IRPs) from the [Power Manager](https://msdn.microsoft.com/library/windows/hardware/ff559829) and the Power WMI Provider component of the [User-Mode Power Service](user-mode-power-service.md) (UMPS).

PMI provides support for various I/O control (IOCTL) request packets that are issued by user-mode services or applications. This IOCTL interface provides information about the following items:

-   The power metering capabilities and configuration of a power meter. This includes the sampling interval and the power thresholds.

-   The power budgeting configuration of a power meter.

-   The asset information of a power meter, such as the vendor's name and the meter's serial number.

-   The current power level and budget information.

PMI also provides support for the notification of power metering events, such as when a power threshold or budget is reached or exceeded.

The power metering information that is accessed from PMI is generally read-only. However, depending on the capabilities of the power meter, its budgeting configuration could have read-only or read/write permission.

For more information about the PMI IOCTL interface, see [PMI IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff543884).

 
**Note**   The PMB infrastructure is supported on Windows 7, Windows Server 2008 R2, and later versions of the Windows operating systems.


 




