---
title: Software Defined Battery
description: Software Defined Battery
keywords:
- Software Defined Battery
- SDB
ms.author: windowsdriverdev
ms.date: 11/04/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Software Defined Battery

Primary goal of this document is to introduce the reader to Software Defined Batteries, describe Windows SDB architecture and detail the Windows API contracts for this feature. 

The document starts by introducing the Simple Age Balancing SDB algorithm for a hypothetical two battery system. Followed by architecture layout and API contract needed to implement SDB algorithm.

TBD

The Power Meter Interface (PMI) is provided through a WDM driver that services I/O request packets (IRPs) from the [Power Manager](https://msdn.microsoft.com/library/windows/hardware/ff559829) and the Power WMI Provider component of the [User-Mode Power Service](user-mode-power-service.md) (UMPS).

PMI provides support for various I/O control (IOCTL) request packets that are issued by user-mode services or applications. This IOCTL interface provides information about the following items:

-   The power metering capabilities and configuration of a power meter. This includes the sampling interval and the power thresholds.

-   The power budgeting configuration of a power meter.

-   The asset information of a power meter, such as the vendor's name and the meter's serial number.

-   The current power level and budget information.

PMI also provides support for the notification of power metering events, such as when a power threshold or budget is reached or exceeded.

The power metering information that is accessed from PMI is generally read-only. However, depending on the capabilities of the power meter, its budgeting configuration could have read-only or read/write permission.

For more information about the PMI IOCTL interface, see [PMI IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff543884).

 

 


--------------------


