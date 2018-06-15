---
title: WDI doc change history
description: This section lists documentation change history for WDI documentation pages
ms.assetid: 29268059-9C33-4768-8F80-195CB28B4663
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDI doc change history

## Windows 10, version 1809

Documentation updated to WDI version 1.1.7.

| Topic | Description |
| --- | --- |
| [**WDI_PHY_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_phy_type) | Added support for 802.11ax PHY. |
| [**WDI_CONNECTION_QUALITY_HINT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_connection_quality_hint) | Changed the name of the **WDI_CONNECTION_QUALITY_HIGH_CHANNEL_AVAILABILITY** value to **WDI_CONNECTION_QUALITY_HIGH_THROUGHPUT**. No change to the description of this value. |
| [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) | Added support for unsolicited device service notifications. |

## Windows 10, version 1803

Documentation updated to WDI version 1.1.6.

| Topic | Description |
| --- | --- |
| [**WDI_TLV_OS_POWER_MANAGEMENT_FEATURES**](wdi-tlv-os-power-management-features.md) | Added this TLV to [OID_WDI_GET_ADAPTER_CAPABILITIES](oid-wdi-get-adapter-capabilities.md) to indicate which OS power management (PM) features that the driver supports. |
| [**WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY**](wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) | Updated this TLV to specify that drivers must now return GTK/iGTK key info, if configured, when queried in [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md). |
| [NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED](ndis-status-wdi-indication-cipher-key-updated.md) | Added this indication for drivers to provide notifications of GTK/iGTK key updates when the keys are updated, while the driver is not in the Offload state. |
| [*MINIPORT_WDI_TX_SUSPECT_FRAME_LIST_ABORT*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dot11wdi/nc-dot11wdi-miniport_wdi_tx_suspect_frame_list_abort) | Updated *TxSuspectFrameListAbortHandle* to *TxSuspectFrameListAbort*. |

## Windows 10, version 1709

Documentation updated to WDI version 1.1.5.

| Topic | Description |
| --- | --- |
| [WDI_TLV_TCP_OFFLOAD_CAPABILITIES](wdi-tlv-tcp-offload-capabilities.md) | Added new [**WDI_TLV_OFFLOAD_SCOPE**](wdi-tlv-offload-scope.md) parameter to indicate whether offloads specified apply to the STA port only or to all ports. |
| [NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE](ndis-status-wdi-indication-send-ap-association-response-complete.md) | Changed the [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md) parameter to make it required. |
| [User-initiated feedback with IHV trace logging](user-initiated-feedback-with-ihv-trace-logging.md) | Added a new section describing how to add IHV logging to user-initiated feedback scenarios. |

## Windows 10, version 1607


Documentation updated to WDI version 1.0.21.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_WDI_TASK_P2P_DISCOVER](https://msdn.microsoft.com/library/windows/hardware/dn925955)</p></td>
<td align="left"><p>Added new task parameters:</p>
<ul>
<li>[<strong>WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769912)</li>
<li>[<strong>WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769913)</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_WDI_GET_ADAPTER_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/dn925838)</p></td>
<td align="left"><p>Added new get property result: [<strong>WDI_TLV_SUPPORTED_GUIDS</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769918)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WDI_CIPHER_ALGORITHM</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897802)</p></td>
<td align="left"><p>Added new value: <strong>WDI_CIPHER_ALGO_GCMP</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WDI_PHY_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926105)</p></td>
<td align="left"><p>Added new value: <strong>WDI_PHY_TYPE_DMG</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WDI_P2P_SERVICE_DISCOVERY_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926101)</p></td>
<td align="left"><p>Added new values:</p>
<ul>
<li><strong>WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY</strong></li>
<li><strong>WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION</strong></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769911)</p>
<p>[<strong>WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769912)</p>
<p>[<strong>WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769913)</p>
<p>[<strong>WDI_TLV_P2P_INSTANCE_NAME</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769914)</p>
<p>[<strong>WDI_TLV_P2P_INSTANCE_NAME_HASH</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769915)</p>
<p>[<strong>WDI_TLV_P2P_SERVICE_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769916)</p>
<p>[<strong>WDI_TLV_P2P_SERVICE_TYPE_HASH</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769917)</p>
<p>[<strong>WDI_TLV_SUPPORTED_GUIDS</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769918)</p></td>
<td align="left"><p>Newly added TLVs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WDI_TLV_P2P_ADVERTISED_SERVICES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897860)</p></td>
<td align="left"><p>Added contained TLV: [<strong>WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY</strong>](https://msdn.microsoft.com/library/windows/hardware/mt769911)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WDI_TLV_INTERFACE_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897836)</p></td>
<td align="left"><p>Added a new value that specifies if the device supports IP docking capability.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WDI_TLV_P2P_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897865)</p></td>
<td align="left"><p>Added a new value that specifies if ASP2 Service Names Discovery is supported.</p>
<p>Added a new value that specifies if ASP2 Service Information Discovery is supported.</p></td>
</tr>
</tbody>
</table>

 

## March 2016


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<em>MINIPORT_WDI_TX_TARGET_DESC_DEINIT</em>](https://msdn.microsoft.com/library/windows/hardware/mt297593)</p></td>
<td align="left"><p>Added note that the IHV miniport is not permitted to make any indication in the context of this call.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<em>MINIPORT_WDI_TX_TARGET_DESC_INIT</em>](https://msdn.microsoft.com/library/windows/hardware/mt297594)</p></td>
<td align="left"><p>Added note that the IHV miniport is not permitted to make any indication in the context of this call.</p></td>
</tr>
</tbody>
</table>

 

## Windows 10, version 1511


Documentation updated to WDI version 1.0.10.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_WDI_TASK_START_AP](https://msdn.microsoft.com/library/windows/hardware/dn925964)</p></td>
<td align="left"><p>Added a new task parameter: [<strong>WDI_TLV_AP_BAND_CHANNEL</strong>](https://msdn.microsoft.com/library/windows/hardware/mt593242).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_WDI_SET_ADAPTER_CONFIGURATION](https://msdn.microsoft.com/library/windows/hardware/dn925853)</p></td>
<td align="left"><p>Added a new task parameter: [<strong>WDI_TLV_PLDR_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/hardware/mt593243).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WDI_TLV_AP_BAND_CHANNEL</strong>](https://msdn.microsoft.com/library/windows/hardware/mt593242)</p></td>
<td align="left"><p>Newly added TLV.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WDI_TLV_P2P_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897865)</p></td>
<td align="left"><p>Added a new value that specifies whether the adapter supports operating a GO on the 5GHz band.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WDI_TLV_PLDR_SUPPORT</strong>](https://msdn.microsoft.com/library/windows/hardware/mt593243)</p></td>
<td align="left"><p>Newly added TLV.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WDI_TLV_START_AP_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898065)</p></td>
<td align="left"><p>Added a new value that specifies whether to allow legacy SoftAP clients to connect.</p>
<p>Added a new value that specifies whether the AP can only be started on the channels specified in [OID_WDI_TASK_START_AP](https://msdn.microsoft.com/library/windows/hardware/dn925964) task parameters with [<strong>WDI_TLV_AP_BAND_CHANNEL</strong>](https://msdn.microsoft.com/library/windows/hardware/mt593242).</p></td>
</tr>
</tbody>
</table>

 

## Windows 10


Initial version.

 

 





