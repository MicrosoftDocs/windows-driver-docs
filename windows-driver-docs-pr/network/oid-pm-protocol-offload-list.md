---
title: OID_PM_PROTOCOL_OFFLOAD_LIST
author: windows-driver-content
description: As a query, overlying drivers can use the OID\_PM\_PROTOCOL\_OFFLOAD\_LIST OID to enumerate the protocol offloads that are set on an underlying network adapter.
ms.assetid: 95ace77b-e583-4611-8460-af67b4d4805d
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_PM_PROTOCOL_OFFLOAD_LIST Network Drivers Starting with Windows Vista
---

# OID\_PM\_PROTOCOL\_OFFLOAD\_LIST


As a query, overlying drivers can use the OID\_PM\_PROTOCOL\_OFFLOAD\_LIST OID to enumerate the protocol offloads that are set on an underlying network adapter. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a list of [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structures that describe the currently active protocol offloads.

Remarks
-------

NDIS handles the query for miniport drivers. NDIS drivers can use the OID\_PM\_PROTOCOL\_OFFLOAD\_LIST OID to get a list of protocol offloads that are set on an underlying network adapter.

For each [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure in the list, NDIS sets the **NextProtocolOffloadOffset** member to the offset from the beginning of the OID information buffer (that is, the beginning of the buffer that the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure points to) to the beginning of the next NDIS\_PM\_PROTOCOL\_OFFLOAD structure in the list. The offset in the **NextProtocolOffloadOffset** member of the last structure in the list is zero.

If there are no protocol offloads that are set on the network adapter, NDIS sets the **DATA.QUERY\_INFORMATION.BytesWritten** member of the NDIS\_OID\_REQUEST structure to zero and returns NDIS\_STATUS\_SUCCESS. The data within the **DATA.QUERY\_INFORMATION.InformationBuffer** member is not modified by NDIS.

NDIS returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** contains a pointer to a list of protocol offloads, if any.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later. Not requested for miniport drivers. (See Remarks section.)</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PM_PROTOCOL_OFFLOAD_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


