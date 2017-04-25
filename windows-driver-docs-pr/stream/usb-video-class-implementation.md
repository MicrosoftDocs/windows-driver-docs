---
title: USB Video Class Implementation
author: windows-driver-content
description: USB Video Class Implementation
ms.assetid: b390d741-9ddc-4bac-bca2-73e32461c5ed
keywords:
- USB Video Class drivers WDK AVStream , implementing
- Video Class drivers WDK USB , implementing
- UVC drivers WDK AVStream , implementing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USB Video Class Implementation


The Microsoft-provided USB Video Class driver (usbvideo.sys) is a pin-centric AVStream minidriver. It creates a filter factory for each USB Video Class?compliant device instance enumerated by the operating system. The driver also creates a pin factory for each input or output terminal on the device, with the **DataFlow** member of the [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure set to the relevant value.

The USB Video Class driver uses the internal device topology reported by the device descriptors to construct a kernel streaming (KS) topology graph comprised of filters, nodes, and connections.

Based on the number and types of controls supported by the device, USB Video Class dynamically reports filter, pin, and node property sets through the KS automation tables in the AVStream filter and pin descriptors.

Based on the data formats supported by each video or still image data endpoint on the device, USB Video Class reports the corresponding list of KS data ranges supported and a data intersection handler in the respective AVStream pin descriptor. The USB Video Class driver exports the information through the [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877) module.

The USB Video Class driver also supports audio/video stream synchronization; usbvideo.sys can serve as a KS master clock and add time stamps to video samples. The USB Video Class specification includes details about how the hardware should provide timing information to the class driver.

To communicate with USB Video Class, user-mode clients call DirectShow or Media Foundation interfaces. These interfaces are COM interface wrappers defined by the kernel streaming proxy as plug-ins. See the Microsoft Windows SDK documentation for more information about [Media Foundation](http://go.microsoft.com/fwlink/p/?linkid=144771).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USB%20Video%20Class%20Implementation%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


