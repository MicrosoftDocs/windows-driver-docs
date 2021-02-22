---
title: Dispatching IRPs to I/O Queues
description: Dispatching IRPs to I/O Queues
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dispatching IRPs to I/O Queues


\[Applies to KMDF and UMDF\]

A framework-based driver can dynamically specify a target queue for an incoming IRP. To dispatch an IRP to a specific queue, a driver must call the [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue) method.

Typically, a driver calls [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue) from either its [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) or [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) callback function. For best performance, most drivers do not provide both callback functions.

**Note**  A UMDF driver can supply a [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) callback function, but only KMDF drivers can provide [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess).

 

If your driver already provides [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess), you can use it to dynamically select a queue. If not, provide [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) and call [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue) from within that callback function.

In addition, you should be aware of the following:

-   An alternate method for dispatching an IRP to an I/O queue is to [create a default queue](creating-i-o-queues.md) and then from within the queue's handler, call [**WdfRequestForwardToIoQueue**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue). This technique is available starting in KMDF 1.0 but does not work well with [forward progress queues](guaranteeing-forward-progress-of-i-o-operations.md) and is in general slower. Consider using [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue) instead.

-   When calling [**WdfDeviceConfigureWdmIrpDispatchCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback) to register a [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) callback function, the driver must set the *MajorFunction* parameter to one of the following: IRP\_MJ\_DEVICE\_CONTROL, IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL, IRP\_MJ\_READ, IRP\_MJ\_WRITE. While this requirement does not apply to [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess), only IRPs of these types can be dynamically dispatched to specified queues.

-   IRPs that go to [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) have an additional stack location. IRPs that go to [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) (without a previous invocation of *EvtDeviceWdmIrpPreprocess*) do not.

-   [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) does not facilitate sending driver-defined context information, whereas [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) does.

## Dispatching Non-Preprocessed IRPs


To dispatch IRPs from a driver's [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) callback function, use the following procedure:

1.  From its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function, the driver calls [**WdfDeviceConfigureWdmIrpDispatchCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback) to register a [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) callback function.

    If the target is the parent device's I/O queue, a KMDF driver must call [**WdfPdoInitAllowForwardingRequestToParent**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent) before it calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate). If a KMDF driver has also provided a [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function, the framework calls that function first when an IRP arrives. After the callback function preprocesses the request, it calls [**WdfDeviceWdmDispatchPreprocessedIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp) to return the IRP to the framework.

2.  The framework calls the driver's [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch) callback function.
3.  From within [*EvtDeviceWdmIrpDispatch*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch), the driver can call either [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue) or [**WdfDeviceWdmDispatchIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirp), but not both. A KMDF driver has the additional option of calling neither of these methods, and instead completing the IRP or marking it pending.
4.  If a KMDF driver has set the WDF\_DISPATCH\_IRP\_TO\_IO\_QUEUE\_INVOKE\_INCALLERCTX\_CALLBACK flag and has not enabled guaranteed forward progress for the target I/O queue, the framework then calls the driver's [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context), if provided. After preprocessing the request, the callback function must either queue it by calling [**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest) or complete it by calling [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete).

## Dispatching Preprocessed IRPs


To dispatch IRPs from a driver's [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function to a specific I/O queue, use the following procedure:

1.  The driver registers a [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function by calling [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback).
2.  The driver calls [**WdfPdoInitAllowForwardingRequestToParent**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent) if the target is the parent device's I/O queue.
3.  From [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess), call [**WdfDeviceWdmDispatchIrpToIoQueue**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue) with *Flags* set to WDF\_DISPATCH\_IRP\_TO\_IO\_QUEUE\_PREPROCESSED\_IRP.
4.  If the driver has set the WDF\_DISPATCH\_IRP\_TO\_IO\_QUEUE\_INVOKE\_INCALLERCTX\_CALLBACK flag and has not enabled guaranteed forward progress for the target I/O queue, the framework then calls the driver's [*EvtIoInCallerContext*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_io_in_caller_context), if provided. After the callback function has finished preprocessing the request, it must either queue it by calling [**WdfDeviceEnqueueRequest**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest) or complete it by calling [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete).

 

