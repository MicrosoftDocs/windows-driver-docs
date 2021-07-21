---
title: Controlling a General I/O Target's State
description: Controlling a General I/O Target's State
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
The in-gate of the I/O target is open, but the out-gate is closed. The framework stops delivering requests to the appropriate driver. To send I/O requests to the I/O target, the driver must set either **WDF\_REQUEST\_SEND\_OPTION\_IGNORE\_TARGET\_STATE** or **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET** in each request's [**WDF\_REQUEST\_SEND\_OPTIONS**](/windows-hardware/drivers/ddi/wdfrequest/ns-wdfrequest-_wdf_request_send_options) structure.

<a href="" id="purged"></a>*Purged*  
Both gates of the I/O target object are closed. The driver cannot send I/O requests to the I/O target unless it sets **WDF\_REQUEST\_SEND\_OPTION\_IGNORE\_TARGET\_STATE** or **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET**. In addition, the framework cancels unprocessed requests in the I/O target object's internal queue. This state is available beginning in KMDF version 1.11.

<a href="" id="closed-for-query-remove"></a>*Closed for Query-Remove*  
A remote I/O target is temporarily closed because its device might soon be removed.

<a href="" id="closed"></a>*Closed*  
The I/O target is closed and cannot be started or stopped.

<a href="" id="deleted"></a>*Deleted*  
The I/O target's device has been removed.

The [**WDF\_IO\_TARGET\_STATE**](/windows-hardware/drivers/ddi/wdfiotarget/ne-wdfiotarget-_wdf_io_target_state) enumeration defines the values that represent these states. Your driver can call [**WdfIoTargetGetState**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetgetstate) to obtain an I/O target's state.

### Local I/O Target States

The framework automatically opens and starts local I/O targets.

If necessary, the driver can call [**WdfIoTargetStop**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop) to temporarily stop a local I/O target and call [**WdfIoTargetStart**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstart) to restart it. For example, the driver might stop a local I/O target if it detects a temporary error condition and then restart the I/O target if the error condition is corrected.

In KMDF version 1.11 and later, the driver can call [**WdfIoTargetPurge**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetpurge) to temporarily prevent I/O requests from being sent to a local I/O target, and to cancel unprocessed requests in the target's queue. For example, as part of file handle cleanup, a driver might purge a local I/O target to ensure that all requests sent to the driver are cancelled.

If a local I/O target's device is removed, the framework automatically stops and closes the I/O target and [cancels](canceling-i-o-requests.md) all I/O requests that are in the target's queue. The framework notifies the driver that the device is no longer available by calling device object event callback functions. For more information about these callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

### Remote I/O Target States

Drivers must call [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen) to open remote I/O targets. When a driver opens a remote I/O target, the framework automatically starts the I/O target.

If necessary, the driver can call [**WdfIoTargetStop**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop) to temporarily stop a remote I/O target and call [**WdfIoTargetStart**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstart) to restart it.

In KMDF version 1.11 and later, the driver can call [**WdfIoTargetPurge**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetpurge) to temporarily prevent I/O requests from being sent to a remote I/O target, and to cancel unprocessed requests in the target's queue.

If a remote I/O target's device is removed, the framework automatically stops and closes the I/O target and cancels all I/O requests that are in the target's queue, unless the driver registers the following event callback functions:

<a href="" id="evtiotargetqueryremove"></a>[*EvtIoTargetQueryRemove*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_query_remove)  
Informs the driver that a remote I/O target's device might be removed. Your driver must call [**WdfIoTargetCloseForQueryRemove**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetcloseforqueryremove) if you want the driver to allow removal of the device.

<a href="" id="evtiotargetremovecomplete"></a>[*EvtIoTargetRemoveComplete*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_remove_complete)  
Informs the driver that a remote I/O target's device has been removed. This callback function must call [**WdfIoTargetClose**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetclose).

<a href="" id="evtiotargetremovecanceled"></a>[*EvtIoTargetRemoveCanceled*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_remove_canceled)  
Informs the driver that an attempt to remove a remote I/O target's device has been canceled. This callback function must call [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen), and the driver typically calls [**WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT\_REOPEN**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdf_io_target_open_params_init_reopen) to initialize its WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT function.

If a driver has finished using a remote I/O target and will not use the target again, and the target has no child request objects that are still pending, the driver can call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) without first calling [**WdfIoTargetClose**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetclose). If the target has any child request objects that are still pending, the driver must call **WdfIoTargetClose** before it can safely call **WdfObjectDelete**.

 

