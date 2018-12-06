---
title: MRxSetFileInfo routine
description: The MRxSetFileInfo routine is called by RDBSS to request that a network mini-redirector set file information on a file system object.
ms.assetid: 4fd8cdc4-2973-4a91-b773-c84cf6f64f70
keywords: ["MRxSetFileInfo routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxSetFileInfo
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxSetFileInfo routine


The *MRxSetFileInfo* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector set file information on a file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxSetFileInfo;

NTSTATUS MRxSetFileInfo(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

Parameters
----------

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

Return value
------------

*MRxSetFileInfo* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>STATUS_ACCESS_DENIED</strong></td>
<td align="left"><p>The caller lacked the proper security for this operation.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the query.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NETWORK_ACCESS_DENIED</strong></td>
<td align="left"><p>Network access was denied. This error can be returned if the network mini-redirector was asked to set file information on a read-only share.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>A feature that is requested, such as setting file information on a remote page file, is not implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_OBJECT_NAME_NOT_FOUND</strong></td>
<td align="left"><p>The object name was not found. This error can be returned if the network mini-redirector was asked to set file information on a file, but the file doesn&#39;t exist.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_OBJECT_PATH_NOT_FOUND</strong></td>
<td align="left"><p>The object path was not found. This error can be returned if an NTFS stream object was passed and the remote file system does not support streams.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_ONLY_IF_CONNECTED</strong></td>
<td align="left"><p>The SRV_OPEN structure is not connected.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_REPARSE</strong></td>
<td align="left"><p>A reparse is required to handle a symbolic link.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS issues a call to *MRxSetFileInfo* in response to receiving an [**IRP\_MJ\_SET\_INFORMATION**](irp-mj-set-information.md) request.

Before calling *MRxSetFileInfo*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.FileInformationClass** member is set to **IrpSp-&gt;Parameters.SetFile.FileInformationClass**, the specified FILE\_INFORMATION\_CLASS value.

The **Info.Buffer** member is set to **Irp-&gt;AssociatedIrp.SystemBuffer**.

The **Info.Length** member is set to **IrpSp-&gt;Parameters.SetFile.Length**.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Mrx.h (include Mrx.h)</td>
</tr>
</tbody>
</table>

## See also


[**MRxIsValidDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff550696)

[**MRxQueryDirectory**](mrxquerydirectory.md)

[**MRxQueryEaInfo**](mrxqueryeainfo.md)

[**MRxQueryFileInfo**](mrxqueryfileinfo.md)

[**MRxQueryQuotaInfo**](mrxqueryquotainfo.md)

[**MRxQuerySdInfo**](mrxquerysdinfo.md)

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

 

 






