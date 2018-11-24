---
title: IRP_MJ_CREATE
description: Every kernel-mode driver must handle IRP_MJ_CREATE requests in a DispatchCreate or DispatchCreateClose routine.
ms.date: 08/12/2017
ms.assetid: 2947f8dc-2e7d-401e-8014-6140cac6905f
keywords:
 - IRP_MJ_CREATE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_CREATE


Every kernel-mode driver must handle **IRP\_MJ\_CREATE** requests in a [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function.

When Sent
---------

The operating system sends an **IRP\_MJ\_CREATE** request to open a handle to a file object or device object. For example, when a driver calls [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), the operating system sends an **IRP\_MJ\_CREATE** request to perform the actual open operation.

## Input Parameters


The **Parameters.Create.SecurityContext** member points to an [**IO\_SECURITY\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff550613) structure that describes the security context for the request. The **Parameters.Create.SecurityContext-&gt;DesiredAccess** member is an access mask that specifies the access rights that are being requested by the caller.

The **Parameters.Create.Options** member is a ULONG value that describes the options that are used when opening the handle. The high 8 bits correspond to the value of the *CreateDisposition* parameter of **ZwCreateFile**, and the low 24 bits correspond to the value of the *CreateOptions* parameter of **ZwCreateFile**.

The **Parameters.Create.ShareAccess** member is a USHORT value that describes the type of share access. This value corresponds to the value of the *ShareAccess* parameter of **ZwCreateFile**.

The **Parameters.Create.FileAttributes** and **Parameters.Create.EaLength** members are reserved for use by file systems and file system filter drivers. For more information, see the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) topic in the Installable File System (IFS) documentation.

## Output Parameters


None

Operation
---------

Most device and intermediate drivers set STATUS\_SUCCESS in the I/O status block of the IRP and complete the create request, but drivers can optionally use their [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function to reserve resources for any subsequent I/O requests for that handle. For example, the system serial driver maps its paged-out code and allocates any resources that are necessary to handle subsequent I/O requests for the user-mode thread that is attempting to open the device for input and output.

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


[*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)

[*DispatchCreateClose*](https://msdn.microsoft.com/library/windows/hardware/ff543270)

[**IO\_SECURITY\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff550613)

[**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)

 

 




