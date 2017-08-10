---
title: Rules for Handling Power IRPs
author: windows-driver-content
description: Rules for Handling Power IRPs
ms.assetid: ea4a1c57-6184-4160-bf23-b86e3e403388
keywords: ["power management WDK kernel , IRPs", "IRPs WDK power management", "power IRPs WDK kernel", "power IRPs WDK kernel , rules", "I/O request packets WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Rules for Handling Power IRPs


## <a href="" id="ddk-rules-for-handling-power-irps-kg"></a>


Drivers that support power management must conform to certain rules pertaining to:

[Calling IoCallDriver versus calling PoCallDriver](calling-iocalldriver-versus-calling-pocalldriver.md) to pass power IRPs

[Calling PoStartNextPowerIrp](calling-postartnextpowerirp.md) to start the next power IRP

[Passing power IRPs](passing-power-irps.md) down to the next-lower driver

[Queuing I/O requests while a device is sleeping](queuing-i-o-requests-while-a-device-is-sleeping.md)

[Handling unsupported or unrecognized power IRPs](handling-unsupported-or-unrecognized-power-irps.md)

[Calling ExSetTimerResolution while processing a power IRP](calling-exsettimerresolution-while-processing-a-power-irp.md)

The sections that follow describe how drivers should perform these tasks.

For a list of power management IRPs, see [Power Management Minor IRPs](power-management-minor-irps.md) .

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Rules%20for%20Handling%20Power%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


