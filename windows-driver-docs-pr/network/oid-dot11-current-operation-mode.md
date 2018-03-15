---
title: OID_DOT11_CURRENT_OPERATION_MODE
author: windows-driver-content
description: OID_DOT11_CURRENT_OPERATION_MODE
ms.assetid: 6fe4261a-ab7a-4aef-a67b-62f76d83796e
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CURRENT_OPERATION_MODE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CURRENT\_OPERATION\_MODE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CURRENT\_OPERATION\_MODE object identifier (OID) requests that the miniport driver set its Native 802.11 or Wi-Fi Direct (WFD) operation mode to the specified value.

When queried, this OID requests that the miniport driver return its Native 802.11 operation mode.

The data type for OID\_DOT11\_CURRENT\_OPERATION\_MODE is the [**DOT11\_CURRENT\_OPERATION\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff547678) structure.

When OID\_DOT11\_CURRENT\_OPERATION\_MODE is set, the miniport driver must do the following:

-   If the miniport driver does not support the specified operation mode, fail the set request by returning NDIS\_STATUS\_BAD\_VERSION from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the operation mode changes, configure the 802.11 station with the default settings defined for the operation mode. The miniport driver must also transition to the initialization (INIT) state for the operation mode.

The operation mode setting must persist through resets resulting from a call to the miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function or a method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

If the miniport driver supports the functionality of multiple MAC entities through [virtualization](https://msdn.microsoft.com/library/windows/hardware/ff571041), the driver should not return NDIS\_STATUS\_DOT11\_MEDIA\_IN\_USE if the medium is blocked by another MAC.

A Wi-Fi Direct–capable miniport must support all defined WFD operation modes.

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
<td><p>Available starting with Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




