---
title: WDI_TLV_BSSID_INFO
author: windows-driver-content
description: WDI_TLV_BSSID_INFO is a TLV that contains BSSID information.
ms.assetid: C9E2B2D5-16CA-438D-AD86-1FA4F4F11CD1
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_BSSID_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSSID\_INFO


WDI\_TLV\_BSSID\_INFO is a TLV that contains BSSID information.

## TLV Type


0x120

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                                                                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | AP reachability. Valid values are 1 (not reachable), 2 (unknown), and 3 (reachable).                                                                                                                                                                                                                                                      |
| UINT8 | Security. If this is set to 1, it indicates that the AP identified by this BSSID supports the same security provisioning as used by the STA in its current association. If this is set to 0, it indicates that either this AP does not support the same security provisioning, or the security information is not available at this time. |
| UINT8 | Key scope bit. If it is set to 1, it indicates the AP indicated by this BSSID has the same authenticator as the AP sending the report. If this bit is set to 0, it indicates a distinct authenticator or the information is not available.                                                                                                |
| UINT8 | This is set to 1 if dot11SpectrumManagementRequired is true.                                                                                                                                                                                                                                                                              |
| UINT8 | This is set to 1 if dot11QosOptionImplemented is true.                                                                                                                                                                                                                                                                                    |
| UINT8 | An AP sets the APSD subfield to 1 within the Capability Information field when dot11APSDOptionImplemented is true, and sets it to 0 otherwise.                                                                                                                                                                                            |
| UINT8 | This is set to 1 if dot11RadioMeasurementActivated is true.                                                                                                                                                                                                                                                                               |
| UINT8 | This is set to 1 if dot11DelayedBlockAckOptionImplemented is true.                                                                                                                                                                                                                                                                        |
| UINT8 | This is set to 1 if dot11ImmediateBlockAckOptionImplemented is true.                                                                                                                                                                                                                                                                      |
| UINT8 | This is set to 1 if the AP represented by this BSSID includes an MDE in its Beacon frames.                                                                                                                                                                                                                                                |
| UINT8 | This is set to 1 to indicate that the AP represented by this BSSID is an HT AP, including the HT Capabilities element in its Beacon.                                                                                                                                                                                                      |

 

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_BSSID_INFO%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


