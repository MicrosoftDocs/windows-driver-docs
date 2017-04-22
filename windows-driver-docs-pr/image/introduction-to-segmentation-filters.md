---
title: Introduction to Segmentation Filters
author: windows-driver-content
description: Introduction to Segmentation Filters
ms.assetid: 3f73aa08-c3ef-4e97-9e3e-a1f0325cd599
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Segmentation Filters


## <a href="" id="ddk-introduction-to-segmentation-filters-si"></a>


A segmentation filter is a WIA extension that can be used by an application to separate the individual pictures laid out on a flatbed scanner, so each of these pictures can be acquired into individual images. The segmentation filter is an in-process COM component running in the application's process.

A segmentation filter is dependent on the driver that it extends. Driver developers can choose to write their own segmentation filter or use the segmentation filter that Microsoft provides beginning with Windows Vista.

The segmentation filter can only be used by applications that support the [IStream based WIA transfer model](wia-transfer-architecture.md).

The following figure shows the segmentation filter component running in the application's process.

![diagram illustrating a segmentation filter component running in an application's process](images/wia-components-app-process.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Introduction%20to%20Segmentation%20Filters%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


