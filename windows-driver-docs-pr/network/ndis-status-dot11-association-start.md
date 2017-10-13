---
title: NDIS_STATUS_DOT11_ASSOCIATION_START
author: windows-driver-content
description: A miniport driver must make an NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication before it initiates an association operation with either an access point (AP) (for infrastructure BSS networks) or peer station (for independent BSS (IBSS) networks).Note  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use Wi-Fi Direct.�
ms.assetid: be5d3c95-3080-496f-83cd-1a7e329102ff
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_ASSOCIATION_START Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_ASSOCIATION\_START


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication before it initiates an association operation with either an access point (AP) (for infrastructure BSS networks) or peer station (for independent BSS (IBSS) networks).

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](https://msdn.microsoft.com/library/windows/hardware/hh440289).

 

The miniport driver indicates the completion of the association operation through the [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](ndis-status-dot11-association-completion.md) indication. Every NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION indication.

For more information about the association operation, see [Association Operations](https://msdn.microsoft.com/library/windows/hardware/ff543789).

The data type for this indication is the DOT11\_ASSOCIATION\_START\_PARAMETERS structure:

```ManagedCPlusPlus
    typedef struct DOT11_ASSOCIATION_START_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         DOT11_MAC_ADDRESS MacAddr;
         DOT11_SSID SSID;
         ULONG uIHVDataOffset;
         ULONG uIHVDataSize;
    } DOT11_ASSOCIATION_START_PARAMETERS, *PDOT11_ASSOCIATION_START_PARAMETERS;
  
```

The DOT11\_ASSOCIATION\_START\_PARAMETERS structure contains the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_ASSOCIATION\_START\_PARAMETERS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_ASSOCIATION\_START\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_ASSOCIATION\_START\_PARAMETERS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="macaddr"></a>**MacAddr**  
The media access control (MAC) address of the AP or peer station with which the 802.11 station attempted to associate.

<a href="" id="ssid"></a>**Ssid**  
The service set identifier (SSID) that the 802.11 station is attempting to associate with.

If the **dot11DesiredBSSType** MIB object is set to **dot11\_BSS\_type\_independent**, the **Ssid** member must contain the same value that the **AdhocSSID** member used in the structures for previous [NDIS\_STATUS\_DOT11\_CONNECTION\_START](ndis-status-dot11-connection-start.md) and [NDIS\_STATUS\_DOT11\_ROAMING\_START](ndis-status-dot11-roaming-start.md) indications.

<a href="" id="uihvdataoffset"></a>**uIHVDataOffset**  
The offset of a block of data in a proprietary format that is defined by the IHV. The IHV can use this data block for any purpose that is related to the NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication.

This offset is relative to the start of the buffer, which contains the DOT11\_ASSOCIATION\_ START\_PARAMETERS structure.

If the miniport driver is not returning IHV data in the NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication, it must set **uIHVDataOffset** to zero.

<a href="" id="uihvdatasize"></a>**uIHVDataSize**  
The length of the block of data that is used by the IHV for the NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication. If the miniport driver is not returning IHV data in this indication, it must set **uIHVDataSize** to zero.

The 802.11 station initiates an association operation when:

-   The 802.11 station is performing a connection operation. The miniport driver indicates the start of a connection operation by the [NDIS\_STATUS\_DOT11\_CONNECTION\_START](ndis-status-dot11-connection-start.md) indication.

    For more information about connection operations, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

-   The 802.11 station is performing a roaming operation. The miniport driver indicates the start of a roaming operation by the [NDIS\_STATUS\_DOT11\_ROAMING\_START](ndis-status-dot11-roaming-start.md) indication.

    For more information about the roaming operation, see [Roaming Operations](https://msdn.microsoft.com/library/windows/hardware/ff570717).

-   A peer station in an IBSS network initiates an association with the 802.11 station. The IEEE 802.11 **dot11DesiredBSSType** MIB object must be set to **dot11\_BSS\_type\_independent**, and the 802.11 station must have joined the IBSS network in a previous connection or roaming operation.

    The 802.11 station can initiate this type of association operation outside of the scope of a connection or roaming operation.

    For more information about the **dot11DesiredBSSType** MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_ASSOCIATION\_START indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_ASSOCIATION\_START.

-   **StatusBuffer** must be set to the address of a DOT11\_ASSOCIATION\_START\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_ASSOCIATION\_START\_PARAMETERS).

**Note**  
Before it initiates an association operation, the miniport driver must allocate all of the resources that it will need to make the corresponding [NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION](ndis-status-dot11-association-completion.md) indication.

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_ASSOCIATION_START%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


