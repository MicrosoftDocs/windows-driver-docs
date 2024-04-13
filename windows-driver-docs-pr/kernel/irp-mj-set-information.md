---
title: IRP_MJ_SET_INFORMATION
description: Device drivers can optionally handle an IRP_MJ_SET_INFORMATION request.
ms.date: 08/12/2017
ms.topic: reference
keywords:
 - IRP_MJ_SET_INFORMATION Kernel-Mode Driver Architecture
---

# IRP\_MJ\_SET\_INFORMATION


Device drivers can optionally handle an **IRP\_MJ\_SET\_INFORMATION** request.

## When Sent

The operating system sends an **IRP\_MJ\_SET\_INFORMATION** request to set metadata about a file or file handle. For example, when a driver calls [**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile), the operating system sends an **IRP\_MJ\_SET\_INFORMATION** request.

## Input Parameters


The **Parameters.SetFile.FileInformationClass** member is a **FILE\_INFORMATION\_CLASS** constant that specifies the type of metadata to set. For more information about the types of metadata, see the *FileInformationClass* parameter of [**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile).

The **Parameters.SetFile.Length** member specifies the length of the buffer that the **AssociatedIrp.SystemBuffer** member points to.

**AssociatedIrp.SystemBuffer** points to the buffer that contains the new information setting. The value of **Parameters.SetFile.FileInformationClass** determines the format of the data (a **FILE\_*XXX*\_INFORMATION** structure) to return. For more information about the formats of metadata, see the [**FILE\_INFORMATION\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class) enumeration.

## Output Parameters


None

## Operation

Drivers are not required to handle this request, and drivers that do are not required to handle every possible value of **Parameters.SetFile.FileInformationClass**. The driver's dispatch routine should return an error code such as STATUS\_INVALID\_DEVICE\_REQUEST for any values that it does not handle.

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


[**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile)

 

