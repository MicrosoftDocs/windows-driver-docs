---
title: MRxQueryVolumeInfo routine
description: The MRxQueryVolumeInfo routine is called by RDBSS to request that a network mini-redirector query volume information.
ms.assetid: 28e36992-2b6b-4484-9e7e-2cea7a2953e9
keywords: ["MRxQueryVolumeInfo routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxQueryVolumeInfo
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxQueryVolumeInfo routine


The *MRxQueryVolumeInfo* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector query volume information.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxQueryVolumeInfo;

NTSTATUS MRxQueryVolumeInfo(
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

*MRxQueryVolumeInfo* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><p>The buffer to receive the volume information was too small.</p>
<p>This return value should be considered success and as much valid data as possible should be returned in the <strong>Info.Buffer</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_BUFFER_TOO_SMALL</strong></td>
<td align="left"><p>The buffer is too small to receive the requested data.</p>
<p>If this value is returned, the <strong>InformationToReturn</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter should be set to the minimum size of the expected buffer for the call to succeed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_CONNECTION_DISCONNECTED</strong></td>
<td align="left"><p>The connection was disconnected.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the query.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NETWORK_NAME_DELETED</strong></td>
<td align="left"><p>A network name was deleted.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>A feature that is requested is not implemented.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS issues a call to *MRxQueryVolumeInfo* in either of the following cases:

-   RDBSS receives an [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](irp-mj-query-volume-information.md) request.

-   RDBSS receives an [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md) request for an FSCTL\_LMR\_GET\_LINK\_TRACKING\_INFORMATION control code.

Before calling *MRxQueryVolumeInfo* in the case of an IRP\_MJ\_QUERY\_VOLUME\_INFORMATION request, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.FsInformationClass** member is set to **IrpSp-&gt;Parameters.QueryVolume.FsInformationClass**.

The **Info.Buffer** member is set to **Irp-&gt;AssociatedIrp.SystemBuffer**.

The **Info.LengthRemaining** member is set to **IrpSp-&gt;Parameters.QueryVolume.Length**.

For an IRP\_MJ\_QUERY\_VOLUME\_INFORMATION request, if the **PostRequest** member of the RX\_CONTEXT structure is **TRUE** on return from *MRxQueryVolumeInfo*, RDBSS will call [**RxFsdPostRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554472) to post the request. For this case, the IRP\_MJ\_QUERY\_VOLUME\_INFORMATION request will pass the RX\_CONTEXT structure to queue RX\_CONTEXT to a worker queue for processing by the file system process (FSP).

If the **PostRequest** member of the RX\_CONTEXT structure is **FALSE** on return from *MRxQueryVolumeInfo*, the network mini-redirector must set the **Info.LengthRemaining** member of the RX\_CONTEXT structure to the length of the volume information returned. RDBSS sets the **IoStatus.Information** member of the IRP to **IrpSp-&gt;Parameters.QueryVolume.Length** minus the **Info.LengthRemaining** member of the RX\_CONTEXT structure.

If the call to *MRxQueryVolumeInfo* is successful, the network mini-redirector should set the **Info.LengthRemaining** member of the RX\_CONTEXT structure to the **Info.Length** member minus the length of the volume information returned. If the call to *MRxQueryVolumeInfo* was successful, RDBSS sets the **IoStatus.Information** member of the IRP to **IrpSp-&gt;Parameters.QueryVolume.Length** minus the **Info.LengthRemaining** member of the RX\_CONTEXT structure.

For an IRP\_MJ\_QUERY\_VOLUME\_INFORMATION request with the **Info.FsInformationClass** member set to **FileFsDeviceInformation**, the network mini-redirector returns the following information in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.Buffer** member contains an FILE\_FS\_DEVICE\_INFORMATION structure

The **Info.Buffer.Characteristics** member is set to the characteristics of the volume, which must include FILE\_REMOTE\_DEVICE as one of the options.

The **Info.Buffer.DeviceType** member is set to the **DeviceType** member of the associated NET\_ROOT structure. If the **Type** member of the associated NET\_ROOT is NET\_ROOT\_PIPE, **Info.Buffer.DeviceType** member is set to FILE\_DEVICE\_NAMED\_PIPE.

For an IRP\_MJ\_QUERY\_VOLUME\_INFORMATION request with the **Info.FsInformationClass** member set to **FileFsVolumeInformation**, the network mini-redirector returns the following information in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.Buffer** member contains a FILE\_FS\_VOLUME\_INFORMATION structure.

The **Info.Buffer** member is set to the **VolumeInfo** member of the associated NET\_ROOT structure.

The **Info.LengthRemaining** member is set to the **VolumeInfoLength** member of the associated NET\_ROOT structure.

An *MRxQueryVolumeInfo* call from RDBSS for [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md) is a request for the link tracking information. Before calling *MRxQueryVolumeInfo* for IRP\_MJ\_FILE\_SYSTEM\_CONTROL, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.FsInformationClass** member is set to **FileFsObjectIdInformation**.

The **Info.Buffer** member is set to a FILE\_FS\_OBJECTID\_INFORMATION structure.

The **Info.LengthRemaining** member is set to **sizeof**(FILE\_FS\_OBJECTID\_INFORMATION).

For this case of an IRP\_MJ\_FILE\_SYSTEM\_CONTROL request, the **AssociatedIrp.SystemBuffer** member of the IRP points to a LINK\_TRACKING\_INFORMATION structure.

If a request is initiated as an IRP\_MJ\_FILE\_SYSTEM\_CONTROL to *MRxQueryVolumeInfo* with a return value of STATUS\_SUCCESS or STATUS\_BUFFER\_OVERFLOW, RDBSS copies the **ObjectId** member of the FILE\_FS\_OBJECTID\_INFORMATION structure passed in the **Info.Buffer** member of RX\_CONTEXT structure to the **NetRoot-&gt;DiskParameters.VolumeId** member of the FCB structure and to the **AssociatedIrp.SystemBuffer.VolumeId** member of the IRP. If the call to *MRxQueryVolumeInfo* was successful, RDBSS sets the **Type** member of the LINK\_TRACKING\_INFORMATION structure. If the **NetRoot-&gt;Flags** member of the FCB structure has the NETROOT\_FLAG\_DFS\_AWARE\_NETROOT bit set, the **Type** member is set by RDBSS to **DfsLinkTrackingInformation**. If the **NetRoot-&gt;Flags** member of the FCB structure does not have the NETROOT\_FLAG\_DFS\_AWARE\_NETROOT bit set, the **Type** member is set by RDBSS to **NtfsLinkTrackingInformation**. On success, RDBSS sets the **IoStatus.Information** member of the IRP to the size of a LINK\_TRACKING\_INFORMATION structure.

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

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

[**RxFsdPostRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554472)

 

 






