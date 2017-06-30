---
title: WDI Task OIDs
description: This section contains WDI task OIDs.
MS-HAID:
- 'netvista.wdi\_miniport\_driver\_oids'
- 'netvista.wdi\_miniport\_driver\_task\_oids'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: CAA92CA5-5CD6-4705-AA4C-54C1AA83ACA3
---

# WDI Task OIDs


This section contains WDI task OIDs.

The Wi-Fi Driver Interface (WDI) object identifiers (OIDs) apply only to miniport drivers that implement WDI.

The following table specifies whether WDI OID query (Q), set (S), and NDIS 6.0 method (M) requests are required or optional to implement:

<a href="" id="r"></a>**R**  
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning the status code NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

<a href="" id="o"></a>**O**  
Indicates that support for the object is optional. The miniport driver can either support query or set requests for the object, or the driver can fail the request by returning NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Q</th>
<th>S</th>
<th>M</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[OID_WDI_TASK_CHANGE_OPERATION_MODE](oid-wdi-task-change-operation-mode.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_CLOSE](oid-wdi-task-close.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_CONNECT](oid-wdi-task-connect.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_CREATE_PORT](oid-wdi-task-create-port.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_DELETE_PORT](oid-wdi-task-delete-port.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_DISCONNECT](oid-wdi-task-disconnect.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_DOT11_RESET](oid-wdi-task-dot11-reset.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_IHV](oid-wdi-task-ihv.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_OPEN](oid-wdi-task-open.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_P2P_DISCOVER](oid-wdi-task-p2p-discover.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME](oid-wdi-task-p2p-send-request-action-frame.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME](oid-wdi-task-p2p-send-response-action-frame.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_ROAM](oid-wdi-task-roam.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_SCAN](oid-wdi-task-scan.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE](oid-wdi-task-send-ap-association-response.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME](oid-wdi-task-send-request-action-frame.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME](oid-wdi-task-send-response-action-frame.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_SET_RADIO_STATE](oid-wdi-task-set-radio-state.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>R</p></td>
</tr>
<tr class="odd">
<td><p>[OID_WDI_TASK_START_AP](oid-wdi-task-start-ap.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
<tr class="even">
<td><p>[OID_WDI_TASK_STOP_AP](oid-wdi-task-stop-ap.md)</p></td>
<td><p></p></td>
<td><p></p></td>
<td><p>O</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI%20Task%20OIDs%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




