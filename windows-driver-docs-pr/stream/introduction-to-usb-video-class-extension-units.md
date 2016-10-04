---
title: Introduction to USB Video Class Extension Units
author: windows-driver-content
description: Introduction to USB Video Class Extension Units
MS-HAID:
- 'uvcds\_6a1bfae4-966f-4caf-b6c7-6552321be23f.xml'
- 'stream.introduction\_to\_usb\_video\_class\_extension\_units'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a46feb97-771e-4efd-872e-4a4b0fb3b705
keywords: ["extension units WDK USB Video Class , about extension units", "USB Video Class drivers WDK AVStream , about extension units", "Video Class drivers WDK USB , extension units, about", "UVC drivers WDK AVStream , extension units, about", "extension units WDK USB Video Class , about"]
---

# Introduction to USB Video Class Extension Units


The *USB Video Class* specification defines a mechanism to extend the functionality of devices that comply with that specification and describes the behavior of Extension Units. Independent hardware vendors (IHVs) can enhance the value of their devices by adding functionality that goes beyond that described in the specification.

This extension mechanism requires operating system support and some user-mode plug-ins so that applications can work with these extensions. The USB Video Class driver architecture provides such a mechanism so that IHVs can expose extended device functionality as COM APIs. This documentation describes the steps required to create and register such a plug-in.

### SDK Information

IKsTopologyInfo, ISelector and IKsNodeControl are defined in Vidcap.h.

In Windows Vista and later releases, Vidcap.h is included as part of the Microsoft Windows SDK.

The Microsoft DirectShow documentation contains the corresponding reference pages. Globally unique identifier (GUID) types and some other USB-video-related constants are defined in Ksmedia.h. For more information, see [USB Video Class Properties](usb-video-class-properties.md) and [Kernel Streaming Topology Nodes](https://msdn.microsoft.com/library/windows/hardware/ff560886).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Introduction%20to%20USB%20Video%20Class%20Extension%20Units%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


