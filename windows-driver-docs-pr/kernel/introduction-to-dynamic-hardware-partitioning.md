---
title: Introduction to Dynamic Hardware Partitioning
author: windows-driver-content
description: Introduction to Dynamic Hardware Partitioning
ms.assetid: 0d909c64-17c4-4f0e-85b7-4e0a6a92eeee
keywords: ["dynamic hardware partitioning WDK , about dynamic hardware partitioning", "hardware partitioning WDK dynamic , about dynamic hardware partitioning", "partitions WDK dynamic hardware , about dynamic hardware partitioning", "hardware partitionable servers WDK", "partition units WDK dynamic hardware partitions", "statically partitionable servers WDK dynamic hardware partitioning", "dynamically partitionable servers WDK dynamic hardware partitioning", "hot add WDK dynamic hardware partitioning", "hot remove WDK dynamic hardware partitioning", "hot replace WDK dynamic hardware partitioning", "servers WDK dynamic hardware partitioning", "hardware partitions WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Dynamic Hardware Partitioning


A *hardware partitionable server* is a server that can be configured into one or more isolated *hardware partitions*. Each hardware partition runs an independent instance of the operating system. You can assign each of the server's hardware resources to each of the various hardware partitions in whatever configuration is appropriate for the server's application. The hardware resources that are assigned to a particular hardware partition are isolated from the other hardware partitions in the server.

A hardware partition consists of one or more *partition units*. A partition unit is the smallest unit of hardware that you can assign to a hardware partition. A partition unit can be a processor, a memory module, or an I/O host bridge. Typically, processors and memory modules are plugged into sockets that can be powered on or off independently.

A hardware partitionable server can be one of two types: *statically partitionable* or *dynamically partitionable*. On a statically partitionable server, you cannot change the configuration of partition units that are assigned to each hardware partition while the server is running. To change the configuration, you must shut down and restart the server computer. Microsoft Windows Server 2000 and later versions of the Windows Server operating system support statically partitionable servers.

On a dynamically partitionable server, you can change the configuration of the partition units that are assigned to each hardware partition while the server is running. This is known as *dynamic hardware partitioning*. If the operating system that is running on a hardware partition supports dynamic hardware partitioning, you can add, replace, or remove partition units without restarting the operating system. Depending on the capabilities of the operating system, you can perform one or more of the following dynamic hardware partitioning operations:

<a href="" id="hot-add"></a>*Hot add*  
Adding a partition unit to a running hardware partition.

<a href="" id="hot-remove"></a>*Hot remove*  
Removing a partition unit from a running hardware partition.

<a href="" id="hot-replace"></a>*Hot replace*  
Replacing a partition unit with an identical replacement partition unit that is already present in the server computer. A hot replace operation is a single operation that differs from a hot remove operation followed by a hot add operation.

Windows Server 2003 with Service Pack 1 (SP1) supports hot add operations for memory modules on x86-based, x64-based, and Itanium-based servers. Windows Server 2003 SP1 does not support hot remove or hot replace operations.

Starting with Windows Server 2008, the operating system supports hot add operations for processors, memory modules, and I/O host bridges, and hot replace operations for processors and memory modules on x64-based and Itanium-based server computers. The operating system also supports hot add operations for memory modules on x86-based server computers. The operating system does not support hot remove operations.

The following table summarizes the dynamic hardware partitioning support that is included in each version of Windows Server.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Windows Server 2003 with SP1</th>
<th>Windows Server 2008 and later versions of Windows Server on x86-based servers</th>
<th>Windows Server 2008 and later versions of Windows Server on x64-based and Itanium-based servers</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>hot add</p></td>
<td><p>memory modules</p></td>
<td><p>memory modules</p></td>
<td>processors,
memory modules,
I/O host bridges</td>
</tr>
<tr class="even">
<td><p>hot remove</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>hot replace</p></td>
<td></td>
<td></td>
<td>processors,
memory modules</td>
</tr>
</tbody>
</table>

 

We suggest that you consider the following guidelines when you develop your device drivers:

-   You should understand dynamic hardware partitioning because certain assumptions about the hardware configuration of a server computer are not valid on dynamically partitionable servers. Device drivers that are not designed to accommodate dynamic hardware partitioning could cause data corruption or cause the operating system to generate a bug check if they are run on a dynamically partitionable server.

-   You should consider the [critical issues](critical-issues-for-device-drivers.md) that are identified for dynamic hardware partitioning, even if you are not developing device drivers for server computers.

-   You should review and update all the device drivers that you are developing for servers that run Windows Server 2008 and later versions of Windows Server. Device drivers can register with the operating system to be notified of changes to the hardware configuration. When the device drivers are notified about a change to the hardware configuration, they can respond to the change as required for safe and optimal operation. This ensures that the drivers function correctly on dynamically partitionable servers.

Drivers that you develop for Windows XP and later versions of Windows that correctly participate in [resource rebalancing](stopping-a-device-to-rebalance-resources.md) and do not make any assumptions about the number of processors, the processor affinity mask, or the amount of physical memory, will continue to operate correctly on a dynamically partitionable server.

Most existing user-mode applications should continue to run on dynamically partitionable servers without any modification. However, if an application allocates threads for each processor or performs memory allocations that are based on how much physical memory is available, the application can register with the operating system to be notified of changes to the hardware configuration. When the application is notified about a change to the hardware configuration, it can adjust its resource allocation accordingly.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Dynamic%20Hardware%20Partitioning%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


