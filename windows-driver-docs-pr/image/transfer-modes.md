---
title: Transfer Modes
description: Transfer Modes
ms.assetid: 79af0d8f-dd04-4ff4-a047-f415562a16a5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transfer Modes





The still image interfaces define two transfer modes − *status mode* and *data mode*. When a client of the **IStillImage** COM interface calls [**IStillImage::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543778) to obtain access to a still image device, it specifies one (or both) of the transfer modes. Multiple clients can open a device in status mode, but only one client at a time is allowed to open a device in data mode.

The still image event monitor opens devices in status mode. Typically, but not always, [image acquisition APIs](creating-device-specific-components-for-image-acquisition-apis.md) open devices in data mode.

Once a client has opened a device in data mode, the event monitor stores subsequent [still image device events](still-image-device-events.md) in an internal queue. If the client calls [**IStiDevice::Subscribe**](https://msdn.microsoft.com/library/windows/hardware/ff543768), it can read events from the queue by calling [**IStiDevice::GetLastNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543751). After the client closes the device, subsequently received events cause the event monitor to again try to start a registered application.

The meanings of the two transfer modes are entirely dependent on the device's user-mode minidriver. The **IStillImage** and **IStiDevice** interfaces allow all methods to be called in either mode.

A minidriver can determine the mode in which it was opened by calling [**IStiDevice::GetLastNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543751). Minidrivers should prohibit a client from performing data transfers if the client requested only status mode when obtaining access to the device.

It is important to note that devices are typically opened in status mode for a relatively long time (for example, the event monitor watches for device events), while they are opened in data mode for a relatively short time (for example, to read in an image). Although the still image architecture allows only one client at a time to open a device in data mode, it might be necessary for a driver to place further restrictions on device access.

For instance, if you are writing a driver for a device connected to a serial port, you might want to call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) from within the driver's [**IStiUSD::LockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543829) method if the device was opened in status mode. This will prohibit other applications from using the port (which might be supporting other devices) while status information is being obtained from the device.

For devices connected to dedicated ports, such as SCSI or USB bus devices, it is typically allowable to call [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) from within [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) if status mode is specified, because the device and port will always be dedicated to one client.

When a device is opened in data mode, [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) is typically called from within **IStiUSD:Initialize**, independent of the bus type.

 

 




