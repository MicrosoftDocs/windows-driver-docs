---
title: OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM
author: windows-driver-content
description: OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM
ms.assetid: c661d254-8614-4282-9887-c7806a4f1606
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ENABLED_MULTICAST_CIPHER_ALGORITHM Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM object identifier (OID) requests that the miniport driver set the Extensible Station (ExtSTA) **msDot11EnabledMulticastCipherAlgo** management information base (MIB) object to the specified data.

When queried, this OID requests that the miniport driver return the value of the **msDot11EnabledMulticastCipherAlgo** MIB object.

The **msDot11EnabledMulticastCipherAlgo** MIB object specifies the list of multicast cipher algorithms that the 802.11 station enables for use when connecting to a basic service set (BSS) network. After [OID\_DOT11\_CONNECT\_REQUEST](oid-dot11-connect-request.md) is set, the 802.11 station will attempt to connect to a BSS whose 802.11 Beacon or Probe Response frames specify support for a multicast cipher algorithm defined by an entry within the **msDot11EnabledMulticastCipherAlgo** MIB object.

**Note**  Support for this OID is mandatory if the 802.11 station supports any multicast cipher algorithms. The miniport driver returns a list of supported multicast cipher algorithms when [OID\_DOT11\_SUPPORTED\_MULTICAST\_ALGORITHM\_PAIR](oid-dot11-supported-multicast-algorithm-pair.md) is queried.

 

The data type for this OID is the [**DOT11\_CIPHER\_ALGORITHM\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff547673) structure.

When OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM is set, the miniport driver must do the following:

-   If the **uNumOfEntries** member of the DOT11\_CIPHER\_ALGORITHM\_LIST structure is set to zero, fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. The **msDot11EnabledMulticastCipherAlgo** MIB object must always contain at least one entry.

-   If the 802.11 station does not support a specified multicast cipher algorithm, return NDIS\_STATUS\_INVALID\_DATA from its *MiniportOidRequest* function.

-   If the 802.11 station does not support any of the specified multicast cipher algorithms for any of the enabled authentication algorithms defined by the ExtSTA **msDot11EnabledAuthAlgo** MIB object, return NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

    For more information about the **msDot11EnabledAuthAlgo** MIB object, see [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](oid-dot11-enabled-authentication-algorithm.md).

-   Enable the specified multicast cipher algorithms for any enabled authentication algorithm that supports the cipher.

-   Disable all supported multicast cipher algorithms that are not in the specified list.

-   Ensure that the value of the **InformationBufferLength** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's OidRequest parameter is at least the value returned by the following formula:

    ```
     FIELD_OFFSET(DOT11_CIPHER_ALGORITHM_LIST, AlgorithmIds) + uNumOfEntries * sizeof(DOT11_CIPHER_ALGORITHM))
    ```

When OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM is queried, the miniport driver must do the following:

-   If this OID was previously set, returns the list of multicast cipher algorithms in the same order as they were set.

-   If OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM was not previously set, returns its default multicast ciphers in the list.

-   The miniport driver cannot return an empty list of multicast cipher algorithms. If the 802.11 station has not enabled any multicast cipher algorithms, the miniport driver must return a list containing DOT11\_CIPHER\_ALGO\_NONE.

The default value for the **msDot11EnabledMulticastCipherAlgo** MIB object is the list of multicast ciphers supported by the enabled authentication algorithms specified by the **msDot11EnabledAuthAlgo** MIB object. The default multicast cipher list must be ordered by preference. For more information about cipher preference, see [**DOT11\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547672).

The miniport driver must set the **msDot11EnabledMulticastCipherAlgo** MIB object to the default multicast cipher if the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the media access control (MAC) layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

-   The **msDot11EnabledAuthAlgo** MIB object is changed in response to a set request of the [OID\_DOT11\_ENABLED\_AUTHENTICATION\_ALGORITHM](oid-dot11-enabled-authentication-algorithm.md) OID.

The following points describe set requests of OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM by the operating system:

-   The operating system might not always issue a set request of OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM. In this case, the 802.11 station should use the default multicast cipher during any connection or roam operations. For more information about these operations, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185) and [Roaming Operations](https://msdn.microsoft.com/library/windows/hardware/ff570717).

-   If the operating system issues a set request of OID\_DOT11\_ENABLED\_MULTICAST\_CIPHER\_ALGORITHM, it will precede a set request of [OID\_DOT11\_ENABLED\_UNICAST\_CIPHER\_ALGORITHM](oid-dot11-enabled-unicast-cipher-algorithm.md).

**Note**  Beginning in Windows 7, the operating system enables only one cipher algorithm at a time.

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_ENABLED_MULTICAST_CIPHER_ALGORITHM%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


