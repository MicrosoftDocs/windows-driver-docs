---
title: Controlling a General I/O Target's State
description: Controlling a General I/O Target's State
ms.assetid: 37f756bf-b655-428e-b72c-f86c71f1a2db
keywords:
- general I/O targets WDK KMDF , states
- started I/O target state WDK KMDF
- stopped I/O target state WDK KMDF
- closed for query-remove state WDK KMDF
- closed I/O target state WDK KMDF
- deleted I/O target state WDK KMDF
- local I/O targets WDK KMDF
- remote I/O targets WDK KMDF
- stopping I/O targets WDK KMDF
- restarting I/O targets WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling a General I/O Target's State


You can visualize I/O target objects as having two gates: an in-gate and an out-gate. The out-gate controls when the framework delivers a request to the target device object, while the in-gate controls when a request is allowed to enter the I/O target at all.

The framework defines the following states for general I/O targets:

<a href="" id="started"></a>*Started*  
Both gates of the I/O target object are open. The driver can send I/O requests to the I/O target queue, and the framework delivers the requests to the appropriate driver.

<a href="" id="stopped"></a>*Stopped*  
The in-gate of the I/O target is open, but the out-gate is closed. The framework stops delivering requests to the appropriate driver. To send I/O requests to the I/O target, the driver must set either **WDF\_REQUEST\_SEND\_OPTION\_IGNORE\_TARGET\_STATE** or **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET** in each request's [**WDF\_REQUEST\_SEND\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff552491) structure.

<a href="" id="purged"></a>*Purged*  
Both gates of the I/O target object are closed. The driver cannot send I/O requests to the I/O target unless it sets **WDF\_REQUEST\_SEND\_OPTION\_IGNORE\_TARGET\_STATE** or **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET**. In addition, the framework cancels unprocessed requests in the I/O target object's internal queue. This state is available beginning in KMDF version 1.11.

<a href="" id="closed-for-query-remove"></a>*Closed for Query-Remove*  
A remote I/O target is temporarily closed because its device might soon be removed.

<a href="" id="closed"></a>*Closed*  
The I/O target is closed and cannot be started or stopped.

<a href="" id="deleted"></a>*Deleted*  
The I/O target's device has been removed.

The [**WDF\_IO\_TARGET\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff552390) enumeration defines the values that represent these states. Your driver can call [**WdfIoTargetGetState**](https://msdn.microsoft.com/library/windows/hardware/ff548631) to obtain an I/O target's state.

### Local I/O Target States

The framework automatically opens and starts local I/O targets.

If necessary, the driver can call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) to temporarily stop a local I/O target and call [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677) to restart it. For example, the driver might stop a local I/O target if it detects a temporary error condition and then restart the I/O target if the error condition is corrected.

In KMDF version 1.11 and later, the driver can call [**WdfIoTargetPurge**](https://msdn.microsoft.com/library/windows/hardware/hh439338) to temporarily prevent I/O requests from being sent to a local I/O target, and to cancel unprocessed requests in the target's queue. For example, as part of file handle cleanup, a driver might purge a local I/O target to ensure that all requests sent to the driver are cancelled.

If a local I/O target's device is removed, the framework automatically stops and closes the I/O target and [cancels](canceling-i-o-requests.md) all I/O requests that are in the target's queue. The framework notifies the driver that the device is no longer available by calling device object event callback functions. For more information about these callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

### Remote I/O Target States

Drivers must call [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634) to open remote I/O targets. When a driver opens a remote I/O target, the framework automatically starts the I/O target.

If necessary, the driver can call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) to temporarily stop a remote I/O target and call [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677) to restart it.

In KMDF version 1.11 and later, the driver can call [**WdfIoTargetPurge**](https://msdn.microsoft.com/library/windows/hardware/hh439338) to temporarily prevent I/O requests from being sent to a remote I/O target, and to cancel unprocessed requests in the target's queue.

If a remote I/O target's device is removed, the framework automatically stops and closes the I/O target and cancels all I/O requests that are in the target's queue, unless the driver registers the following event callback functions:

<a href="" id="evtiotargetqueryremove"></a>[*EvtIoTargetQueryRemove*](https://msdn.microsoft.com/library/windows/hardware/ff541793)  
Informs the driver that a remote I/O target's device might be removed. Your driver must call [**WdfIoTargetCloseForQueryRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548589) if you want the driver to allow removal of the device.

<a href="" id="evtiotargetremovecomplete"></a>[*EvtIoTargetRemoveComplete*](https://msdn.microsoft.com/library/windows/hardware/ff541806)  
Informs the driver that a remote I/O target's device has been removed. This callback function must call [**WdfIoTargetClose**](https://msdn.microsoft.com/library/windows/hardware/ff548586).

<a href="" id="evtiotargetremovecanceled"></a>[*EvtIoTargetRemoveCanceled*](https://msdn.microsoft.com/library/windows/hardware/ff541800)  
Informs the driver that an attempt to remove a remote I/O target's device has been canceled. This callback function must call [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634), and the driver typically calls [**WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT\_REOPEN**](https://msdn.microsoft.com/library/windows/hardware/ff552382) to initialize its WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT function.

If a driver has finished using a remote I/O target and will not use the target again, and the target has no child request objects that are still pending, the driver can call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) without first calling [**WdfIoTargetClose**](https://msdn.microsoft.com/library/windows/hardware/ff548586). If the target has any child request objects that are still pending, the driver must call **WdfIoTargetClose** before it can safely call **WdfObjectDelete**.

 

 





