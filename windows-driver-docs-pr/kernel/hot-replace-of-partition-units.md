---
title: Hot Replace of Partition Units
description: Hot Replace of Partition Units
ms.assetid: 6d50dc7d-6c3b-41e5-b6eb-aead9833dd1e
keywords: ["dynamic hardware partitioning WDK , hot replace", "hardware partitioning WDK dynamic , hot replace", "partitioning WDK dynamic hardware , hot replace", "hot replace WDK dynamic hardware partitioning"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Hot Replace of Partition Units


On a dynamically partitionable server, you can dynamically replace partition units in a hardware partition at any time. This is known as a hot replace operation. When you replace a partition unit, the operating system puts the hardware partition into a pseudo S4 sleep state. To put the hardware partition into this special sleep state, the operating system sends an S4 *set power* power management request to all the device drivers in the system. However, unlike a typical S4 power state, the operating system does not write out the state of the system to a hibernation file.

A device driver must support this pseudo S4 sleep state by correctly handling the *query power* and *set power* power management requests. A device driver should never reject a *query power* request. When a device driver receives an S4 *set power* power management request, it must transition its devices into a D3 device power state and stop all I/O operations. This includes any direct memory access (DMA) transfers that are currently in progress. By putting the driver's devices into a low power state, disabling interrupts, and halting all I/O operations that are in progress, the replace operation can continue without affecting the device driver.

While a device driver's devices are in the D3 power state, the device driver should queue any new I/O requests that it receives. A device driver should use an I/O time-out period for the I/O requests that it processes. This time-out period must be long enough so that the I/O requests will not time out if they are stopped or queued during the replacement of a partition unit. When the operating system resumes from the pseudo S4 sleep state, the device driver can resume processing any stopped or queued I/O requests.

For more information about how to implement support for power management in a device driver, see [Power Management](implementing-power-management.md).

A device driver must not bind itself to a uniquely identifiable instance of system hardware such as a specific processor. Otherwise, the driver might fail if the partition unit that contains that hardware is replaced in the hardware partition.

 

 




