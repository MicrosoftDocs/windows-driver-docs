---
title: Registering for Application Notification
author: windows-driver-content
description: Registering for Application Notification
ms.assetid: e8f76014-6068-4012-96c6-88ea2bbd9bbf
keywords: ["dynamic hardware partitioning WDK , application notification", "hardware partitioning WDK dynamic , application notification", "partitions WDK dynamic hardware , application notification", "application notification WDK dynamic hardware partitioning , registering", "notification WDK dynamic hardware partitioning , application", "registering for application notifications WDK dynamic hardware partitioning"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering for Application Notification


A user-mode application calls the [RegisterDeviceNotification](http://go.microsoft.com/fwlink/p/?linkid=97892) function to register itself to be notified when a processor or memory module is dynamically added to the hardware partition. An application calls the **RegisterDeviceNotification** function two times, one time to register for notification of processor events and a second time to register for notification of memory events. The application specifies one of the following GUIDs when it registers for notification of these events:

<a href="" id="guid-device-processor"></a>GUID\_DEVICE\_PROCESSOR  
Registers the application to be notified when a processor is dynamically added to the hardware partition.

<a href="" id="guid-device-memory"></a>GUID\_DEVICE\_MEMORY  
Registers the application to be notified when memory is dynamically added to the hardware partition.

These GUIDs are defined in the header file, Poclass.h.

The following code example shows how to register for both notifications:

```
HWND hWnd;
DEV_BROADCAST_DEVICEINTERFACE ProcessorFilter;
DEV_BROADCAST_DEVICEINTERFACE MemoryFilter;
HDEVNOTIFY ProcessorNotifyHandle;
HDEVNOTIFY MemoryNotifyHandle;

// The following example assumes that hWnd already
// contains a handle to the application window that
// is to receive the WM_DEVICECHANGE messages.

// Initialize the filter for processor event notification
ZeroMemory(
  &amp;ProcessorFilter,
  sizeof(ProcessorFilter)
  );
ProcessorFilter.dbcc_size =
  sizeof(DEV_BROADCAST_DEVICEINTERFACE);
ProcessorFilter.dbcc_devicetype =
  DBT_DEVTYP_DEVICEINTERFACE;
ProcessorFilter.dbcc_classguid =
  GUID_DEVICE_PROCESSOR;

// Register the application window to receive
// WM_DEVICECHANGE messages for processor events.
ProcessorNotifyHandle =
  RegisterDeviceNotification(
    hWnd,
    &amp;ProcessorFilter,
    DEVICE_NOTIFY_WINDOW_HANDLE
    );

// Initialize the filter for memory event notification
ZeroMemory(
  &amp;MemoryFilter,
  sizeof(MemoryFilter)
  );
MemoryFilter.dbcc_size =
  sizeof(DEV_BROADCAST_DEVICEINTERFACE);
MemoryFilter.dbcc_devicetype =
  DBT_DEVTYP_DEVICEINTERFACE;
MemoryFilter.dbcc_classguid =
  GUID_DEVICE_MEMORY;

// Register the application&#39;s window to receive
// WM_DEVICECHANGE messages for memory events.
MemoryNotifyHandle =
  RegisterDeviceNotification(
    hWnd,
    &amp;MemoryFilter,
    DEVICE_NOTIFY_WINDOW_HANDLE
    );
```

**Note**   If an application only has to be notified about processors, it does not have to register for notification of memory events. Similarly, if an application only has to be notified about memory, it does not have to register for notification of processor events.

 

When an application no longer has to receive notification of processor or memory events, it can unregister the window from receiving WM\_DEVICECHANGE messages for these events by calling the [UnregisterDeviceNotification](http://go.microsoft.com/fwlink/p/?linkid=97893) function. The following code example shows how to unregister for the application notifications:

```
// Unregister the application window from receiving
// WM_DEVICECHANGE messages for processor events.
UnregisterDeviceNotification(ProcessorNotifyHandle);

// Unregister the application window from receiving
// WM_DEVICECHANGE messages for memory events.
UnregisterDeviceNotification(MemoryNotifyHandle);
```

For more information about the **RegisterDeviceNotification** and **UnregisterDeviceNotification** functions, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20for%20Application%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


