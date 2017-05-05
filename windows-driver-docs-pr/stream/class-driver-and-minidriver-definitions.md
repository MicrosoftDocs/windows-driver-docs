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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Class%20Driver%20and%20Minidriver%20Definitions%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


