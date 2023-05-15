---
title: Still image device events
description: Still image device events
ms.date: 05/02/2023
---

# Still image device events

A *still image device event* is a device-level occurrence that upper-level software should be notified about, if that software has requested such notification. The user-mode minidriver is responsible for defining most device events and delivering notifications when an event occurs. In general, events indicate that upper-level software is going to be required to perform some action.

A typical still image device event is the detection of a push button being pressed. For example, a scanner might provide a user with separate buttons to initiate scanning text and photographs. When a button is pressed, upper-level software will be needed in order to display or store the image. The still image event monitor detects that the event has occurred (using the [IStiDevice COM interface](istidevice-com-interface.md)) and can call a still image application that was previously registered (using the [IStillImage COM interface](istillimage-com-interface.md)).

Still image device events are represented by GUIDs. In *sti.h*, Microsoft defines the following still image device events:

| Event GUID | Purpose |
|--|--|
| **GUID_DeviceArrivedLaunch** | A still image device has just been attached to the system. |
| **GUID_ScanImage** | An image should be scanned into the computer. |
| **GUID_ScanFaxImage** | An image should be scanned into the computer and then faxed. |
| **GUID_ScanPrintImage** | An image should be scanned into the computer and then printed. |
| **GUID_STIUserDefined1** | A user-definable button has been pressed. |
| **GUID_STIUserDefined2** | A user-definable button has been pressed. |
| **GUID_STIUserDefined3** | A user-definable button has been pressed. |

Developers of user-mode minidrivers should use these predefined event GUIDs whenever possible. If these GUIDs are not appropriate, GUIDs for device-specific events must be defined.

To define a still image device event, you must:

- Specify a GUID for each event.

- Include each GUID in the user-mode driver's INF file.

Within the driver's INF file, each GUID specification must include either an asterisk (meaning "all applications") or a list of specific applications, indicating which applications should be started when the event occurs. The still image event monitor uses this list to provide default assignments of applications to events. The user can modify these assignments with the Scanners and Cameras Control Panel.

## Event Notification

The driver must monitor the device (using either asynchronous I/O or polling) to determine when the event associated with each GUID occurs. Depending on device capabilities, the driver can notify clients of the occurrence of device events either asynchronously or by responding to a request to poll the device. All drivers that are capable of delivering notification of device events (by either method) must set the STI_GENCAP_NOTIFICATIONS flag in the device's [**STI_DEV_CAPS**](/windows-hardware/drivers/ddi/sti/ns-sti-_sti_dev_caps) structure. Drivers that support polling, and not asynchronous notification, must also set the STI_GENCAP_POLLING_NEEDED flag in the same structure. (These capabilities must also be indicated using the **Capabilities** keyword in [INF files for still image devices](inf-files-for-still-image-devices.md).)

If a driver supports asynchronous notification of events, the event monitor calls [**IStiUSD::SetNotificationHandle**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-setnotificationhandle) to request notifications and to supply an event handle. When a device event occurs, the driver must notify the event monitor by calling **SetEvent** (see the Microsoft Windows SDK documentation), using the event handle as an argument. The client can then call [**IStiUSD::GetNotificationData**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getnotificationdata) to obtain the event's GUID.

If polling is required, the event monitor calls [**IStiUSD::GetStatus**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getstatus) to poll the driver, which must in turn poll the device and return results in an [**STI_DEVICE_STATUS**](/windows-hardware/drivers/ddi/sti/ns-sti-_sti_device_status) structure.
