---
title: Using \_\_sdv\_save\_request and \_\_sdv\_retrieve\_request for Deferred Procedure Calls
description: Using \_\_sdv\_save\_request and \_\_sdv\_retrieve\_request for Deferred Procedure Calls
ms.assetid: 14d3a022-3e74-4526-9bf5-fee1ce36ac9e
keywords: ["__sdv_save_request", "__sdv_retrieve_request", "DeferredRequestCompleted", "AliasWithinTimerDpc", "AliasWithinDispatch", "analyzing DPCs"]
---

# Using \_\_sdv\_save\_request and \_\_sdv\_retrieve\_request for Deferred Procedure Calls


Deferred procedure calls (DPCs) present challenges to Static Driver Verifier (SDV) because it is difficult to track the framework request object. One difficulty is that the request must be retrieved from a global pointer, usually from queue context, or from a work item. To overcome this difficulty, Static Driver Verifier provides two functions: **\_\_sdv\_save\_request**, and **\_\_sdv\_retrieve\_request**. These functions map the deferred request to a request that SDV can track.

The **\_\_sdv\_save\_request**, and **\_\_sdv\_retrieve\_request** functions have the following syntax:

```
__sdv_save_request( request ) 
```

```
__sdv_retrieve_request( request ) 
```

Where *request* can be a handle to any framework request object.

These functions are only used by the static analysis tools. The functions are ignored by the compiler.

The following code example shows how the **\_\_sdv\_save\_request** and \_**\_sdv\_retrieve\_request** functions are used to guide SDV, so that SDV can map the deferred request. SDV can use this mapping to verify the [DeferredRequestCompleted](https://msdn.microsoft.com/library/windows/hardware/ff544670) rule. The DeferredRequestCompleted rule requires that **\_\_sdv\_save\_request** and \_**\_sdv\_retrieve\_request** appear in your code. There are two driver property rules (**AliasWithinDispatch**, **AliasWithinTimerDpc**) that look for the existence of the **\_\_sdv\_save\_request** and \_**\_sdv\_retrieve\_request** functions.

In the following code example, the function *EchoEvtIoRead* is an [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776) event callback function that saves the handle to the framework request object in the queue context area. The function *EchoEvtTimerFunc* is an [*EvtTimerFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541823) event callback function that retrieves it.

```
VOID
EchoEvtIoRead(
 )in WDFQUEUE   Queue,
 __in WDFREQUEST Request,
 __in size_t      Length
    )
{
/* ..................... */
    // Mark the request as cancelable
    WdfRequestMarkCancelable(Request, EchoEvtRequestCancel);
 
 
    // Defer the completion to another thread from the timer DPC and save the handle to the framework request object by using the __sdv_save_request function. 
    queueContext->CurrentRequest = Request;    
 __sdv_save_request(Request);

    queueContext->CurrentStatus  = Status;

    return;
}
```

The following code example demonstrates how the **\_\_sdv\_retrieve\_request** function maps an existing request so that SDV can track it for completion.

```
VOID
EchoEvtTimerFunc(
    IN WDFTIMER     Timer
    )
{...................................................
    queue = WdfTimerGetParentObject(Timer);
    queueContext = QueueGetContext(queue);

    //
    // The DPC is automatically synchronized to the queue lock,
    // so this prevents race conditions from occurring without explicit driver-managed locking. The __sdv_retrieve_request function is used so that SDV can restore the deferred request in the timer DPC. Because we know that this deferred request is valid (because it has been previously saved), the __analysis_assume function is used to suppress false defects that might otherwise result in this code path.

    //
 __sdv_retrieve_request(queueContext->CurrentRequest);
    Request = queueContext->CurrentRequest;
 __analysis_assume(Request != NULL);
    if( Request != NULL ) {

        //
        // Try to remove cancel status from the request.
        //
        // The request is not completed if it is already canceled
        // because the EchoEvtIoCancel function has run, or is about to run,
        // and we are racing with it. 

        Status = WdfRequestUnmarkCancelable(Request);
// Because we know that the request is not NULL in this code path and that the request is no longer marked cancelable, we can use the __analysis_assume function to suppress the reporting of a false defect. 

 __analysis_assume(Status != STATUS_CANCELLED);
        if( Status != STATUS_CANCELLED ) {

            queueContext->CurrentRequest = NULL;
            Status = queueContext->CurrentStatus;

            KdPrint(("CustomTimerDPC Completing request 0x%p, Status 0x%x \n", Request,Status));

            WdfRequestComplete(Request, Status);
        }
        else {
            KdPrint(("CustomTimerDPC Request 0x%p is STATUS_CANCELLED, not completing\n",
                                Request));
        }
    }

    return;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Using%20__sdv_save_request%20and%20__sdv_retrieve_request%20for%20Deferred%20Procedure%20Calls%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




