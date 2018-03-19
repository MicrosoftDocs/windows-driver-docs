---
title: OID_DOT11_WFD_GET_DIALOG_TOKEN
author: windows-driver-content
description: When queried, the OID_DOT11_WFD_GET_DIALOG_TOKEN object identifier (OID) requests that the miniport driver return a dialog token for use in a later action frame send request OID.
ms.assetid: 5F283F85-4470-4605-877E-E6DC143DA659
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_GET_DIALOG_TOKEN Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_GET\_DIALOG\_TOKEN


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_WFD\_GET\_DIALOG\_TOKEN object identifier (OID) requests that the miniport driver return a dialog token for use in a later action frame send request OID.

The data type for OID\_DOT11\_WFD\_GET\_DIALOG\_TOKEN is the **DOT11\_DIALOG\_TOKEN** definition.

```ManagedCPlusPlus
    typedef UCHAR DOT11_DIALOG_TOKEN;
  
```

The meaning of the data type is:

<a href="" id="dot11-dialog-token"></a>**DOT11\_DIALOG\_TOKEN**  
The dialog token value from the action request and response packets.

Before issuing an OID to send a Group Owner (GO) negotiation request, a Peer-to-Peer (P2P) invitation request, or a provision discovery request, the system issues an OID\_DOT11\_WFD\_GET\_DIALOG\_TOKEN to query the miniport for the dialog token to use in the send request.

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

 

 




