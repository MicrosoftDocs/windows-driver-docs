---
title: Using I/O Targets in UMDF
description: Using I/O Targets in UMDF
ms.assetid: 5633242c-ffab-4af5-9650-7449395deb6b
keywords:
- user-mode drivers WDK UMDF , I/O targets
- UMDF WDK , I/O targets
- User-Mode Driver Framework WDK , I/O targets
- framework-based drivers WDK UMDF , I/O targets
- I/O targets WDK UMDF
- targets WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using I/O Targets in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When a driver receives an I/O request, the driver might be able to process the request by itself, or it might require the assistance of other drivers. If the driver requires assistance, it can forward the request to another driver, or it can create one or more new requests and send them to another driver.

UMDF-based drivers use *I/O targets* to send I/O requests to another driver. Each I/O target is represented by an I/O target object. Each I/O target object is primarily a queue. When a driver sends a request to an I/O target, the framework stores the request in the queue until it can deliver the request to the I/O target.

The framework supports both general I/O targets and specialized I/O targets:

-   [General I/O targets](general-i-o-targets-in-umdf.md) can be used by all UMDF drivers, but they do not support any special, device-specific data formats.

-   Specialized I/O targets enable UMDF drivers to send I/O requests that require special, target-specific data formatting. Currently, the framework provides support for [USB I/O targets](usb-i-o-targets-in-umdf.md).

If the framework provides specialized I/O targets that support your device's data format, your driver should use the specialized I/O targets. Otherwise, the driver should use general I/O targets.

 

 





