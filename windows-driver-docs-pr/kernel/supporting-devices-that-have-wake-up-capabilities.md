---
title: Supporting Devices that Have Wake-Up Capabilities
author: windows-driver-content
description: Supporting Devices that Have Wake-Up Capabilities
ms.assetid: 70b9d0af-c3d7-44dc-b11a-3274391508c5
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "restoring power WDK kernel", "IRPs WDK power management", "wait/wake IRPs WDK power management", "I/O request packets WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Devices that Have Wake-Up Capabilities


## <a href="" id="ddk-supporting-devices-that-have-wake-up-capabilities-kg"></a>


Drivers for devices that can respond to external wake signals must be able to handle [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) requests (*wait/wake IRPs*). The power policy owner for such a device must be able to send an **IRP\_MN\_WAIT\_WAKE** request.

Typically, whatever causes the device to assert the wake signal is also a normal service event for the device. For example, user input, which might cause a keyboard to wake up the system, is a normal event for the keyboard and its drivers.

The first topic of this section, [Overview of Wait/Wake Operation](overview-of-wait-wake-operation.md), contains information useful in writing any driver. The following additional topics provide detailed information about handling and sending wait/wake IRPs:

[Receiving a Wait/Wake IRP](receiving-a-wait-wake-irp.md)

[Sending a Wait/Wake IRP](sending-a-wait-wake-irp.md)

[Canceling a Wait/Wake IRP](canceling-a-wait-wake-irp.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Supporting%20Devices%20that%20Have%20Wake-Up%20Capabilities%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


