---
title: OID_WDI_GET_AUTO_POWER_SAVE
description: OID_WDI_GET_AUTO_POWER_SAVE gets the power save state of the port.
ms.assetid: b7a14348-66ad-4728-986d-05145eb49b27
ms.date: 07/18/2017
keywords:
 - OID_WDI_GET_AUTO_POWER_SAVE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




