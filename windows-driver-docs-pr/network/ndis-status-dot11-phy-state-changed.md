---
title: NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED
author: windows-driver-content
description: A miniport driver must make the NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED indication whenever the hardware or software power state of a PHY changes on the 802.11 station.
ms.assetid: 276fb352-f355-4047-adce-ef9e51b5c1b7
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - NDIS_STATUS_DOT11_PHY_STATE_CHANGED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make the NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED indication whenever the hardware or software power state of a PHY changes on the 802.11 station.

The data type for this indication is the DOT11\_PHY\_STATE\_PARAMETERS structure:

```ManagedCPlusPlus
    typedef struct DOT11_PHY_STATE_PARAMETERS {
         NDIS_OBJECT_HEADER Header;
         ULONG uPhyId;
         BOOLEAN bHardwarePhyState;
         BOOLEAN bSoftwarePhyState;
    } DOT11_PHY_STATE_PARAMETERS,   *PDOT11_PHY_STATE_PARAMETERS;
  
```

The DOT11\_PHY\_STATE\_PARAMETERS structure contains the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_PHY\_STATE\_PARAMETERS structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_PHY\_STATE\_PARAMETERS\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_PHY\_STATE\_PARAMETERS).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md).

<a href="" id="uphyid"></a>**uPhyId**  
The PHY identifier (ID) of the PHY whose state has changed.

The PHY ID is an index into the table of supported PHYs that are specified by the Native 802.11 Operational **msDot11SupportedPhyTypes** MIB object. For more information about PHY IDs and the **msDot11SupportedPhyTypes** MIB object, see [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

If the **uPhyId** member is set to DOT11\_PHY\_ID\_ANY, the NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED indication applies to all PHYs in the **msDot11SupportedPhyTypes** MIB object.

<a href="" id="bhardwarephystate"></a>**bHardwarePhyState**  
A Boolean value that specifies the hardware power state of the PHY that is referenced by **uPhyId**. If **TRUE**, the hardware power state is enabled. If **FALSE**, the hardware power state is disabled.

For more information about the PHY's hardware power state, see [OID\_DOT11\_HARDWARE\_PHY\_STATE](oid-dot11-hardware-phy-state.md).

<a href="" id="bsoftwarephystate"></a>**bSoftwarePhyState**  
A Boolean value that specifies the software power state of the PHY that is referenced by **uPhyId**. If **TRUE**, the software power state is enabled. If **FALSE**, the software power state is disabled.

For more information about the PHY's software power state, see [OID\_DOT11\_NIC\_POWER\_STATE](oid-dot11-nic-power-state.md).

The miniport driver calls [**NdisMIndicateStatusEx**](ndismindicatestatusex.md) to make an NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](ndis-status-indication.md) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_PHY\_STATE\_CHANGED.

-   **StatusBuffer** must be set to the address of a DOT11\_PHY\_STATE\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_PHY\_STATE\_PARAMETERS).

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_PHY_STATE_CHANGED%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


