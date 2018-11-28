---
title: Creating Device-Specific Components for Image Acquisition APIs
description: Creating Device-Specific Components for Image Acquisition APIs
ms.assetid: c4906dec-6d34-47f5-abde-0513c4499a66
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Device-Specific Components for Image Acquisition APIs





Image acquisition APIs, such as TWAIN, typically require device-specific components, such as TWAIN data sources. These device-specific components should use the [IStillImage COM Interface](istillimage-com-interface.md) and the [IStiDevice COM Interface](istidevice-com-interface.md) to communicate with user-mode still image device drivers and the event monitor.

Image acquisition APIs can call [**IStillImage::GetDeviceValue**](https://msdn.microsoft.com/library/windows/hardware/ff543786) and [**IStillImage::SetDeviceValue**](https://msdn.microsoft.com/library/windows/hardware/ff543801) to read and write [Registry Entries for Still Image Devices](registry-entries-for-still-image-devices.md). For example, the name of each still image device's TWAIN data source is stored in the registry.

Because the TWAIN API does not allow an application to specify the active device when calling a data source, the data source will typically call [**IStillImage::GetDeviceList**](https://msdn.microsoft.com/library/windows/hardware/ff543784) to obtain a list of all still image devices, and then will search the list to find the correct device, usually based on the manufacturer and model names. The manufacturer and model text names are obtained from the setup information (INF) file. Because TWAIN has a 32-character limit for data source names, and because WIA appends "WIA-" to strings to construct the compatible names, the text in the INF file should not be longer than 28 characters. Otherwise, TWAIN-compatible applications that perform a comparison on the entire string, and not just the first 32 characters, might not be able to automatically find the device that caused the application to launch.

To access a device, image acquisition software calls [**IStillImage::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543778) to create an instance of the COM object that defines the **IStiDevice** interface. The **IStiDevice** interface provides several methods for performing device I/O operations. When creating the object instance, image acquisition software should specify the "data" [Transfer Modes](transfer-modes.md).

Image acquisition software can call [**IStiDevice::Subscribe**](https://msdn.microsoft.com/library/windows/hardware/ff543768) to request the event monitor to deliver notification of [Still Image Device Events](still-image-device-events.md). Once notification is received, [**IStiDevice::GetLastNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543751) can be called to determine the type of event. [**IStiDevice::UnSubscribe**](https://msdn.microsoft.com/library/windows/hardware/ff543773) should be called when notifications are no longer needed.

When the image acquisition software has finished using the **IStiDevice** interface, it must call [**IStiDevice::Release**](https://msdn.microsoft.com/library/windows/hardware/ff543765).

 

 




