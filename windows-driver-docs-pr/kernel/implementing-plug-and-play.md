---
title: Implementing Plug and Play
author: windows-driver-content
description: Implementing Plug and Play
ms.assetid: ebd3aaa2-a701-41f3-88ff-2a6bdf7bd7cb
keywords: ["PnP WDK kernel", "Plug and Play WDK kernel", "kernel-mode drivers WDK , Plug and Play", "hardware configuration changes WDK PnP", "resource allocations WDK PnP", "hardware resource allocations WDK PnP", "automatic resource allocations WDK PnP", "dynamic resource allocations WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implementing Plug and Play


## <a href="" id="ddk-plug-and-play-kg"></a>


This section describes Plug and Play (PnP) concepts and operating system components, and explains how to support PnP capabilities of device hardware in kernel-mode drivers. The section contains the following topics:

[Introduction to Plug and Play](introduction-to-plug-and-play.md)

[Adding a PnP Device to a Running System](adding-a-pnp-device-to-a-running-system.md)

[Passing PnP IRPs Down the Device Stack](passing-pnp-irps-down-the-device-stack.md)

[Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md)

[Starting a Device](starting-a-device.md)

[Stopping a Device](stopping-a-device.md)

[Removing a Device](removing-a-device.md)

[Using PnP Notification](using-pnp-notification.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Implementing%20Plug%20and%20Play%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


