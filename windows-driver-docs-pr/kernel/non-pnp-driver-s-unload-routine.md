---
title: Non-PnP Driver's Unload Routine
author: windows-driver-content
description: Non-PnP Driver's Unload Routine
MS-HAID:
- 'DrvComps\_1336eec0-f8ad-43a9-b1f4-e0c0e7721b97.xml'
- 'kernel.non\_pnp\_driver\_s\_unload\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5917648f-1e7e-4b39-9aa6-d6cdaac7a2cd
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel"]
---

# Non-PnP Driver's Unload Routine


## <a href="" id="ddk-a-non-pnp-driver-s-unload-routine-kg"></a>


Earlier drivers and high-level file system drivers, which do not handle PnP device-removal requests, must release resources, delete device objects, and detach from the device stack in their [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routines.

If it has not done so already, the first thing a legacy device driver should do in its *Unload* routine is to disable interrupts from the device. Otherwise, its ISR might be called to handle a device interrupt while the *Unload* routine is releasing resources in the device extension that the ISR needs to handle the interrupt. Even if its ISR runs successfully in these circumstances, the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine that the ISR queues, and possibly other driver routines that run at IRQL &gt;= DISPATCH\_LEVEL, will execute before the *Unload* routine regains control, thereby increasing the likelihood that the *Unload* routine has deleted a resource that another driver routine references. See [Managing Hardware Priorities](managing-hardware-priorities.md) for more information.

After disabling interrupts, file system and legacy drivers must release resources and objects. For details, see the following two sections:

[Releasing Driver-Allocated Resources](releasing-driver-allocated-resources.md)

[Releasing Device and Controller Objects](releasing-device-and-controller-objects.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Non-PnP%20Driver's%20Unload%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


