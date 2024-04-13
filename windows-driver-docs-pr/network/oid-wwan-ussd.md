---
title: OID_WWAN_USSD
ms.topic: reference
description: OID_WWAN_USSD sends Unstructured Supplementary Service Data (USSD) requests to the underlying MB device.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_USSD Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_USSD


OID\_WWAN\_USSD sends Unstructured Supplementary Service Data (USSD) requests to the underlying MB device.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [NDIS\_STATUS\_WWAN\_USSD](./ndis-status-wwan-ussd.md) status notification containing the status of the initial USSD request when they have completed the transaction.

Windows does not send an OID\_WWAN\_USSD request to a miniport driver if a previous request is still in progress, with the exception of a request to cancel a pending operation by setting the [WWAN\_USSD\_REQUEST](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_ussd_request) **RequestType** member of the request to *WwanUssdRequestCancel*.

When a request is canceled, the miniport driver must respond to both the canceled request and the cancel request.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[NDIS\_STATUS\_WWAN\_USSD](./ndis-status-wwan-ussd.md)

[WWAN\_USSD\_REQUEST](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_ussd_request)

 

