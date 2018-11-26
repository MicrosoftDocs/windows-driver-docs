---
title: OID_WWAN_MODEM_CONFIG_INFO
description: OID_WWAN_MODEM_CONFIG_INFO retrieves information about the modem configuration information.
ms.assetid: 527B970C-09FC-4E49-A309-44D5C6A39778
ms.date: 08/08/2017
keywords: 
 - OID_WWAN_MODEM_CONFIG_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_MODEM\_CONFIG\_INFO


OID\_WWAN\_MODEM\_CONFIG\_INFO retrieves information about the modem configuration information.

MBB drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [NDIS\_STATUS\_WWAN\_MODEM\_CONFIG\_INFO](ndis-status-wwan-modem-config-info.md) status notification containing an [**NDIS\_WWAN\_MODEM\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/07C2BAED-157A-459C-B558-115C0091ECE5) structure, which in turn contains a [**WWAN\_MODEM\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/14FBFA51-F4A5-417A-8905-241CEA543774) structure, to provide information about the modem's configuration.

Set requests are not applicable.

Remarks
-------

The MBB driver may not have valid information yet from the modem during early queries. The non-valid information will be set to zero.

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
<td><p>the next major update to Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[NDIS\_STATUS\_WWAN\_MODEM\_CONFIG\_INFO](ndis-status-wwan-modem-config-info.md)

[**NDIS\_WWAN\_MODEM\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/07C2BAED-157A-459C-B558-115C0091ECE5)

[**WWAN\_MODEM\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/14FBFA51-F4A5-417A-8905-241CEA543774)



