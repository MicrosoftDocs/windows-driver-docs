---
title: Dynamic Hardware Partitioning Architecture
author: windows-driver-content
description: Dynamic Hardware Partitioning Architecture
MS-HAID:
- 'dhp\_f1c7dbf2-5849-4178-931e-375c6080d427.xml'
- 'kernel.dynamic\_hardware\_partitioning\_architecture'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e
keywords: ["dynamic hardware partitioning WDK , architecture", "hardware partitioning WDK dynamic , architecture", "partitions WDK dynamic hardware , architecture", "architecture WDK dynamic hardware partitioning", "dynamically partitionable servers WDK", "servers WDK dynamic hardware partitioning"]
---

# Dynamic Hardware Partitioning Architecture


A hardware partitionable server can be configured into one or more isolated hardware partitions. A hardware partition consists of one or more partition units. A partition unit can be a processor, a memory module, or an I/O host bridge.

The following figure shows an example of a hardware partitionable server.

![diagram illustrating a hardware partitionable server](images/dhparch.gif)

In the previous figure, the server has a total of 12 partition units: four memory modules, four processor modules, and four I/O host bridge modules. Each of these partition units is assigned to one of three hardware partitions. Each hardware partition is completely isolated from the other hardware partitions. The service processor is responsible for the configuration of the hardware partitions. It controls the mapping of the partition units to the hardware partitions and creates isolation between the hardware partitions.

Starting with Windows Server 2008, each partition unit is considered a Plug and Play (PnP) device. Because these devices are PnP, you can add them after the operating system has started.

For more information about how a device driver can register itself with the operating system to receive notification when partition units are dynamically added to the hardware partition, see [Driver Notification](driver-notification.md).

For more information about how an application can register itself with the operating system to receive notification when partition units are dynamically added to the hardware partition, see [Application Notification](application-notification.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Dynamic%20Hardware%20Partitioning%20Architecture%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


