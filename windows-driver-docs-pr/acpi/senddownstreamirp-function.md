---
title: SendDownStreamIrp Function
description: SendDownStreamIrp Function
MS-HAID:
- 'acpi-meth-eval-dg\_b374e5d4-529f-42b9-9ca2-49717d7154ec.xml'
- 'acpi.senddownstreamirp\_function'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 09a06041-5b26-4796-b9b8-d7d27321d955
---

# SendDownStreamIrp Function


The code example for the `SendDownStreamIrp` function that is provided in this topic shows how to implement a driver-supplied function that sends synchronous IOCTL requests to the ACPI driver. The `SendDownStreamIrp` function can be used to send an [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148) request, an [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) request, or an [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request.

The example code for the `SendDownStreamIrp` function that is included in this section performs the following sequence of operations:

-   Creates an event object.

-   Calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) to create the IOCTL request.

-   Calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the IOCTL request.

-   Waits until the ACPI driver signals the event object, which indicates that the request has completed.

-   Returns the status of the request to the caller.

```
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
    KeInitializeEvent(&amp;myIoctlEvent, SynchronizationEvent, FALSE);

    // Build the request
    irp = IoBuildDeviceIoControlRequest(
        Ioctl, 
        Pdo,
        InputBuffer,
        InputSize,
        OutputBuffer,
        OutputSize,
        FALSE,
        &amp;myIoctlEvent,
        &amp;ioBlock);

    if (!irp) {
        return STATUS_INSUFFICIENT_RESOURCES;
    }

    // Pass request to Pdo, always wait for completion routine
    status = IoCallDriver(Pdo, irp);

    if (status == STATUS_PENDING) {
        // Wait for the IRP to be completed, and then return the status code
        KeWaitForSingleObject(
            &amp;myIoctlEvent,
            Executive,
            KernelMode,
            FALSE,
            NULL);

        status = ioBlock.Status;
    }

    return status;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20SendDownStreamIrp%20Function%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




