---
title: Synchronizing Interrupt Code (UMDF 1)
description: Synchronizing Interrupt Code
ms.assetid: 5E2D0063-2251-40B3-8982-46001E67EB55
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Interrupt Code (UMDF 1)


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

All driver code that accesses the interrupt data buffer must be synchronized so that only one routine accesses the data at a time.

You can synchronize interrupt code by using either manual interrupt locking or automatic callback serialization.

## Manual Interrupt Locking


UMDF acquires the interrupt lock before calling the [*OnInterruptIsr*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr), [*OnInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_disable), or [*OnInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_enable) callbacks.

If a driver needs to synchronize any code using the interrupt lock, it calls [**IWDFInterrupt::AcquireInterruptLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-acquireinterruptlock) and [**IWDFInterrupt::ReleaseInterruptLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-releaseinterruptlock). For example, a driver acquires and releases the interrupt lock in its [*OnInterruptWorkItem*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_workitem) callback routine by using these methods. However, in I/O dispatch callbacks (such as [**OnRead**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackread-onread) and [**OnWrite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackwrite-onwrite)), the driver first calls [**IWDFInterrupt::TryToAcquireInterruptLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-trytoacquireinterruptlock) to decide whether to queue a work item or do the work in same thread to avoid potential deadlock. For an example of a deadlock scenario that can be caused by calling **IWDFInterrupt::AcquireInterruptLock** from an arbitrary thread context, see the Remarks section of [**IWDFInterrupt::AcquireInterruptLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-acquireinterruptlock).

If [**IWDFInterrupt::TryToAcquireInterruptLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-trytoacquireinterruptlock) returns **TRUE**, the driver has acquired the interrupt lock in the same thread. In this case, the driver performs the work that required that lock, and then calls [**ReleaseInterruptLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-releaseinterruptlock). If **IWDFInterrupt::TryToAcquireInterruptLock** returns **FALSE**, the driver queues a work item and performs the work in its [*OnWorkItem*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback. In this case, the work item must not use automatic serialization.

## Using Automatic Serialization


A UMDF driver can request automatic callback synchronization by calling [**IWDFDeviceInitialize::SetLockingConstraint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-setlockingconstraint) with the *LockType* parameter set to **WdfDeviceLevel**.

The driver then sets the **AutomaticSerialization** member of its [**WUDF\_INTERRUPT\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/ns-wudfinterrupt-_wudf_interrupt_config) structure to **TRUE** before calling [**CreateInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt).

As a result, UMDF serializes the driver's [*OnInterruptWorkItem*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_workitem) callbacks with I/O queue, request cancellation, and file object callback routines. In this scenario, UMDF uses the callback lock instead of a per-interrupt object lock.

 

 





