---
title: OID\_DOT11\_DESIRED\_PHY\_LIST
author: windows-driver-content
description: OID\_DOT11\_DESIRED\_PHY\_LIST
ms.assetid: 48f68993-1b30-4eec-abb3-9f3d32905818
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_DESIRED_PHY_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DESIRED\_PHY\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_DESIRED\_PHY\_LIST object identifier (OID) requests that the miniport driver set the value of the Extensible Station (ExtSTA) **msDot11DesiredPhyList** management information base (MIB) object to the specified data.

When queried, OID\_DOT11\_DESIRED\_PHY\_LIST requests that the miniport driver return the value of the **msDot11DesiredPhyList** MIB object.

The **msDot11DesiredPhyList** MIB object specifies the desired PHY list that the 802.11 station uses when connecting to and operating in a BSS network. Each entry in the **msDot11DesiredPhyList** MIB object is a PHY identifier (IDs), which can be one of the following:

-   An index into the table of supported PHYs as defined by the Native 802.11 Operational **msDot11SupportedPhyTypes** MIB object. For more information about PHY IDs and the **msDot11SupportedPhyTypes** MIB object, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

-   A PHY ID with the value of DOT11\_PHY\_ID\_ANY is the wildcard PHY ID. If the **msDot11DesiredPhyList** MIB object contains the wildcard PHY ID, the 802.11 station can use any supported PHY to connect to and operate in a BSS network.

The **msDot11DesiredPhyList** MIB object does not define the PHY IDs that can be used by the 802.11 station for scan operations. The PHY IDs that the 802.11 station uses for scanning are specified when [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md) is set.

The data type for OID\_DOT11\_DESIRED\_PHY\_LIST is the [**DOT11\_PHY\_ID\_LIST**](dot11-phy-id-list.md) structure.

When OID\_DOT11\_DESIRED\_PHY\_LIST is set, the miniport driver should ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](miniportoidrequest.md) function's OidRequest parameter is at least the value returned by the following formula:

```
 FIELD_OFFSET(DOT11_PHY_ID_LIST, dot11PhyId) + uNumOfEntries * sizeof(ULONG))
```

When OID\_DOT11\_DESIRED\_PHY\_LIST is set, the miniport driver must fail the set request if the members of the [**DOT11\_PHY\_ID\_LIST**](dot11-phy-id-list.md) structure meet the following conditions:

-   The desired PHY list must always contain at least one entry. If **uNumOfEntries** is set to zero, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   A desired PHY list containing a wildcard PHY ID cannot contain other PHY IDs. When OID\_DOT11\_DESIRED\_PHY\_LIST is set, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its *MiniportOidRequest* function if the **dot11PhyIds** array contains the wildcard PHY ID and **uNumOfEntries** is greater than one.

-   If the **dot11PhyId** array contains a PHY ID that is not the wildcard PHY ID and has a value greater than or equal to the number of entries defined by the **msDot11SupportedPhyTypes** MIB object, the miniport driver must fail the request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   If the **dot11PhyId** array contains a PHY ID that is not supported on the 802.11 station, the miniport driver must fail the request by returning NDIS\_STATUS\_UNSUPPORTED\_MEDIA from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   If the **dot11PhyId** array contains a PHY ID that has been disabled on the 802.11 station through a proprietary mechanism implemented by the independent hardware vendor (IHV), the miniport driver must fail the request by returning NDIS\_STATUS\_UNSUPPORTED\_MEDIA from its [*MiniportOidRequest*](miniportoidrequest.md) function.

    **Note**  This condition does not apply to PHYs disabled through a set request of [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

     

When OID\_DOT11\_DESIRED\_PHY\_LIST is queried, the miniport driver must verify that the **InformationBuffer** member of its [*MiniportOidRequest*](miniportoidrequest.md) function's *OidRequest* parameter is large enough to return the desired PHY ID list. For more information about this procedure, see [**DOT11\_PHY\_ID\_LIST**](dot11-phy-id-list.md).

The default for the **msDot11DesiredPhyList** MIB object contains a single entry with the members of the [**DOT11\_PHY\_ID\_LIST**](dot11-phy-id-list.md) structure set as follows:

-   **dot11PhyId\[0\]** is set to DOT11\_PHY\_ID\_ANY.

-   **uNumEntries** is set to one.

The miniport driver must set the **msDot11DesiredPhyList** MIB object to its default whenever the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](miniportinitializeex.md) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the media access control (MAC) layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

Beginning in Windows 7, the default behavior of the ExtAP mode is to support only one desired PHY ID at a time. If multiple PHY IDs are present in a set request to this OID, the NIC should start a BSS using the first PHY ID in the list.

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_DESIRED_PHY_LIST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


