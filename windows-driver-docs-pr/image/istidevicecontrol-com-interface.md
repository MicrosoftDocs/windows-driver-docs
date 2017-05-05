---
title: IStiDeviceControl COM Interface
author: windows-driver-content
description: IStiDeviceControl COM Interface
ms.assetid: 6d98f5d7-c471-4abb-8e69-dbac3d336c2f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IStiDeviceControl COM Interface


## <a href="" id="ddk-istidevicecontrol-com-interface-si"></a>


The **IStiDeviceControl** COM interface provides [User-Mode Still Image Minidrivers](overview-of-sti-components.md#ddk-user-mode-still-image-minidrivers-si) with access to information stored within the [Still Image Event Monitor](overview-of-sti-components.md#ddk-still-image-event-monitor-si). It also allows minidrivers to write information into the still image error log.

The methods defined by the **IStiDeviceControl** interface include the following:

<a href="" id="istidevicecontrol--addref"></a>[**IStiDeviceControl::AddRef**](https://msdn.microsoft.com/library/windows/hardware/ff542933)  
Increments the **IStiDeviceControl** interface's reference count.

<a href="" id="istidevicecontrol--getmydeviceopenmode"></a>[**IStiDeviceControl::GetMyDeviceOpenMode**](https://msdn.microsoft.com/library/windows/hardware/ff542942)  
Allows a still image minidriver to obtain the transfer mode that an application specified when it created an instance of a still image device.

<a href="" id="istidevicecontrol--getmydeviceportname"></a>[**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944)  
Allows a still image minidriver to obtain a device's port name.

<a href="" id="istidevicecontrol--release"></a>[**IStiDeviceControl::Release**](https://msdn.microsoft.com/library/windows/hardware/ff543725)  
Closes an instance COM object that defines the **IStiDeviceControl** interface, and removes access to the interface.

<a href="" id="istidevicecontrol--writetoerrorlog"></a>[**IStiDeviceControl::WriteToErrorLog**](https://msdn.microsoft.com/library/windows/hardware/ff543727)  
Allows a still image minidriver to write a message into the still image error log.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IStiDeviceControl%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


