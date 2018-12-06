---
title: IRP_MJ_QUERY_QUOTA
description: IRP\_MJ\_QUERY\_QUOTA
ms.assetid: eb48b5ef-7eac-49d4-ab23-2d3efe783fa3
keywords: ["IRP_MJ_QUERY_QUOTA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_QUOTA
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_QUERY\_QUOTA


## When Sent


The IRP\_MJ\_QUERY\_QUOTA request is sent by the I/O Manager. This request can be sent, for example, when a user-mode application has called a Microsoft Win32 method such as **IDiskQuotaControl::GetQuotaState**.

## Operation: File System Drivers


If the file system supports disk quotas, the file system driver should extract and decode the file object to determine whether it represents a user open of a file or directory. If it does, the driver should process the query and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the query.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack, unless it needs to explicitly override quota behavior.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a query quota information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="deviceobject--flags"></a>*DeviceObject-&gt;Flags*  
The DO\_BUFFERED\_IO and DO\_DIRECT\_IO flags are used as follows to specify the method by which data is passed to the driver:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag Setting</th>
<th align="left">I/O Method</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>~DO_BUFFERED_IO</p>
<p>&amp; ~DO_DIRECT_IO</p></td>
<td align="left"><p>METHOD_NEITHER</p></td>
</tr>
<tr class="even">
<td align="left"><p>~DO_BUFFERED_IO</p>
<p>&amp; DO_DIRECT_IO</p></td>
<td align="left"><p>METHOD_DIRECT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DO_BUFFERED_IO</p>
<p>&amp; ~DO_DIRECT_IO</p></td>
<td align="left"><p>METHOD_BUFFERED</p></td>
</tr>
<tr class="even">
<td align="left"><p>DO_BUFFERED_IO</p>
<p>&amp; DO_DIRECT_IO</p></td>
<td align="left"><p>METHOD_BUFFERED</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied buffer to be used as an intermediate system buffer, if the DO\_BUFFERED\_IO flag is set in *DeviceObject-&gt;Flags*. Otherwise, this member is set to **NULL**.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied FILE\_QUOTA\_INFORMATION-structured output buffer that receives the quota information for the volume.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_QUERY\_QUOTA and should not be used.

<a href="" id="irpsp--flags"></a>*IrpSp-&gt;Flags*  
This member can be one or more of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>SL_INDEX_SPECIFIED</p></td>
<td align="left"><p>Begin the scan at the entry in the quota list whose index is given by <em>IrpSp-&gt;Parameters.QueryQuota.StartSid</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_RESTART_SCAN</p></td>
<td align="left"><p>Begin the scan at the first entry in the list. If this flag is not set, resume the scan from a previous IRP_MJ_QUERY_QUOTA request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SL_RETURN_SINGLE_ENTRY</p></td>
<td align="left"><p>Return only the first entry that is found.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_QUERY\_QUOTA.

<a href="" id="irpsp--parameters-queryquota-length"></a>*IrpSp-&gt;Parameters.QueryQuota.Length*  
Length, in bytes, of the buffer pointed to by *Irp-&gt;UserBuffer*.

<a href="" id="irpsp--parameters-queryquota-sidlist"></a>*IrpSp-&gt;Parameters.QueryQuota.SidList*  
Optional pointer to a list of SIDs whose quota information is to be returned. Each entry in the list is a [**FILE\_GET\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540298) structure. This structure is defined as follows:

```cpp
typedef struct _FILE_GET_QUOTA_INFORMATION {
    ULONG NextEntryOffset;
    ULONG SidLength;
    SID Sid;
} FILE_GET_QUOTA_INFORMATION, *PFILE_GET_QUOTA_INFORMATION;
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>NextEntryOffset</strong></p></td>
<td align="left"><p>Byte offset of the next FILE_GET_QUOTA_INFORMATION entry, if multiple entries are present in a buffer. This member is zero if no other entries follow this one.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SidLength</strong></p></td>
<td align="left"><p>Length, in bytes, of the <strong>Sid</strong> member.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Sid</strong></p></td>
<td align="left"><p>Security identifier (SID).</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--parameters-queryquota-sidlistlength"></a>*IrpSp-&gt;Parameters.QueryQuota.SidListLength*  
Length, in bytes, of the list of SIDs, if one is specified.

<a href="" id="irpsp--parameters-queryquota-startsid"></a>*IrpSp-&gt;Parameters.QueryQuota.StartSid*  
Optional pointer to a SID that indicates that the returned information is to start with an entry other than the first. This parameter is ignored if a SID list is specified.

## See also


[**FILE\_GET\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540298)

[**FILE\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540342)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCheckQuotaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548279)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_SET\_QUOTA**](irp-mj-set-quota.md)

 

 






