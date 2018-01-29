---
title: MRxQueryQuotaInfo routine
description: The MRxQueryQuotaInfo routine is called by RDBSS to request that a network mini-redirector query quota information on a file system object.
ms.assetid: 44bf976b-09bc-4270-8c2e-8e55784aaa38
keywords: ["MRxQueryQuotaInfo routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxQueryQuotaInfo
api_location:
- mrx.h
api_type:
- UserDefined
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MRxQueryQuotaInfo routine


The *MRxQueryQuotaInfo* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector query quota information on a file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxQueryQuotaInfo;

NTSTATUS MRxQueryQuotaInfo(
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

*MRxQueryQuotaInfo* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><p>The buffer to receive the quota information was too small.</p>
<p>This return value should be considered success and as much valid data as possible should be returned in the <strong>Info.Buffer</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_BUFFER_TOO_SMALL</strong></td>
<td align="left"><p>The buffer is too small to receive the requested data.</p>
<p>If this value is returned, the <strong>InformationToReturn</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter should be set to the minimum size of the expected buffer for the call to succeed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_CONNECTION_DISCONNECTED</strong></td>
<td align="left"><p>The connection was disconnected. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the query. This is an error code.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified. This is an error code.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>Quotas are not supported.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS issues a call to *MRxQueryQuotaInfo* in response to receiving an [**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md) request.

Before calling *MRxQueryQuotaInfo*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **Info.Buffer** member is set to user buffer from I/O request packet. This buffer has already been locked by RDBSS if needed.

The **Info.LengthRemaining** member is set to **IrpSp-&gt;Parameters.QueryQuota.Length**.

The **QueryQuota.SidList** member is set to **IrpSp-&gt;Parameters.QueryQuota.SidList**.

The **QueryQuota.SidListLength** member is set to **IrpSp-&gt;Parameters.QueryQuota.SidListLength**.

The **QueryQuota.StartSid** member is set to **IrpSp-&gt;Parameters.QueryQuota.StartSid**.

The **QueryQuota.Length** member is set to **IrpSp-&gt;Parameters.QueryQuota.Length**.

The **QueryQuota.RestartScan** member is set to nonzero if **IrpSp-&gt;Flags** has the SL\_RESTART\_SCAN bit set.

The **QueryQuota.ReturnSingleEntry** member is set to nonzero if **IrpSp-&gt;Flags** has the SL\_RETURN\_SINGLE\_ENTRY bit set.

The **QueryQuota.IndexSpecified** member is set to nonzero if **IrpSp-&gt;Flags** has the SL\_INDEX\_SPECIFIED bit set.

On success, the network mini-redirector should set the **Info.LengthRemaining** member of the RX\_CONTEXT structure to the length of the quota information to return. If the call to *MRxQueryQuotaInfo* was successful, RDBSS sets the **IoStatus.Information** member of the IRP to the **Info.LengthRemaining** member of RX\_CONTEXT.

If the call to *MRxQueryQuotaInfo* is successful, the **InformationToReturn** member of the RX\_CONTEXT structure should be set to the length of quota information returned. If the call is unsuccessful, the **InformationToReturn** member of RX\_CONTEXT should be set to zero.

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

[**MRxQuerySdInfo**](mrxquerysdinfo.md)

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20MRxQueryQuotaInfo%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





