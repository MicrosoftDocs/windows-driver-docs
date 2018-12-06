---
title: Evaluating a Control Method That Takes Input Arguments
description: Evaluating a Control Method That Takes Input Arguments
ms.assetid: 3a4be8a8-0906-4d38-bf6d-f245e6ae236a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Evaluating a Control Method That Takes Input Arguments


To synchronously evaluate a control method that takes input arguments, a driver for a device sends an [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148) request or an [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) request to the device. The general procedure for using both these requests is described in [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md). The specific difference between using these two requests is as follows:

-   If the control method is an immediate child object of the device, the driver sends an IOCTL\_ACPI\_EVAL\_METHOD request and supplies one of the following input structures: [**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER**](https://msdn.microsoft.com/library/windows/hardware/ff536119), [**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff536121), or [**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX**](https://msdn.microsoft.com/library/windows/hardware/ff536116).

-   If the control method is a child object in the ACPI namespace of the device, but is not an immediate child object of the device, the driver sends an IOCTL\_ACPI\_EVAL\_METHOD\_EX request and supplies one of the following input structures: [**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536120), [**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536122), or [**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536117).

The example *EvaluateABCDWithInputArgument* function that is provided in this topic shows how a driver can use an IOCTL\_ACPI\_EVAL\_METHOD request to evaluate a control method named 'ABCD' that takes a single integer input argument.

If the input argument was a string or an array of custom data instead of an integer, the required change to the example code is to supply a string input structure or a complex input structure instead of an integer input structure.

In addition, if the 'ABCD' control method was not an immediate child object, the required changes to the example code are as follows:

-   Send an IOCTL\_ACPI\_EVAL\_METHOD\_EX request instead of an IOCTL\_ACPI\_EVAL\_METHOD request.

-   Supply the type of extended input structure that corresponds to the input argument type (simple integer, simple string, or complex).

*EvaluateABCDWithInputArgument* first allocates an ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER structure *inputBuffer* and then sets the **MethodNameAsUlong** member to the name of the control method, sets the **IntegerArgument** member to the input integer value, and sets the **Signature** member to ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER\_SIGNATURE.

```cpp
    // Fill in the input data
    inputBuffer.MethodNameAsUlong = (ULONG) ('DCBA');
    inputBuffer.IntegerArgument  =  Argument1;
    inputBuffer.Signature = ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE;
```

*EvaluateABCDWithInputArgument* also allocates an [**ACPI\_EVAL\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536123) structure *outputBuffer*, but does not set any of the members of *outputBuffer*.

*EvaluateABCDWithInputArgument* then calls a driver-supplied function named [SendDownStreamIrp](senddownstreamirp-function.md) that performs the following:

1.  Calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) to build the request.

2.  Calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the request down the device stack.

3.  Waits for the I/O manager to signal the driver that the lower-level drivers have completed the request.

**SendDownStreamIrp** returns after the I/O manager signals that the lower-level drivers have completed the request.

Although not included in *EvaluateABCDWithInputArgument*, the driver should also perform the following additional operations after **SendDownStreamIrp** returns:

1.  Check the status that **SendDownStreamIrp** returns. If **SendDownStreamIrp** does not return STATUS\_SUCCESS, the driver should return without additional processing.

2.  Check the validity of the output parameters. For the *outputBuffer* to contain valid output data, **Signature** must be set to ACPI\_EVAL\_OUTPUT\_BUFFER\_SIGNATURE and **Count** must be set to greater than zero.

3.  Process the output parameters that were passed back to the driver.

4.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IOCTL\_ACPI\_EVAL\_METHOD request.

The ACPI data structures and constants used in the following example are defined in *Acpiioct.h*.

```cpp
NTSTATUS
EvaluateABCDWithInputArgument(
    IN PDEVICE_OBJECT   Pdo,
    IN ULONG            Argument1,
    OUT PULONG          ReturnStatus
    )
/*
Routine Description:
    Called to evaluate the example 'ABCD' method with a single integer input argument

Parameters:
    Pdo             - For the device.
    Argument1       - Input argument.
    ReturnStatus    - Pointer to where the status data is placed.

Return Value:
    NT Status of the operation
*/
{
 ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER  inputBuffer;
    ACPI_EVAL_OUTPUT_BUFFER                outputBuffer; 
    NTSTATUS                               status;
    PACPI_METHOD_ARGUMENT                  argument;

    .
    .
    // Omitted: bounds checking on Argument1 value.


    ASSERT( ReturnStatus != NULL );
    *ReturnStatus = 0x0;

    // Fill in the input data
    inputBuffer.MethodNameAsUlong = (ULONG) ('DCBA');
    inputBuffer.IntegerArgument  =  Argument1;
    inputBuffer.Signature = ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_SIGNATURE;

    // Send the request along
    status = SendDownStreamIrp(
       Pdo,
       IOCTL_ACPI_EVAL_METHOD,
       &inputBuffer,
       sizeof(ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER),
       &outputBuffer,
       sizeof(ACPI_EVAL_OUTPUT_BUFFER)
       );

    return status;
}
```

 

 




