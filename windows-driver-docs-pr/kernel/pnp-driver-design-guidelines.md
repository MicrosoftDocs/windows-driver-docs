---
title: PnP Driver Design Guidelines
author: windows-driver-content
description: PnP Driver Design Guidelines
ms.assetid: 4e4a6a8e-3c7f-4561-bbe1-a8c06fe22d0a
keywords: ["PnP WDK kernel , design guidelines", "Plug and Play WDK kernel , design guidelines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PnP Driver Design Guidelines


## <a href="" id="ddk-pnp-driver-design-guidelines-kg"></a>


Plug and Play provides:

-   Automatic and dynamic recognition of installed hardware

-   Hardware resource allocation (and reallocation)

-   Loading of appropriate drivers

-   An interface for drivers to interact with the PnP system

-   Mechanisms for drivers and applications to learn of changes in the hardware environment

To support PnP, a driver must follow these guidelines:

-   It must contain a [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

    This dispatch routine must handle [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) requests and associated minor function codes. For more information, see [DispatchPnP Routines](dispatchpnp-routines.md).

-   It must not search for hardware.

    The PnP manager is responsible for determining the presence of hardware devices. When the PnP manager detects a device, it notifies the driver by calling its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. Hardware can be detected when the system is booted, or any time that a user adds a device to, or removes one from, a running system.

-   It must not allocate hardware resources.

    A PnP driver must provide the PnP manager with lists of resources that a device can potentially use. The PnP manager is responsible for assigning resources to each device, and notifying the driver of each device's assignments when it sends an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. The driver must thus be capable of working with various configurations of hardware resources.

Some drivers are insulated from the details of the PnP and power management by system-supplied port or class drivers. For example, a SCSI port driver insulates a SCSI miniport driver from many of the details of the power and PnP systems, so a SCSI miniport driver does not need to handle power and PnP IRPs directly. For such drivers, see the driver-specific documentation for details of the required PnP support.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PnP%20Driver%20Design%20Guidelines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


