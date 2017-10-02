---
title: IRP_MJ_SET_INFORMATION
author: windows-driver-content
description: Device drivers can optionally handle an IRP\_MJ\_SET\_INFORMATION request.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 1bcca676-2926-4d0f-9c0f-c6ea56481153
keywords:
 - IRP_MJ_SET_INFORMATION Kernel-Mode Driver Architecture
---

# IRP\_MJ\_SET\_INFORMATION


Device drivers can optionally handle an **IRP\_MJ\_SET\_INFORMATION** request.

When Sent
---------

The operating system sends an **IRP\_MJ\_SET\_INFORMATION** request to set metadata about a file or file handle. For example, when a driver calls [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096), the operating system sends an **IRP\_MJ\_SET\_INFORMATION** request.

## Input Parameters


The **Parameters.SetFile.FileInformationClass** member is a **FILE\_INFORMATION\_CLASS** constant that specifies the type of metadata to set. For more information about the types of metadata, see the *FileInformationClass* parameter of [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096).

The **Parameters.SetFile.Length** member specifies the length of the buffer that the **AssociatedIrp.SystemBuffer** member points to.

**AssociatedIrp.SystemBuffer** points to the buffer that contains the new information setting. The value of **Parameters.SetFile.FileInformationClass** determines the format of the data (a **FILE\_*XXX*\_INFORMATION** structure) to return. For more information about the formats of metadata, see the [**FILE\_INFORMATION\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff728840) enumeration.

## Output Parameters


None

Operation
---------

Drivers are not required to handle this request, and drivers that do are not required to handle every possible value of **Parameters.SetFile.FileInformationClass**. The driver's dispatch routine should return an error code such as STATUS\_INVALID\_DEVICE\_REQUEST for any values that it does not handle.

Not all of the possible values of [**FILE\_INFORMATION\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff728840) can occur.

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


[**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_SET_INFORMATION%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


