---
title: OID_DOT11_WFD_SEND_GO_NEGOTIATION_CONFIRMATION
author: windows-driver-content
description: When set, the OID_DOT11_WFD_SEND_GO_NEGOTIATION_CONFIRMATION object identifier (OID) provides the miniport driver with the parameters for a Group Owner (GO) negotiation confirmation.
ms.assetid: 4D836BED-F3F0-4224-9438-C39B8122EE03
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_SEND_GO_NEGOTIATION_CONFIRMATION Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_CONFIRMATION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_CONFIRMATION object identifier (OID) provides the miniport driver with the parameters for a Group Owner (GO) negotiation confirmation. The OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_CONFIRMATION request is sent after the miniport inidicates a [**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_GO\_NEGOTIATION\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh439791) indication.

The data type for OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_CONFIRMATION is the [**DOT11\_SEND\_GO\_NEGOTIATION\_COMFIRMATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406537) structure.

This is a direct OID called in the context of a [**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_GO\_NEGOTIATION\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh439791) indication.

After receiving this OID, the miniport must create and populate all the required Peer-to-Peer (P2P) attributes in the P2P Information Element (IE) before it sends the GO negotiation confirmation packet.

**Note**  Miniports must handle this OID synchronously. They must not process requests as pending.

 

The completion of the attempt to send the GO negotiation response attempt must be indicated to the system with a [**NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_CONFIRMATION\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh451706) indication. The miniport driver must send the **NDIS\_STATUS\_DOT11\_WFD\_GO\_NEGOTIATION\_CONFIRMATION\_SEND\_COMPLETE** indication after it has stopped the attempt to send the GO negotiation response. This must occur in either case of success or failure.
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


[**DOT11\_SEND\_GO\_NEGOTIATION\_COMFIRMATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406537)

[**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_GO\_NEGOTIATION\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh439791)

 

 




