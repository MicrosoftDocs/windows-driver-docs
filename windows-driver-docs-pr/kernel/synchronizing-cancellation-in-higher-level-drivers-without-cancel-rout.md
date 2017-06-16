---
title: Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines
author: windows-driver-content
description: Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines
ms.assetid: 741d504e-7e61-4f60-a8cf-e4ea92f0654e
---

# Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines


## <a href="" id="ddk-synchronizing-cancellation-in-higher-level-drivers-without-cancel-"></a>


A higher-level driver can make no assumptions about whether or how existing lower-level drivers handle cancelable IRPs. As soon as any higher-level driver calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) for an IRP, it no longer owns that IRP and it can neither ascertain nor control processing of the IRP by lower-level drivers.

However, any higher-level driver can set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for an IRP by calling [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) before it calls **IoCallDriver**. The higher-level driver can determine whether any pending IRP is canceled in a lower driver by calling **IoSetCompletionRoutine** with the *InvokeOnCancel* parameter set to **TRUE** before it passes the IRP on to lower drivers. Doing so ensures that the driver's *IoCompletion* routine will be called whether the IRP is canceled or completed.

A higher-level driver can call [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) with any pending IRP that the driver has allocated. However, making this call does not ensure that the driver-allocated IRP will be completed with its I/O status block set to STATUS\_CANCELLED; another thread might already be completing the IRP. To check whether the IRP was canceled, the higher-level driver must call **IoSetCompletionRoutine** with the *InvokeOnCancel* parameter set to **TRUE** before passing the IRP on to the next lower driver. See [Completing IRPs](completing-irps.md) for more information about completion routines.

A higher-level driver must not call **IoCancelIrp** with an IRP that it did not allocate.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronizing%20Cancellation%20in%20Higher-Level%20Drivers%20without%20Cancel%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


