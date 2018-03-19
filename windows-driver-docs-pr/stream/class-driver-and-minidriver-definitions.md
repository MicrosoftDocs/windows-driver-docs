---
title: Class Driver and Minidriver Definitions
author: windows-driver-content
description: Class Driver and Minidriver Definitions
ms.assetid: eb428e8b-0c47-4843-8770-c22088ba5c6c
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , class driver/minidriver relationship
- streaming minidrivers WDK Windows 2000 Kernel , class driver/minidriver relationship
- minidrivers WDK Windows 2000 Kernel Streaming , class driver/minidriver relationship
- class driver/minidriver relationship WDK streaming minidriver
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Class Driver and Minidriver Definitions


## <a href="" id="ddk-class-driver-and-minidriver-definitions-ksg"></a>


A Microsoft-provided class driver is an intermediate driver designed to provide a simple interface between a vendor-written minidriver and the operating system. A minidriver is a hardware-specific DLL that uses a Microsoft-provided class driver to accomplish most actions through function calls, and provides only device-specific controls.

Under WDM, the minidriver registers its associated hardware adapters with the class driver, and the class driver creates a file object to represent each adapter that registers. The minidriver uses the class driver's device object to make system calls. The class driver is accessed by user-mode clients through WDM Streaming.

The interactions between class driver and minidriver include:

-   The minidriver does not create a device object, but shares the class driver's device object as necessary. This saves system resources.

-   Only one device object is created per adapter. Multiple subdevices (called *streams*) supported by the adapter are represented by WDM Streaming pins.

 

 




