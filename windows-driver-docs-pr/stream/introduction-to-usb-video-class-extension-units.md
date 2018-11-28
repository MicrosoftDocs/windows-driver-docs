---
title: Introduction to USB Video Class Extension Units
description: Introduction to USB Video Class Extension Units
ms.assetid: a46feb97-771e-4efd-872e-4a4b0fb3b705
keywords:
- extension units WDK USB Video Class , about extension units
- USB Video Class drivers WDK AVStream , about extension units
- Video Class drivers WDK USB , extension units, about
- UVC drivers WDK AVStream , extension units, about
- extension units WDK USB Video Class , about
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to USB Video Class Extension Units


The *USB Video Class* specification defines a mechanism to extend the functionality of devices that comply with that specification and describes the behavior of Extension Units. Independent hardware vendors (IHVs) can enhance the value of their devices by adding functionality that goes beyond that described in the specification.

This extension mechanism requires operating system support and some user-mode plug-ins so that applications can work with these extensions. The USB Video Class driver architecture provides such a mechanism so that IHVs can expose extended device functionality as COM APIs. This documentation describes the steps required to create and register such a plug-in.

### SDK Information

IKsTopologyInfo, ISelector and IKsNodeControl are defined in Vidcap.h.

In Windows Vista and later releases, Vidcap.h is included as part of the Microsoft Windows SDK.

The Microsoft DirectShow documentation contains the corresponding reference pages. Globally unique identifier (GUID) types and some other USB-video-related constants are defined in Ksmedia.h. For more information, see [USB Video Class Properties](usb-video-class-properties.md) and [Kernel Streaming Topology Nodes](https://msdn.microsoft.com/library/windows/hardware/ff560886).

 

 




