---
title: Synchronizing Interrupt Code
author: windows-driver-content
description: Synchronizing Interrupt Code
ms.assetid: 5E2D0063-2251-40B3-8982-46001E67EB55
---

# Synchronizing Interrupt Code


\[This topic applies to UMDF 1.*x*.\]

All driver code that accesses the interrupt data buffer must be synchronized so that only one routine accesses the data at a time.

You can synchronize interrupt code by using either manual interrupt locking or automatic callback serialization.

## Manual Interrupt Locking


UMDF acquires the interrupt lock before calling the [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902), [*OnInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/hh463895), or [*OnInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/hh463899) callbacks.

If a driver needs to synchronize any code using the interrupt lock, it calls [**IWDFInterrupt::AcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh451289) and [**IWDFInterrupt::ReleaseInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh451319). For example, a driver acquires and releases the interrupt lock in its [*OnInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463905) callback routine by using these methods. However, in I/O dispatch callbacks (such as [**OnRead**](https://msdn.microsoft.com/library/windows/hardware/ff556875) and [**OnWrite**](https://msdn.microsoft.com/library/windows/hardware/ff556885)), the driver first calls [**IWDFInterrupt::TryToAcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh451332) to decide whether to queue a work item or do the work in same thread to avoid potential deadlock. For an example of a deadlock scenario that can be caused by calling **IWDFInterrupt::AcquireInterruptLock** from an arbitrary thread context, see the Remarks section of [**IWDFInterrupt::AcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh451289).

If [**IWDFInterrupt::TryToAcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh451332) returns **TRUE**, the driver has acquired the interrupt lock in the same thread. In this case, the driver performs the work that required that lock, and then calls [**ReleaseInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh451319). If **IWDFInterrupt::TryToAcquireInterruptLock** returns **FALSE**, the driver queues a work item and performs the work in its [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback. In this case, the work item must not use automatic serialization.

## Using Automatic Serialization


A UMDF driver can request automatic callback synchronization by calling [**IWDFDeviceInitialize::SetLockingConstraint**](https://msdn.microsoft.com/library/windows/hardware/ff556991) with the *LockType* parameter set to **WdfDeviceLevel**.

The driver then sets the **AutomaticSerialization** member of its [**WUDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/hh464084) structure to **TRUE** before calling [**CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208).

As a result, UMDF serializes the driver's [*OnInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463905) callbacks with I/O queue, request cancellation, and file object callback routines. In this scenario, UMDF uses the callback lock instead of a per-interrupt object lock.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Synchronizing%20Interrupt%20Code%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




