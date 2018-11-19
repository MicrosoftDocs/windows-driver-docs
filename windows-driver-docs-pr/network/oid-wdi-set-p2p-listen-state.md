---
title: OID_WDI_SET_P2P_LISTEN_STATE
description: OID_WDI_SET_P2P_LISTEN_STATE sets the Wi-Fi Direct listen state on the port.
ms.assetid: d488903b-ef64-44b6-b07a-70168a0ccfd8
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_P2P_LISTEN_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_P2P\_LISTEN\_STATE


OID\_WDI\_SET\_P2P\_LISTEN\_STATE sets the Wi-Fi Direct listen state on the port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

There are different levels of listen state, and the port is expected to adhere to concurrency requirements across ports.

This property is only applicable to virtualized Wi-Fi Direct Adapter Port interfaces.

When the listen state is active, the port is expected to park the radio on a social channel for a certain period of time.

If the adapter has a virtualized port operating on a non-social channel, the port may become discoverable on that channel. If this behavior is used, the port must be very highly available to allow other adapters to quickly discover it when in the scan phase of Wi-Fi Direct discovery. This is provided as a trade-off to avoid channel hopping in low latency scenarios.

**Note**  This property specifies a radio time slice requirement to the port, which may cause conflicts with other properties or tasks issued to the port.

 

## Set property parameters


| TLV                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                                                      |
|-----------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_LISTEN\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn897975)       |                                |          | Desired listen state.                                                                                                                                            |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/dn897869)   |                                | X        | The host’s desired listen channel when enabling the Wi-Fi Direct listen state. If this option is not specified, the port may select a listen channel on its own. |
| [**WDI\_TLV\_P2P\_LISTEN\_DURATION**](https://msdn.microsoft.com/library/windows/hardware/dn897973) |                                |          | Cycle duration and listen time.                                                                                                                                  |

 

## Set property results


No additional data. The data in the header is sufficient.
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

 

 




