---
title: WDI doc change history
description: .
ms.assetid: 29268059-9C33-4768-8F80-195CB28B4663
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDI doc change history


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

 

 





