---
title: NDIS_STATUS_DOT11_CONNECTION_START
author: windows-driver-content
description: A miniport driver must make an NDIS\_STATUS\_DOT11\_CONNECTION\_START indication after the set request of OID\_DOT11\_CONNECT\_REQUEST.
ms.assetid: 08602585-6ef9-4b9e-992f-5b16bd1855f0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_CONNECTION_START Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_CONNECTION\_START


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_CONNECTION\_START indication after the set request of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md). This indication defines the start of the connection operation, in which the 802.11 station attempts to connect to a basic service set (BSS) network.

The miniport driver indicates the completion of the connection operation through the [NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION](ndis-status-dot11-connection-completion.md) indication. Every NDIS\_STATUS\_DOT11\_CONNECTION\_START indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication.

For more information about connection operations, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

The data type for this indication is the DOT11\_CONNECTION\_START\_PARAMETERS structure:

```ManagedCPlusPlus
    typedef struct DOT11_CONNECTION_START_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         DOT11_BSS_TYPE BSSType;
         DOT11_MAC_ADDRESS AdhocBSSID;
         DOT11_SSID AdhocSSID;
    } DOT11_CONNECTION_START_PARAMETERS,   *PDOT11_CONNECTION_START_PARAMETERS;
  
```

The DOT11\_CONNECTION\_START\_PARAMETERS structure contains the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_CONNECTION\_START\_PARAMETERS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_CONNECTION\_START\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_CONNECTION\_START\_PARAMETERS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="bsstype"></a>**BssType**  
The type of BSS network that the 802.11 station is connecting to. The data type for the **BssType** member is the [**DOT11\_BSS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff547669) enumeration.

The 802.11 station connects to a BSS type based on the setting of the IEEE 802.11 **dot11DesiredBssType** MIB object. For more information about this MIB object, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

<a href="" id="adhocbssid"></a>**AdhocBSSID**  
If **BssType** is set to **dot11\_BSS\_type\_independent**, the **AdhocBSSID** member contains the BSS identifier (BSSID) of the IBSS network that the 802.11 station will join or start.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](https://msdn.microsoft.com/library/windows/hardware/hh440289).

 

If **BssType** is set to **dot11\_BSS\_type\_infrastructure**, the miniport driver must fill **AdhocBSSID** with zeros.

For more information about the data type for this member, see [**DOT11\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff548681).

<a href="" id="adhocssid"></a>**AdhocSSID**  
If **BssType** is set to **dot11\_BSS\_type\_independent**, the **AdhocSSID** member contains the service set identifier (SSID) of the IBSS network that the 802.11 station will join or start.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](https://msdn.microsoft.com/library/windows/hardware/hh440289).

 

If **BssType** is set to **dot11\_BSS\_type\_infrastructure**, the miniport driver must fill **AdhocSSID** with zeros.

For more information about the data type for this member, see [**DOT11\_SSID**](https://msdn.microsoft.com/library/windows/hardware/ff548773).

After the set request of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) is made, the 802.11 station begins the connection operation by using the BSS parameters that were previously configured through set requests of Native 802.11 OIDs. The miniport driver begins the connection operation by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_CONNECTION\_START.

-   **StatusBuffer** must be set to the address of a DOT11\_CONNECTION\_START\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_CONNECTION\_START\_PARAMETERS).

After the 802.11 station connects to a BSS network or has failed to connect to any BSS network, the miniport driver indicates the completion of the connection operation through an [NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION](ndis-status-dot11-connection-completion.md) indication.

After the 802.11 station starts the connection operation, the miniport driver must complete the connection operation by making an [NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION](ndis-status-dot11-connection-completion.md) indication before it makes the following indications:

-   [NDIS\_STATUS\_DOT11\_ROAMING\_START](ndis-status-dot11-roaming-start.md)

-   [NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION](ndis-status-dot11-roaming-completion.md)

After the miniport driver makes the NDIS\_STATUS\_DOT11\_CONNECTION\_START indication, it cannot make another NDIS\_STATUS\_DOT11\_CONNECTION\_START indication until:

-   The miniport driver returns to the Extensible Station (ExtSTA) INIT mode through a set request of either [OID\_DOT11\_DISCONNECT\_REQUEST](oid-dot11-disconnect-request.md) or [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md).

-   A set request of [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) is made.

Before it initiates a connection operation, the miniport driver must allocate all of the resources that it will need to make the corresponding [NDIS\_STATUS\_DOT11\_CONNECTION\_COMPLETION](ndis-status-dot11-connection-completion.md) indication.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_CONNECTION_START%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


