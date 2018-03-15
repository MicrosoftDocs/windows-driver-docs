---
title: OID_DOT11_WFD_SEND_INVITATION_REQUEST
author: windows-driver-content
description: When set, the OID_DOT11_WFD_SEND_INVITATION_REQUEST object identifier (OID) is sent to the miniport driver with the parameters for an invitation request.
ms.assetid: 1612EE79-FF44-4FC5-9266-39314E511BD0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_SEND_INVITATION_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_SEND\_INVITATION\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_SEND\_INVITATION\_REQUEST object identifier (OID) is sent to the miniport driver with the parameters for an invitation request.

The data type for OID\_DOT11\_WFD\_SEND\_INVITATION\_REQUEST is the [**DOT11\_SEND\_INVITATION\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406546) structure.

This OID is sent to the miniport as an **NdisRequestMethod** OID request type.

After receiving this OID, the miniport must create and populate all the required Peer-to-Peer (P2P) attributes in the P2P Information Element (IE) before it sends the invitation request packet.

After creating the packet for transmission, the miniport must complete the OID with a status of **NDIS\_STATUS\_INDICATION\_REQUIRED**. The completion of the attempt to send the invitation request attempt must be indicated to the system with an [**NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439779) indication. The miniport driver must send the **NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE** indication after it has stopped the attempt to send the invitation request. This must occur in either case of success or failure.

Miniport drivers should periodically attempt sending the Invitation Request frame at intervals no longer than 50ms because a remote device may not be constantly available on its listen channel (or, operating channel in case of GO).

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_SEND\_INVITATION\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406546)

[**NDIS\_STATUS\_DOT11\_WFD\_INVITATION\_REQUEST\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439779)

 

 




