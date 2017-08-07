---
title: OID\_DOT11\_RESET\_REQUEST
author: windows-driver-content
description: When a method request of the OID\_DOT11\_RESET\_REQUEST OID is made, the miniport driver must reset the specified IEEE layers of the 802.11 station and transition to the initialization (INIT) state of the current operation mode.
ms.assetid: 1338f6fa-fe87-4c10-8c32-6525561354e0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_RESET_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_RESET\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When a method request of the OID\_DOT11\_RESET\_REQUEST OID is made, the miniport driver must reset the specified IEEE layers of the 802.11 station and transition to the initialization (INIT) state of the current operation mode. For more information about the method request type, see [**NDIS\_OID\_REQUEST**](ndis-oid-request.md).

The data type for this OID is the DOT11\_RESET\_REQUEST structure.

```ManagedCPlusPlus
    typedef struct _DOT11_RESET_REQUEST {
         DOT11_RESET_TYPE dot11ResetType;
         DOT11_MAC_ADDRESS dot11MacAddress;
         BOOLEAN bSetDefaultMIB;
    } DOT11_RESET_REQUEST, *PDOT11_RESET_REQUEST;
  
```

This structure includes the following members:

<a href="" id="dot11resettype"></a>**dot11ResetType**  
The IEEE layer to be reset on the 802.11 station. The data type for this member is the DOT11\_RESET\_TYPE enumeration:

<a href="" id="dot11-reset-type-phy"></a>**dot11\_reset\_type\_phy**  
Only the PHY layer is reset.

<a href="" id="dot11-reset-type-mac"></a>**dot11\_reset\_type\_mac**  
Only the MAC layer is reset.

<a href="" id="dot11-reset-type-phy-and-mac"></a>**dot11\_reset\_type\_phy\_and\_mac**  
Both the PHY and MAC layers are reset.

**Note**  A miniport driver operating in Extensible Station (ExtSTA) mode must only support the reset type of **dot11\_reset\_type\_phy\_and\_mac**. In this situation, the driver must reset the MAC and all PHY layers supported on the 802.11 station.

 

<a href="" id="dot11macaddress"></a>**dot11MacAddress**  
The unicast media access control (MAC) address used by the 802.11 station following the reset. This member can be used to configure a locally administered MAC address on the 802.11 station.

The miniport driver must not ignore this member if **dot11ResetType** is set to **dot11\_reset\_type\_mac** or **dot11\_reset\_type\_phy\_and\_mac**.

<a href="" id="bsetdefaultmib"></a>**bSetDefaultMIB**  
The 802.11 station resets the specified IEEE layers and resets the 802.11 management information base (MIB) objects of the IEEE layer to their default values. The default values are mostly defined by the miniport implementation. However, some Native 802.11 MIB objects have explicit default values defined, such as [OID\_DOT11\_RTS\_THRESHOLD](oid-dot11-rts-threshold.md) and [OID\_DOT11\_SHORT\_RETRY\_LIMIT](oid-dot11-short-retry-limit.md). For more information about the default values for the Native 802.11 MIB objects, see [IEEE 802.11 MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff553782).

The Native 802.11 miniport driver must follow these guidelines when it resets the 802.11 MIB objects to their default values:

-   In a call to the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function, if the Native 802.11 miniport driver sets *MiniportAttributes-*&gt; **Native\_802\_11\_Attributes**-&gt; **Header-**&gt; **Revision** to NDIS\_MINIPORT\_ADAPTER\_802\_11\_ATTRIBUTES\_REVISION\_1, the driver must always reset the 802.11 MIB objects to their default value regardless of the value of the **bSetDefaultMIB** member.

-   In a call to the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function, if the Native 802.11 miniport driver sets *MiniportAttributes-*&gt; **Native\_802\_11\_Attributes**-&gt; **Header-**&gt; **Revision** to a higher revision number, the driver should reset the 802.11 MIB objects to their default value only when the value of the **bSetDefaultMIB** member is set to **TRUE**.

    If this member is **FALSE**, the 802.11 station resets the specified IEEE layers but retains the current values of the 802.11 MIB objects.

When the method request of OID\_DOT11\_RESET\_REQUEST is made, the miniport driver can do one of the following:

-   Wait for the reset operation to complete before completing the set request.

-   Initiate the reset operation and complete the set request. In this situation, the miniport driver must return NDIS\_STATUS\_PENDING from its [*MiniportOidRequest*](miniportoidrequest.md) function after initiating the reset operation. After the reset operation has finished, the miniport driver completes the set request by calling [**NdisMRequestComplete**](ndismoidrequestcomplete.md).

When the method request of OID\_DOT11\_RESET\_REQUEST is made, the miniport driver must do the following regardless of the value of **dot11ResetType**:

-   Fail the query request if the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](miniportoidrequest.md) function is less than the length, in bytes, of the [**DOT11\_STATUS\_INDICATION**](dot11-status-indication.md) structure. In this situation, the miniport driver returns NDIS\_STATUS\_BUFFER\_OVERFLOW from the *MiniportOidRequest* function.

-   Disconnect from the basic service set (BSS) network if the miniport driver is operating in ExtSTA mode and the 802.11 station is connected to the BSS network. If the 802.11 station connected to an infrastructure BSS, it must send an 802.11 Disassociation frame.

    When the 802.11 disconnects from the BSS, the miniport driver must make a media-specific [NDIS\_STATUS\_DOT11\_DISASSOCIATION](ndis-status-dot11-disassociation.md) indication. The **uSource** member of the DOT11\_DISASSOCIATION\_PARAMETERS structure must be set to **DOT11\_DISASSOC\_SOURCE\_OS**.

    **Note**  The miniport driver must make the NDIS\_STATUS\_DOT11\_DISASSOCIATION indication before it completes the method request of DOT11\_RESET\_REQUEST.

     

-   Cancel any scan operation the 802.11 station is performing.

    If the 802.11 station is performing an explicit scan operation initiated through a set request of [OID\_DOT11\_SCAN\_REQUEST](oid-dot11-scan-request.md), the miniport driver must make the [NDIS\_STATUS\_DOT11\_SCAN\_CONFIRM](ndis-status-dot11-scan-confirm.md) indication before it completes the method request of DOT11\_RESET\_REQUEST.

-   Clear its transmit and receive queues. If transmit packets are pending, the miniport driver must call [**NdisMSendNetBufferListsComplete**](ndismsendnetbufferlistscomplete.md) for each packet in the transmit queue. When it calls **NdisMSendNetBufferListsComplete**, the miniport driver must set the **Status** member of each NET\_BUFFER\_LIST structure that is specified by the *NetBufferLists* parameter to NDIS\_STATUS\_RESET\_IN\_PROGRESS.

-   Retain the current power state of the 802.11 station as specified through the Native 802.11 Operational **msDot11NICPowerState** MIB object. For more information about this MIB object, see [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

-   Transition to the INIT state of the current operation mode.

    For more information about the operation modes of a Native 802.11 miniport driver, see [Native 802.11 Operation Modes](https://msdn.microsoft.com/library/windows/hardware/ff560671).

    For more information about the operating states of a Native 802.11 miniport driver, see [Native 802.11 Operating States](https://msdn.microsoft.com/library/windows/hardware/ff560664).

The miniport driver can also choose to re-initialize data that is specific to the Extensible AP (ExtAP) operating mode, such as beacon data and cached information elements (IEs).

When the method request of OID\_DOT11\_RESET\_REQUEST is made and the miniport driver is operating in the Extensible Station (ExtSTA) mode, the miniport driver must do the following:

-   Clear the PMKID cache that was previously set through [OID\_DOT11\_PMKID\_LIST](oid-dot11-pmkid-list.md). The miniport driver must set the PMKID list to its default value of an empty list.

-   Clear the privacy exemption list that was previously set through [OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST](oid-dot11-privacy-exemption-list.md). The miniport driver must set the privacy exemption list to its default value of an empty list.

-   Discard all cipher keys.

    If the miniport driver is operating in Extensible Station (ExtSTA) mode, these keys were previously set through [OID\_DOT11\_CIPHER\_DEFAULT\_KEY](oid-dot11-cipher-default-key.md) or [OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY](oid-dot11-cipher-key-mapping-key.md).

-   Set the members of its DOT11\_STATISTICS structure to zero. For more information about this structure, see [OID\_DOT11\_STATISTICS](oid-dot11-statistics.md).

-   If the miniport driver previously made a media-specific indication of [NDIS\_STATUS\_DOT11\_CONNECTION\_START](ndis-status-dot11-connection-start.md) but did not make the [NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION](ndis-status-dot11-connection-completion.md) indication, make the completion indication before it completes the method request of DOT11\_RESET\_REQUEST.

-   If the miniport driver previously made a media-specific indication of [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](ndis-status-dot11-association-start.md) but did not make the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](ndis-status-dot11-association-completion.md) indication, make the completion indication before it completes the method request of DOT11\_RESET\_REQUEST.

-   If the miniport driver previously made a media-specific indication of [NDIS\_STATUS\_DOT11\_ROAMING\_START](ndis-status-dot11-roaming-start.md) but did not make the [NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION](ndis-status-dot11-roaming-completion.md) indication, make the completion indication before it completes the method request of DOT11\_RESET\_REQUEST.

When resetting the MAC layer, the 802.11 station must set the following MIB objects to their default values if **bSetDefaultMIB** is set to **TRUE**:

-   All Native 802.11 MIB objects associated with the MAC layer. For more information about these MIB objects, see [Native 802.11 MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff560645).

-   All ExtSTA MIB objects associated with the MAC layer. For more information about these MIB objects, see [Extensible Station MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff549882).

    The miniport driver resets these MIB objects to their default values only if the driver is operating in ExtSTA mode.

-   All ExtAP MIB objects associated with the MAC layer. For more information about these MIB objects, see [Extensible AP MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff549865).

-   All Native 802.11 Operational MIB objects associated with the MAC layer. For more information about these MIB objects, see [Native 802.11 Operational MIB Objects](https://msdn.microsoft.com/library/windows/hardware/ff560668).

The 802.11 station must do the following when it resets the PHY layer:

-   Reset all supported PHY types.

-   If **bSetDefaultMIB** is set to **TRUE**, set the standard 802.11 MIB objects for the PHY layer to the default values. The station must set the MIB objects pertaining to all of the supported PHY types to their default values.

When the reset operation is complete, the miniport driver must return a [**DOT11\_STATUS\_INDICATION**](dot11-status-indication.md) structure to confirm the reset operation. The miniport driver does this by:

-   Formatting the **InformationBuffer** member of the *OidRequest* parameter as a [**DOT11\_STATUS\_INDICATION**](dot11-status-indication.md) structure.

    The miniport driver sets the **uStatusType** member of the DOT11\_STATUS\_INDICATION structure to DOT11\_STATUS\_RESET\_CONFIRM.

    The miniport driver sets the **ndisStatus** member of the [**DOT11\_STATUS\_INDICATION**](dot11-status-indication.md) structure to NDIS\_STATUS\_SUCCESS if the reset operation completed successfully. If the reset operation failed, the miniport driver sets this member to the appropriate NDIS\_STATUS value.

-   Setting the value of the **BytesRead** member of the *OidRequest* parameter to the size of the DOT11\_RESET\_REQUEST structure.

    **Note**  The miniport driver must not set the value of the **BytesWritten** member of the *OidRequest* parameter.

     

Starting with Windows 8, the Wi-Fi Direct port must reset the specified layers of the 802.11 state and all the Wi-Fi Direct state programmed on it whenever an OID\_DOT11\_RESET\_REQUEST request is made. The miniport must transition to the initialization (INIT) state of the current operation mode. If it is operating as a Wi-Fi Direct Group Owner, it must stop the group and disconnect all its clients. If it is operating as a Wi-Fi Direct Client in a group, it must leave the group.

The Wi-Fi Direct state configured by the following OIDs must be reset to their default values whenever an OID\_DOT11\_RESET\_REQUEST request is made:

-   [OID\_DOT11\_WFD\_DEVICE\_INFO](oid-dot11-wfd-device-info.md)
-   [OID\_DOT11\_WFD\_DEVICE\_CAPABILITY](oid-dot11-wfd-device-capability.md)
-   [OID\_DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY](oid-dot11-wfd-group-owner-capability.md)
-   [OID\_DOT11\_WFD\_SECONDARY\_DEVICE\_TYPE\_LIST](oid-dot11-wfd-secondary-device-type-list.md)
-   [OID\_DOT11\_WFD\_ADDITIONAL\_IE](oid-dot11-wfd-additional-ie.md)
-   [OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY](oid-dot11-wfd-listen-state-discoverability.md)
-   [OID\_DOT11\_WFD\_GROUP\_START\_PARAMETERS](oid-dot11-wfd-group-start-parameters.md)
-   [OID\_DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS](-oid-dot11-wfd-group-join-parameters.md)

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_RESET_REQUEST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


