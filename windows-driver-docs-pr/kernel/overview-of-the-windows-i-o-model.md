---
title: Overview of the Windows I/O Model
description: Overview of the Windows I/O Model
ms.assetid: 17a012b7-946e-4f42-8d80-e270bc26de06
keywords: ["IRPs WDK kernel , about Windows I/O model", "Windows I/O model WDK", "I/O WDK kernel , model"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Overview of the Windows I/O Model





Every operating system has an implicit or explicit I/O model for handling the flow of data to and from peripheral devices. One feature of the Microsoft Windows I/O model is its support for asynchronous I/O. In addition, the I/O model has the following general features:

-   The I/O manager presents a consistent interface to all kernel-mode drivers, including lowest-level, intermediate, and file system drivers. All I/O requests to drivers are sent as I/O request packets (IRPs).

-   I/O operations are layered. The I/O manager exports I/O system services, which user-mode protected subsystems call to carry out I/O operations on behalf of their applications and/or end users. The I/O manager intercepts these calls, sets up one or more IRPs, and routes them through possibly layered drivers to physical devices.

-   The I/O manager defines a set of standard routines, some required and others optional, that drivers can support. All drivers follow a relatively consistent implementation model, given the differences among peripheral devices and the differing functionality required of bus, function, filter, and file system drivers.

-   Like the operating system itself, drivers are object-based. Drivers, their devices, and system hardware are represented as objects. The I/O manager and other operating system components export kernel-mode support routines that drivers can call to get work done by manipulating the appropriate objects.

In addition to using IRPs to convey traditional I/O requests, the I/O manager works with the PnP and power managers to send IRPs containing PnP and power requests.

 

 




