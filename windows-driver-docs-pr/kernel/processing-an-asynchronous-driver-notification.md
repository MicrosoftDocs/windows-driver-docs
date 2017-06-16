---
title: Processing an Asynchronous Driver Notification
author: windows-driver-content
description: Processing an Asynchronous Driver Notification
ms.assetid: 7e7ed971-5891-4b91-909a-1e140b764fed
keywords: ["driver notification WDK dynamic hardware partitioning , processing", "asynchronous driver notification WDK dynamic hardware partitioning , processing", "registering for driver notification WDK dynamic hardware partitioning , asynchronous"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing an Asynchronous Driver Notification


When the operating system calls a registered callback function, it passes a pointer to a [**DEVICE\_INTERFACE\_CHANGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff543134) structure in the *NotificationStructure* parameter.

The following code example shows an implementation of a callback function that processes asynchronous driver notifications for processors:

```
// Asynchronous processor notification callback function
NTSTATUS
  AsyncProcessorCallback(
    IN PVOID NotificationStructure,
    IN PVOID Context
    )
{
  PDEVICE_INTERFACE_CHANGE_NOTIFICATION Notification;
  ULONG ProcessorCount;
  KAFFINITY ActiveProcessors;

  Notification = 
    (PDEVICE_INTERFACE_CHANGE_NOTIFICATION)
      NotificationStructure;

  // Verify that this notification is about a processor
  // that is being added to the hardware partition.
  if (IsEqualGUID(
        &amp;Notification->Event,
        &amp;GUID_DEVICE_INTERFACE_ARRIVAL
        ))
  {
    // Get the current processor count and affinity
    ProcessorCount =
      KeQueryActiveProcessorCount(
        &amp;ActiveProcessors
        );

    // Adjust any resource allocations that are based
    // on the number of processors.
    ...

    // Adjust the assignment of resources that are
    // assigned to specific processors.
    ...

    // Begin scheduling any per processor threads
    // on the new processor.
    ...

    // Adjust the scheduling of DPCs and other threads
    ...

    // Adjust any load balancing algorithms
    ...
  }

  // Always return success status
 return STATUS_SUCCESS;
}
```

The following code example shows an implementation of a callback function that processes asynchronous driver notifications for memory:

```
// Asynchronous memory notification callback function
NTSTATUS
  AsyncMemoryCallback(
    IN PVOID NotificationStructure,
    IN PVOID Context
    )
{
  PDEVICE_INTERFACE_CHANGE_NOTIFICATION Notification;

  Notification = 
    (PDEVICE_INTERFACE_CHANGE_NOTIFICATION)
      NotificationStructure;

  // Verify that this notification is about memory
  // that is being added to the hardware partition.
  if (IsEqualGUID(
        &amp;Notification->Event,
        &amp;GUID_DEVICE_INTERFACE_ARRIVAL
        ))
  {
    // Increase the size of any memory buffers
    // for optimal performance of the driver.
    ...
  }

  // Always return success status
  return STATUS_SUCCESS;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Processing%20an%20Asynchronous%20Driver%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


