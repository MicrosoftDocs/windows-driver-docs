---
title: OID_DOT11_ADDITIONAL_IE
author: windows-driver-content
description: OID_DOT11_ADDITIONAL_IE
ms.assetid: 50c539c0-9106-42e6-b4e8-255169eb0089
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ADDITIONAL_IE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ADDITIONAL\_IE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_ADDITIONAL\_IE object identifier (OID) requests that the miniport driver set the value of the **msDot11AdditionalIEs** management information base (MIB) object to the specified data.

When queried, this OID requests that the miniport driver return the value of the **msDot11AdditionalIEs** MIB object.

The **msDot11AdditionalIEs** MIB object specifies the values of the additional information elements (IEs) in the BSS 802.11 beacon or probe response frame.

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_ADDITIONAL\_IE**](https://msdn.microsoft.com/library/windows/hardware/ff547645) structure.

When this OID is set, the NIC must behave as follows:

-   If the Extensible AP is in the INIT state, the NIC must complete the request.

-   If the Extensible AP is in the OP state, the NIC must complete the request and, upon completion of the set request, the NIC must begin using the new additional IEs in the beacon or probe response frames that it sends.

The NIC should place additional IEs at the end of beacon or probe response frames.

The NIC must ensure that the corresponding additional IEs appear in every beacon or probe response frame that it sends, unless the additional IEs would cause the size of the frame to exceed the MAC management protocol data unit (MMPDU) limit. In this case, the NIC should discard the new additional IEs, keep the original list of additional IEs, and return NDIS\_STATUS\_BUFFER\_OVERFLOW. However, this overflow situation should not change the NIC operational mode or state.

The miniport driver should reset the members of the DOT11\_ADDITIONAL\_IE structure to the default values when it receives an [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) request.

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


[**DOT11\_ADDITIONAL\_IE**](https://msdn.microsoft.com/library/windows/hardware/ff547645)

[OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




