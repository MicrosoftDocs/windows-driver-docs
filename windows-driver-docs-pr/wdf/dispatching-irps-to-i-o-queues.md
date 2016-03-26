---
title: Dispatching IRPs to I/O Queues
description: Dispatching IRPs to I/O Queues
ms.assetid: 71872114-2A38-47FE-9D18-EF8923273811
---

# Dispatching IRPs to I/O Queues


\[Applies to KMDF and UMDF\]

A framework-based driver can dynamically specify a target queue for an incoming IRP. To dispatch an IRP to a specific queue, a driver must call the [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105) method.

Typically, a driver calls [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105) from either its [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) or [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function. For best performance, most drivers do not provide both callback functions.

**Note**  A UMDF driver can supply a [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function, but only KMDF drivers can provide [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925).

 

If your driver already provides [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925), you can use it to dynamically select a queue. If not, provide [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) and call [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105) from within that callback function.

In addition, you should be aware of the following:

-   An alternate method for dispatching an IRP to an I/O queue is to [create a default queue](creating-i-o-queues.md) and then from within the queue's handler, call [**WdfRequestForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549958). This technique is available starting in KMDF 1.0 but does not work well with [forward progress queues](guaranteeing-forward-progress-of-i-o-operations.md) and is in general slower. Consider using [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105) instead.

-   When calling [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://msdn.microsoft.com/library/windows/hardware/hh451093) to register a [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function, the driver must set the *MajorFunction* parameter to one of the following: IRP\_MJ\_DEVICE\_CONTROL, IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL, IRP\_MJ\_READ, IRP\_MJ\_WRITE. While this requirement does not apply to [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925), only IRPs of these types can be dynamically dispatched to specified queues.

-   IRPs that go to [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) have an additional stack location. IRPs that go to [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) (without a previous invocation of *EvtDeviceWdmIrpPreprocess*) do not.

-   [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) does not facilitate sending driver-defined context information, whereas [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) does.

## Dispatching Non-Preprocessed IRPs


To dispatch IRPs from a driver's [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function, use the following procedure:

1.  From its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, the driver calls [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://msdn.microsoft.com/library/windows/hardware/hh451093) to register a [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function.

    If the target is the parent device's I/O queue, a KMDF driver must call [**WdfPdoInitAllowForwardingRequestToParent**](https://msdn.microsoft.com/library/windows/hardware/ff548789) before it calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926). If a KMDF driver has also provided a [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function, the framework calls that function first when an IRP arrives. After the callback function preprocesses the request, it calls [**WdfDeviceWdmDispatchPreprocessedIrp**](https://msdn.microsoft.com/library/windows/hardware/ff546927) to return the IRP to the framework.

2.  The framework calls the driver's [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function.
3.  From within [*EvtDeviceWdmIrpDispatch*](https://msdn.microsoft.com/library/windows/hardware/hh406404), the driver can call either [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105) or [**WdfDeviceWdmDispatchIrp**](https://msdn.microsoft.com/library/windows/hardware/hh451100), but not both. A KMDF driver has the additional option of calling neither of these methods, and instead completing the IRP or marking it pending.
4.  If a KMDF driver has set the WDF\_FORWARD\_IRP\_TO\_IO\_QUEUE\_INVOKE\_INCALLERCTX\_CALLBACK flag and has not enabled guaranteed forward progress for the target I/O queue, the framework then calls the driver's [*EvtIoInCallerContext*](https://msdn.microsoft.com/library/windows/hardware/ff541764), if provided. After preprocessing the request, the callback function must either queue it by calling [**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945) or complete it by calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

## Dispatching Preprocessed IRPs


To dispatch IRPs from a driver's [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function to a specific I/O queue, use the following procedure:

1.  The driver registers a [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function by calling [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043).
2.  The driver calls [**WdfPdoInitAllowForwardingRequestToParent**](https://msdn.microsoft.com/library/windows/hardware/ff548789) if the target is the parent device's I/O queue.
3.  From [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925), call [**WdfDeviceWdmDispatchIrpToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/hh451105) with *Flags* set to WDF\_FORWARD\_IRP\_TO\_IO\_QUEUE\_PREPROCESSED\_IRP.
4.  If the driver has set the WDF\_FORWARD\_IRP\_TO\_IO\_QUEUE\_INVOKE\_INCALLERCTX\_CALLBACK flag and has not enabled guaranteed forward progress for the target I/O queue, the framework then calls the driver's [*EvtIoInCallerContext*](https://msdn.microsoft.com/library/windows/hardware/ff541764), if provided. After the callback function has finished preprocessing the request, it must either queue it by calling [**WdfDeviceEnqueueRequest**](https://msdn.microsoft.com/library/windows/hardware/ff545945) or complete it by calling [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Dispatching%20IRPs%20to%20I/O%20Queues%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




