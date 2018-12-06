---
title: MB Miniport Driver INF Requirements
description: MB Miniport Driver INF Requirements
ms.assetid: 1f248e1c-7faf-4a11-a4c2-3c0e829e1583
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Miniport Driver INF Requirements


MB miniport drivers must have the following entries in their INF file:

```INF
*IfType  = 243; IF_TYPE_WWANPP 
*MediaType  = 9; <mark type="enumval">NdisMediumWirelessWan</mark> 
*PhysicalMediaType  = 8; NdisPhysicalMediumWirelessWan
EnableDhcp  = 0; Disable DHCP

;Entries to be put in add-registry-section for NdisMediumWirelessWan
HKR, Ndi\Interfaces, UpperRange, 0, "flpp4, flpp6"
HKR, Ndi\Interfaces, LowerRange, 0, "ppip"
```

All the entries mentioned in the preceding code example, except UpperRange and LowerRange, should be under the same INF section as that of keywords such as AddReg and CopyFiles. UpperRange and LowerRange should be put in the [add-registry-section](add-registry-sections-in-a-network-inf-file.md) of the INF file.

### <a href="" id="-iftype"></a>\*IfType

Dual-mode devices can specify either of the *IfType* values from the following table:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Description</strong></p></td>
<td align="left"><p><strong>Name</strong></p></td>
<td align="left"><p><strong>IfType</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>GSM-based MB devices</p></td>
<td align="left"><p>IF_TYPE_WWANPP</p></td>
<td align="left"><p>243</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CDMA-based MB devices</p></td>
<td align="left"><p>IF_TYPE_WWANPP2</p></td>
<td align="left"><p>244</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="-mediatype"></a>\*MediaType

MB miniport drivers must specify one of the MediaType values from the following table based on the type of packet framing the miniport driver is capable of interpreting in its send and receive data path.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Description</strong></p></td>
<td align="left"><p><strong>Name</strong></p></td>
<td align="left"><p><strong>MediaType</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>MB miniport drivers that interpret 802.3 packets must report this media type. This framework is only for migration of old miniport drivers and is not recommended for production-quality miniport drivers.</p></td>
<td align="left"><p>NdisMedium802_3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MB miniport drivers that are able to handle raw IP traffic must set this media type. This is the recommended media type to be used in production-quality miniport drivers.</p></td>
<td align="left"><p>NdisMediumWirelessWan</p></td>
<td align="left"><p>9</p></td>
</tr>
</tbody>
</table>

 

### EnableDhcp

MB miniport drivers must specify one of the EnableDhcp values from the following table based on whether they implement DHCP server emulation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Value</strong></p></td>
<td align="left"><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>Disable DHCP for this interface. The miniport driver does not implement DHCP server spoofing. This is the recommended value to be used in production-quality drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Enable DHCP for this interface. The miniport driver implements DHCP server spoofing. That is, the miniport driver will need to spoof a DHCP server and ARP resolutions.</p></td>
</tr>
</tbody>
</table>

 

### UpperRange

This keyword is set with one or more combinations of the following strings as applicable when media type is NdisMediumWirelessWan. NdisMedium802\_3 miniport drivers should use the existing values in UpperRange.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Value</strong></p></td>
<td align="left"><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;flpp4&quot;</p></td>
<td align="left"><p>Miniport drivers specify &quot;flpp4&quot; if the MB device supports IPv4.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>&quot;flpp6&quot;</p></td>
<td align="left"><p>Miniport drivers specify &quot;flpp6&quot; if the MB device supports IPv6. This value is needed only for devices that support IPv6.</p></td>
</tr>
</tbody>
</table>

 

### LowerRange

This keyword must have, at the minimum, the following value when media type is NdisMediumWirelessWan. NdisMedium802\_3 miniport drivers should use the existing values in LowerRange.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Value</strong></p></td>
<td align="left"><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;ppip&quot;</p></td>
<td align="left"><p>MB device type on the lower edge.</p></td>
</tr>
</tbody>
</table>

 

 

 





