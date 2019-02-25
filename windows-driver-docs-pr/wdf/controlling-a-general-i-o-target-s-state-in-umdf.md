---
title: Controlling a General I/O Target's State in UMDF
description: Controlling a General I/O Target's State in UMDF
ms.assetid: 479487b2-5ce5-4522-b195-58ee50d210b6
keywords:
- general I/O targets WDK UMDF , states
- started I/O target state WDK UMDF
- stopped I/O target state WDK UMDF
- closed for query-remove state WDK UMDF
- closed I/O target state WDK UMDF
- deleted I/O target state WDK UMDF
- local I/O targets WDK UMDF
- remote I/O targets WDK UMDF
- stopping I/O targets
- restarting I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling a General I/O Target's State in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework defines the following states for general I/O targets:

<a href="" id="started"></a>**Started**  
The I/O target is open (that is, available to the UMDF driver) and the driver can send I/O requests to it. The framework delivers the requests to the appropriate driver.

<a href="" id="stopped"></a>**Stopped**  
The I/O target is open, but the UMDF driver cannot send I/O requests to the I/O target unless the driver passes the WDF\_REQUEST\_SEND\_OPTION\_IGNORE\_TARGET\_STATE flag to the *Flags* parameter in a call to the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method.

The framework stops delivering requests to the appropriate driver.

<a href="" id="closed-for-query-remove-------"></a>**Closed for Query-Remove**   
The I/O target is temporarily closed because its device might soon be removed.

<a href="" id="closed"></a>**Closed**  
The I/O target is closed and cannot be started or stopped.

<a href="" id="deleted"></a>**Deleted**  
The I/O target's device has been removed.

The [**WDF\_IO\_TARGET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff552390) enumeration defines the values that represent these states.

### Local I/O Target States

The framework automatically opens and starts local I/O targets.

If necessary, the driver can call [**IWDFIoTargetStateManagement::Stop**](https://msdn.microsoft.com/library/windows/hardware/ff559217) to temporarily stop a local I/O target and call [**IWDFIoTargetStateManagement::Start**](https://msdn.microsoft.com/library/windows/hardware/ff559213) to restart it. For example, the driver might stop a local I/O target if it detects a temporary error condition and then restart the I/O target if the error condition is corrected.

If a local I/O target's device is removed, the framework automatically stops and closes the I/O target and [cancels](canceling-i-o-requests.md) all I/O requests that are in the target's queue. The framework notifies the driver that the device is no longer available by calling device object event callback functions. For more information about these callback functions, see [PnP and Power Management Scenarios in UMDF](pnp-and-power-management-scenarios-in-umdf.md).

Drivers can call [**IWDFIoTargetStateManagement::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff559202) to obtain the current state of a local I/O target.

### Remote I/O Target States

Drivers must call [**IWDFRemoteTarget::OpenFileByName**](https://msdn.microsoft.com/library/windows/hardware/ff560273) or [**IWDFRemoteTarget::OpenRemoteInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560276) to open remote I/O targets. When a driver opens a remote I/O target, the framework automatically starts the I/O target.

If necessary, the driver can call [**IWDFRemoteTarget::Stop**](https://msdn.microsoft.com/library/windows/hardware/ff560289) to temporarily stop a remote I/O target and call [**IWDFRemoteTarget::Start**](https://msdn.microsoft.com/library/windows/hardware/ff560280) to restart it.

If a remote I/O target's device is removed, the framework automatically stops and closes the I/O target and cancels all I/O requests that are in the target's queue, unless the driver registers the following event callback functions:

<a href="" id="---------iremotetargetcallbackremoval--onremotetargetqueryremove--------"></a>[**IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove**](https://msdn.microsoft.com/library/windows/hardware/ff556897)  
Informs the driver that a remote I/O target's device might be removed. Your driver must call [**IWDFRemoteTarget::CloseForQueryRemove**](https://msdn.microsoft.com/library/windows/hardware/ff560259) if you want the driver to allow removal of the device.

<a href="" id="---------iremotetargetcallbackremoval--onremotetargetremovecomplete--------"></a>[**IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveComplete**](https://msdn.microsoft.com/library/windows/hardware/ff556900)  
Informs the driver that a remote I/O target's device has been removed. This callback function must call [**IWDFRemoteTarget::Close**](https://msdn.microsoft.com/library/windows/hardware/ff560253).

<a href="" id="---------iremotetargetcallbackremoval--onremotetargetremovecanceled--------"></a>[**IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled**](https://msdn.microsoft.com/library/windows/hardware/ff556899)  
Informs the driver that an attempt to remove a remote I/O target's device has been canceled. If you want the driver to continue to use the target, the driver must call [**IWDFRemoteTarget::Reopen**](https://msdn.microsoft.com/library/windows/hardware/ff560278). Typically, a driver calls **Reopen** from within the **OnRemoteTargetRemoveCanceled** callback function, but **Reopen** can instead be called after **OnRemoteTargetRemoveCanceled** returns.

Drivers can call [**IWDFRemoteTarget::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff560265) to obtain the current state of a remote I/O target.

 

 





