---
title: WDI\_TLV\_STATION\_CAPABILITIES
description: WDI\_TLV\_STATION\_CAPABILITIES is a TLV that contains the capabilities of a station.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 567445F1-EEDC-4302-B709-ED76D044A971
keywords: ["WDI_TLV_STATION_CAPABILITIES Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WDI_TLV_STATION_CAPABILITIES
api_location:
- wditypes.hpp
api_type:
- HeaderDef
---

# WDI\_TLV\_STATION\_CAPABILITIES


WDI\_TLV\_STATION\_CAPABILITIES is a TLV that contains the capabilities of a station.

## TLV Type


0x11

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
<td>UINT32</td>
<td>The scan SSID list size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The desired BSSID list size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The desired SSID list size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The privacy exemption list size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The key mapping table size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The default key table size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The maximum length of the WEP key value.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum number per STA default key tables.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Supported QoS flags. Specifies whether the device supports WMM.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether host-FIPS mode is implemented.
<p>If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_OID_SUPPORTED with no other bits set, the driver implements the 802.11 safe mode of operation.</p>
<p>If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_CERTIFIED, the NIC has received a validation certificate from the National Institute of Standards and Technology (NIST) under Federal Information Processing Standards (FIPS) Publication 140-2, Security Requirements for Cryptographic Modules. In this mode, the hardware is responsible for ensuring compliance to FIPS standard.</p>
<p>If the field is set to zero (0), FIPS mode is not implemented by the NIC.</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether 802.11w MFP capability is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether auto power save is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether the adapter maintains the Station BSS List cache.
<p>Valid values are 0 (no) and 1 (yes).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether the adapter may attempt association to a BSSID that is not specified in the Preferred BSSID list during a Station connect.
<p>Valid values are 0 (no) and 1 (yes).</p></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The maximum supported Network Offload List size.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether or not the adapter can track HESSIDs associated with SSIDs and connect/roam only to those APs that match the specified SSID+HESSID.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>Specifies whether the adapter can offload connectivity to networks belonging to specific HESSIDs.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether disconnected standby is supported.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_STATION_CAPABILITIES%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




