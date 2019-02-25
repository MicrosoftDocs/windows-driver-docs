---
title: Configurable
description: Configurable
ms.assetid: 0dcdc2eb-0a27-4739-be9d-48a0382347cf
keywords: ["hardware-configurable devices WDK kernel", "software-configurable drivers WDK kernel", "configurable devices and drivers WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Configurable





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

 

 




