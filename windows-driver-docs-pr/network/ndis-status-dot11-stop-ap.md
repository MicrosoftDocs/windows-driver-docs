---
title: NDIS\_STATUS\_DOT11\_STOP\_AP
author: windows-driver-content
description: NDIS\_STATUS\_DOT11\_STOP\_AP
ms.assetid: b35e6280-72cd-470b-a3c3-31136f8961cf
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_STOP_AP Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_STOP\_AP


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_STOP\_AP status indication when the NIC cannot sustain 802.11 access point (AP) functionality on any of the available PHYs. The driver should send this indication only after the NIC has stopped any APs that are operating on the available PHYs.

The data type for this indication is the [**DOT11\_STOP\_AP\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548783) structure.

While the NIC is in the Extensible Station AP (ExtAP) mode, it could determine that it can no longer operate the AP on the current PHY. For example, if a PHY is operating in orthogonal frequency division multiplexing (OFDM) mode, radar signals might interfere with how the PHY changes frequency.

If, because of these or similar circumstances, the NIC determines that it must stop AP operations, the miniport driver should perform the following operations:

-   Disassociate all peer stations from the AP.

-   Drop all pending frames.

-   Send all appropriate NDIS status indications to the operating system, which includes NDIS\_STATUS\_DOT11\_STOP\_AP.

After the miniport driver has performed these actions, it must send an [NDIS\_STATUS\_DOT11\_CAN\_SUSTAIN\_AP](ndis-status-dot11-can-sustain-ap.md) status indication to indicate that it is ready to receive an [OID\_DOT11\_START\_AP\_REQUEST](oid-dot11-start-ap-request.md) request to start the AP again.

If the miniport driver receives an [OID\_DOT11\_START\_AP\_REQUEST](oid-dot11-start-ap-request.md) set request after it has indicated NDIS\_STATUS\_DOT11\_STOP\_AP but before it has indicated [NDIS\_STATUS\_DOT11\_CAN\_SUSTAIN\_AP](ndis-status-dot11-can-sustain-ap.md), the driver should fail the OID request with a failure code of NDIS\_STATUS\_INVALID\_STATE.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_STOP\_AP indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure by using the *StatusIndication* parameter. When the driver makes this indication, it must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_STOP\_AP.

-   **StatusBuffer** must be set to the address of a DOT11\_STOP\_AP\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_STOP\_AP\_PARAMETERS).

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


[**DOT11\_STOP\_AP\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548783)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

[OID\_DOT11\_START\_AP\_REQUEST](oid-dot11-start-ap-request.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_STOP_AP%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


