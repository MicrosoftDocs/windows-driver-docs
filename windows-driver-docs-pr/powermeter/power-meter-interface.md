---
title: Power Meter Interface
description: Power Meter Interface
ms.assetid: be3ffb33-f1da-403d-b888-378ffd5cac8a
keywords: ["Power Metering and Budgeting WDK , interface", "Power Meter Interface WDK", "PMI WDK Power Meter"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[powermeter\powermeter]:%20Power%20Meter%20Interface%20%20RELEASE:%20%286/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


