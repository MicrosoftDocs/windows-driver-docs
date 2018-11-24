---
title: Introduction to Driver Notification
description: Introduction to Driver Notification
ms.assetid: c0c09480-628a-4f12-b6a3-881cc3e12fd5
keywords: ["driver notification WDK dynamic hardware partitioning , synchronous", "driver notification WDK dynamic hardware partitioning , asynchronous", "driver notification WDK dynamic hardware partitioning , memory notification"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Driver Notification


Starting with Windows Server 2008, the operating system can notify a device driver when a processor or memory module is dynamically added to a hardware partition. There are several different notifications that occur at different stages of the process of a hot add operation. Each of these notifications uses a different notification method to notify the device driver about the event. You can use one or more of these notification methods to have the operating system notify your driver when a hot add operation occurs. Your driver can then respond as required for safe and optimal operation.

The following table identifies the different notification methods and whether they apply to processors, memory, or both processors and memory.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Notification method</th>
<th>For processors</th>
<th>For memory</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Synchronous driver notification</p></td>
<td><p>X</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>Asynchronous driver notification</p></td>
<td><p>X</p></td>
<td><p>X</p></td>
</tr>
<tr class="odd">
<td><p>Memory notification event</p></td>
<td></td>
<td><p>X</p></td>
</tr>
<tr class="even">
<td><p>Resource rebalancing</p></td>
<td><p>X</p></td>
<td></td>
</tr>
</tbody>
</table>

 

```cpp

```

### Synchronous Driver Notification

With [Synchronous Driver Notification](synchronous-driver-notification.md), the operating system synchronously notifies device drivers that a new processor has been added to the hardware partition. This is the first notification that a device driver receives about a change to the number of processors.

When a new processor is added to the hardware partition, the operating system sends this notification to device drivers after the operating system has started the new processor, but before the operating system begins scheduling threads on the processor. When a device driver receives this notification, it can allocate any per processor data structures and assign any other per processor resources to the new processor. This prepares the device driver to run its dispatch routines, interrupt service routines (ISRs), deferred procedure calls (DPCs), and any other driver threads on the new processor.

A device driver must register itself with the operating system to receive synchronous driver notification. For more information, see [Registering for Synchronous Driver Notification](registering-for-synchronous-driver-notification.md).

This notification method is only applicable to processors. There is no synchronous notification mechanism for memory.

### Asynchronous Driver Notification

With [Asynchronous Driver Notification](asynchronous-driver-notification.md), the operating system asynchronously notifies device drivers that a new processor or memory module has been added to the hardware partition. Starting with Windows Server 2008, processors and memory modules are considered Plug and Play (PnP) devices. Therefore, the operating system uses the PnP notification mechanism for asynchronous driver notification.

When a new processor or memory module is added to the hardware partition, the operating system sends this notification to device drivers after the operating system has started the new processor or memory device. In the case of a new processor, the operating system does not send this notification to device drivers until after it has started scheduling threads on the new processor.

**Note**   All PnP notifications are asynchronous. Therefore, these notifications might not be received by a device driver until sometime after the operating system has started the processor or memory module.

 

When a device driver receives this notification, it can adjust some or all of the following items accordingly:

-   Memory buffer and other resource allocations

-   Assignment of resources to specific processors

-   Scheduling of DPCs and other threads on specific processors

-   Load balancing algorithms

**Important**   When you add a new processor to a hardware partition, the operating system does not send the PnP notification until after the new processor has been started and the operating system has begun scheduling threads on it. If a device driver must perform certain tasks before the operating system begins scheduling threads on the new processor, such as allocating a per processor data structure, you must use the synchronous notification method for the driver.

 

A device driver must register itself with the operating system to receive asynchronous driver notification. For more information, see [Registering for Asynchronous Driver Notification](registering-for-asynchronous-driver-notification.md).

### Memory Notification Event

With the memory notification event method, you can have your device driver schedule a thread that waits for the operating system to set the **\\KernelObjects\\HighMemoryCondition** event object. The operating system sets this event object when the amount of free physical memory exceeds a certain value. This event notifies any threads that are waiting on the event object that a significant amount of physical memory is currently available in the system. This event could be an indication that you dynamically added a new memory module to the system. When the operating system sets this event object, your device driver can respond to the event by allocating additional memory buffers.

For more information about the **\\KernelObjects\\HighMemoryCondition** event object, see [Standard Event Objects](standard-event-objects.md).

**Important**  If the operating system sets the **\\KernelObjects\\HighMemoryCondition** event object, the event only provides an indication that you might have dynamically added a new memory module to the hardware partition. There are other situations that can cause the operating system to set this event object. Therefore, starting with Windows Server 2008, we do not recommend that device drivers use this notification method. Instead, device drivers should use the asynchronous driver notification method.

 

This method is only applicable to memory. There is no corresponding notification mechanism for processors.

### Resource Rebalance

Starting with Windows Server 2008, when you add a new processor to a hardware partition, the operating system initiates a system-wide resource rebalance. Whether a device will participate in such a resource rebalance is determined by the setting of the [**DEVPKEY\_Device\_DHP\_Rebalance\_Policy**](https://msdn.microsoft.com/library/windows/hardware/ff542423) device property for the device. The default behavior for devices in the Network Adapter (Class = Net) [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) is that they will not participate in resource rebalancing when a new processor is dynamically added to the system. The default behavior for devices in all other device setup classes is that they will participate in resource rebalancing when a new processor is dynamically added to the system.

If a device is a Plug and Play (PnP) device and it participates in such a resource rebalance, the operating system sends [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725), [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755), and [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) PnP IRPs to the driver for the device during the resource rebalancing operation. These PnP requests notify the driver that a hardware change has occurred in the hardware partition. A device driver should support resource rebalancing by correctly handling the **IRP\_MN\_QUERY\_STOP\_DEVICE** and **IRP\_MN\_STOP\_DEVICE** PnP requests. A device driver should never reject a **IRP\_MN\_QUERY\_STOP\_DEVICE** PnP request.

These PnP requests enable a device driver to fully use the new set of active processors in the hardware partition after you add a new processor. Specifically, a device driver that supports resource rebalancing uses the PnP requests that it receives during the resource rebalance to disconnect its interrupt service routines (ISRs) and reconnect them with the updated processor affinity value. This enables the device driver to use all the currently active processors in the hardware partition, including any new processors, for handling interrupt requests.

Device drivers should queue all I/O requests during resource rebalancing.

For more information about resource rebalancing, see [Stopping a Device to Rebalance Resources](stopping-a-device-to-rebalance-resources.md).

This method is only applicable to processors. The operating system does not initiate a system-wide resource rebalance when you add a new memory module to a hardware partition.

 

 




