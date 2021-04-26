---
title: Win32 Services Interacting with Devices
description: Win32 Services Interacting with Devices
ms.date: 03/02/2020
ms.localizationpriority: medium
---

# Win32 Services Interacting with Devices

## Motivation:

An ideal Win32 service installed via [INF AddService](./inf-addservice-directive.md) that interacts with devices behaves similar to how a *driver* interacts with *devices*.  A driver is loaded and unloaded depending on the presence of a device, and a Win32 service that interacts with devices should follow this same pattern of **starting** and **stopping** depending on the presence of a device.  

Services should start only when a device interface is present to interact and stopped when the associated device is no longer present.  This design pattern ensures a robust service that minimizes undesired and undefined behavior.  We will walk through how a service should be designed to follow this pattern.

## Service Install

To install the service, use the [INF AddService](./inf-addservice-directive.md) directive.  This will allow you to create and start the service.

Add the flag that makes the service demand-start.  This can be accomplished by setting **StartType=0x3** which makes the service trigger started.

The final step in this section is to use the **AddTrigger** directive to make the service start when a device interface arrives (see [AddService](./inf-addservice-directive.md) for more details regarding **AddTrigger**).  Below is an example of how AddTrigger should be used:

```
[UserSvc_AddTrigger]
TriggerType = 1                                   ; SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL
Action      = 1                                   ; SERVICE_TRIGGER_ACTION_SERVICE_START
SubType     = %GUID_DEVINTERFACE_OSRFX2%          ; Interface class GUID
DataItem    = 2, "USB\VID_0547&PID_1002"          ; SERVICE_TRIGGER_DATA_TYPE_STRING

[UserSvc_Install]
ServiceType   = 0x10 ; SERVICE_WIN32_OWN_PROCESS
StartType     = 3   ; SERVICE_DEMAND_START
ErrorControl  = 0   ; SERVICE_ERROR_IGNORE
ServiceBinary = %13%\oemsvc.exe
AddTrigger    = UserSvc_AddTrigger

```
Note that the HardwareId specified in DataItem is optional and generally only needed when using a generic class interface to scope the trigger to a more specific device.  

## Service Runtime
	
From a runtime perspective, the first step for your service should be to register for device interface notifications.  Prescriptive guidance on how to accomplish this can be found on this page: [Registering for Notification of Device Interface Arrival and Device Removal](./registering-for-notification-of-device-interface-arrival-and-device-removal.md).

In particular, you should use **CM_Register_Notification** with the **CM_NOTIFY_FILTERY_TYPE_DEVICEINTERFACE** flag to accomplish the appropriate registration of device interface notifications.

>[!NOTE]
>When a service has started, you cannot rely on the fact that you will receive device interface notifications as the arrival notification may have already passed. Instead, you must get a list of device interfaces to check if there are already interfaces present.

Once you have registered for notifications, you can find your desired device interface in these two steps:

1. Discover the interface from the notification callback
2. Query the list of existing device interfaces and find the desired interface using **CM_Get_Device_Interface_List**

>[!NOTE] 
>Note, there is a chance that the interface arrives between registering for notifications and finding the desired device interface.  In that case, the interface will be listed in both the notification callback and the list of interfaces.

Once you have found the desired device interface, open a handle to the interface via [CreateFile](/windows/win32/api/fileapi/nf-fileapi-createfilea).  

The next step is to register for secondary per-interface notifications to operate and manage the device. This can be done using **CM_Register_Notification** with the **CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE** flag.  This will ensure that when a device is going away, the handle can be released accordingly.

Device interface arrivals and removals should be tracked so that the removal of the last device interface means the service can be stopped.  Once the last interface has been removed, stop your service (detailed information can be found on this [page](/windows/desktop/Services/service-servicemain-function)). This can be accomplished by following these steps:

1. Post **SERVICE_STOP_PENDING** state to SCM to indicate the service is going down
2. Unitialize/clean-up everything the service was using
3. Post **SERVICE_STOP** state to SCM to complete the stop operation

If the service is being stopped, make sure to check for and go through all existing open handles to device interfaces (there may be none) and clean them up. 
  
The device interface can come back either during device installation, device enable/disable, device re-enumeration, system reboot, or during other scenarios not listed.  When the device interface comes back, the service will be trigger started based on its trigger start registration.

This flow will ensure that the service starts on the arrival of a device interface and stops when the last device interface is no longer present.

## Code Sample & Related Links

There is a sample on GitHub that walks through how a service can leverage this flow of events.  The sample can be found here: [Win32 Service Sample](https://github.com/microsoft/Windows-driver-samples/tree/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_usersvc).

Additionally, you can find useful documentation regarding **AddTrigger** on the [AddService](./inf-addservice-directive.md) page.
