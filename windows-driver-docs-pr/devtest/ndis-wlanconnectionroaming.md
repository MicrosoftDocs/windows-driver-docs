---
title: WlanConnectionRoaming rule (ndis)
description: The WlanConnectionRoaming rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) connection and roaming sequence.
ms.assetid: 7DB1881B-4DD8-4E06-AAF2-C6EAD0EEC5FC
keywords: ["WlanConnectionRoaming rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanConnectionRoaming
api_type:
- NA
---

# WlanConnectionRoaming rule (ndis)


The **WlanConnectionRoaming** rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) connection and roaming sequence.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) ( 0x00093005) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportHaltEx**](https://msdn.microsoft.com/library/windows/hardware/ff559388)
[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)
See also
--------

[General Connection Operation Guidelines](https://msdn.microsoft.com/library/windows/hardware/ff552458)
[NDIS\_STATUS\_DOT11\_CONNECTION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567328)
[OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409)
[NDIS\_STATUS\_DOT11\_ROAMING\_START](https://msdn.microsoft.com/library/windows/hardware/ff567360)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20WlanConnectionRoaming%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




