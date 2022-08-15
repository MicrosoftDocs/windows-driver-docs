---
title: Evaluating a Control Method Without Input Arguments
description: Provides information about evaluating a control method without input arguments
ms.date: 08/17/2021
---

# Evaluating a Control Method Without Input Arguments

To synchronously evaluate a control method that does not take input arguments, a driver for a device sends an [**IOCTL_ACPI_EVAL_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method) request or an [**IOCTL_ACPI_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method_ex) request to the device. The general procedure for using both these requests is described in [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md). The specific difference between using these two requests is as follows:

- If the control method is an immediate child object of the device, the driver sends an IOCTL_ACPI_EVAL_METHOD request and supplies an [**ACPI_EVAL_INPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1) input structure.

- If the control method is a child object in the ACPI namespace of the device, but is not an immediate child object of the device, the driver sends an IOCTL_ACPI_EVAL_METHOD_EX request and supplies an [**ACPI_EVAL_INPUT_BUFFER_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1_ex) structure.

The example *GetAbcData* function that is provided in this topic shows how a driver for a device can use an IOCTL_ACPI_EVAL_METHOD request to evaluate a control method named 'ABCD' that the device supports. The 'ABCD' control method is an immediate child of the device in the ACPI namespace and does not take input arguments or return output arguments.

If the 'ABCD' control method was not an immediate child object, the required changes to this example code are as follows:

- Send an IOCTL_ACPI_EVAL_METHOD_EX request instead of an IOCTL_ACPI_EVAL_METHOD request.

- Supply an ACPI_EVAL_INPUT_BUFFER_EX structure instead of an ACPI_EVAL_INPUT_BUFFER structure.

*GetAbcData* first allocates an ACPI_EVAL_INPUT_BUFFER structure *inputBuffer* and sets the **MethodNameAsUlong** member to the name of the control method and sets the **Signature** member to ACPI_EVAL_INPUT_BUFFER_SIGNATURE.

```cpp
    // Fill in the input data
    inputBuffer.MethodNameAsUlong = (ULONG) ('DCBA');
    inputBuffer.Signature = ACPI_EVAL_INPUT_BUFFER_SIGNATURE;
```

*GetAbcData* also allocates an [**ACPI_EVAL_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_output_buffer_v1) structure *outputBuffer*, but does not set any of the members of *outputBuffer*.

*GetAbcData* then calls a driver-supplied function named [SendDownStreamIrp](senddownstreamirp-function.md) that performs the following:

1. Calls [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) to build the request.

1. Calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to send the request down the device stack.

1. Waits for the I/O manager to signal the driver that the lower-level drivers completed request.

**SendDownStreamIrp** returns after the I/O manager signals that the lower-level drivers have completed the request. The code example mentioned earlier then performs the following:

1. Checks the status of the request and returns without additional processing if the lower-level drivers did not return STATUS_SUCCESS.

1. Checks the validity of the output arguments. For the *outputBuffer* to contain valid output data, **Signature** must be set to ACPI_EVAL_OUTPUT_BUFFER_SIGNATURE and **Count** must be set to greater than zero.

1. Processes the output arguments that the ACPI driver passed back to the driver.

Although this step is not included in the sample code, the driver should also call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) after processing the output data to complete the pending IOCTL_ACPI_EVAL_METHOD request or IOCTL_ACPI_EVAL_METHOD request that the driver sent to evaluate a control method.

The ACPI data structures and constants used in the following example are defined in *Acpiioct.h*.

```cpp
NTSTATUS
GetAbcdData(
    IN PDEVICE_OBJECT   Pdo,
    OUT PULONG          ReturnStatus
    )
/*++

Routine Description:
    Evaluates the ABCD method on the device in the ACPI namespace referenced by Pdo

Parameters
    Pdo             - PDO for the device
    ReturnStatus    - Pointer to where the status data is placed

Return Value:
    NT Status of the operation

--*/
{
    ACPI_EVAL_INPUT_BUFFER  inputBuffer;
    ACPI_EVAL_OUTPUT_BUFFER outputBuffer;
    NTSTATUS                status;
    PACPI_METHOD_ARGUMENT   argument;

    .
    .

    ASSERT( ReturnStatus != NULL );
    *ReturnStatus = 0x0;

    // Fill in the input data
    inputBuffer.MethodNameAsUlong = (ULONG) ('DCBA');
    inputBuffer.Signature = ACPI_EVAL_INPUT_BUFFER_SIGNATURE;

    // Send the request along
    status = SendDownStreamIrp(
       Pdo,
       IOCTL_ACPI_EVAL_METHOD,
       &inputBuffer,
       sizeof(ACPI_EVAL_INPUT_BUFFER),
       &outputBuffer,
       sizeof(ACPI_EVAL_OUTPUT_BUFFER)
       );

    if (!NT_SUCCESS(status)) {
       return status;
    }

    // Verify the data
    if (outputBuffer != NULL) {
        if ( ( (PACPI_EVAL_OUTPUT_BUFFER) outputBuffer->Signature != 
            ACPI_EVAL_OUTPUT_BUFFER_SIGNATURE ||
            ( (PACPI_EVAL_OUTPUT_BUFFER) outputBuffer->Count == 0) {
            return STATUS_ACPI_INVALID_DATA;
        } 
}

    // Retrieve the output argument
    argument = outputBuffer.Argument;
 
// Process the output argument
 .
.
.
 
    return status;
}
```
