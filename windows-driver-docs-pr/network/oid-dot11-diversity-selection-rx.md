---
title: OID_DOT11_DIVERSITY_SELECTION_RX
author: windows-driver-content
description: When queried, the OID_DOT11_DIVERSITY_SELECTION_RX object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 dot11DiversitySelectionRx management information base (MIB) object for the current PHY type on the 802.11 station.
ms.assetid: b5be9319-3702-4bda-8dfa-3c94da2b1a69
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_DIVERSITY_SELECTION_RX Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_DIVERSITY\_SELECTION\_RX


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_DIVERSITY\_SELECTION\_RX object identifier (OID) requests that the miniport driver return the value of the IEEE 802.11 **dot11DiversitySelectionRx** management information base (MIB) object for the current PHY type on the 802.11 station.

This MIB object specifies the list of antennas on the current PHY type that are available for receive (RX) diversity operations.

The data type for OID\_DOT11\_DIVERSITY\_SELECTION\_RX is the DOT11\_DIVERSITY\_SELECTION\_RX\_LIST.

```ManagedCPlusPlus
    typedef struct _DOT11_DIVERSITY_SELECTION_RX_LIST {
         ULONG uNumOfEntries;
         ULONG uTotalNumOfEntries;
         DOT11_DIVERSITY_SELECTION_RX dot11DiversitySelectionRx[1];
    } DOT11_DIVERSITY_SELECTION_RX_LIST, *PDOT11_DIVERSITY_SELECTION_RX_LIST;
  
```

This structure includes the following members:

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **dot11DiversitySelectionRx** array. A zero value for this member indicates an empty list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **dot11DiversitySelectionRx** array requires.

<a href="" id="dot11diversityselectionrx"></a>**dot11DiversitySelectionRx**  
The list of receive (RX) antennas that may be used for RX diversity operations.

The data type for the elements of the **dot11DiversitySelectionRx** array is the DOT11\_DIVERSITY\_SELECTION\_RX structure.

``` syntax
typedef struct _DOT11_DIVERSITY_SELECTION_RX {         ULONG uAntennaListIndex;
 BOOLEAN
 bDiversitySelectionRX; } DOT11_DIVERSITY_SELECTION_RX,*PDOT11_DIVERSITY_SELECTION_RX;
```

This structure includes the following members:

<a href="" id="uantennalistindex"></a>**uAntennaListIndex**  
The antenna index. The value of **uAntennaListIndex** must be from 1 through 255.

The antenna index value must match the index of a supported RX antenna previously specified by the miniport driver when queried by [OID\_DOT11\_SUPPORTED\_RX\_ANTENNA](oid-dot11-supported-rx-antenna.md).

<a href="" id="bdiversityselectionrx"></a>**bDiversitySelectionRX**  
When set to **TRUE**, this indicates that the antenna represented by **uAntennaListIndex** can be used for receive diversity.

When OID\_DOT11\_DIVERSITY\_SELECTION\_RX is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure, including all entries in the **dot11DiversitySelectionRx** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as the following list shows:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure, the miniport driver must do the following:

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to the length, in bytes, of the entire DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **dot11DiversitySelectionRx** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure. The miniport driver must also copy the entire DOT11\_DIVERSITY\_SELECTION\_RX\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, the current PHY type is determined through the ExtSTA **msDot11CurrentPhyID** MIB object. This MIB object specifies the index of the current PHY type within the 802.11 station's list of supported PHY types. For more information about **msDot11CurrentPhyID**, see [OID\_DOT11\_CURRENT\_PHY\_ID](oid-dot11-current-phy-id.md).

**Note**  A Native 802.11 miniport driver that is designed to run on the Windows Vista or Windows Server 2008 operating systems must always reset this 802.11 MIB OID to its default value. This is the case regardless of the value of the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure. This requirement applies to a miniport driver that, in a call to the **NdisMSetMiniportAttributes** function, sets **MiniportAttributes** -&gt; **Native\_802\_11\_Attributes** -&gt; **Header** -&gt; **Revision** to NDIS\_MINIPORT\_ADAPTER\_802\_11\_ATTRIBUTES\_REVISION\_1.

 

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


[Native 802.11 MIB OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560645)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_DIVERSITY_SELECTION_RX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


