---
title: OID\_WDI\_GET\_AUTO\_POWER\_SAVE
author: windows-driver-content
description: OID\_WDI\_GET\_AUTO\_POWER\_SAVE gets the power save state of the port.
ms.assetid: b7a14348-66ad-4728-986d-05145eb49b27
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_GET_AUTO_POWER_SAVE Network Drivers Starting with Windows Vista
---

# OID\_WDI\_GET\_AUTO\_POWER\_SAVE


OID\_WDI\_GET\_AUTO\_POWER\_SAVE gets the power save state of the port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Not applicable           | 1                               |

 

There is a trade-off between power saving and latency. When auto power save mode is set to be enabled with the [OID\_WDI\_SET\_CONNECTION\_QUALITY](oid-wdi-set-connection-quality.md) command, the firmware tries to interact with the connected access point to go to power save mode as much as appropriate to save power. The firmware is also responsible for detecting if the connected access point confirms to the 802.11 specification and follows the power save mode protocol. If the access point does not conform (does not support power save mode correctly), the firmware should not go into power save mode, even when Auto Power Save is set to enabled. When Auto Power Save is set to disabled, the firmware focuses on low latency of sending and receiving packets. Examples of this are when streaming mode is on, and when the system is using AC power so low latency is preferred to saving power.

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                          | Multiple TLV instances allowed | Optional | Description                  |
|------------------------------------------------------------------------------|--------------------------------|----------|------------------------------|
| [**WDI\_TLV\_GET\_AUTO\_POWER\_SAVE**](https://msdn.microsoft.com/library/windows/hardware/dn926307) |                                |          | Auto power save information. |

 

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
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_GET_AUTO_POWER_SAVE%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


