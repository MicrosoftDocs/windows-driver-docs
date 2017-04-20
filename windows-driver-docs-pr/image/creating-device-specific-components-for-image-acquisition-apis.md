---
title: Creating Device-Specific Components for Image Acquisition APIs
author: windows-driver-content
description: Creating Device-Specific Components for Image Acquisition APIs
ms.assetid: c4906dec-6d34-47f5-abde-0513c4499a66
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Device-Specific Components for Image Acquisition APIs


## <a href="" id="ddk-creating-device-specific-components-for-image-acquisition-apis-si"></a>


Image acquisition APIs, such as TWAIN, typically require device-specific components, such as TWAIN data sources. These device-specific components should use the [IStillImage COM Interface](istillimage-com-interface.md) and the [IStiDevice COM Interface](istidevice-com-interface.md) to communicate with user-mode still image device drivers and the event monitor.

Image acquisition APIs can call [**IStillImage::GetDeviceValue**](https://msdn.microsoft.com/library/windows/hardware/ff543786) and [**IStillImage::SetDeviceValue**](https://msdn.microsoft.com/library/windows/hardware/ff543801) to read and write [Registry Entries for Still Image Devices](registry-entries-for-still-image-devices.md). For example, the name of each still image device's TWAIN data source is stored in the registry.

Because the TWAIN API does not allow an application to specify the active device when calling a data source, the data source will typically call [**IStillImage::GetDeviceList**](https://msdn.microsoft.com/library/windows/hardware/ff543784) to obtain a list of all still image devices, and then will search the list to find the correct device, usually based on the manufacturer and model names. The manufacturer and model text names are obtained from the setup information (INF) file. Because TWAIN has a 32-character limit for data source names, and because WIA appends "WIA-" to strings to construct the compatible names, the text in the INF file should not be longer than 28 characters. Otherwise, TWAIN-compatible applications that perform a comparison on the entire string, and not just the first 32 characters, might not be able to automatically find the device that caused the application to launch.

To access a device, image acquisition software calls [**IStillImage::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543778) to create an instance of the COM object that defines the **IStiDevice** interface. The **IStiDevice** interface provides several methods for performing device I/O operations. When creating the object instance, image acquisition software should specify the "data" [Transfer Modes](transfer-modes.md).

Image acquisition software can call [**IStiDevice::Subscribe**](https://msdn.microsoft.com/library/windows/hardware/ff543768) to request the event monitor to deliver notification of [Still Image Device Events](still-image-device-events.md). Once notification is received, [**IStiDevice::GetLastNotificationData**](https://msdn.microsoft.com/library/windows/hardware/ff543751) can be called to determine the type of event. [**IStiDevice::UnSubscribe**](https://msdn.microsoft.com/library/windows/hardware/ff543773) should be called when notifications are no longer needed.

When the image acquisition software has finished using the **IStiDevice** interface, it must call [**IStiDevice::Release**](https://msdn.microsoft.com/library/windows/hardware/ff543765).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Creating%20Device-Specific%20Components%20for%20Image%20Acquisition%20APIs%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


