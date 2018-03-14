---
title: OID_DOT11_DELETE_MAC
author: windows-driver-content
description: OID_DOT11_DELETE_MAC
ms.assetid: 84ca1060-5460-4f63-b452-a0f6429aaca8
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DELETE_MAC Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DELETE\_MAC


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When a set request of the OID\_DOT11\_DELETE\_MAC object identifier (OID) is made, the miniport driver must delete an 802.11 MAC entity that corresponds to a caller-provided [**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689) structure.

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689) structure.

If there is no 802.11 MAC entity that corresponds to the **uNdisPortNumber** NDIS port in the caller-provided DOT11\_MAC\_INFO structure, the miniport driver should return the NDIS\_STATUS\_INVALID\_PARAMETER status code.

Before the miniport driver returns from a set request from this OID, it should call the [**NdisMFreePort**](https://msdn.microsoft.com/library/windows/hardware/ff563588) function to free the corresponding NDIS port that was earlier created in a call to [OID\_DOT11\_CREATE\_MAC](oid-dot11-create-mac.md).

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
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisMFreePort**](https://msdn.microsoft.com/library/windows/hardware/ff563588)

[OID\_DOT11\_CREATE\_MAC](oid-dot11-create-mac.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




