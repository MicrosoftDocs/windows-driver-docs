---
title: IRP_MN_CHANGE_SINGLE_INSTANCE
author: windows-driver-content
description: All drivers that support WMI must handle this IRP.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 180d40a4-b300-4801-b9da-9239500ca15f
keywords:
 - IRP_MN_CHANGE_SINGLE_INSTANCE Kernel-Mode Driver Architecture
---

# IRP\_MN\_CHANGE\_SINGLE\_INSTANCE


All drivers that support WMI must handle this IRP. A driver can handle WMI IRPs either by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) or by handling the IRP itself, as described in [Handling WMI Requests](https://msdn.microsoft.com/library/windows/hardware/ff546968).

If a driver calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) to handle an **IRP\_MN\_CHANGE\_SINGLE\_INSTANCE** request, WMI in turn calls that driver's [*DpWmiSetDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544104) routine.

Major Code
----------

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)
When Sent
---------

WMI sends this IRP to change all data items in a single instance of a data block.

WMI sends this IRP at IRQL = PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


**Parameters.WMI.ProviderId** points to the device object of the driver that should respond to the request. This pointer is found in the driver's I/O stack location in the IRP.

**Parameters.WMI.DataPath** points to a GUID that identifies the data block associated with the instance to be changed.

**Parameters.WMI.BufferSize** indicates the size of the nonpaged buffer at **Parameters.WMI.Buffer**.

**Parameters.WMI.Buffer** points to a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure that identifies the instance and specifies new data values.

## Output Parameters


None.

## I/O Status Block


If the driver handles the IRP by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), WMI sets **Irp-&gt;IoStatus.Status** and **Irp-&gt;IoStatus.Information** in the I/O status block.

Otherwise, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as the following:

STATUS\_WMI\_INSTANCE\_NOT\_FOUND

STATUS\_WMI\_GUID\_NOT\_FOUND

STATUS\_WMI\_READ\_ONLY

STATUS\_WMI\_SET\_FAILURE

On success, the driver sets **Irp-&gt;IoStatus.Information** to zero.

Operation
---------

If a driver handles WMI IRPs by calling [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834), that routine calls the driver's [*DpWmiSetDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544104) routine, or returns STATUS\_WMI\_READ\_ONLY if the driver does not define the routine.

If a driver handles an **IRP\_MN\_CHANGE\_SINGLE\_INSTANCE** request itself, it does so only if the device object pointer at **Parameters.WMI.ProviderId** matches the pointer passed by the driver in its call to [**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480). Otherwise, the driver must forward the request to the next-lower driver.

If the driver handles the request, it must first check the GUID at **Parameters.WMI.DataPath** to determine whether it identifies a data block supported by the driver. If not, the driver must fail the IRP and return STATUS\_WMI\_GUID\_NOT\_FOUND.

If the driver supports the data block, it must check the received [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure at **Parameters.WMI.Buffer** for the instance name, as follows:

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is set in **WnodeHeader.Flags**, the driver uses **InstanceIndex** as an index into the driver's list of static instance names for that block. WMI obtains the index from registration data provided by the driver when it registered the block.

-   If WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES is clear in **WnodeHeader.Flags,** the driver uses the offset at **OffsetInstanceName** to locate the instance name string in the input [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377). **OffsetInstanceName** is the offset in bytes from the beginning of the structure to a USHORT-sized length of the instance name string in bytes (not characters), including the terminating null if present, followed by the instance name string in Unicode.

The driver is responsible for validating all input values. Specifically, the driver must do the following if it handles the IRP request itself:

-   For static names, verify that the **InstanceIndex** member of the [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure is within the range of instance indexes supported by the driver for the data block.

-   For dynamic names, verify that the instance name string identifies a data block instance supported by the driver.

-   Verify that the **DataBlockOffset** and **SizeDataBlock** members of the **WNODE\_SINGLE\_INSTANCE** structure describe a valid-sized data block, including any padding that exists between data items, and that the contents of the buffer are valid for the data block.

-   Verify that the specified data block is one for which the driver allows caller-initiated modifications. In other words, the driver should not allow modifications to data blocks that you intended to be read-only.

Do not assume the thread context is that of the initiating user-mode application — a higher-level driver might have changed it.

If the driver cannot locate the specified instance, it must fail the IRP and return STATUS\_WMI\_INSTANCE\_NOT\_FOUND. If the instance has a dynamic instance name, this status indicates that the driver does not support the instance. WMI can therefore continue to query other data providers, and return an appropriate error to the data consumer if another provider finds the instance but cannot handle the request for some other reason.

If the driver locates the instance and can handle the request, it sets the writable data items in the instance to the values in the [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) structure, leaving any read-only items unchanged. If the entire data block is read-only, the driver should fail the IRP and return STATUS\_WMI\_READ\_ONLY.

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


[*DpWmiSetDataBlock*](https://msdn.microsoft.com/library/windows/hardware/ff544104)

[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)

[**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813)

[**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834)

[**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_CHANGE_SINGLE_INSTANCE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


