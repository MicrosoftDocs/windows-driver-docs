---
title: Powering Down a Device
author: windows-driver-content
description: Powering Down a Device
ms.assetid: d2525e15-9590-4fc0-955c-ca3540c13375
keywords: ["device power downs WDK kernel", "powering down devices WDK kernel", "IRP_MN_REMOVE_DEVICE", "turning off devices WDK power management", "automatic power downs WDK kernel", "shutdown power management WDK kernel", "off power WDK kernel", "IRPs WDK power management", "surprise removals WDK power management", "device removals WDK power management", "removing devices", "I/O WDK power management", "unexpected device removal WDK power management", "idle detection WDK power management", "conserving power WDK kernel", "I/O request packets WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Powering Down a Device


## <a href="" id="ddk-powering-down-a-device-kg"></a>


Unless a device is enabled for wake-up, its drivers power it off when the system shuts down. Devices must always be powered off upon removal or surprise removal.

When a device is removed, the Plug and Play manager sends an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to the device stack. In response to this IRP, the drivers for the device should ensure that the device powers down. Powering down the device is an implicit part of removal handling; the device power policy owner is not required to send an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) for **PowerDeviceD3**.

As drivers handle the **IRP\_MN\_REMOVE\_DEVICE** request, they wait for pending I/O to complete, perform any necessary removal processing, call [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to notify the power manager that the device is in state D3, and delete the device objects they created for this device. Typically, the bus driver turns off power to the device.

If a device is unexpectedly removed from a Windows 2000 or later operating system, the Plug and Play manager sends an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request to the top of the corresponding device stack. In response to this IRP, the drivers for the device should perform surprise removal processing, as described in [Handling an IRP\_MN\_SURPRISE\_REMOVAL Request](handling-an-irp-mn-surprise-removal-request.md).

At system shutdown, the power manager sends an **IRP\_MN\_SET\_POWER** for a system power state (either S4 or S5). When the device power policy owner receives this IRP, it should send an **IRP\_MN\_SET\_POWER** for **PowerDeviceD3** so that lower drivers can finish their work and power down the device.

A driver can optionally perform idle detection for its device, or can request that the power manager perform idle detection, so that the device can be powered down when not in use. For further information, see [Detecting an Idle Device](detecting-an-idle-device.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Powering%20Down%20a%20Device%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


