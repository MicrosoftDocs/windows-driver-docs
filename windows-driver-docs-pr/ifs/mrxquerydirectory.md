---
title: MRxQueryDirectory routine
description: The MRxQueryDirectory routine is called by RDBSS to request that a network mini-redirector query information on a file directory.
ms.assetid: 26c7c7fa-7dfa-43fb-a1db-cfc2fc40b969
keywords: ["MRxQueryDirectory routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxQueryDirectory
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxQueryDirectory routine


The *MRxQueryDirectory* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector query information on a file directory.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxQueryDirectory;

NTSTATUS MRxQueryDirectory(
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

*MRxQueryDirectory* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_INVALID_NETWORK_RESPONSE</strong></td>
<td align="left"><p>An invalid file information buffer was received from the remote server or a filename length that was returned exceeded the maximum allowed length.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid FileInformationClass was specified in the <strong>Info.FileInformationClass</strong> member in the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_LINK_FAILED</strong></td>
<td align="left"><p>The attempt to reconnect to a remote server to complete the query failed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NO_SUCH_FILE</strong></td>
<td align="left"><p>The query failed to find any entries.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_SHARING_VIOLATION</strong></td>
<td align="left"><p>A sharing violation occurred.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Before calling *MRxQueryDirectory*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.FileInformationClass** member is set to **IrpSp-&gt;Parameters.QueryDirectory.FileInformationClass**.

The **Info.Buffer** member is set to user buffer from I/O request packet. This buffer has already been locked by RDBSS if needed.

The **Info.LengthRemaining** member is set to **IrpSp-&gt;Parameters.QueryDirectory.Length**.

The **QueryDirectory.FileIndex** member is set to **IrpSp-&gt;Parameters.QueryDirectory.FileIndex**.

The **QueryDirectory.RestartScan** member is set to nonzero if **IrpSp-&gt;Flags** has the SL\_RESTART\_SCAN bit on.

The **QueryDirectory.ReturnSingleEntry** member is set to nonzero if **IrpSp-&gt;Flags** has the SL\_RETURN\_SINGLE\_ENTRY bit on.

The **QueryDirectory.IndexSpecified** member is set to nonzero if **IrpSp-&gt;Flags** has the SL\_INDEX\_SPECIFIED bit on.

The **QueryDirectory.InitialQuery** member is set to nonzero if **UnicodeQueryTemplate.Buffer** member of the associated FOBX is **NULL** and the **Flags** member of the FOBX does not have the FOBX\_FLAG\_MATCH\_ALL bit on.

For a wild card query ("\*.\*", for example), RDBSS will set the **UnicodeQueryTemplate.Buffer** member of the associated FOBX to the wild card query passed.

If the **PostRequest** member of the RX\_CONTEXT structure is **TRUE** on return from *MRxQueryDirectory*, then RDBSS will call [**RxFsdPostRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554472) passing the RX\_CONTEXT structure to a worker queue for processing by the file system process (FSP).

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

[**MRxQueryEaInfo**](mrxqueryeainfo.md)

[**MRxQueryFileInfo**](mrxqueryfileinfo.md)

[**MRxQueryQuotaInfo**](mrxqueryquotainfo.md)

[**MRxQuerySdInfo**](mrxquerysdinfo.md)

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

[**RxFsdPostRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554472)

 

 






