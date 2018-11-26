---
title: IRP_MN_EXECUTE_METHOD
description: All drivers that support methods within data blocks must handle this IRP.
ms.date: 08/12/2017
ms.assetid: cc42340e-4a7c-475c-b44d-2127e8a0d7dc
keywords:
 - IRP_MN_EXECUTE_METHOD Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_EXECUTE\_METHOD


All drivers that support methods within data blocks must handle this IRP. A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) to handle an **IRP\_MN\_EXECUTE\_METHOD** request, WMI in turn calls that driver's [*DpWmiExecuteMethod*](https://msdn.microsoft.com/library/windows/hardware/ff544090) routine.

Major Code
----------

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)
When Sent
---------

WMI sends this IRP to execute a method associated with a data block.

WMI sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

WMI will send an [**IRP\_MN\_QUERY\_SINGLE\_INSTANCE**](irp-mn-query-single-instance.md) prior to sending an **IRP\_MN\_EXECUTE\_METHOD**. If a driver supports **IRP\_MN\_EXECUTE\_METHOD** it must have a **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** handler for the same data block whose method is being executed.

## Input Parameters


**Parameters.WMI.ProviderId** points to the device object of the driver that should respond to the request. This pointer is located in the driver's I/O stack location in the IRP.

**Parameters.WMI.DataPath** points to a GUID that identifies the data block associated with the method to execute.

**Parameters.WMI.BufferSize** indicates the size of the nonpaged buffer at **Parameters.WMI.Buffer** which must be &gt;= **sizeof**(**WNODE\_METHOD\_ITEM**) plus the size of any output data for the method.

**Parameters.WMI.Buffer** points to a [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) structure in which **MethodID** indicates the identifier of the method to execute and **DataBlockOffset** indicates the offset in bytes from the beginning of the structure to the first byte of input data, if any. **Parameters.WMI.Buffer-&gt;SizeDataBlock** indicates the size in bytes of the input **WNODE\_METHOD\_ITEM** including input data, or zero if there is no input.

## Output Parameters


If the driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI fills in the [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) with data returned by the driver's [*DpWmiExecuteMethod*](https://msdn.microsoft.com/library/windows/hardware/ff544090) routine.

Otherwise, the driver fills in the **WNODE\_METHOD\_ITEM** structure that **Parameters.WMI.Buffer** points to as follows:

-   Updates **WnodeHeader.BufferSize** with the size of the output **WNODE\_METHOD\_ITEM**, including any output data.

-   Updates **SizeDataBlock** with the size of the output data, or zero if there is no output data.

-   Checks **Parameters.WMI.Buffersize** to determine whether the buffer is large enough to receive the output **WNODE\_METHOD\_ITEM** including any output data. If the buffer is not large enough, the driver fills in the needed size in a [**WNODE\_TOO\_SMALL**](https://msdn.microsoft.com/library/windows/hardware/ff566379) structure pointed to by **Parameters.WMI.Buffer**. If the buffer is smaller than **sizeof**(**WNODE\_TOO\_SMALL**), the driver fails the IRP and returns STATUS\_BUFFER\_TOO\_SMALL.

-   Writes output data, if any, over input data starting at **DataBlockOffset**. The driver must not change the input value of **DataBlockOffset**.

## I/O Status Block


If the driver handles the IRP by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI sets **Irp-&gt;IoStatus.Status** and **Irp-&gt;IoStatus.Information** in the I/O status block.

Otherwise, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as the following:

STATUS\_BUFFER\_TOO\_SMALL

STATUS\_WMI\_GUID\_NOT\_FOUND

STATUS\_WMI\_INSTANCE\_NOT\_FOUND

STATUS\_WMI\_ITEMID\_NOT\_FOUND

On success, a driver sets **Irp-&gt;IoStatus.Information** to the number of bytes written to the buffer at **Parameters.WMI.Buffer**.

Operation
---------

A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), that routine calls the driver's [*DpWmiExecuteMethod*](https://msdn.microsoft.com/library/windows/hardware/ff544090) routine, or returns STATUS\_INVALID\_DEVICE\_REQUEST if the driver does not define the routine.

If a driver handles an **IRP\_MN\_EXECUTE\_METHOD** request itself, it must do so only if **Parameters.WMI.ProviderId** points to the same device object as the pointer that the driver passed to [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480). Otherwise, the driver must forward the request to the next-lower driver.

The driver is responsible for validating all input values. Specifically, the driver must do the following if it handles the IRP request itself:

-   For static names, verify that the **InstanceIndex** member of the [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) structure is within the range of instance indexes supported by the driver for the data block.

-   For dynamic names, verify that the instance name string identifies a data block instance supported by the driver.

-   Verify that the **MethodId** member of the [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) structure is within the range of method identifiers supported by the driver for the data block, and that the caller is allowed to execute the method.

-   Verify that the **DataBlockOffset** and **SizeDataBlock** members of the [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) structure describe a buffer that is large enough to contain the specified method's parameters, and that the parameters are valid for the method.

-   Verify that **Parameters.WMI.Buffersize** specifies a buffer that is large enough to receive the **WNODE\_METHOD\_ITEM** structure after it has been updated with output data.

Do not assume the thread context is that of the initiating user-mode application — a higher-level driver might have changed it.

Before handling the request, the driver must determine whether **Parameters.WMI.DataPath** points to a GUID supported by the driver. If not, the driver must fail the IRP and return STATUS\_WMI\_GUID\_NOT\_FOUND.

If the driver supports the data block, it checks the input [**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376) at **Parameters.WMI.Buffer** for the instance name, as follows:

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is set in **WnodeHeader.Flags**, the driver uses **InstanceIndex** as an index into the driver's list of static instance names for that block. WMI obtains the index from registration data that was provided by the driver when it registered the block.

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is clear in **WnodeHeader.Flags,** the driver uses the offset at **OffsetInstanceName** to locate the instance name string in the input **WNODE\_METHOD\_ITEM**. **OffsetInstanceName** is the offset in bytes from the beginning of the structure to a USHORT which is the length of the instance name string in bytes (not characters), including the terminating null if present, followed by the instance name string in Unicode.

If the driver cannot locate the specified instance, it must fail the IRP and return STATUS\_WMI\_INSTANCE\_NOT\_FOUND. For an instance with a dynamic instance name, this status indicates that the driver does not support the instance. WMI can therefore continue to query other data providers, and return an appropriate error to the data consumer if another provider finds the instance but cannot handle the request for some other reason.

The driver then checks the method ID in the input **WNODE\_METHOD\_ITEM** to determine whether it is a valid method for that data block. If not, the driver fails the IRP and returns STATUS\_WMI\_ITEMID\_NOT\_FOUND.

If the method generates output, the driver should check the size of the output buffer in **Parameters.WMI.BufferSize** before performing any operation that might have side effects or that should not be performed twice. For example, if a method returns the values of a group of counters and then resets the counters, the driver should check the buffer size (and fail the IRP if the buffer is too small) before resetting the counters. This ensures that WMI can safely resend the request with a larger buffer.

If the instance and method ID are valid and the buffer is adequate in size, the driver executes the method. If **SizeDataBlock** in the input **WNODE\_METHOD\_ITEM** is nonzero, the driver uses the data starting at **DataBlockOffset** as input for the method.

If the method generates output, the driver writes the output data to the buffer starting at **DataBlockOffset** and sets **SizeDataBlock** in the output **WNODE\_METHOD\_ITEM** to the number of bytes of output data. If the method has no output data, the driver sets **SizeDataBlock** to zero. The driver must not change the input value of **DataBlockOffset**.

If the instance is valid but the driver cannot handle the request, it can return any appropriate error status.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[*DpWmiExecuteMethod*](https://msdn.microsoft.com/library/windows/hardware/ff544090)

[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)

[**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813)

[**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834)

[**WNODE\_METHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566376)

 

 




