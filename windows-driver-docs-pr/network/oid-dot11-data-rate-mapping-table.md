---
title: OID_DOT11_DATA_RATE_MAPPING_TABLE
author: windows-driver-content
description: When queried, the OID_DOT11_DATA_RATE_MAPPING_TABLE object identifier (OID) requests that the miniport driver return the table of data rates supported by a PHY on the 802.11 station for transmit and receive operations.
ms.assetid: f0d7a91d-9eaa-4a54-98dd-6e60641c8386
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DATA_RATE_MAPPING_TABLE Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DATA\_RATE\_MAPPING\_TABLE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_DATA\_RATE\_MAPPING\_TABLE object identifier (OID) requests that the miniport driver return the table of data rates supported by a PHY on the 802.11 station for transmit and receive operations.

The data type for OID\_DOT11\_DATA\_RATE\_MAPPING\_TABLE is the DOT11\_DATA\_RATE\_MAPPING\_TABLE structure.

```ManagedCPlusPlus
    typedef struct _DOT11_DATA_RATE_MAPPING_TABLE {
         NDIS_OBJECT_HEADER Header;
         ULONG uDataRateMappingLength;
         DOT11_DATA_RATE_MAPPING_ENTRY DataRateMappingEntries[126];
    } DOT11_DATA_RATE_MAPPING_TABLE, *PDOT11_DATA_RATE_MAPPING_TABLE;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_DATA\_RATE\_MAPPING\_TABLE structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_DATA\_RATE\_MAPPING\_TABLE\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_DATA\_RATE\_MAPPING\_TABLE).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="udataratemappinglength"></a>**uDataRateMappingLength**  
The number of entries in the **DataRateMappingEntries** array.

<a href="" id="dataratemappingentries"></a>**DataRateMappingEntries**  
The data rates supported by the 802.11 station. Each entry in the **DataRateMappingEntries** array is formatted as a [**DOT11\_DATA\_RATE\_MAPPING\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff547679) structure.

When OID\_DOT11\_DATA\_RATE\_MAPPING\_TABLE is queried, the miniport driver must do the following:

-   Return the data rates for the current PHY type.

    The current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** management information base (MIB) object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about this MIB object, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

-   Return all of the IEEE 802.11 standard data rates, even if the PHY does not support the data rate.

-   Return any proprietary, non-standard data rates supported by the PHY.

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

 

 




