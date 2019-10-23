---
title: MB Miniport Driver Performance Requirements
description: MB Miniport Driver Performance Requirements
ms.assetid: 16986208-7572-412d-8839-71f1a66b074f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Miniport Driver Performance Requirements


The following table describes the expectations for MB miniport drivers to respond to different MB operations. For the best experience, miniport drivers should complete operations within the time identified in the "Best case time (sec)" column.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">MB operation</th>
<th align="left">Best case time (sec)</th>
<th align="left">Worst case time (sec)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Time for device to initialize (to reach <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/wwan/ne-wwan-_wwan_ready_state" data-raw-source="[&lt;strong&gt;WwanReadyStateInitialized&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/wwan/ne-wwan-_wwan_ready_state)"><strong>WwanReadyStateInitialized</strong></a>) after being inserted into the machine ( <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-ready-info" data-raw-source="[OID_WWAN_READY_INFO](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-ready-info)">OID_WWAN_READY_INFO</a>)</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p>Manual network registration ( <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-register-state" data-raw-source="[OID_WWAN_REGISTER_STATE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-register-state)">OID_WWAN_REGISTER_STATE</a>)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>50</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Network scan operation ( <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-visible-providers" data-raw-source="[OID_WWAN_VISIBLE_PROVIDERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-visible-providers)">OID_WWAN_VISIBLE_PROVIDERS</a>)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>200</p></td>
</tr>
<tr class="even">
<td align="left"><p>Packet-attach operation ( <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-packet-service" data-raw-source="[OID_WWAN_PACKET_SERVICE](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-packet-service)">OID_WWAN_PACKET_SERVICE</a>)</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Packet-detach operation (OID_WWAN_PACKET_SERVICE)</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p>PDP activation ( <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-connect" data-raw-source="[OID_WWAN_CONNECT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-connect)">OID_WWAN_CONNECT</a>)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PDP deactivation (OID_WWAN_CONNECT)</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Update system with IP address, default gateway, and DNS address</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-link-state" data-raw-source="[&lt;strong&gt;NDIS_STATUS_LINK_STATE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-link-state)"><strong>NDIS_STATUS_LINK_STATE</strong></a> notification after PDP activation</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Completion of the following PIN operations ( <a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pin" data-raw-source="[OID_WWAN_PIN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pin)">OID_WWAN_PIN</a>):</p>
<p>Enter</p>
<p>Enable</p>
<p>Disable</p>
<p>Change</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Query OID_WWAN_PIN to get the current PIN state of the MB device</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pin-list" data-raw-source="[OID_WWAN_PIN_LIST](https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pin-list)">OID_WWAN_PIN_LIST</a> response to get a list of supported PIN types</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Time for SMS subsystem to be ready (should send the NDIS_STATUS_WWAN_SMS_CONFIGURATION unsolicited indication)</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>60</p></td>
</tr>
<tr class="even">
<td align="left"><p>Time for miniport driver to complete all other WWAN OIDs except OID_WWAN_VENDOR_SPECIFIC which are not covered in this table</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>15</p></td>
</tr>
</tbody>
</table>

 

 

 





