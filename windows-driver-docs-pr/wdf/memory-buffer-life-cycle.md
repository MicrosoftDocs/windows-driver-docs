---
title: Memory Buffer Life Cycle
description: Memory Buffer Life Cycle
ms.assetid: abf43bf5-a4a3-4aeb-9ec5-3458252933d5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Memory Buffer Life Cycle


A memory buffer's life cycle spans the time from when the buffer is created to when it is deleted. This topic describes buffer usage scenarios and how they affect when the buffer is deleted.

In the kernel-mode driver framework (KMDF), a request object represents an I/O request. Every request object is associated with one or more memory objects, and each memory object represents a buffer that is used for input or output in the request.

When the framework creates request and memory objects to represent an incoming I/O request, it sets the request object as the parent of the associated memory objects. Therefore, the memory object can persist no longer than the lifetime of the request object. When the framework-based driver completes the I/O request, the framework deletes the request object and the memory object, so the handles to these two objects become invalid.

However, the underlying buffer is different. Depending on which component created the buffer and how it created the buffer, the buffer might have a reference count and might be owned by the memory object—or it might not. If the memory object owns the buffer, then the buffer has a reference count and its lifetime is limited to that of the memory object. If some other component created the buffer, then the lifetimes of the buffer and the memory object are not related.

A framework-based driver can also create its own request objects to send to I/O targets. A driver-created request can reuse an existing memory object that the driver received in an I/O request. A driver that frequently sends requests to I/O targets can [reuse the request objects](reusing-framework-request-objects.md) that it creates.

Understanding the lifetimes of the request object, the memory object, and the underlying buffer is important to ensure that your driver does not attempt to reference an invalid handle or buffer pointer.

Consider the following usage scenarios:

-   Scenario 1: [Driver receives an I/O request from KMDF, handles it, and completes it](#drv-rec-complete).
-   Scenario 2: [Driver receives an I/O request from KMDF and forwards it to an I/O target](#drv-rec-fwd).
-   Scenario 3: [Driver issues an I/O request that uses an existing memory object](#drv-create-reuse).
-   Scenario 4: [Driver issues an I/O request that uses a new memory object.](#drv-create-new)
-   Scenario 5: [Driver reuses a request object that it created.](#drv-reuse)

### <a href="" id="drv-rec-complete"></a>Scenario 1: Driver receives an I/O request from KMDF, handles it, and completes it.

In the simplest scenario, KMDF dispatches a request to the driver, which performs I/O and completes the request. In this case, the underlying buffer might have been created by a user-mode application, by another driver, or by the operating system itself. For information about how to access buffers, see [Accessing Data Buffers in Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540701).

When the driver [completes the request](completing-i-o-requests.md), the framework deletes the memory object. The buffer pointer is then invalid.

### <a href="" id="drv-rec-fwd"></a>Scenario 2: Driver receives an I/O request from KMDF and forwards it to an I/O target.

In this scenario, the driver [forwards the request](forwarding-i-o-requests.md) to an I/O target. The following sample code shows how a driver retrieves a handle to the memory object from an incoming request object, formats the request to send to the I/O target, and sends the request:

```cpp
VOID
EvtIoRead(
    IN WDFQUEUE Queue,
    IN WDFREQUEST Request,
    IN size_t Length
    )
{
    NTSTATUS status;
    WDFMEMORY memory;
    WDFIOTARGET ioTarget;
    BOOLEAN ret;
    ioTarget = WdfDeviceGetIoTarget(WdfIoQueueGetDevice(Queue));

    status = WdfRequestRetrieveOutputMemory(Request, &memory);
    if (!NT_SUCCESS(status)) {
        goto End;
    }

    status = WdfIoTargetFormatRequestForRead(ioTarget,
                                    Request,
                                    memory,
                                    NULL,
                                    NULL);
    if (!NT_SUCCESS(status)) {
        goto End;
    }

    WdfRequestSetCompletionRoutine(Request,
                                    RequestCompletionRoutine,
                                    WDF_NO_CONTEXT);

    ret = WdfRequestSend (Request, ioTarget, WDF_NO_SEND_OPTIONS);
    if (!ret) {
        status = WdfRequestGetStatus (Request);
        goto End;
    }

    return;

End:
    WdfRequestComplete(Request, status);
    return;

}
```

When the I/O target has completed the request, the framework calls the completion callback that the driver set for the request. The following code shows a simple completion callback:

```cpp
VOID
RequestCompletionRoutine(
    IN WDFREQUEST                  Request,
    IN WDFIOTARGET                 Target,
    PWDF_REQUEST_COMPLETION_PARAMS CompletionParams,
    IN WDFCONTEXT                  Context
    )
{
    UNREFERENCED_PARAMETER(Target);
    UNREFERENCED_PARAMETER(Context);

    WdfRequestComplete(Request, CompletionParams->IoStatus.Status);

    return;

}
```

When the driver calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) from its completion callback, the framework deletes the memory object. The memory object handle that the driver retrieved is now invalid.

## Scenario 3: Driver issues an I/O request that uses an existing memory object.


Some drivers issue their own I/O requests and send them to I/O targets, which are represented by I/O target objects. The driver can either create its own request object or [reuse a framework-created request object](reusing-framework-request-objects.md). Using either technique, a driver can reuse a memory object from a previous request. The driver must not change the underlying buffer, but it can pass a buffer offset when it formats the new I/O request.

For information about how to format a new I/O request that uses an existing memory object, see [Sending I/O Requests to General I/O Targets](sending-i-o-requests-to-general-i-o-targets.md).

When the framework formats the request to send to the I/O target, it takes out a reference on the recycled memory object on behalf of the I/O target object. The I/O target object retains this reference until one of the following actions occurs:

-   The request has been completed.
-   The driver reformats the request object again by calling one of the *WdfIoTargetFormatRequestXxx* or *WdfIoTargetSendXxxSynchronously* methods. For more information about these methods, see [Framework I/O Target Object Methods](https://msdn.microsoft.com/library/windows/hardware/dn265644).
-   The driver calls [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026).

When the new I/O request is complete, the framework calls the I/O completion callback that the driver set for this request. At this point, the I/O target object still holds a reference on the memory object. Therefore, in the I/O completion callback, the driver must call [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026) on the driver-created request object before it completes the original request from which it retrieved the memory object. If the driver does not call **WdfRequestReuse**, a bug check occurs because of the extra reference.

## Scenario 4: Driver issues an I/O request that uses a new memory object.


The framework provides three ways for drivers to create new memory objects, depending on the source of the underlying buffer. For more information, see [Using Memory Buffers](using-memory-buffers.md).

If the buffer is allocated by the framework or from a driver-created [lookaside list](using-memory-buffers.md#using-lookaside-lists), the memory object owns the buffer, so the buffer pointer remains valid as long as the memory object exists. Drivers that issue asynchronous I/O requests should always use buffers that are owned by memory objects so that the framework can ensure that the buffers persist until the I/O request has completed back to the issuing driver.

If the driver assigns a previously allocated buffer to a new memory object by calling [**WdfMemoryCreatePreallocated**](https://msdn.microsoft.com/library/windows/hardware/ff548712), the memory object does not own the buffer. In this case, the lifetime of the memory object and the lifetime of the underlying buffer are not related. The driver must manage the lifetime of the buffer and must not attempt to use an invalid buffer pointer.

## Scenario 5: Driver reuses a request object that it created.


A driver can reuse the request objects that it creates, but it must reinitialize each such object by calling [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026) before each reuse. For more information, see [Reusing Framework Request Objects](reusing-framework-request-objects.md).

For sample code that reinitializes a request object, see the [Toaster](http://go.microsoft.com/fwlink/p/?linkid=256195) and [NdisEdge](http://go.microsoft.com/fwlink/p/?linkid=256154) samples that are provided with the KMDF release.









