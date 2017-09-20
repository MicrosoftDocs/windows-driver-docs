---
title: NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION
author: windows-driver-content
description: NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION
ms.assetid: 331aab73-af87-4241-80ac-d60420607270
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION indication after an association operation completes.

The miniport driver indicates the start of the association operation through the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](ndis-status-dot11-association-start.md) indication. Every NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION indication.

For more information about this association operation, see [Association Operations](https://msdn.microsoft.com/library/windows/hardware/ff543789).

The data type for this indication is the [**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547647) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION.

-   **StatusBuffer** must be set to the address of a DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS).

After the miniport driver makes the NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION indication with the **uStatus** member set to DOT11\_ASSOCIATION\_STATUS\_SUCCESS, the miniport driver must do the following:

-   Be prepared to send and receive packets. If the 802.11 station performed the association operation within the context of either a connection or roaming operation, the miniport driver must be able to send or receive packets before it makes the [NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION](ndis-status-dot11-connection-completion.md) or [NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION](ndis-status-dot11-roaming-completion.md) indications.

-   Add an entry for the current association into its association information list. If the IEEE 802.11 **dot11DesiredBSSType** MIB object is set to **dot11\_BSS\_type\_infrastructure**, the miniport driver must remove the entry for the previous association from its association information list.

    For more information about the association information list, see [OID\_DOT11\_ENUM\_ASSOCIATION\_INFO](oid-dot11-enum-association-info.md).

-   Initialize the authentication algorithm (which is specified by the **AuthAlgo** member) and cipher algorithms (which are specified by the **UnicastCipher** and **MulticastCipher** members) for the association.

-   Delete all non-static default cipher keys. Non-static default cipher keys are created with the **bStatic** member of the DOT11\_CIPHER\_DEFAULT\_KEY\_VALUE structure set to **FALSE**. For more information about this structure, see [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](oid-dot11-cipher-default-key.md).

-   Delete any non-static key-mapping keys for the AP or peer station identified by the **MacAddr** member. Non-static key-mapping keys are created with the **bStatic** member of the DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE structure set to **FALSE**. For more information about this structure, see [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](oid-dot11-cipher-key-mapping-key.md).

For more information about the IEEE 802.11 **dot11DesiredBSSType** MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md)

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_ASSOCIATION_COMPLETION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


