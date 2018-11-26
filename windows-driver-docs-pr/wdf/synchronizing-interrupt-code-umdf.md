---
title: Synchronizing Interrupt Code
description: Synchronizing Interrupt Code
ms.assetid: 5E2D0063-2251-40B3-8982-46001E67EB55
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Interrupt Code


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

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

 

 





