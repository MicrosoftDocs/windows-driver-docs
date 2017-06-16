---
title: Power IRPs for Individual Devices
author: windows-driver-content
description: Power IRPs for Individual Devices
ms.assetid: a8d5db12-8f6b-4c65-9814-0bc3e476dd1c
keywords: ["power IRPs WDK kernel , devices", "device power IRPs WDK kernel", "power sequence values WDK kernel", "working state returns WDK power management", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Power IRPs for Individual Devices


## <a href="" id="ddk-power-irps-for-individual-devices-kg"></a>


A *device power IRP* specifies major IRP code [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784), one of the minor power IRP codes listed below, and the value **DevicePowerState** in the **Power.Type** member.

[**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)

[**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)

[**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766)

[**IRP\_MN\_POWER\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff551644)

All drivers in a device stack receive such IRPs; normally, only the device power policy manager can send these IRPs. However, the power manager can send a device power IRP when performing idle detection on behalf of a device, as explained in [Using Power Manager Routines for Idle Detection](using-power-manager-routines-for-idle-detection.md).

A driver sends a device power IRP for any of the following reasons:

-   To query or change the device power state in response to a system power IRP

-   To put the device in a sleep state to conserve power

-   To return the device to the working state after it has been asleep

-   To enable the device to awaken in response to an external signal

-   To get a power sequence value when powering up a device

The following figure shows the sequence of steps that occur to send, forward, and complete a device power IRP.

![diagram illustrating the path of a device power irp](images/devpoirp.png)

As the previous figure shows, a device power IRP is sent, forwarded, and completed in the following steps:

1.  The device power policy owner calls [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to allocate a device power IRP, specifying the PDO that is the target of the IRP and a callback routine to be invoked when the IRP is complete.

2.  The power manager allocates a device power IRP and sends it to the top driver in the device stack for the target PDO.

3.  The driver performs the following actions:

    -   Sets an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine if one is necessary.

    -   Calls [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) (Windows Server 2003, Windows XP, and Windows 2000) if a completion routine is not used. Beginning with Windows Vista, this call is not required and such a call performs no power management operation.

    -   Calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (Windows 7 and Windows Vista) or calls [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (Windows Server 2003, Windows XP, and Windows 2000) to pass the IRP down to the next-lower driver.

    Each driver in the stack does this until the IRP reaches the bus driver. If a driver must fail the IRP, it should do so immediately and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

4.  The bus driver, which maintains the device PDO, performs the requested action, and then calls **IoCompleteRequest** to complete the IRP. A bus driver can fail a device power-up IRP if a device is removed or in the process of being removed.

5.  The I/O manager calls *IoCompletion* routines that were set by drivers as they passed the IRP down the stack. After all the *IoCompletion* routines have been called, the callback routine is run.

For more information about device power IRPs, see [Managing Power for Individual Devices](managing-power-for-individual-devices.md) and [Supporting Devices that Have Wake-Up Capabilities](supporting-devices-that-have-wake-up-capabilities.md). For details on the power sequence IRP, see [**IRP\_MN\_POWER\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff551644).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Power%20IRPs%20for%20Individual%20Devices%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


