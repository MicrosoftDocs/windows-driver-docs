---
title: Registering for Asynchronous Driver Notification
description: Registering for Asynchronous Driver Notification
keywords: ["driver notification WDK dynamic hardware partitioning , registering", "asynchronous notification WDK dynamic hardware partitioning", "notification WDK dynamic hardware partitioning , registering", "asynchronous driver notification WDK dynamic hardware partitioning , registering", "registering for driver notifications WDK dynamic hardware partitioning"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering for Asynchronous Driver Notification


To use asynchronous driver notification, a device driver implements callback functions that the operating system calls when you dynamically add a processor or memory module to the hardware partition. The following code example shows prototypes for such callback functions:

```cpp
// Prototypes for the asynchronous
// notification callback functions
NTSTATUS
  AsyncProcessorCallback(
    IN PVOID NotificationStructure,
    IN PVOID Context
    );

NTSTATUS
  AsyncMemoryCallback(
    IN PVOID NotificationStructure,
    IN PVOID Context
    );
```

A device driver registers for asynchronous notification by calling the [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification) function, one time for each of the device driver's callback functions, specifying a pointer to one of the following GUIDs for the *EventCategoryData* parameter:

<a href="" id="guid-device-processor"></a>GUID\_DEVICE\_PROCESSOR  
Register to be notified when a processor is dynamically added to the hardware partition.

<a href="" id="guid-device-memory"></a>GUID\_DEVICE\_MEMORY  
Register to be notified when memory is dynamically added to the hardware partition.

These GUIDs are defined in the header file, Poclass.h.

The following code example shows how to register for both notifications:

```cpp
PVOID ProcessorNotificationEntry;
PVOID MemoryNotificationEntry;
NTSTATUS Status;

Status =
  IoRegisterPlugPlayNotification(
    EventCategoryDeviceInterfaceChange,
    0,
    &GUID_DEVICE_PROCESSOR,
    DriverObject,
    AsyncProcessorCallback,
    NULL,
    &ProcessorNotificationEntry
    );

Status =
  IoRegisterPlugPlayNotification(
    EventCategoryDeviceInterfaceChange,
    0,
    &GUID_DEVICE_MEMORY,
    DriverObject,
    AsyncMemoryCallback,
    NULL,
    &MemoryNotificationEntry
    );
```

**Note**   If a device driver only has to be notified about processors, it does not have to implement a callback function for memory or register for notification about memory. Similarly, if a device driver only has to be notified about memory, it does not have to implement a callback function for processors or register for notification about processors.

 

When a device driver must stop receiving asynchronous driver notifications, such as when it is being unloaded, it must unregister each callback function by calling the [**IoUnregisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iounregisterplugplaynotification) function. The following code example shows how to unregister the callback functions:

```cpp
// Unregister for asynchronous notifications
Status =
  IoUnregisterPlugPlayNotification(
    ProcessorNotificationEntry
    );

Status =
  IoUnregisterPlugPlayNotification(
    MemoryNotificationEntry
    );
```

 

