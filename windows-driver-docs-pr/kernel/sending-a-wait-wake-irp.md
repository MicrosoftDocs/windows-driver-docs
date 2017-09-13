---
title: Sending a Wait/Wake IRP
author: windows-driver-content
description: Sending a Wait/Wake IRP
ms.assetid: ed582644-af51-4841-be59-6a3deb6d9de5
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "wait/wake IRPs WDK power management , sending", "sending wait/wake IRPs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sending a Wait/Wake IRP


## <a href="" id="ddk-sending-a-wait-wake-irp-kg"></a>


The minor power IRP code [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) provides for waking a device or waking the system. Drivers of devices that can wake themselves or the system send **IRP\_MN\_WAIT\_WAKE** requests. The system sends **IRP\_MN\_WAIT\_WAKE** requests only to devices that always wake the system, such as the power-on switch.

A driver sends an **IRP\_MN\_WAIT\_WAKE** request for one of two reasons:

1.  Its device must be able to return to the working state from a sleep state in response to an external wake-up signal.

    For example, a modem's driver might send it a wait/wake IRP before setting it in power state D1 to conserve energy. The wait/wake IRP enables the modem to respond to an incoming call.

2.  Its device must be able to wake the system in response to a wake-up signal.

    When the system goes to sleep, the modem might remain in state D1 with an **IRP\_MN\_WAIT\_WAKE** pending. In this case, an incoming call would wake the system as well as the modem.

Whether a device is prepared to wake itself or the system, the actions its drivers must take are the same. The primary difference lies in how the device and system hardware respond to the initial wake-up signal. Driver behavior is the same in either case.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sending%20a%20Wait/Wake%20IRP%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


