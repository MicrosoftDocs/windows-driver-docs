---
title: PTP Events
author: windows-driver-content
description: PTP Events
ms.assetid: 69bbe1e1-46e7-4615-93ff-ecd640e7d56b
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PTP Events


## <a href="" id="ddk-ptp-events-si"></a>


When an object is added or removed, including in response to the **StoreAdded** or **StoreRemoved** events (described in the PIMA 15740 standard), a WIA event is triggered. The WIA\_EVENT\_ITEM\_CREATED event is fired when an object is added, and the WIA\_EVENT\_ITEM\_DELETED event is fired when an object is removed. (See the Microsoft Windows SDK documentation for a description of these and other WIA event identifiers.) The PTP driver uses the other PTP events to update internal structures, but these events are not reported to applications. Note that the PTP driver monitors for events only while an application has the device open.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PTP%20Events%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


