---
title: MRxQueryFileInfo routine
description: TheMRxQueryFileInfo routine is called by RDBSS to request that a network mini-redirector query file information on a file system object.
ms.assetid: 201b749c-527b-4c02-a860-d2f54777dc32
keywords: ["MRxQueryFileInfo routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxQueryFileInfo
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxQueryFileInfo routine


The*MRxQueryFileInfo* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector query file information on a file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxQueryFileInfo;

NTSTATUS MRxQueryFileInfo(
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

*MRxQueryFileInfo* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_BUFFER_OVERFLOW</strong></td>
<td align="left"><p>The buffer to receive the file information was too small.</p>
<p>This return value should be considered success and as much valid data as possible should be returned in the <strong>Info.Buffer</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_BUFFER_TOO_SMALL</strong></td>
<td align="left"><p>The buffer is too small to receive the requested data.</p>
<p>If this value is returned, the <strong>InformationToReturn</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter should be set to the minimum size of the expected buffer for the call to succeed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the query.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INVALID_NETWORK_RESPONSE</strong></td>
<td align="left"><p>An invalid file information buffer was received from the remote server.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified.</p>
<p>This value can be returned if an invalid value for the <strong>FileInformationClass</strong> member in the RX_CONTEXT is passed. This value can also be returned if the <strong>FileInformationClass</strong> member specified is for <strong>FileStreamInformation</strong> and the remote file system does not support streams.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_OBJECT_NAME_NOT_FOUND</strong></td>
<td align="left"><p>The object name was not found. This is an error code.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS issues a call to *MRxQueryFileInfo* in response to receiving an [**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md) request.

Before calling *MRxQueryFileInfo*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.FileInformationClass** member is set to **IrpSp-&gt;Parameters.QueryFile.FileInformationClass**, the requested FILE\_INFORMATION\_CLASS value.

The **Info.Buffer** member is set to the user buffer from the I/O request packet.

The **Info.LengthRemaining** member is set to **IrpSp-&gt;Parameters.QueryFile.Length**.

The **QueryDirectory.FileIndex** member is set to **IrpSp-&gt;Parameters.QueryDirectory.FileIndex**.

The **QueryDirectory.RestartScan** member is set if **IrpSp-&gt;Flags** has the SL\_RESTART\_SCAN bit set.

The **QueryDirectory.ReturnSingleEntry** member is set if **IrpSp-&gt;Flags** has SL\_RETURN\_SINGLE\_ENTRY bit set.

The **QueryDirectory.InitialQuery** member is set if **Fobx-&gt;UnicodeQueryTemplate.Buffer** is **NULL** and **Fobx-&gt;Flags** does not have the FOBX\_FLAG\_MATCH\_ALL bit set.

On success, the network mini-redirector should set the **Info.LengthRemaining** member of the RX\_CONTEXT structure to **Info.Length** member minus the length of the file information returned. If the call to *MRxQueryFileInfo* was successful, RDBSS sets the **IoStatus.Information** member of the IRP to **IrpSp-&gt;Parameters.QueryFile.Length** minus the **Info.LengthRemaining** member of RX\_CONTEXT.

RDBSS does not support requests with the SL\_INDEX\_SPECIFIED bit of the **IrpSp-&gt;Flags** set. A network mini-redirector will not receive calls to *MRxQueryFileInfo* with the SL\_INDEX\_SPECIFIED bit of **IrpSp-&gt;Flags** set.

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

[**MRxQueryQuotaInfo**](mrxqueryquotainfo.md)

[**MRxQuerySdInfo**](mrxquerysdinfo.md)

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

 

 






