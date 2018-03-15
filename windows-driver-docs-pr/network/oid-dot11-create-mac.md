---
title: OID_DOT11_CREATE_MAC
author: windows-driver-content
description: OID_DOT11_CREATE_MAC
ms.assetid: 808f60d4-bd3d-46c9-8bb4-f6d6e9307ff5
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_CREATE_MAC Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CREATE\_MAC


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When a method request of the OID\_DOT11\_CREATE\_MAC object identifier (OID) is made, the miniport driver must create a new 802.11 MAC entity and return a [**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689) structure. For more information about the method request type, see [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710).

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689) structure.

If the miniport driver has already created the maximum number of MAC entities that it can support, it should fail this OID method request and return the status indication NDIS\_STATUS\_OPEN\_LIST\_FULL.

Before the miniport driver completes its response to this OID request, it should call the [**NdisMAllocatePort**](https://msdn.microsoft.com/library/windows/hardware/ff562779) function to allocate a corresponding NDIS port for each 802.11 MAC entity that the driver creates.

Starting in Windows 8, if the input buffer size is &gt; 0, the input for this OID is formatted as a [**DOT11\_MAC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406491) structure.

Remarks
-------

If the MAC is to function as a Wi-Fi Direct device port, **uOpmodeMask** in [**DOT11\_MAC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406491) will contain the **DOT11\_OPERATION\_MODE\_WFD\_DEVICE** flag. In this case, the miniport driver must return the same device address in [**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689) as the one specified in the **DeviceAddress** member of [**DOT11\_WFD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/hh406574) sent with the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

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
<td><p>Available starting with Windows 7.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689)

[**DOT11\_MAC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406491)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NdisMAllocatePort**](https://msdn.microsoft.com/library/windows/hardware/ff562779)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




