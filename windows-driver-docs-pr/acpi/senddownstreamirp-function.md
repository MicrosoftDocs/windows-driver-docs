---
title: SendDownStreamIrp Function
description: SendDownStreamIrp Function
ms.assetid: 09a06041-5b26-4796-b9b8-d7d27321d955
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SendDownStreamIrp Function


The code example for the `SendDownStreamIrp` function that is provided in this topic shows how to implement a driver-supplied function that sends synchronous IOCTL requests to the ACPI driver. The `SendDownStreamIrp` function can be used to send an [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148) request, an [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) request, or an [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request.

The example code for the `SendDownStreamIrp` function that is included in this section performs the following sequence of operations:

-   Creates an event object.

-   Calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) to create the IOCTL request.

-   Calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the IOCTL request.

-   Waits until the ACPI driver signals the event object, which indicates that the request has completed.

-   Returns the status of the request to the caller.

```cpp
NTSTATUS
SendDownStreamIrp(
    IN PDEVICE_OBJECT   Pdo,
    IN ULONG            Ioctl,
    IN PVOID            InputBuffer,
    IN ULONG            InputSize,
    IN PVOID            OutputBuffer,
    IN ULONG            OutputSize
)
/*
Routine Description:
    General-purpose function called to send a request to the PDO. 
    The IOCTL argument accepts the control method being passed down
    by the calling function

    This subroutine is only valid for the IOCTLS other than ASYNC EVAL. 

Parameters:
    Pdo             - the request is sent to this device object
    Ioctl           - the request - specified by the calling function
    InputBuffer     - incoming request
    InputSize       - size of the incoming request
    OutputBuffer    - the answer
    OutputSize      - size of the answer buffer

Return Value:
    NT Status of the operation
*/
{
    IO_STATUS_BLOCK     ioBlock;
    KEVENT              myIoctlEvent;
    NTSTATUS            status;
    PIRP                irp;

    // Initialize an event to wait on
    KeInitializeEvent(&myIoctlEvent, SynchronizationEvent, FALSE);

    // Build the request
    irp = IoBuildDeviceIoControlRequest(
        Ioctl, 
        Pdo,
        InputBuffer,
        InputSize,
        OutputBuffer,
        OutputSize,
        FALSE,
        &myIoctlEvent,
        &ioBlock);

    if (!irp) {
        return STATUS_INSUFFICIENT_RESOURCES;
    }

    // Pass request to Pdo, always wait for completion routine
    status = IoCallDriver(Pdo, irp);

    if (status == STATUS_PENDING) {
        // Wait for the IRP to be completed, and then return the status code
        KeWaitForSingleObject(
            &myIoctlEvent,
            Executive,
            KernelMode,
            FALSE,
            NULL);

        status = ioBlock.Status;
    }

    return status;
}
```

 

 




