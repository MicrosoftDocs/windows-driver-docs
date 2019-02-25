---
title: IRP_MN_QUERY_ALL_DATA
description: All drivers that support WMI must handle this IRP.
ms.date: 08/12/2017
ms.assetid: 9d4e1c2e-73ad-4fc3-99e6-391a64edfa5c
keywords:
 - IRP_MN_QUERY_ALL_DATA Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_ALL\_DATA


All drivers that support WMI must handle this IRP. A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) to handle an **IRP\_MN\_QUERY\_ALL\_DATA** request, WMI in turn calls that driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine.

Major Code
----------

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)
When Sent
---------

WMI sends this IRP to query for all instances of a given data block.

WMI sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


**Parameters.WMI.ProviderId** in the driver's I/O stack location in the IRP points to the device object of the driver that should respond to the request.

**Parameters.WMI.DataPath** points to a GUID that identifies the data block.

**Parameters.WMI.BufferSize** indicates the maximum size of the nonpaged buffer at **Parameters.WMI.Buffer**, which receives output data from the request. The buffer size must be greater than or equal to **sizeof**(**WNODE\_ALL\_DATA**) plus the sizes of instance names and data for all instances to be returned.

## Output Parameters


If the driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI fills in a **WNODE\_ALL\_DATA** by calling the driver's *DpWmiQueryDataBlock* routine once for each block registered by the driver.

Otherwise, the driver fills in a [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) structure at **Parameters.WMI.Buffer** as follows:

-   Sets **WnodeHeader.BufferSize** to the number of bytes of the entire **WNODE\_ALL\_DATA** to be returned, sets **WnodeHeader.Timestamp** to the value returned by **KeQuerySystemTime**, and sets **WnodeHeader.Flags** as appropriate for the data to be returned.

-   Sets **InstanceCount** to the number of instances to be returned.

-   If the block uses dynamic instance names, sets **OffsetInstanceNameOffsets** to the offset in bytes from the beginning of the **WNODE\_ALL\_DATA** to where an array of ULONG offsets begins. Each element in this array is the offset from the **WNODE\_ALL\_DATA** to where each dynamic instance name is stored. Each dynamic instance name is stored as a counted Unicode string where the count is a USHORT followed by the Unicode string. The count does not include any terminating null character that may be part of the Unicode string. If the Unicode string does include a terminating null character, this null character must still fit within the size established in **WNodeHeader.BufferSize**.

-   If all instances are the same size:
    -   Sets WNODE\_FLAG\_FIXED\_INSTANCE\_SIZE in **WnodeHeader.Flags** and sets **FixedInstanceSize** to that size, in bytes.
    -   Writes instance data starting at **DataBlockOffset**, with padding so that each instance is aligned to an 8-byte boundary. For example, if **FixedInstanceSize** is 6, the driver adds 2 bytes of padding between instances.
-   If instances vary in size:
    -   Clears WNODE\_FLAG\_FIXED\_INSTANCE\_SIZE in **WnodeHeader.Flags** and writes an array of **InstanceCount** **OFFSETINSTANCEDATAANDLENGTH** structures starting at **OffsetInstanceDataAndLength**. Each **OFFSETINSTANCEDATAANDLENGTH** structure specifies the offset in bytes from the beginning of the **WNODE\_ALL\_DATA** structure to the beginning of the data for each instance, and the length of the data. **DataBlockOffset** is not used.

    -   Writes instance data following the last element of the **OffsetInstanceDataAndLength** array, plus padding so that each instance is aligned to an 8-byte boundary.

If the buffer at **Parameters.WMI.Buffer** is too small to receive all of the data, a driver fills in the needed size in a [**WNODE\_TOO\_SMALL**](https://msdn.microsoft.com/library/windows/hardware/ff566379) structure at **Parameters.WMI.Buffer**. If the buffer is smaller than **sizeof**(**WNODE\_TOO\_SMALL**), the driver fails the IRP and returns STATUS\_BUFFER\_TOO\_SMALL.

## I/O Status Block


If the driver handles the IRP by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI sets **Irp-&gt;IoStatus.Status** and **Irp-&gt;IoStatus.Information** in the I/O status block.

Otherwise, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as the following:

STATUS\_BUFFER\_TOO\_SMALL

STATUS\_WMI\_GUID\_NOT\_FOUND

On success, a driver sets **Irp-&gt;IoStatus.Information** to the number of bytes written to the buffer at **Parameters.WMI.Buffer**.

Operation
---------

A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), that routine calls the driver's [*DpWmiQueryDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine.

If a driver handles an **IRP\_MN\_QUERY\_ALL\_DATA** request, it should do so only if **Parameters.WMI.ProviderId** points to the same device object that the driver passed to [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480). Otherwise, the driver must forward the request to the next-lower driver.

Before handling the request, the driver must determine whether **Parameters.WMI.DataPath** points to a GUID that the driver supports. If not, the driver must fail the IRP and return STATUS\_WMI\_GUID\_NOT\_FOUND.

If the driver supports the data block, it must do the following:

-   Verify that **Parameters.WMI.BufferSize** specifies a buffer that is large enough to receive all the data that the driver will return.

-   Fill in a [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) structure at **Parameters.WMI.Buffer** with data for all instances of that data block.

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

[**KeQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff553068)

[**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813)

[**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834)

[**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372)

 

 




