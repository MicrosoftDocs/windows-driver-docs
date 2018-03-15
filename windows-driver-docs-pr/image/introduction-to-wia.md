---
title: Introduction to WIA
author: windows-driver-content
description: Introduction to WIA
ms.assetid: 51674b06-f9d5-4e35-a2ec-9d6cc0a09ef3
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to WIA


## <a href="" id="ddk-introduction-to-wia-si"></a>


The Microsoft Windows Image Acquisition (WIA) interface is both an application programming interface (API) and a device driver interface (DDI). The WIA API is designed to allow applications to:

-   Run in a robust and stable environment.

-   Minimize interoperability problems.

-   Enumerate available image acquisition devices.

-   Create connections to multiple devices simultaneously.

-   Query properties of devices in a standard and expandable manner.

-   Acquire device data using standard and high performance transfer mechanisms.

-   Maintain image properties across data transfers.

-   Be notified of a wide variety of device events.

The WIA DDI is designed to minimize the amount of code a hardware vendor must write, while maintaining the flexibility to craft individual solutions. This is accomplished by:

-   Providing a standard device service library that performs most driver operations.

-   Promoting industry device communications standards, such as the Picture Transfer Protocol (PTP), so that one WIA driver supports most WIA devices.

This section presents a brief overview of WIA in the following areas:

[WIA Architecture Overview](wia-architecture-overview.md)

[WIA Core Components](wia-core-components.md)

 

 




