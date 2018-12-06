---
title: User-Mode Power Service
description: User-Mode Power Service
ms.assetid: 57f3affd-18cc-440c-ba18-9ba89fd3c84f
keywords:
- Power Metering and Budgeting WDK , User-Mode Power Service
- User-Mode Power Service WDK Power Meter
- UMPS WDK Power Meter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User-Mode Power Service


Starting with Windows 7 and Windows Server 2008 R2, the User-Mode Power Service (UMPS) provides an interface for all aspects of power management to user-mode services and applications. This interface includes support for the Power Metering and Budgeting (PMB) infrastructure for power-related information. This information is used by applications, such as the Windows Performance Monitor (PerfMon), for power management and reporting.

UMPS provides access to PMB information by using a set of PMB WMI classes. These WMI classes comply with version 1.1.0 of the Distributed Management Task Force (DMTF) Power Supply Profile. For more information, see the [DMTF Power Supply Profile](http://go.microsoft.com/fwlink/p/?linkid=145048).

The PMB WMI classes provide support for the following:

-   Query of the current power metering and budgeting information for a power meter device.

-   Register for a callback notification when the meter's power threshold or budget is exceeded.

When UPMS services PMB WMI requests, it calls into the Power Meter Interface (PMI) through I/O request packets (IRPs) that are supported by PMI. For more information about PMI, see [Power Meter Interface](power-meter-interface.md).

For more information about the PMB WMI classes, see the Windows SDK documentation.

 

 




