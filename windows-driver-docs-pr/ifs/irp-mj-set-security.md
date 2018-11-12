---
title: IRP_MJ_SET_SECURITY
description: IRP\_MJ\_SET\_SECURITY
ms.assetid: 8d8b06b9-5d63-4506-831c-9c533dbe95f4
keywords: ["IRP_MJ_SET_SECURITY Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_SECURITY
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_SET\_SECURITY


## When Sent


The IRP\_MJ\_SET\_SECURITY request is sent by the I/O Manager. This request can be sent, for example, when a user-mode application has called a Win32 function such as **SetSecurityInfo**.

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether it represents a user file or directory open. If it does, the driver should process the request and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the request.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set security information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
A pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
A pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
A pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_SET\_SECURITY and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_SET\_SECURITY.

<a href="" id="irpsp--parameters-setsecurity-securitydescriptor"></a>*IrpSp-&gt;Parameters.SetSecurity.SecurityDescriptor*  
A pointer to a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610) structure that contains the values of the security information to be assigned to the object.

<a href="" id="irpsp--parameters-setsecurity-securityinformation"></a>*IrpSp-&gt;Parameters.SetSecurity.SecurityInformation*  
A value of type [**SECURITY\_INFORMATION**](security-information.md) that specifies which security information is to be set in the security descriptor. This value can be one of the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SecurityInformation Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the discretionary access control list (DACL) of the object is being set. Requires WRITE_DAC access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GROUP_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the primary group identifier of the object is being set. Requires WRITE_OWNER access.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>OWNER_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the owner identifier of the object is being set. Requires WRITE_OWNER access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the system ACL (SACL) of the object is being set. Requires ACCESS_SYSTEM_SECURITY access.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_SECURITY**](irp-mj-query-security.md)

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff556610)

[**SECURITY\_INFORMATION**](security-information.md)

 

 






