---
title: IRP_MN_QUERY_SINGLE_INSTANCE
description: All drivers that support WMI must handle this IRP.
ms.date: 08/12/2017
ms.assetid: 104b6b3e-aa5d-437f-8236-02e4abb1ba46
keywords:
 - IRP_MN_QUERY_SINGLE_INSTANCE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_SINGLE\_INSTANCE


All drivers that support WMI must handle this IRP. A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) to handle an **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** request, WMI in turn calls that driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine.

Major Code
----------

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)
When Sent
---------

WMI sends this IRP to query for a single instance of a given data block.

WMI sends an **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** prior to sending an [**IRP\_MN\_EXECUTE\_METHOD**](irp-mn-execute-method.md). If a driver supports **IRP\_MN\_EXECUTE\_METHOD**, it must have an **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** handler for the same data block whose method is being executed.

WMI sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


**Parameters.WMI.ProviderId** points to the device object of the driver that should respond to the request. This pointer is located in the driver's I/O stack location in the IRP.

**Parameters.WMI.DataPath** points to a GUID that identifies the data block to query.

**Parameters.WMI.BufferSize** indicates the maximum size of the nonpaged buffer at **Parameters.WMI.Buffer**, which points to a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure that identifies the instance to query.

## Output Parameters


If the driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI fills in a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure with data provided by the driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine.

Otherwise, the driver fills in the **WNODE\_SINGLE\_INSTANCE** structure at **Parameters.WMI.Buffer** as follows:

-   Updates **WnodeHeader.BufferSize** with the size, in bytes, of the output **WNODE\_SINGLE\_INSTANCE** structure, including instance data. This value should include the length of the instance name (padded such that the instance data begins on a quad word boundary), even if the class being queried registered static instance names and the driver writer is not explicitly supplying the name when servicing this IRP.

-   Sets **SizeDataBlock** to the size, in bytes, of the instance data. If static instance names are in use, this value should not include the size of the instance name.

-   Writes the instance data to **Parameters.WMI.Buffer** starting at **DataBlockOffset**. The driver must not change the input value of **DataBlockOffset**.

If the buffer at **Parameters.WMI.Buffer** is too small to receive all of the data, the driver fills in the needed size in a [**WNODE\_TOO\_SMALL**](https://msdn.microsoft.com/library/windows/hardware/ff566379) structure at **Parameters.WMI.Buffer**. If the buffer is smaller than **sizeof**(**WNODE\_TOO\_SMALL**), the driver fails the IRP and returns STATUS\_BUFFER\_TOO\_SMALL.

## I/O Status Block


If the driver handles the IRP by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI sets **Irp-&gt;IoStatus.Status** and **Irp-&gt;IoStatus.Information** in the I/O status block.

Otherwise, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as the following:

STATUS\_BUFFER\_TOO\_SMALL

STATUS\_WMI\_GUID\_NOT\_FOUND

STATUS\_WMI\_INSTANCE\_NOT\_FOUND

On success, a driver sets **Irp-&gt;IoStatus.Information** to the value entered into **WnodeHeader.BufferSize**. This value includes the length of the static instance name.

Operation
---------

A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), **WmiSystemControl** calls the driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine.

If a driver handles an **IRP\_MN\_QUERY\_SINGLE\_INSTANCE** request itself, it should do so only if **Parameters.WMI.ProviderId** points to the same device object as the pointer that the driver passed in its call to [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480). Otherwise, the driver must forward the request to the next lower driver in the device stack.

Before handling the request, the driver must determine whether **Parameters.WMI.DataPath** points to a GUID that the driver supports. If not, the driver must fail the IRP and return STATUS\_WMI\_GUID\_NOT\_FOUND.

The driver is responsible for validating all input values. Specifically, the driver must do the following if it handles the IRP request itself:

-   For static names, verify that the **InstanceIndex** member of the [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure is within the range of instance indexes supported by the driver for the data block.

-   For dynamic names, verify that the instance name string identifies a data block instance supported by the driver.

-   Verify that **Parameters.WMI.BufferSize** specifies a buffer that is large enough to receive all the data that the driver will return.

If the driver supports the data block, it checks the input [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) at **Parameters.WMI.Buffer** for the instance name, as follows:

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is set in **WnodeHeader.Flags**, the driver uses **InstanceIndex** as an index into the driver's list of static instance names for that block. WMI obtains the index from registration data provided by the driver when it registered the block.

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is clear in **WnodeHeader.Flags**, the driver uses the offset at **OffsetInstanceName** to locate the instance name string in the input **WNODE\_SINGLE\_INSTANCE**. **OffsetInstanceName** is the offset, in bytes, from the beginning of the structure to a USHORT, which is the length of the instance name string in bytes (not characters), including the terminating null if present, followed by the instance name string in Unicode.

If the driver cannot locate the specified instance, it must fail the IRP and return STATUS\_WMI\_INSTANCE\_NOT\_FOUND. For an instance with a dynamic instance name, this status indicates that the driver does not support the instance. WMI can therefore continue to query other data providers, and return an appropriate error to the data consumer if another provider finds the instance but cannot handle the request for some other reason.

If the driver locates the instance and can handle the request, it fills in the **WNODE\_SINGLE\_INSTANCE** structure at **Parameters.WMI.Buffer** with data for the instance.

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


[*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096)

[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)

[**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813)

[**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834)

[**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377)

 

 




