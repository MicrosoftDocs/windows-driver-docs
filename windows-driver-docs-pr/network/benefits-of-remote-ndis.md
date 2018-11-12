---
title: Benefits of Remote NDIS
description: Benefits of Remote NDIS
ms.assetid: ca559f2e-c7e3-4b8e-a04d-f3a544d33a68
keywords:
- Remote NDIS WDK networking , advantages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Benefits of Remote NDIS





Remote NDIS is an extension of the well-understood and time-tested NDIS architecture. NDIS defines a function-call interface for device-specific NDIS miniport drivers. This interface defines primitives to send and receive network data, and to query and set configuration parameters and statistics. Remote NDIS leverages NDIS by defining a message wrapping for the NDIS miniport driver interface, thus moving the NDIS-handling code from a miniport driver into the device itself. In this and other ways, Remote NDIS allows for a wide range of device functionality and performance levels. The Remote NDIS model has many advantages:

-   Extensibility without change to the bus-specific message transport mechanisms

-   Ability to support more protocols over more buses in a short time

-   Driver architecture that has been proven for both networking and external bus device models

Value-added mechanisms that already exist in the NDIS network stack are supported for Remote NDIS devices.

 

 





