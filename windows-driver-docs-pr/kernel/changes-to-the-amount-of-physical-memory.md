---
title: Changes to the Amount of Physical Memory
author: windows-driver-content
description: Changes to the Amount of Physical Memory
MS-HAID:
- 'dhp\_ffa1a2bd-1a63-4011-80af-f57829d7bdbe.xml'
- 'kernel.changes\_to\_the\_amount\_of\_physical\_memory'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5ab1d598-e702-4fc7-aab4-7b7726c3a552
keywords: ["dynamic hardware partitioning WDK , physical memory", "hardware partitioning WDK dynamic , physical memory", "partitions WDK dynamic hardware , physical memory", "physical memory WDK dynamic hardware partitioning", "memory WDK dynamic hardware partitioning"]
---

# Changes to the Amount of Physical Memory


On a dynamically partitionable server, you can add memory modules to a hardware partition at any time. Therefore, do not make any assumptions about how much physical memory exists in a hardware partition.

If a device driver uses the amount of physical memory in the hardware partition to determine the size of the memory buffers that it allocates, you must update the driver so that it will function correctly on a dynamically partitionable server when you dynamically add memory to the hardware partition.

If a device driver is affected by changes to the amount of physical memory, it must register itself with the operating system to be notified when memory is added to the hardware partition. When the device driver is notified, it can respond as required to ensure safe and optimal operation. For more information about how a device driver can register itself with the operating system, see [Driver Notification](driver-notification.md).

**Note**  Starting with Windows Server 2008, the size of the paged and nonpaged system memory pools do not change after the operating system has started. Therefore, if you add memory to the hardware partition, the amount of memory in these system memory pools does not change.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Changes%20to%20the%20Amount%20of%20Physical%20Memory%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


