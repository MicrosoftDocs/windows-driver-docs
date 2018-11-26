---
title: WDI_TLV_P2P_CAPABILITIES
description: WDI_TLV_P2P_CAPABILITIES is a TLV that contains Wi-Fi Direct capabilities.
ms.assetid: 3BE13A87-ECA2-4204-87F1-2BE393F33D4C
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CAPABILITIES


WDI\_TLV\_P2P\_CAPABILITIES is a TLV that contains Wi-Fi Direct capabilities.

## TLV Type


0x17

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT8</td>
<td>Specifies the concurrent Group Owner count.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies the concurrent Client count.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the supported WPS version.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether Service discovery is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Wi-Fi Direct Service Names Discovery support. Specifies whether, when given a list of service name hashes, the adapter can probe for service hashes and indicate the responses as they arrive.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Wi-Fi Direct Service Information Discovery support. Specifies whether, when given a list of service name hashes, the adapter can perform probes and ANQP queries to get full service information.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>Specifies the maximum supported number of Service Name Advertisements bytes (to be sent in the beacon and probe responses). This sets a hard limit on the number of services that can be advertised.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Specifies the maximum supported number of Service Information Advertisement bytes the adapter can respond to using the GAS protocol. This is only valid if the device supports responding to Service Advertisement queries. This value is for firmware optimization so that the firmware does not wake up the host to respond to every query. The operating system does not limit the number of service advertisements if the firmware has a limitation because there is a fallback in the operating system. If the firmware cannot handle the ANQP query response, it should pass up the request and the operating system handles it.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Background discovery of Wi-Fi Direct devices and services. Specifies whether the adapter can periodically query for Wi-Fi Direct devices and service names so any new devices show up within 5 minutes of becoming visible.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether Client Discoverability is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether infrastructure management is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The maximum size of the secondary adapter type list.</td>
</tr>
<tr class="odd">
<td>UINT8[6]</td>
<td>The device address in network byte order.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The discovery filter list size.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The GO client table size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum size, in bytes, of vendor specific extension IEs that can be added to WFD management frames.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether the adapter supports OID_WDI_P2P_LISTEN_STATE_PASSIVE_AVAILABILITY.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether the adapter supports indicating updates to the GO operating channel(s).
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Added in Windows 10, version 1511, WDI version 1.0.10.
<p>Specifies whether the adapter supports operating a GO on the 5GHz band.</p>
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td><p>UINT8</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
Specifies if the adapter, when provided with a list of ASP2 Service name instances, can probe for service hashes and indicate the responses as they arrive. Valid values are 0 (not supported) and 1 (supported).</td>
</tr>
<tr class="odd">
<td><p>UINT8</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
Specifies if the adapter, when given a set of service name instances, can perform probes and ANQP queries to get the full service information. Valid values are 0 (not supported) and 1 (supported).</td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




