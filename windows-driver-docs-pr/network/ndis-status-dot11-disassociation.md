---
title: NDIS_STATUS_DOT11_DISASSOCIATION
author: windows-driver-content
description: NDIS\_STATUS\_DOT11\_DISASSOCIATION
ms.assetid: 5945f733-6b06-430a-863f-4ba82cff2dbe
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_DISASSOCIATION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_DISASSOCIATION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_DISASSOCIATION indication if the 802.11 station performs a disassociation operation with either an access point (AP) (for infrastructure BSS networks) or peer station (for independent BSS (IBSS) networks). For more information about disassociation operations, see [Disassociation Operations](https://msdn.microsoft.com/library/windows/hardware/ff546439).

The data type for this indication is the [**DOT11\_DISASSOCIATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547682) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_DISASSOCIATION indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_DISASSOCIATION.

-   **StatusBuffer** must be set to the address of a DOT11\_DISASSOCIATION\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_DISASSOCIATION\_PARAMETERS).

The miniport driver can make the NDIS\_STATUS\_DOT11\_DISASSOCIATION indication only after it has completed an association operation with an AP or peer station that is identified by the **MacAddr** member. The miniport driver indicates the completion of an association operation through the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](ndis-status-dot11-association-completion.md) indication. For more information about the association operation, see [Association Operations](https://msdn.microsoft.com/library/windows/hardware/ff543789).

After the miniport driver makes the NDIS\_STATUS\_DOT11\_DISASSOCIATION indication and if the IEEE 802.11 **dot11DesiredBssType** MIB object is set to **dot11\_BSS\_type\_infrastucture**, the 802.11 station must do the following:

-   If the **uReason** member was set to DOT11\_DISASSOC\_REASON\_OS, the 802.11 station must not attempt to roam or associate with any AP in the BSS. The miniport driver must transition to the ExtSTA INIT operation mode. The 802.11 station must also wait until the next set request of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) before attempting an association operation.

-   If the **uReason** member was not set to DOT11\_DISASSOC\_REASON\_OS, the 802.11 station must attempt to roam to other APs within the basic service set (BSS) that the station was previously associated with.

    For more information about the roaming operation, see [Roaming Operations](https://msdn.microsoft.com/library/windows/hardware/ff570717).

For more information about the **dot11DesiredBssType** MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

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
<td><p>Available in Windows Vista and later versions of the Windows operating systemss.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_DISASSOCIATION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


