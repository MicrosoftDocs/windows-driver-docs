---
title: PnP Driver Design Guidelines
description: PnP Driver Design Guidelines
ms.assetid: 4e4a6a8e-3c7f-4561-bbe1-a8c06fe22d0a
keywords: ["PnP WDK kernel , design guidelines", "Plug and Play WDK kernel , design guidelines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# PnP Driver Design Guidelines





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

 

 




