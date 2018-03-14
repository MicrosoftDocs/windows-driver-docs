---
title: OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_REQUEST
author: windows-driver-content
description: When set, the OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_REQUEST object identifier (OID) requests that the Wi-Fi Direct (WFD) device send a provision discovery request packet to a peer WFD device.
ms.assetid: 69490609-60CB-426F-8ED7-F8B35CDFCE2A
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_REQUEST Network Drivers Starting with Windows Vista
---

#  OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_REQUEST object identifier (OID) requests that the Wi-Fi Direct (WFD) device send a provision discovery request packet to a peer WFD device.

The data type for OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_REQUEST is the [**DOT11\_SEND\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406556) structure.

This OID is sent to the miniport as an **NdisRequestSetInformation** OID request type.

After receiving this OID, the miniport must create and populate all the required Peer-to-Peer (P2P) attributes in the P2P Information Element (IE) before it sends the provision discovery request packet.

After creating the packet for transmission, the miniport must complete the OID with status of **NDIS\_STATUS\_INDICATION\_REQUIRED**. The completion of the attempt to send the provision discovery request attempt must be indicated to the system with a [**NDIS\_STATUS\_DOT11\_WFD\_PROVISION\_DISCOVERY\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439783) indication. The miniport driver must send the **NDIS\_STATUS\_DOT11\_WFD\_PROVISION\_DISCOVERY\_REQUEST\_SEND\_COMPLETE** indication once it has stopped the attempt to send the provision discovery request. This must occur in either case of success or failure.

Miniport drivers should periodically attempt sending the Provision Discovery Request frame at intervals no longer than 50ms because a remote device may not be constantly available on its listen channel (or, operating channel in case of GO).

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
<td><p>Versions: Supported in Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_SEND\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406556)

[**NDIS\_STATUS\_DOT11\_WFD\_PROVISION\_DISCOVERY\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439783)

 

 




