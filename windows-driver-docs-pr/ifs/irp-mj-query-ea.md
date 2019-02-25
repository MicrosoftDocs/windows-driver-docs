---
title: IRP_MJ_QUERY_EA
description: IRP\_MJ\_QUERY\_EA
ms.assetid: 5d60a6e9-e940-44cf-844b-86837b36237a
keywords: ["IRP_MJ_QUERY_EA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_EA
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_QUERY\_EA


## When Sent


The IRP\_MJ\_QUERY\_EA request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers, when a user-mode application has requested information about a file's extended attributes.

## Operation: File System Drivers


If the file system supports extended attributes, the file system driver should process the query and complete the IRP. Otherwise, it should return STATUS\_EAS\_NOT\_SUPPORTED.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing an IRP\_MJ\_QUERY\_EA request:

<a href="" id="deviceobject"></a>*DeviceObject*  
A pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
A pointer to a system-supplied output buffer to be used as an intermediate system buffer. Used for METHOD\_BUFFERED I/O.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
A pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--mdladdress"></a>*Irp-&gt;MdlAddress*  
Address of a memory descriptor list (MDL) describing an output buffer that receives the extended attribute information. Used for METHOD\_DIRECT I/O.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
A pointer to a caller-supplied [**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)-structured output buffer that receives the extended attribute information. Used for METHOD\_NEITHER I/O.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
A pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBJECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_QUERY\_EA and should not be used.

<a href="" id="irpsp--flags"></a>*IrpSp-&gt;Flags*  
Specifies one or more of the following values.

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
<td align="left"><p>Begin the scan at the entry in the extended attribute list whose index is given by <em>IrpSp-&gt;Parameters.QueryEa.EaIndex</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_RESTART_SCAN</p></td>
<td align="left"><p>Begin the scan at the first entry in the list. If this flag is not set, resume the scan from a previous IRP_MJ_QUERY_EA request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SL_RETURN_SINGLE_ENTRY</p></td>
<td align="left"><p>Return only the first entry that is found.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_QUERY\_EA.

<a href="" id="irpsp--parameters-queryea-eaindex"></a>*IrpSp-&gt;Parameters.QueryEa.EaIndex*  
Index of the entry at which to begin scanning the extended-attribute list. This parameter is ignored if the SL\_INDEX\_SPECIFIED flag is not set or if *IrpSp-&gt;Parameters.QueryEa.EaList* points to a nonempty list.

<a href="" id="irpsp--parameters-queryea-ealist"></a>*IrpSp-&gt;Parameters.QueryEa.EaList*  
A pointer to a caller-supplied [**FILE\_GET\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540295)-structured input buffer specifying the extended attributes to be queried.

<a href="" id="irpsp--parameters-queryea-ealistlength"></a>*IrpSp-&gt;Parameters.QueryEa.EaListLength*  
Length in bytes of the buffer pointed to by *IrpSp-&gt;Parameters.QueryEa.EaList*.

<a href="" id="irpsp--parameters-queryea-length"></a>*IrpSp-&gt;Parameters.QueryEa.Length*  
Length in bytes of the output buffer.

Remarks
-------

When a short buffer is supplied and STATUS\_BUFFER\_OVERFLOW is returned, NTFS returns the last whole FILE\_FULL\_EA\_INFORMATION entry that fits. When a short buffer is supplied and STATUS\_BUFFER\_TOO\_SMALL is returned, NTFS could not fit any FILE\_FULL\_EA\_INFORMATION entries.

&gt; \[!Note\]
&gt;   On Windows Vista and later, FAT16 no longer supports extended attributes.

 

## See also


[**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)

[**FILE\_GET\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540295)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCheckEaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548252)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_SET\_EA**](irp-mj-set-ea.md)

 

 






