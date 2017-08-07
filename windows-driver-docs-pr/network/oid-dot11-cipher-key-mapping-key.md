---
title: OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY
author: windows-driver-content
description: OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY
ms.assetid: 45ee67a9-28f8-43e6-a6c0-8cf233498204
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_CIPHER_KEY_MAPPING_KEY Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY object identifier (OID) requests that the miniport driver add, modify, or delete one or more entries in its key-mapping key table.

The 802.11 station uses key-mapping keys for data encryption and decryption between the 802.11 station and a specific AP or peer station in the basic service set (BSS) network. These keys are different from the default cipher keys, which the 802.11 station uses for data encryption and decryption between the 802.11 station and any AP or peer station in the BSS network.

**Note**  Support for this OID is mandatory if the 802.11 station supports one or more key-mapping keys. The miniport driver returns the number of key-mapping keys it supports when [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md) is queried.

 

The data type for this OID is the [**DOT11\_BYTE\_ARRAY**](dot11-byte-array.md) structure. The miniport driver sets the members of this structure as follows:

<a href="" id="header"></a>**Header**  
The type and size of the DOT11\_BYTE\_ARRAY structure and the revision of the [**DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE**](dot11-cipher-key-mapping-key-value.md) structures that follows it. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE\_BYTE\_ARRAY\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_BYTE\_ARRAY).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](ndis-object-header.md).

<a href="" id="unumofbytes"></a>**uNumOfBytes**  
Number of bytes within the **ucBuffer** array pertaining to the set request.

<a href="" id="utotalnumofbytes"></a>**uTotalNumOfBytes**  
Total number of bytes within the **ucBuffer** array. This value must be greater than or equal to **uNumOfBytes** .

<a href="" id="ucbuffer"></a>**ucBuffer**  
The list of key-mapping keys.

Each element in the list of key-mapping keys is formatted as a variable-length [**DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE**](dot11-cipher-key-mapping-key-value.md) structure. There must not be padding between key entries within the **ucBuffer** array.

When the OID\_DOT11\_CIPHER\_KEY\_MAPPING\_KEY OID is set, the miniport driver must do the following:

-   If the 802.11 station does not support key-mapping keys, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](miniportoidrequest.md) function.

-   Follow these guidelines when validating the members of the [**DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE**](dot11-cipher-key-mapping-key-value.md) structure in the following ways:
    -   If the 802.11 station does not support the cipher algorithm specified by the **AlgorithmId** member, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](miniportoidrequest.md) function.
    -   If the **bDelete** member of the [**DOT11\_CIPHER\_KEY\_MAPPING\_KEY\_VALUE**](dot11-cipher-key-mapping-key-value.md) structure is set to **TRUE**, delete the key material for the key referenced by the **PeerMacAddr** and **Direction** members. If the driver had previously deleted the specified key, it must accept the set request by returning NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](miniportoidrequest.md) function.
-   When modifying TKIP keys, synchronize the key update with the packet-processing path of the 802.11 station.

    For example, the miniport driver must avoid situations in which the packet payload was decrypted using the old cipher key and verified using the new message integrity code (MIC) key.

The 802.11 station must clear its key-mapping keys if the following conditions are met:

-   The miniport driver's [*MiniportInitializeEx*](miniportinitializeex.md) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_CIPHER_KEY_MAPPING_KEY%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


