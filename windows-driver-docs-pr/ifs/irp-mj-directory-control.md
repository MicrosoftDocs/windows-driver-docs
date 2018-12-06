---
title: IRP_MJ_DIRECTORY_CONTROL
description: IRP\_MJ\_DIRECTORY\_CONTROL
ms.assetid: cb1bed36-bcb5-419b-87ca-6d9107ece6d1
keywords: ["IRP_MJ_DIRECTORY_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_DIRECTORY_CONTROL
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_DIRECTORY\_CONTROL


## When Sent


The IRP\_MJ\_DIRECTORY\_CONTROL request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **ReadDirectoryChangesW** or **FindNextVolumeMountPoint** or when a kernel-mode component has called [**ZwQueryDirectoryFile**](https://msdn.microsoft.com/library/windows/hardware/ff567047).

## Operation: File System Drivers


The file system driver should check the minor function code to determine which directory control operation is requested. The following are the valid minor function codes:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IRP_MN_NOTIFY_CHANGE_DIRECTORY</p></td>
<td align="left"><p>Indicates a request for notification of changes to the directory. Usually, instead of satisfying this request immediately, the file system driver holds the IRP in a private queue. When a change occurs to the directory, the file system driver performs the notification, and dequeues and completes the IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IRP_MN_QUERY_DIRECTORY</p></td>
<td align="left"><p>Indicates a directory query request. The types of information that can be queried are file-system-dependent, but generally include the following:</p>
FileBothDirectoryInformation
FileDirectoryInformation
FileFullDirectoryInformation
FileIdBothDirectoryInformation
FileIdFullDirectoryInformation
FileNamesInformation
FileObjectIdInformation
FileReparsePointInformation</td>
</tr>
</tbody>
</table>

 

&gt; \[!Note\]
&gt;   The FileQuotaInformation information class is obsolete. [**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md) should be used instead.

 

After performing the requested operation, the file system driver should complete the IRP.

## Operation: File System Filter Drivers


The filter driver must pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a directory control request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied output buffer that receives the requested information about the contents of the directory.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_DIRECTORY\_CONTROL and should not be used.

<a href="" id="irpsp--flags"></a>*IrpSp-&gt;Flags*  
The following flags can be set for IRP\_MN\_QUERY\_DIRECTORY.

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
<td align="left"><p>Begin the scan at the entry in the directory whose index is given by <em>IrpSp-&gt;Parameters.QueryDirectory.FileIndex</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_RESTART_SCAN</p></td>
<td align="left"><p>Begin the scan at the first entry in the directory. If this flag is not set, resume the scan from a previous IRP_MN_QUERY_DIRECTORY request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SL_RETURN_SINGLE_ENTRY</p></td>
<td align="left"><p>Return only the first entry that is found.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SL_RETURN_ON_DISK_ENTRIES_ONLY</p></td>
<td align="left"><p>Instructs any filters that perform directory virtualization or just-in-time expansion to simply pass the request through to the file system and return entries that are currently on disk.</p></td>
</tr>
</tbody>
</table>

 

The following flag can be set for IRP\_MN\_NOTIFY\_CHANGE\_DIRECTORY:

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
<td align="left"><p>SL_WATCH_TREE</p></td>
<td align="left"><p>Set to <strong>TRUE</strong> if all subdirectories of this directory should also be watched. Set to <strong>FALSE</strong> if only the directory itself is to be watched.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_DIRECTORY\_CONTROL.

<a href="" id="irpsp--minorfunction"></a>*IrpSp-&gt;MinorFunction*  
One of the following:

-   IRP\_MN\_NOTIFY\_CHANGE\_DIRECTORY
-   IRP\_MN\_QUERY\_DIRECTORY

<a href="" id="irpsp--parameters-notifydirectory-completionfilter"></a>*IrpSp-&gt;Parameters.NotifyDirectory.CompletionFilter*  
For more information, see the description of the *CompletionFilter* parameter to [**FsRtlNotifyFullChangeDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff547026).

<a href="" id="irpsp--parameters-notifydirectory-length"></a>*IrpSp-&gt;Parameters.NotifyDirectory.Length*  
Length in bytes of the buffer pointed to by *Irp-&gt;UserBuffer*.

<a href="" id="irpsp--parameters-querydirectory-fileindex"></a>*IrpSp-&gt;Parameters.QueryDirectory.FileIndex*  
Index of the file at which to begin the directory scan. Ignored if the SL\_INDEX\_SPECIFIED flag is not set. This parameter cannot be specified in any Win32 function or kernel-mode support routine. Currently it is used only by the NT virtual DOS machine (NTVDM), which exists only on 32-bit NT-based platforms. Note that the file index is undefined for file systems, such as NTFS, in which the position of a file within the parent directory is not fixed and can be changed at any time to maintain sort order.

<a href="" id="irpsp--parameters-querydirectory-fileinformationclass"></a>*IrpSp-&gt;Parameters.QueryDirectory.FileInformationClass*  
Specifies one of the values described below.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>FileBothDirectoryInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540235" data-raw-source="[&lt;strong&gt;FILE_BOTH_DIR_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540235)"><strong>FILE_BOTH_DIR_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileDirectoryInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540248" data-raw-source="[&lt;strong&gt;FILE_DIRECTORY_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540248)"><strong>FILE_DIRECTORY_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFullDirectoryInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540289" data-raw-source="[&lt;strong&gt;FILE_FULL_DIR_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540289)"><strong>FILE_FULL_DIR_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileIdBothDirectoryInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540303" data-raw-source="[&lt;strong&gt;FILE_ID_BOTH_DIR_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540303)"><strong>FILE_ID_BOTH_DIR_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileIdFullDirectoryInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540310" data-raw-source="[&lt;strong&gt;FILE_ID_FULL_DIR_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540310)"><strong>FILE_ID_FULL_DIR_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileNamesInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540329" data-raw-source="[&lt;strong&gt;FILE_NAMES_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540329)"><strong>FILE_NAMES_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileObjectIdInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540335" data-raw-source="[&lt;strong&gt;FILE_OBJECTID_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540335)"><strong>FILE_OBJECTID_INFORMATION</strong></a> structure for each file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileQuotaInformation</strong></p></td>
<td align="left"><p>This information class is obsolete. <a href="irp-mj-query-quota.md" data-raw-source="[&lt;strong&gt;IRP_MJ_QUERY_QUOTA&lt;/strong&gt;](irp-mj-query-quota.md)"><strong>IRP_MJ_QUERY_QUOTA</strong></a> should be used instead.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileReparsePointInformation</strong></p></td>
<td align="left"><p>Return a single <a href="https://msdn.microsoft.com/library/windows/hardware/ff540354" data-raw-source="[&lt;strong&gt;FILE_REPARSE_POINT_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540354)"><strong>FILE_REPARSE_POINT_INFORMATION</strong></a> structure for the directory.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--parameters-querydirectory-filename"></a>*IrpSp-&gt;Parameters.QueryDirectory.FileName*  
Optional name of a file within the specified directory.

<a href="" id="irpsp--parameters-querydirectory-length"></a>*IrpSp-&gt;Parameters.QueryDirectory.Length*  
Length in bytes of the buffer pointed to by *Irp-&gt;UserBuffer*.

## See also


[**FILE\_BOTH\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540235)

[**FILE\_DIRECTORY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540248)

[**FILE\_FULL\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540289)

[**FILE\_ID\_BOTH\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540303)

[**FILE\_ID\_FULL\_DIR\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540310)

[**FILE\_NAMES\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540329)

[**FILE\_OBJECTID\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540335)

[**FILE\_REPARSE\_POINT\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540354)

[**FsRtlNotifyFullChangeDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff547026)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md)

[**ZwQueryDirectoryFile**](https://msdn.microsoft.com/library/windows/hardware/ff567047)

 

 






