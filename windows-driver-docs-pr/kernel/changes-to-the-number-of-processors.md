---
title: Changes to the Number of Processors
description: Changes to the Number of Processors
ms.assetid: 9ced4b42-c83d-49da-8405-b95b0c0144fa
keywords: ["dynamic hardware partitioning WDK , changing number of processors", "hardware partitioning WDK dynamic , changing number of processors", "partitions WDK dynamic hardware , changing number of processors", "active processors WDK dynamic hardware partitioning", "processor count WDK dynamic hardware partitioning", "processor affinity WDK dynamic hardware paritioning", "per-processor data structures WDK dynamic hardware partitioning"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Changes to the Number of Processors


On a dynamically partitionable server, you can add a processor to a hardware partition at any time. Therefore, you should not make any assumptions about the number of active processors in a hardware partition, the processor affinity value, or the processor number that is assigned to each active processor. The bits that are set in the processor affinity value represent each of the currently active processors in the hardware partition. The particular bits that are set will change if you add a processor to the hardware partition.

If any of the following statements are true for a device driver, you must update the driver so that it will function correctly on a dynamically partitionable server when a processor is dynamically added to a hardware partition:

-   The device driver uses the number of active processors in the hardware partition to determine the amount of resources that it uses, such as the amount of memory that it allocates, the number of threads that it creates, or the amount of other resources that it uses. In this situation, the device driver's resource allocation will be incorrect if a processor is dynamically added to the hardware partition. This could adversely affect the performance or behavior of the driver.

-   The device driver walks the bits of the processor affinity value. In this situation, the device driver might not work correctly if it cannot handle dynamic changes to the processor affinity value or cannot handle gaps in the sequence of bits that are set.

-   The device driver uses the bits in the processor affinity value to assign driver-allocated resources to specific processors. In this situation, the device driver's resource assignments will be incorrect if a processor is dynamically added to the hardware partition. This could adversely affect the performance or behavior of the driver.

-   The device driver allocates data structures for each active processor in the hardware partition. In this situation, the device driver could cause adverse behavior, data corruption, or a bug check to occur if it tries to access these data structures for a processor that was dynamically added to the hardware partition.

-   The device driver's dispatch routines use the processor number of the processor on which they are running to access data structures or other resources that are assigned to that particular processor. In this situation, the device driver's dispatch routines can cause adverse behavior, data corruption, or a bug check to occur if they try to access these resources for a processor that has been dynamically added to the hardware partition.

-   The device driver schedules its interrupt service routines (ISRs), deferred procedure calls (DPCs), or other threads on specific processors. In this situation, the device driver might stop functioning correctly if you add a processor to the hardware partition, and the device driver will be unable to fully use any new processors.

-   The device driver does not support resource rebalancing. In this situation, the device driver will be unable to use any new processors that are added to the hardware partition for handling interrupts.

-   The device driver uses a load balancing algorithm to distribute the processing of I/O requests across multiple processors. In this situation, the device driver might stop functioning correctly if you add a processor to the hardware partition, and the device driver will be unable to fully use any new processors.

If a device driver is affected by changes to the number of active processors, it must register itself with the operating system to be notified when you add processors to the hardware partition. When the device driver is notified, it can respond as required for safe and optimal operation. For more information about how a device driver can register itself with the operating system, see [Driver Notification](driver-notification.md).

To retrieve the current number of active processors in the hardware partition, device drivers should call the [**KeQueryActiveProcessorCount**](https://msdn.microsoft.com/library/windows/hardware/ff552985) function. To retrieve the current processor affinity value, device drivers can call either the [**KeQueryActiveProcessors**](https://msdn.microsoft.com/library/windows/hardware/ff553001) function or the **KeQueryActiveProcessorCount** function.

**Note**  If a device driver allocates data structures for each active processor in the hardware partition and the device driver would fail if the memory allocation for the data structures for a new processor failed, the device driver can allocate enough of these data structures during driver initialization to handle the maximum number of processors that the operating system supports. In this situation, the device driver would not have to allocate new data structures when you add new processors to the hardware partition. However, unless the size of these data structures is fairly small, this can be an inefficient use of memory resources. A device driver can query the maximum number of processors that the operating system supports by calling the [**KeQueryMaximumProcessorCount**](https://msdn.microsoft.com/library/windows/hardware/ff553042) function.

 

**Important**  Device drivers should always update any saved value of the number of active processors and the processor affinity when it is notified that you added a processor to the hardware partition.

 

**Important**  A device driver should not count the number of set bits in the processor affinity value to determine the number of active processors in the hardware partition. We recommended that device drivers call the **KeQueryActiveProcessorCount** function for this purpose. This function returns both the number of active processors and the associated processor affinity value.

 

**Important**  Device drivers that are built for Windows Vista, Windows Server 2008 and later versions of Windows must not use the [**KeNumberProcessors**](https://msdn.microsoft.com/library/windows/hardware/ff552975) kernel variable to determine the number of active processors in the hardware partition. The **KeNumberProcessors** kernel variable is obsolete in Windows Vista with Service Pack 1 (SP1), Windows Server 2008, and later versions of Windows.

 

 

 




