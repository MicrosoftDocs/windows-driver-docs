---
title: IRP_MN_CHANGE_SINGLE_ITEM
description: All drivers that support WMI must handle this IRP.
ms.date: 08/12/2017
ms.assetid: 9839ebb2-31a9-4cb0-adbf-1882583849fc
keywords:
 - IRP_MN_CHANGE_SINGLE_ITEM Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_CHANGE\_SINGLE\_ITEM


All drivers that support WMI must handle this IRP. A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) to handle an **IRP\_MN\_CHANGE\_SINGLE\_ITEM** request, WMI in turn calls that driver's [*DpWmiSetDataItem*](https://msdn.microsoft.com/library/windows/hardware/ff544108) routine.

Major Code
----------

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)
When Sent
---------

WMI sends this IRP to change a single data item in a single instance of a data block.

WMI sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


**Parameters.WMI.ProviderId** points to the device object of the driver that should respond to the request. This pointer is located in the driver's I/O stack location in the IRP.

**Parameters.WMI.DataPath** points to a GUID that identifies the data block to be set.

**Parameters.WMI.BufferSize** indicates the size of the nonpaged buffer at **Parameters.WMI.Buffer**.

**Parameters.WMI.Buffer**, points to a [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378) structure that identifies the instance of the data block, the ID of the item to set, and a new data value.

## Output Parameters


None.

## I/O Status Block


If the driver handles the IRP by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI sets **Irp-&gt;IoStatus.Status** and **Irp-&gt;IoStatus.Information** in the I/O status block.

Otherwise, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as the following:

STATUS\_WMI\_INSTANCE\_NOT\_FOUND

STATUS\_WMI\_ITEMID\_NOT\_FOUND

STATUS\_WMI\_GUID\_NOT\_FOUND

STATUS\_WMI\_READ\_ONLY

STATUS\_WMI\_SET\_FAILURE

On success, a driver sets **Irp-&gt;IoStatus.Information** to zero.

Operation
---------

If a driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), that routine calls the driver's [*DpWmiSetDataItem*](https://msdn.microsoft.com/library/windows/hardware/ff544108) routine, or returns STATUS\_WMI\_READ\_ONLY if the driver does not define the routine.

If a driver handles **IRP\_MN\_CHANGE\_SINGLE\_ITEM** requests itself, it should do so only if **Parameters.WMI.ProviderId** points to the same device object as the pointer that the driver passed to [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480). Otherwise, the driver must forward the request to the next-lower driver.

Do not implement support for **IRP\_MN\_CHANGE\_SINGLE\_ITEM** unless you are sure that a system-supplied user-mode component requires this capability.

Before handling a request, the driver must determine whether **Parameters.WMI.DataPath** points to a GUID that the driver supports. If it does not, the driver must fail the IRP and return STATUS\_WMI\_GUID\_NOT\_FOUND.

If the driver supports the data block, it must check the input [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378) structure that **Parameters.WMI.Buffer** points to for the instance name, as follows:

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is set in **WnodeHeader.Flags**, the driver uses **InstanceIndex** as an index into the driver's list of static instance names for that block. WMI obtains the index from registration data provided by the driver when it registered the block.

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is clear in **WnodeHeader.Flags,** the driver uses the offset at **OffsetInstanceName** to locate the instance name string in the input [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378) structure. **OffsetInstanceName** is the offset in bytes from the beginning of the structure to a USHORT-sized length of the instance name string in bytes (not characters). This length includes the NULL terminator if present, followed by the instance name string in Unicode.

The driver is responsible for validating all input values. Specifically, the driver must do the following if it handles the IRP request itself:

-   For static names, verify that the **InstanceIndex** member of the WNODE\_SINGLE\_ITEM structure is within the range of instance indexes supported by the driver for the data block.

-   For dynamic names, verify that the instance name string identifies a data block instance supported by the driver.

-   Verify that the **ItemId** member of the [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378) structure is within the range of item identifiers supported by the driver for the data block.

-   Verify that the **DataBlockOffset** and **SizeDataItem** members of the **WNODE\_SINGLE\_ITEM** structure describe a valid-sized data block, and that the contents of the buffer are valid for the data item.

-   Verify that the specified data item is one for which the driver allows caller-initiated modifications. In other words, the driver should not allow modifications to data items that you intended to be read-only.

Do not assume the thread context is that of the initiating user-mode application—a higher-level driver might have changed it.

If the driver cannot locate the specified instance, it must fail the IRP and return STATUS\_WMI\_INSTANCE\_NOT\_FOUND. For an instance with a dynamic instance name, this status indicates that the driver does not support the instance. WMI can therefore continue to query other data providers, and return an appropriate error to the data consumer if another provider finds the instance but cannot handle the request for some other reason.

If the driver locates the instance and can handle the request, it sets the data item in the instance to the value in the [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378). If the data item is read-only, the driver leaves the item unchanged, fails the IRP, and returns STATUS\_WMI\_READ\_ONLY.

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


[*DpWmiSetDataItem*](https://msdn.microsoft.com/library/windows/hardware/ff544108)

[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)

[**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813)

[**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834)

[**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378)

 

 




