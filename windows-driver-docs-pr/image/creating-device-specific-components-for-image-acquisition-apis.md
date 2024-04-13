---
title: Creating Device-Specific Components for Image Acquisition APIs
description: Creating Device-Specific Components for Image Acquisition APIs
ms.date: 04/20/2017
---

# Creating Device-Specific Components for Image Acquisition APIs





Image acquisition APIs, such as TWAIN, typically require device-specific components, such as TWAIN data sources. These device-specific components should use the [IStillImage COM Interface](istillimage-com-interface.md) and the [IStiDevice COM Interface](istidevice-com-interface.md) to communicate with user-mode still image device drivers and the event monitor.

Image acquisition APIs can call [**IStillImage::GetDeviceValue**](/previous-versions/windows/hardware/drivers/ff543786(v=vs.85)) and [**IStillImage::SetDeviceValue**](/previous-versions/windows/hardware/drivers/ff543801(v=vs.85)) to read and write [Registry Entries for Still Image Devices](registry-entries-for-still-image-devices.md). For example, the name of each still image device's TWAIN data source is stored in the registry.

Because the TWAIN API does not allow an application to specify the active device when calling a data source, the data source will typically call [**IStillImage::GetDeviceList**](/previous-versions/windows/hardware/drivers/ff543784(v=vs.85)) to obtain a list of all still image devices, and then will search the list to find the correct device, usually based on the manufacturer and model names. The manufacturer and model text names are obtained from the setup information (INF) file. Because TWAIN has a 32-character limit for data source names, and because WIA appends "WIA-" to strings to construct the compatible names, the text in the INF file should not be longer than 28 characters. Otherwise, TWAIN-compatible applications that perform a comparison on the entire string, and not just the first 32 characters, might not be able to automatically find the device that caused the application to launch.

To access a device, image acquisition software calls [**IStillImage::CreateDevice**](/previous-versions/windows/hardware/drivers/ff543778(v=vs.85)) to create an instance of the COM object that defines the **IStiDevice** interface. The **IStiDevice** interface provides several methods for performing device I/O operations. When creating the object instance, image acquisition software should specify the "data" [Transfer Modes](transfer-modes.md).

Image acquisition software can call [**IStiDevice::Subscribe**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-subscribe) to request the event monitor to deliver notification of [Still Image Device Events](still-image-device-events.md). Once notification is received, [**IStiDevice::GetLastNotificationData**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-getlastnotificationdata) can be called to determine the type of event. [**IStiDevice::UnSubscribe**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-unsubscribe) should be called when notifications are no longer needed.

When the image acquisition software has finished using the **IStiDevice** interface, it must call [**IStiDevice::Release**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-release).

 

