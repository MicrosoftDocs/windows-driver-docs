---
title: WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY
description: WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY is a TLV that contains the policy used by the firmware for operating channel selection after a Wi-Fi Direct GO Reset is stopped/restarted.
ms.assetid: 6EA61C65-8573-491D-9268-8A02440A1175
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_INTERNAL\_RESET\_POLICY


WDI\_TLV\_P2P\_GO\_INTERNAL\_RESET\_POLICY is a TLV that contains the policy used by the firmware for operating channel selection after a Wi-Fi Direct GO Reset is stopped/restarted.

## TLV Type


0xB2

## Length


The size (in bytes) of a UINT32.

## Values


| Type                                                                                            | Description                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_GO\_INTERNAL\_RESET\_POLICY**](https://msdn.microsoft.com/library/windows/hardware/dn926096) (UINT32) | If an Wi-Fi Direct GO Reset is stopped/restarted by the IHV component on its own (for example, for Bluetooth co-ex spatial stream downgrade), this configuration defines the policy to be adopted by the firmware for operating channel selection after the reset. |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




