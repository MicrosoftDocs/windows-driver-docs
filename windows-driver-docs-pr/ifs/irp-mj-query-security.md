---
title: IRP_MJ_QUERY_SECURITY
description: IRP\_MJ\_QUERY\_SECURITY
keywords: ["IRP_MJ_QUERY_SECURITY Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_SECURITY
api_type:
- NA
ms.date: 11/28/2017
---

# IRP\_MJ\_QUERY\_SECURITY


## When Sent


The IRP\_MJ\_QUERY\_SECURITY request is sent by the I/O Manager. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **GetSecurityInfo**.

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether it represents a user file or directory open. If it does, the driver should process the query and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the query.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a query security request:

<a href="" id="deviceobject"></a>*DeviceObject*  
A pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
A pointer to an [**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
A pointer to a caller-supplied output buffer that receives a copy of the security descriptor of the specified object. The calling process must have the right to view the specified aspects of the object's security status. The [**SECURITY\_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85)) structure is returned in self-relative format.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
A pointer to the file object that is associated with *DeviceObject*.

On Windows XP and later, the file object can represent a named data stream. For more information about named data streams, see [**FILE\_STREAM\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information).

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBJECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_QUERY\_SECURITY and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_QUERY\_SECURITY.

<a href="" id="irpsp--parameters-querysecurity-length"></a>*IrpSp-&gt;Parameters.QuerySecurity.Length*  
The size, in bytes, of the buffer pointed to by the *Irp-&gt;UserBuffer* parameter.

<a href="" id="irpsp--parameters-querysecurity-securityinformation"></a>*IrpSp-&gt;Parameters.QuerySecurity.SecurityInformation*  
A pointer to the [**SECURITY\_INFORMATION**](security-information.md) structure for the operation.

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
<td align="left"><p>OWNER_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the owner identifier of the object is being queried. Requires READ_CONTROL access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GROUP_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the primary group identifier of the object is being queried. Requires READ_CONTROL access.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the discretionary access control list (DACL) of the object is being queried. Requires READ_CONTROL access.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SACL_SECURITY_INFORMATION</p></td>
<td align="left"><p>Indicates that the system ACL (SACL) of the object is being queried. Requires ACCESS_SYSTEM_SECURITY access.</p></td>
</tr>
</tbody>
</table>

 

## See also


[**FILE\_STREAM\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)

[**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP\_MJ\_SET\_SECURITY**](irp-mj-set-security.md)

[**SECURITY\_DESCRIPTOR**](/previous-versions/windows/hardware/drivers/ff556610(v=vs.85))

[**SECURITY\_INFORMATION**](security-information.md)

 

