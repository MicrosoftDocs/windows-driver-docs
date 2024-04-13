---
title: IRP_MJ_QUERY_INFORMATION
description: Drivers can optionally handle an IRP_MJ_QUERY_INFORMATION request.
ms.date: 08/12/2017
ms.topic: reference
keywords:
 - IRP_MJ_QUERY_INFORMATION Kernel-Mode Driver Architecture
---

# IRP\_MJ\_QUERY\_INFORMATION


Drivers can optionally handle an **IRP\_MJ\_QUERY\_INFORMATION** request.

## When Sent

The operating system sends an **IRP\_MJ\_QUERY\_INFORMATION** request to obtain metadata about a file or file handle. For example, when a driver calls [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile), the operating system sends an **IRP\_MJ\_QUERY\_INFORMATION** request.

## Input Parameters


The **Parameters.QueryFile.FileInformationClass** member is a **FILE\_INFORMATION\_CLASS** constant that specifies the type of metadata to provide. For more information about the types of metadata, see the *FileInformationClass* parameter of the [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile) routine.

The **Parameters.QueryFile.Length** member specifies the length of the buffer that the **AssociatedIrp.SystemBuffer** member points to.

## Output Parameters


The **AssociatedIrp.SystemBuffer** member points to the buffer where the driver supplies the requested information. The value of **Parameters.QueryFile.FileInformationClass** determines the format of the metadata (a **FILE\_*XXX*\_INFORMATION** structure) to return. For more information about the formats of metadata, see the [**FILE\_INFORMATION\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class) enumeration.

## Operation

Drivers are not required to handle this request, and drivers that do are not required to handle every possible value of **Parameters.QueryFile.FileInformationClass**. The driver's dispatch routine should return an error code such as STATUS\_INVALID\_DEVICE\_REQUEST for any values that it does not handle.

Not all of the possible values of [**FILE\_INFORMATION\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class) can occur.

## Requirements

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


[**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)

 

