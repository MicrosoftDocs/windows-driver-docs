---
title: Sending an IOCTL_ACPI_ENUM_CHILDREN Request
description: Sending an IOCTL_ACPI_ENUM_CHILDREN Request
ms.assetid: cbad53dd-4320-4920-9d16-231d0aaae839
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending an IOCTL\_ACPI\_ENUM\_CHILDREN Request


A driver typically uses a sequence of two [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) requests to enumerate the objects of interest in the namespace of the device to which the request is sent. The driver sends the first request to obtain the size of a driver-allocated output buffer that is required to contain the path and name of the objects. The driver sends the second request to return the path and name of the objects in a driver-allocated output buffer.

The following code example shows how to send a sequence of two synchronous IOCTL\_ACPI\_ENUM\_CHILDREN requests to recursively enumerate all the child devices of the parent device to which the requests are sent. The code performs the following sequence of operations to handle the first request:

1.  Sets the input buffer for the first request. The input buffer is an [**ACPI\_ENUM\_CHILDREN\_INPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536110) structure with **Signature** set to ENUM\_CHILDREN\_INPUT\_BUFFER\_SIGNATURE and **Flags** set to ENUM\_CHILDREN\_MULTILEVEL.

2.  Sets the output buffer for the first request. The output buffer is set to an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112) structure. This output buffer contains only one [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structure which is not large enough to return a name of a device.

3.  Calls a caller-supplied [SendDownStreamIrp Function](senddownstreamirp-function.md) to send the first request synchronously to the parent device.

4.  Checks if the ACPI driver set the return status to STATUS\_BUFFER\_OVERFLOW. If another status was returned, this indicates an error occurred and the code terminates.

5.  Checks that the ACPI driver set the **Signature** member to ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER\_SIGNATURE and sets **NumberOfChildren** to a value greater than or equal the **sizeof**(ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER). If both are true, the value of **NumberOfChildren** is the size, in bytes, of the output buffer that is required to contain the requested child object names.

After the example code obtains the required size of the output buffer, it performs the following sequence of operations to handle the second request, which returns the path and name of the requested child objects:

1.  Allocates an output buffer of the required size, in bytes.

2.  Calls the driver-supplied **SendDownStreamIrp** function to send the second request synchronously to the parent device.

3.  Checks that the ACPI driver set the **Signature** member to ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER\_SIGNATURE, sets **NumberOfChildren** to one or more (indicating that the path and name of at least one object was returned), and sets the **Information** member of the [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) to the allocated size of the output buffer.

4.  Processes the array of child object names in the output buffer.

```cpp
#define MY_TAG 'gTyM'   // Pool tag for memory allocation

 ACPI_ENUM_CHILDREN_INPUT_BUFFER  inputBuffer;
    ACPI_ENUM_CHILDREN_OUTPUT_BUFFER outputSizeBuffer = { 0 };
    ACPI_ENUM_CHILDREN_OUTPUT_BUFFER outputBuffer = { 0 };
    ULONG                            bufferSize;
 PACPI_ENUM_CHILD                 childObject = NULL;
 ULONG                            index;

    NTSTATUS                         status;

    ASSERT( ReturnStatus != NULL );
    *ReturnStatus = 0x0;

    // Fill in the input data
    inputBuffer.Signature = ACPI_ENUM_CHILDREN_INPUT_BUFFER_SIGNATURE;
    inputBuffer.Flags = ENUM_CHILDREN_MULTILEVEL;

    // Send the request along
    status = SendDownStreamIrp(
       Pdo,
 IOCTL_ACPI_ENUM_CHILDREN,
       &inputBuffer,
       sizeof(inputBuffer),
       &outputSizeBuffer,
       sizeof(outputSizeBuffer)
       );

 if (Status != STATUS_BUFFER_OVERFLOW) {
        // There should be at least one child device (that is the device itself)
        // Return error return status
    }

    // Verify the data
    // NOTE: The NumberOfChildren returned by ACPI actually contains the required size
 // when the status returned is STATUS_BUFFER_OVERFLOW 

    if ((outputSizeBuffer.Signature != ACPI_ENUM_CHILDREN_OUTPUT_BUFFER_SIGNATURE) ||
       (outputSizeBuffer.NumberOfChildren < sizeof(ACPI_ENUM_CHILDREN_OUTPUT_BUFFER)))
    {
        return STATUS_ACPI_INVALID_DATA;
    }

    //
    // Allocate a buffer to hold all the child devices
    //
    bufferSize = outputSizeBuffer.NumberOfChildren;
    outputBuffer = (PACPI_ENUM_CHILDREN_OUTPUT_BUFFER)
 ExAllocatePoolWithTag(PagedPool, bufferSize, MY_TAG);

    if (outputBuffer == NULL){
        return STATUS_INSUFFICIENT_RESOURCES;
    }

    RtlZeroMemory(outputBuffer, bufferSize);

    // Allocate a new IRP with the new output buffer
    // Send another request together with the new output buffer
    status = SendDownStreamIrp(
       Pdo,
 IOCTL_ACPI_ENUM_CHILDREN,
       &inputBuffer,
       sizeof(inputBuffer),
       &outputBuffer,
       bufferSize
       );

    // Verify the data
    if ((outputBuffer->Signature != ACPI_ENUM_CHILDREN_OUTPUT_BUFFER_SIGNATURE) ||
        (outputBuffer->NumberOfChildren == 0) ||
        (IoStatusBlock.Information != bufferSize)) {
        return STATUS_ACPI_INVALID_DATA;
    }

    // Skip the first child device because ACPI returns the device itself 
 // as the first child device
    childObject = &(outputBuffer->Children[0]);

    for (index = 1; index < outputBuffer->NumberOfChildren; ++index) {

        // Proceed to the next ACPI child device. 
        childObject = ACPI_ENUM_CHILD_NEXT(childObject);

        //  Process each child device.
 
 
 
    }
```

 

 




