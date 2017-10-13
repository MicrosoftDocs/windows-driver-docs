---
title: OID_DOT11_ENABLED_AUTHENTICATION_ALGORITHM
author: windows-driver-content
description: When set, the OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM object identifier (OID) requests that the miniport driver set the Extensible Station (ExtSTA) msDot11EnabledAuthAlgo management information base (MIB) object to the specified data.
ms.assetid: d3c262b0-1b04-4a98-be2d-baae4abbd58f
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ENABLED_AUTHENTICATION_ALGORITHM Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM object identifier (OID) requests that the miniport driver set the Extensible Station (ExtSTA) **msDot11EnabledAuthAlgo** management information base (MIB) object to the specified data.

When queried, this OID requests that the miniport driver return the value of the **msDot11EnabledAuthAlgo** MIB object.

The **msDot11EnabledAuthAlgo** MIB object defines the list of authentication algorithms the 802.11 station has enabled for use when connecting to a basic service set (BSS) network. After [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) is set, the 802.11 station will attempt to connect to a BSS whose 802.11 Beacon or Probe Response frames specify support for an authentication algorithm defined by an entry within the **msDot11EnabledAuthAlgo** MIB object.

The data type for OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM is the DOT11\_AUTH\_ALGORITHM\_LIST structure.

```ManagedCPlusPlus
    typedef struct DOT11_AUTH_ALGORITHM_LIST {
         NDIS_OBJECT_HEADER Header;
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_AUTH_ALGORITHM AlgorithmIds[1];
    } DOT11_AUTH_ALGORITHM_LIST,   *PDOT11_AUTH_ALGORITHM_LIST;
  
```

This structure includes the following members:

<a href="" id="header"></a>**Header**  
The type, revision, and size of the DOT11\_AUTH\_ALGORITHM\_LIST structure. This member is formatted as an [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588) structure.

The miniport driver must set the members of **Header** to the following values:

<a href="" id="type"></a>**Type**  
This member must be set to NDIS\_OBJECT\_TYPE\_DEFAULT.

<a href="" id="revision"></a>**Revision**  
This member must be set to DOT11\_AUTH\_ALGORITHM\_LIST\_REVISION\_1.

<a href="" id="size"></a>**Size**  
This member must be set to sizeof(DOT11\_AUTH\_ALGORITHM\_LIST).

For more information about these members, see [**NDIS\_OBJECT\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff566588).

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **AlgorithmIds** array. A zero value for this member indicates an empty list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **AlgorithmIds** array can contain.

<a href="" id="algorithmids"></a>**AlgorithmIds**  
The authentication algorithm list, with each entry specified by a [**DOT11\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547655) enumerator value.

The list of authentication algorithms is sorted by preference. **AlgorithmIds\[0\]** specifies the authentication algorithm with the highest preference.

The Microsoft 802.1X supplicant enables only one standard 802.11 authentication algorithm. However, a supplicant developed by the independent hardware vendor (IHV) can enable one or more authentication algorithms. For more information about 802.1X supplicants, refer to the IEEE 802.1X-2001 standard.

The 802.11 station uses the list of authentication algorithms when performing a connection operation to a BSS network. Depending on the authentication algorithms supported by the BSS (as advertised in the 802.11 Beacon or Probe Response frames), the following apply to the 802.11 station:

-   If none of the advertised authentication algorithms matches an algorithm from its list, the 802.11 station cannot connect to the BSS network.

-   If the BSS advertises one or more authentication algorithm that match algorithms from its list, the 802.11 station must connect to the BSS using the most preferred algorithm from the intersection of the advertised algorithms with its list. For example, if the Beacon frame advertises authentication algorithms that match **AlgorithmIds\[0\]** and **AlgorithmIds\[3\]**, the station must connect to the BSS using **AlgorithmIds\[0\]**.

For more information about the connection operation, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

When OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM is set, the miniport driver must do the following:

-   If **uNumOfEntries** is set to zero, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. The **msDot11EnabledAuthAlgo** MIB object must always contain at least one entry.

-   If the 802.11 station does not support any of the authentication algorithms in the specified list, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its *MiniportOidRequest* function.

-   Reload the default values for the enabled unicast cipher algorithms for each authentication algorithm in the specified list. For more information about the default values for unicast cipher algorithms, see [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-unicast-cipher-algorithm.md).

-   Reload the default values for the enabled multicast cipher algorithms for each authentication algorithm in the specified list. For more information about the default values for multicast cipher algorithms, see [OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-multicast-cipher-algorithm.md).

-   Disable any authentication algorithms that are not in the specified list.

-   Ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's OidRequest parameter is at least the value returned by the following formula:

    ```
     FIELD_OFFSET(DOT11_AUTH_ALGORITHM_LIST, AlgorithmIds) + uNumOfEntries * sizeof(DOT11_AUTH_ALGORITHM))
    ```

When OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_AUTH\_ALGORITHM\_LIST structure, including all entries in the **AlgorithmIds** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_AUTH\_ALGORITHM\_LIST structure, the miniport driver must do the following:

    -   Set the **uNumOfEntries** member to zero.

    -   Set the **uTotalNumOfEntries** member to the number of entries in the **AlgorithmIds** array.

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_AUTH\_ALGORITHM\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to than the length, in bytes, of the entire DOT11\_AUTH\_ALGORITHM\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_AUTH\_ALGORITHM\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **AlgorithmIds** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_AUTH\_ALGORITHM\_LIST structure. The miniport driver must also copy the entire DOT11\_AUTH\_ALGORITHM\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

The miniport driver must define a default authentication algorithm from its supported algorithms based on the following:

-   If the desired BSS type is **dot11\_BSS\_type\_infrastructure**, the miniport driver must choose the default authentication algorithm based on the following order of preference:

    **DOT11\_AUTH\_ALGO\_RSNA**(highest preference)

    **DOT11\_AUTH\_ALGO\_WPA**

    **DOT11\_AUTH\_ALGO\_RSNA\_PSK**

    **DOT11\_AUTH\_ALGO\_WPA\_PSK**

    **DOT11\_AUTH\_ALGO\_80211\_OPEN**

    **DOT11\_AUTH\_ALGO\_80211\_SHARED\_KEY**(lowest preference)

-   If the desired BSS type is **dot11\_BSS\_type\_independent**, the miniport driver must choose the default authentication algorithm based on the following preference order:

    **DOT11\_AUTH\_ALGO\_RSNA\_PSK**(highest preference)

    **DOT11\_AUTH\_ALGO\_80211\_OPEN**

    **DOT11\_AUTH\_ALGO\_80211\_SHARED\_KEY**(lowest preference)

-   If the 802.11 station supports one or more vendor-defined authentication algorithms, the miniport driver must select the most preferred vendor algorithm as its default authentication algorithm.

The miniport driver must set the **msDot11EnabledAuthAlgo** MIB object to the default authentication algorithm whenever the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

-   A set request of [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md) is made.

**Note**  Beginning in Windows 7, the operating system enables only one authentication algorithm at a time.

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_ENABLED_AUTHENTICATION_ALGORITHM%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


