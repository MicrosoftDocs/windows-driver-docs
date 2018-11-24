---
title: Changes to the Amount of Physical Memory
description: Changes to the Amount of Physical Memory
ms.assetid: 5ab1d598-e702-4fc7-aab4-7b7726c3a552
keywords: ["dynamic hardware partitioning WDK , physical memory", "hardware partitioning WDK dynamic , physical memory", "partitions WDK dynamic hardware , physical memory", "physical memory WDK dynamic hardware partitioning", "memory WDK dynamic hardware partitioning"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Changes to the Amount of Physical Memory


On a dynamically partitionable server, you can add memory modules to a hardware partition at any time. Therefore, do not make any assumptions about how much physical memory exists in a hardware partition.

If a device driver uses the amount of physical memory in the hardware partition to determine the size of the memory buffers that it allocates, you must update the driver so that it will function correctly on a dynamically partitionable server when you dynamically add memory to the hardware partition.

If a device driver is affected by changes to the amount of physical memory, it must register itself with the operating system to be notified when memory is added to the hardware partition. When the device driver is notified, it can respond as required to ensure safe and optimal operation. For more information about how a device driver can register itself with the operating system, see [Driver Notification](driver-notification.md).

**Note**  Starting with Windows Server 2008, the size of the paged and nonpaged system memory pools do not change after the operating system has started. Therefore, if you add memory to the hardware partition, the amount of memory in these system memory pools does not change.

 

 

 




