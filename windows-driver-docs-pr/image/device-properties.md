---
title: Device Properties
author: windows-driver-content
description: Device Properties
ms.assetid: f41040c5-0eac-450d-b532-9165c543cc1a
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Properties


## <a href="" id="ddk-device-properties-si"></a>


All still image devices have specific characteristics that describe that device. For example, two characteristics of a flatbed scanner are its horizontal and vertical bed sizes. A possible characteristic of a digital still camera is its battery status, which indicates remaining battery life.

Similarly, data that the device produces or stores can also be described with characteristics. For example, the data produced by a scanner can be described by the number of pixels on a line and the number of bits per pixel.

In WIA, characteristics that describe both devices and data are referred to as *properties*. Properties exist in sets; the WIA minidriver maintains them in a WIA driver item.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Device%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


