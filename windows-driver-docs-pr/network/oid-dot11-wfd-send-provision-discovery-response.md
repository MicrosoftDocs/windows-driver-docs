---
title: OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_RESPONSE
author: windows-driver-content
description: When set, the OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_RESPONSE object identifier (OID) is sent to the miniport driver with the parameters to send in a provision discovery response.
ms.assetid: 07EEB56F-EC84-4C7E-AF06-A4B87269A992
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_SEND_PROVISION_DISCOVERY_RESPONSE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE object identifier (OID) is sent to the miniport driver with the parameters to send in a provision discovery response. The OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE request is sent after the miniport indicates an [**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh439797) indication.

The data type for OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE is the [**DOT11\_SEND\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406561) structure.

This is a direct OID called in the context of an [**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh439797) indication.

**Note**  Miniports must handle this OID synchronously. They must not process requests as pending.

 

The completion of the attempt to send the invitation response attempt must be indicated to the system with an [**NDIS\_STATUS\_DOT11\_WFD\_PROVISION\_DISCOVERY\_RESPONSE\_SEND\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/hh439781) indication. The miniport driver must send the **NDIS\_STATUS\_DOT11\_WFD\_PROVISION\_DISCOVERY\_RESPONSE\_SEND\_COMPLETE** indication after it has stopped the attempt to send the provision discovery response. This must occur in either case of success or failure.
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


[**DOT11\_SEND\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406561)

[**NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh439797)

 

 




