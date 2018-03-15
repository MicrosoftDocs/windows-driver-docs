---
title: NDIS_STATUS_DOT11_WFD_RECEIVED_PROVISION_DISCOVERY_REQUEST
author: windows-driver-content
ms.assetid: AC3A4E34-C4AA-4604-ABBC-73CDBD6C0704
description: 
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_DOT11_WFD_RECEIVED_PROVISION_DISCOVERY_REQUEST Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The status of the reception of a provision discovery request transmission is reported with an NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST indication.

The data type for this indication is the [**DOT11\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406531) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST.

-   **StatusBuffer** must be set to the address of a [**DOT11\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406531) structure.

-   **StatusBufferSize** must be set to the total of both the size of [**DOT11\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406531) and the size of the list of returned Information Elements (IEs).

After receiving the status indication, the system will determine the appropriate response for the provision discovery request. The system may then send [OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451808) OID to the driver for creation and transmission of the provision discovery response.

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_RECEIVED\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406531)

[OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451808)

 

 




