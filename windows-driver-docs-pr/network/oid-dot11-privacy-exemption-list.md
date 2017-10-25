---
title: OID_DOT11_PRIVACY_EXEMPTION_LIST
author: windows-driver-content
description: When set, the OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST object identifier (OID) requests that the miniport driver set its Extensible Station (ExtSTA) msDot11PrivacyExemptionList management information base (MIB) object to the specified data.
ms.assetid: 0867c5b2-035e-47c1-970b-a928f6e8aab9
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_PRIVACY_EXEMPTION_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST object identifier (OID) requests that the miniport driver set its Extensible Station (ExtSTA) **msDot11PrivacyExemptionList** management information base (MIB) object to the specified data.

When queried, this OID requests that the miniport driver return the value of the **msDot11PrivacyExemptionList** MIB object.

The **msDot11PrivacyExemptionList** MIB object contains a list of exemptions for packet decryption. The 802.11 station applies these exemptions to packets it receives that match the IEEE EtherType value specified for the exemption.

**Note**  Support for OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST is mandatory if the 802.11 station supports any cipher algorithms. The miniport driver returns a list of supported cipher algorithms when [OID\_DOT11\_SUPPORTED\_UNICAST\_ALGORITHM\_PAIR](oid-dot11-supported-unicast-algorithm-pair.md) or [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) are queried.

 

The data type for OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST is the DOT11\_PRIVACY\_EXEMPTION\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_PRIVACY_EXEMPTION_LIST {
         NDIS_OBJECT_HEADER Header;
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_PRIVACY_EXEMPTION PrivacyExemptionEntries[1];
    } DOT11_PRIVACY_EXEMPTION_LIST, *PDOT11_PRIVACY_EXEMPTION_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_PRIVACY\_EXEMPTION\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_PRIVACY\_EXEMPTION\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_PRIVACY\_EXEMPTION\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **PrivacyExemptionEntries** array. A zero value for this member indicates an empty privacy exemption list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **PrivacyExemptionEntries** array can contain.

<a href="" id="privacyexemptionentries"></a>**PrivacyExemptionEntries**  
The list of exempted EtherTypes. Each entry in the list is formatted as a [**DOT11\_PRIVACY\_EXEMPTION**](https://msdn.microsoft.com/library/windows/hardware/ff548756) structure.

When OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST is set, the miniport driver should ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's OidRequest parameter is at least the value returned by the following formula:

```
 FIELD_OFFSET(DOT11_PRIVACY_EXEMPTION_LIST, PrivacyExemptionEntries) + uNumOfEntries * sizeof(DOT11_PRIVACY_EXEMPTION))
```

When OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST is set, the miniport driver must fail the set request if the **uNumOfEntries** member has a value greater than the value of **uPrivacyExemptionListSize** that the driver previously returned through a query of [OID\_DOT11\_EXTSTA\_CAPABILITY](oid-dot11-extsta-capability.md). In this situation, the miniport driver must return NDIS\_STATUS\_INVALID\_LENGTH from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

When OID\_DOT11\_PRIVACY\_EXEMPTION\_LIST is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_PRIVACY\_EXEMPTION\_LIST structure, including all entries in the **PrivacyExemptionEntries** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_PRIVACY\_EXEMPTION\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **PrivacyExemptionEntries** array.

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_PRIVACY\_EXEMPTION\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to than the length, in bytes, of the entire DOT11\_PRIVACY\_EXEMPTION\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_PRIVACY\_EXEMPTION\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **PrivacyExemptionEntries** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_PRIVACY\_EXEMPTION\_LIST structure. The miniport driver must also copy the entire DOT11\_PRIVACY\_EXEMPTION\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

The default for the **msDot11PrivacyExemptionList** MIB object is an empty list with **uNumEntries** set to zero. The miniport driver must set this MIB object to its default if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the media access control (MAC) layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_PRIVACY_EXEMPTION_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


