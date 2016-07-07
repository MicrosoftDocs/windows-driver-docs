---
title: User-Mode Power Service
description: User-Mode Power Service
ms.assetid: 57f3affd-18cc-440c-ba18-9ba89fd3c84f
keywords: ["Power Metering and Budgeting WDK , User-Mode Power Service", "User-Mode Power Service WDK Power Meter", "UMPS WDK Power Meter"]
---

# User-Mode Power Service


Starting with Windows 7 and Windows Server 2008 R2, the User-Mode Power Service (UMPS) provides an interface for all aspects of power management to user-mode services and applications. This interface includes support for the Power Metering and Budgeting (PMB) infrastructure for power-related information. This information is used by applications, such as the Windows Performance Monitor (PerfMon), for power management and reporting.

UMPS provides access to PMB information by using a set of PMB WMI classes. These WMI classes comply with version 1.1.0 of the Distributed Management Task Force (DMTF) Power Supply Profile. For more information, see the [DMTF Power Supply Profile](http://go.microsoft.com/fwlink/p/?linkid=145048).

The PMB WMI classes provide support for the following:

-   Query of the current power metering and budgeting information for a power meter device.

-   Register for a callback notification when the meter's power threshold or budget is exceeded.

When UPMS services PMB WMI requests, it calls into the Power Meter Interface (PMI) through I/O request packets (IRPs) that are supported by PMI. For more information about PMI, see [Power Meter Interface](power-meter-interface.md).

For more information about the PMB WMI classes, see the Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[powermeter\powermeter]:%20User-Mode%20Power%20Service%20%20RELEASE:%20%286/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


