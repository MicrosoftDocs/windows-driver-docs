---
title: WlanTimedConnectRequest rule (ndis)
description: The WlanTimedConnectRequest rule verifies that an OID\_DOT11\_CONNECT\_REQUEST is followed by a NDIS\_STATUS\_DOT11\_CONNECTION\_START within 10 seconds.
ms.assetid: F40D92B1-CA48-4060-B9E2-A965900EAF7B
keywords: ["WlanTimedConnectRequest rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanTimedConnectRequest
api_type:
- NA
---

# WlanTimedConnectRequest rule (ndis)


The **WlanTimedConnectRequest** rule verifies that an OID\_DOT11\_CONNECT\_REQUEST is followed by a NDIS\_STATUS\_DOT11\_CONNECTION\_START within 10 seconds.

Furthermore, an NDIS\_STATUS\_DOT11\_CONNECTION\_START is indicated only if the OID\_DOT11\_CONNECT\_REQUEST is completed with NDIS\_STATUS\_SUCCESS. This rule applies only to the Extensible Station port (Port 0).

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00094009) |

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportHaltEx**](https://msdn.microsoft.com/library/windows/hardware/ff559388)
[**MiniportOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559416)
[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
See also
--------

[General Connection Operation Guidelines](https://msdn.microsoft.com/library/windows/hardware/ff552458)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20WlanTimedConnectRequest%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




