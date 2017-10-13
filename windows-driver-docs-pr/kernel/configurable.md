---
title: Configurable
author: windows-driver-content
description: Configurable
ms.assetid: 0dcdc2eb-0a27-4739-be9d-48a0382347cf
keywords: ["hardware-configurable devices WDK kernel", "software-configurable drivers WDK kernel", "configurable devices and drivers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configurable


## <a href="" id="ddk-configurable-kg"></a>


Today's peripheral devices must be *hardware-configurable*, and their drivers must be *software-configurable*.

A device is hardware-configurable if it can accept different assignments of the system's hardware resources, such as I/O port numbers, without being physically modified. For example, if a set of hot-pluggable Plug and Play disks are connected in a redundant array of independent disks (RAID) configuration, a user can swap disks while the system is running. If a device is hardware-configurable, its drivers cannot contain hard-coded, system-dependent values for the device's hardware resources.

A driver is software-configurable if:

-   It can receive and change its device's hardware resources dynamically.

    Drivers that support Plug and Play do not contain hard-coded values for a device's hardware resources, nor does the driver poll the device to determine its resource assignments. Instead, the system dynamically assigns resources to the device, and then supplies resource values to the driver.

-   It was written with no assumptions about other drivers that might reside above or below it in its driver stack.

    For example, the design of a lower-level device driver for a disk must be flexible enough to support multiple file systems that are implemented by multiple high-level file system drivers, possibly on a single computer.

    Additionally, if a computer has sufficient mass storage capacity, that same lower-level disk driver must not interfere with an intermediate driver's support for fault tolerance (implemented as mirrored partitions, stripe sets, or volume sets) within a file system.

The PnP manager and each PnP hardware bus driver work together to provide an interface between the platform's hardware for a specific type of I/O bus and the system's software. The PnP manager builds a [device tree](device-tree.md), with nodes that represent all the devices on the system, including buses. For each device, the PnP manager maintains two lists:

-   A list of the [hardware resources](hardware-resources.md) that the device is capable of using.

-   A list of the hardware resources that are actually assigned to the device.

Device drivers assist the PnP manager in creating these lists, which are maintained in the registry. As devices are added to and removed from the system, the PnP manager reassigns resources as necessary and updates the lists.

The system's hardware abstraction layer (HAL) component, which is implemented as a dynamic-link library, is responsible for some of the hardware-level, platform-specific support that is needed by other system components, including kernel-mode drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Configurable%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


