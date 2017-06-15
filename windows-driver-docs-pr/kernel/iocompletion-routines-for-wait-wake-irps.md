---
title: IoCompletion Routines for Wait/Wake IRPs
author: windows-driver-content
description: IoCompletion Routines for Wait/Wake IRPs
MS-HAID:
- 'PwrMgmt\_14bd319a-74a6-4c8e-a54d-cb90cde06031.xml'
- 'kernel.iocompletion\_routines\_for\_wait\_wake\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 61239398-2d37-4163-8128-7a4a0916a262
keywords: ["receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving", "IoCompletion routines"]
---

# IoCompletion Routines for Wait/Wake IRPs


## <a href="" id="ddk-iocompletion-routines-for-wait-wake-irps-kg"></a>


The I/O manager calls a driver's wait/wake [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine after the next-lower driver in the device stack has completed the wait/wake IRP. Each function and filter (FDO) driver that handles a wait/wake IRP should set an *IoCompletion* routine for the IRP.

Each function or filter driver sets an *IoCompletion* routine as it handles the wait/wake IRP on its way down the device stack. The device power policy owner, which sends the IRP, might therefore have an *IoCompletion* routine in addition to a callback routine. Keep in mind that the callback routine is invoked after the *IoCompletion* routine and that the two have different requirements. For more information, see [Wait/Wake Callback Routines](wait-wake-callback-routines.md).

The actions required in a wait/wake *IoCompletion* routine depend on the device and the type of driver. The following are some actions a driver might need to perform in its wait/wake *IoCompletion* routine:

1.  Reset any relevant fields in the device extension. For example, when a wait/wake IRP is pending, most drivers set a flag and keep a pointer to the IRP in the device extension.

2.  Reset the [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine, if any, for the IRP by calling [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674), specifying a **NULL** pointer for the routine.

3.  Call **IoCompleteRequest**, specifying IO\_NO\_INCREMENT, to complete the IRP.

As each successive driver completes the IRP, the I/O manager passes control to the *IoCompletion* routine of the next-higher driver going back up the stack.

After calling the *IoCompletion* routines set by drivers as they passed the wait/wake IRP down the device stack, the I/O manager calls the callback routine passed to [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) by the driver that sent the IRP. For further information, see [Wait/Wake Callback Routines](wait-wake-callback-routines.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IoCompletion%20Routines%20for%20Wait/Wake%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


