---
title: OID_DOT11_RECV_SENSITIVITY_LIST
author: windows-driver-content
description: When queried, the OID\_DOT11\_RECV\_SENSITIVITY\_LIST object identifier (OID) requests that the miniport driver return the list of receive sensitivity ranges for all data rates supported on a PHY.
ms.assetid: 6220b866-b914-4bc9-9a26-13f2109736e6
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_RECV_SENSITIVITY_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_RECV\_SENSITIVITY\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_RECV\_SENSITIVITY\_LIST object identifier (OID) requests that the miniport driver return the list of receive sensitivity ranges for all data rates supported on a PHY. The miniport driver returns the receive sensitivity list for the PHY that is specified in the query request.

The data type for this OID is the DOT11\_RECV\_SENSITIVITY\_LIST structure.

```ManagedCPlusPlus
 typedef struct _DOT11_RECV_SENSITIVITY_LIST {
    union {
        DOT11_PHY_TYPE dot11PhyType;
        ULONG uPhyId;
    };
    ULONG uNumOfEntries;
    ULONG uTotalNumOfEntries;
    DOT11_RECV_SENSITIVITY dot11RecvSensitivity[1];
} DOT11_RECV_SENSITIVITY_LIST, * PDOT11_RECV_SENSITIVITY_LIST;
  
```

This structure includes the following members:

<a href="" id="dot11phytype"></a>**dot11PhyType**  
The PHY type queried for the receive sensitivity list. The PHY type is defined by the [**DOT11\_PHY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548741) enumeration.

If the 802.11 station does not support the specified PHY type, the miniport driver must fail the query request by returning NDIS\_STATUS\_BAD\_VERSION from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

**Note**  The miniport driver must not use this member if it is operating in Extensible Station (ExtSTA) mode.

 

<a href="" id="uphyid"></a>**uPhyId**  
The identifier (ID) of the PHY that is queried for the receive sensitivity list. The PHY ID is the index within the list of supported PHYs returned by the driver through a query of [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](oid-dot11-supported-phy-types.md).

If the ID is invalid, the miniport driver must fail the query request by returning NDIS\_STATUS\_BAD\_VERSION from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

**Note**  The miniport driver must use this member if it is operating in ExtSTA mode.

 

<a href="" id="unumofentries"></a>**uNumOfEntries**  
Number of entries in the **dot11RecvSensitivity** array. A zero value for this member indicates an empty receive sensitivity list.

<a href="" id="utotalnumofentries"></a>**uTotalNumOfEntries**  
Maximum number of entries that the **dot11RecvSensitivity** array requires.

<a href="" id="dot11recvsensitivity"></a>**dot11RecvSensitivity**  
The receive sensitivity list for the PHY that is specified by the **dot11PhyType** member.

The data type for the elements of the **dot11RecvSensitivity** array is the DOT11\_RECV\_SENSITIVITY structure.

``` syntax
typedef struct _DOT11_RECV_SENSITIVITY {         UCHAR ucDataRate;
         LONG lRSSIMin;
 LONG
 lRSSIMax; } DOT11_RECV_SENSITIVITY, *PDOT11_RECV_SENSITIVITY;
```

This structure includes the following members:

<a href="" id="ucdatarate"></a>**ucDataRate**  
A data rate supported by the PHY that is specified by the **dot11PhyType** member. The miniport driver must specify a data rate from 2 through 127 and in units of 500 kilobits per second (kbps).

<a href="" id="lrssimin"></a>**lRSSIMin**  
The minimum receive signal strength indication (RSSI) value, in units of decibels referenced to 1.0 milliwatts (dBm), for the data rate specified by the **ucDataRate** member.

<a href="" id="lrssimax"></a>**lRSSIMax**  
The maximum RSSI value, in units of dBm, for the data rate that is specified by the **ucDataRate** member.

When OID\_DOT11\_RECV\_SENSITIVITY\_LIST is queried, the miniport driver must verify that the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the entire DOT11\_RECV\_SENSITIVITY\_LIST structure, including all entries in the **dot11RecvSensitivity** array. The value of the **InformationBufferLength** member of the *OidRequest* parameter determines what the miniport driver must do, as shown in the following list:

-   If the value of the **InformationBufferLength** member is less than the length, in bytes, of the entire DOT11\_RECV\_SENSITIVITY\_LIST structure, the miniport driver must do the following:

    -   For the *OidRequest* parameter, set the **BytesWritten** member to zero and the **BytesNeeded** member to the length, in bytes, of the entire DOT11\_RECV\_SENSITIVITY\_LIST structure.

    -   Fail the query request by returning NDIS\_STATUS\_BUFFER\_OVERFLOW from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   If the value of the **InformationBufferLength** member is greater than or equal to the length, in bytes, of the entire DOT11\_RECV\_SENSITIVITY\_LIST structure, the miniport driver must do the following to complete a successful query request:

    -   For the DOT11\_RECV\_SENSITIVITY\_LIST structure, set the **uNumOfEntries** and **uTotalNumOfEntries** members to the total number of entries in the **dot11RecvSensitivity** array.

    -   For the *OidRequest* parameter, set the **BytesNeeded** member to zero and the **BytesWritten** member to the length, in bytes, of the entire DOT11\_RECV\_SENSITIVITY\_LIST structure. The miniport driver must also copy the entire DOT11\_RECV\_SENSITIVITY\_LIST structure to the **InformationBuffer** member.

    -   Return NDIS\_STATUS\_SUCCESS from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_RECV_SENSITIVITY_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


