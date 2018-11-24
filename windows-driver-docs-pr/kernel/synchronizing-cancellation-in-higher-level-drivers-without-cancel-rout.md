---
title: Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines
description: Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines
ms.assetid: 741d504e-7e61-4f60-a8cf-e4ea92f0654e
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines





A higher-level driver can make no assumptions about whether or how existing lower-level drivers handle cancelable IRPs. As soon as any higher-level driver calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) for an IRP, it no longer owns that IRP and it can neither ascertain nor control processing of the IRP by lower-level drivers.

However, any higher-level driver can set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for an IRP by calling [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) before it calls **IoCallDriver**. The higher-level driver can determine whether any pending IRP is canceled in a lower driver by calling **IoSetCompletionRoutine** with the *InvokeOnCancel* parameter set to **TRUE** before it passes the IRP on to lower drivers. Doing so ensures that the driver's *IoCompletion* routine will be called whether the IRP is canceled or completed.

A higher-level driver can call [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) with any pending IRP that the driver has allocated. However, making this call does not ensure that the driver-allocated IRP will be completed with its I/O status block set to STATUS\_CANCELLED; another thread might already be completing the IRP. To check whether the IRP was canceled, the higher-level driver must call **IoSetCompletionRoutine** with the *InvokeOnCancel* parameter set to **TRUE** before passing the IRP on to the next lower driver. See [Completing IRPs](completing-irps.md) for more information about completion routines.

A higher-level driver must not call **IoCancelIrp** with an IRP that it did not allocate.

 

 




