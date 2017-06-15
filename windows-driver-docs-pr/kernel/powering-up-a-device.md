---
title: Powering Up a Device
author: windows-driver-content
description: Powering Up a Device
MS-HAID:
- 'PwrMgmt\_e8b355e0-2c93-4d26-af82-74d50dad3eb1.xml'
- 'kernel.powering\_up\_a\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 115cc904-922d-447e-b221-cb3e489dd08d
keywords: ["I/O WDK power management", "device power ups WDK kernel", "powering up devices WDK kernel", "IRP_MN_SET_POWER", "working state returns WDK power management", "turning on devices WDK power management", "automatic power ups WDK kernel", "on power WDK kernel", "IRPs WDK power management", "startup power management WDK kernel"]
---

# Powering Up a Device


## <a href="" id="ddk-powering-up-a-device-kg"></a>


When a bus driver handles a PnP [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request for one of its child devices, it should power on the device and call [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to report the device power state to the power manager. Powering on the device is an implicit part of device start-up. The device power policy owner does not send an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request for **PowerDeviceD0**, so drivers should not expect to receive these IRPs at start-up.

When a device has been powered down to conserve power, its drivers should power it up when an I/O request arrives. In this case, the device power policy owner must send an **IRP\_MN\_SET\_POWER** to return the device to the working state. When the IRP completes, the drivers for the device stop queuing I/O and begin to process requests off the queue.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Powering%20Up%20a%20Device%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


