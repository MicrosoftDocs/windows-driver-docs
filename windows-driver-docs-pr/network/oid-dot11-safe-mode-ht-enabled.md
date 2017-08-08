---
title: OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED
author: windows-driver-content
description: When set, the OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED object identifier (OID) requests that the miniport driver enable 802.11n safe mode on the 802.11 station by setting the Boolean value msDot11SafeModeHtEnabled to TRUE.
ms.assetid: 55E517EA-046B-43FF-9FA1-52A89AC8255B
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_SAFE_MODE_HT_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED object identifier (OID) requests that the miniport driver enable 802.11n safe mode on the 802.11 station by setting the Boolean value **msDot11SafeModeHtEnabled** to **TRUE**.

The data type for this OID is a Boolean value.

The miniport driver must fail a set request with error code **NDIS\_STATUS\_INVALID\_STATE** if the 802.11 station is in any state except the initialization (INIT) state.

When this OID is queried, if the extensible station is in the INIT state, the miniport driver must complete the request if the NIC set the **bSafeModeImplemented** member of the [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688) structure to **TRUE**. Otherwise, the miniport driver should fail the set request.

This OID is set only if the NIC implements the 802.11n safe mode of operation, as indicated by the value of the **bSafeModeImplemented** member of [**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688).

If this OID is not set, its default value is used.

Safe mode is disabled by default. The default value of **msDot11SafeModeHtEnabled** is **FALSE**.

When queried, OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED requests that the miniport driver return the value of **msDot11SafeModeHtEnabled**.

When in safe mode, the miniport driver should ignore **dot11ExcludeUnencrypted**.

The NIC must not use traffic specification (TSPEC) in safe mode.

When processing an OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED OID request, the miniport should do the following:

-   Indicate that QoS is in use on the network by setting the **ucActiveQoSProtocol** member of the [**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547647) structure to one of the flag values listed in the **ucActiveQoSProtocolmember description**.
-   In the case of an 802.11g association, the miniport should not use QoS. The **ucActiveQoSProtocol** member of [**DOT11\_ASSOCIATION\_COMPLETION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff547647) should be set to zero on association completion.
-   On the TX path, the miniport should extend the 802.11 header with QoS priority-received in-frame OOB data, based on the condition that WMM was negotiated on the current association.
-   On the RX path, the miniport should not strip the QoS flag from the 802.11 header when operating in safe mode.
-   Pass the QoS data in the 802.11 frame as-is to the Nwifi driver.
-   Disable 802.11w when in Federal Information Processing Standards (FIPS) mode. Otherwise, Windows would not succeed the association.
-   While it is transmitting RSN capabilities, the miniport should ensure that the SPP (signaling and payload protected) A-MSDU capable bit (Bit 10) is set to zero. Only PP (payload protected) A-MSDU is supported in safe mode.

**Note**  The miniport will not receive [OID\_DOT11\_SAFE\_MODE\_ENABLED](oid-dot11-safe-mode-enabled.md) if it completes OID\_DOT11\_SAFE\_MODE\_HT\_ENABLED successfully.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>None supported</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_EXTSTA\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff547688)

[OID\_DOT11\_SAFE\_MODE\_ENABLED](oid-dot11-safe-mode-enabled.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_SAFE_MODE_HT_ENABLED%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


