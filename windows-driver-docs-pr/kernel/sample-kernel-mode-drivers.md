---
title: Sample Kernel-Mode Drivers
author: windows-driver-content
description: Sample Kernel-Mode Drivers
ms.assetid: 09d08e07-e991-458f-aedf-018a0dd20af5
keywords: ["kernel-mode drivers WDK , samples", "sample drivers WDK kernel-mode"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sample Kernel-Mode Drivers


## <a href="" id="ddk-sample-kernel-mode-drivers-kg"></a>


The WDK provides various sample kernel-mode drivers. After you have installed the WDK, the src\\general subdirectory contains sample driver code that is applicable to all kernel-mode drivers. These samples include the following:

<a href="" id="toaster"></a>**toaster**  
Provides sample code for a set of drivers that conform to the [Windows Driver Model](windows-driver-model.md) (WDM). This sample also includes sample installation software.

<a href="" id="ioctl"></a>**ioctl**  
Demonstrates how drivers should support I/O control codes.

<a href="" id="event"></a>**event**  
Demonstrates techniques that kernel-mode drivers can use to notify applications of hardware events, if the application requests notification. One technique uses [event objects](event-objects.md) and the other relies on [queuing](queuing-and-dequeuing-irps.md) the notification request until an event occurs.

<a href="" id="cancel"></a>**cancel**  
Demonstrates the use of [cancel-safe IRP queues](cancel-safe-irp-queues.md).

<a href="" id="tracedrv"></a>**tracedrv**  
Shows how to use [WPP software tracing](https://msdn.microsoft.com/library/windows/hardware/ff556204).

Other subdirectories of the \\src directory contain sample code for kernel-mode drivers for various types of hardware.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sample%20Kernel-Mode%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


