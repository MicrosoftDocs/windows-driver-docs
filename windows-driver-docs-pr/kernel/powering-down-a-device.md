---
title: Powering Down a Device
description: Powering Down a Device
ms.assetid: d2525e15-9590-4fc0-955c-ca3540c13375
keywords: ["device power downs WDK kernel", "powering down devices WDK kernel", "IRP_MN_REMOVE_DEVICE", "turning off devices WDK power management", "automatic power downs WDK kernel", "shutdown power management WDK kernel", "off power WDK kernel", "IRPs WDK power management", "surprise removals WDK power management", "device removals WDK power management", "removing devices", "I/O WDK power management", "unexpected device removal WDK power management", "idle detection WDK power management", "conserving power WDK kernel", "I/O request packets WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Powering Down a Device





Unless a device is enabled for wake-up, its drivers power it off when the system shuts down. Devices must always be powered off upon removal or surprise removal.

When a device is removed, the Plug and Play manager sends an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to the device stack. In response to this IRP, the drivers for the device should ensure that the device powers down. Powering down the device is an implicit part of removal handling; the device power policy owner is not required to send an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) for **PowerDeviceD3**.

As drivers handle the **IRP\_MN\_REMOVE\_DEVICE** request, they wait for pending I/O to complete, perform any necessary removal processing, call [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to notify the power manager that the device is in state D3, and delete the device objects they created for this device. Typically, the bus driver turns off power to the device.

If a device is unexpectedly removed from a Windows 2000 or later operating system, the Plug and Play manager sends an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request to the top of the corresponding device stack. In response to this IRP, the drivers for the device should perform surprise removal processing, as described in [Handling an IRP\_MN\_SURPRISE\_REMOVAL Request](handling-an-irp-mn-surprise-removal-request.md).

At system shutdown, the power manager sends an **IRP\_MN\_SET\_POWER** for a system power state (either S4 or S5). When the device power policy owner receives this IRP, it should send an **IRP\_MN\_SET\_POWER** for **PowerDeviceD3** so that lower drivers can finish their work and power down the device.

A driver can optionally perform idle detection for its device, or can request that the power manager perform idle detection, so that the device can be powered down when not in use. For further information, see [Detecting an Idle Device](detecting-an-idle-device.md).

 

 




