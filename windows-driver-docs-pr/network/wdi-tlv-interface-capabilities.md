---
title: WDI_TLV_INTERFACE_CAPABILITIES
ms.topic: reference
description: WDI_TLV_INTERFACE_CAPABILITIES is a TLV that contains the capabilities of the Wi-Fi interface.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INTERFACE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI\_TLV\_INTERFACE\_CAPABILITIES


WDI\_TLV\_INTERFACE\_CAPABILITIES is a TLV that contains the capabilities of the Wi-Fi interface.

## TLV Type

0xF

## Length

The sum (in bytes) of the sizes of all contained elements.

## Values


| Type | Description |
| --- | --- |
| UINT32 | The maximum transfer unit (MTU) size. |
| UINT32 | The multicast list size for the adapter. |
| UINT16 | The backfill size in bytes. This value cannot be greater than 256 bytes. |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | The permanent MAC address for the adapter. If the device supports multiple permanent MAC addresses, the first MAC address that will be used by the device should be returned. |
| UINT32 | The maximum supported send rate for this adapter in kbps. |
| UINT32 | The maximum supported receive rate for this adapter in kbps. |
| UINT8 | Specifies whether the radio is enabled by hardware. Valid values are 0 (disabled) and 1 (enabled). |
| UINT8 | Specifies whether they radio is enabled by software. Valid values are 0 (disabled) and 1 (enabled). |
| UINT8 | Specifies whether the interface supports PLR. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether the interface supports FLR. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether sending and receiving action frames is supported. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | The supported number of RX spatial streams. |
| UINT8 | The supported number of TX spatial streams. |
| UINT8 | The number of channels that the adapter can work in concurrently, regardless of operation mode. |
| UINT8 | Specifies whether antenna diversity is supported. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether eCSA is supported. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether the adapter supports MAC address randomization. Valid values are 0 (not supported) and 1 (supported). |
 | [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | A bit mask that specifies for each address bit whether it can be randomized (0) or should keep the same value as the permanent address (1). The default is all zeros. |
| [**WDI\_BLUETOOTH\_COEXISTENCE\_SUPPORT**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_bluetooth_coexistence_support) (UINT32) | The supported level of Wi-Fi - Bluetooth coexistence. |
| UINT8 | Specifies non-WDI OID support. Valid values are: <ul><li>0 : Not supported. OIDs that the Microsoft component does not understand are not forwarded to the adapter.</li><li>1 : Supported. OIDs that the Microsoft component does not understand are forwarded to the adapter.</li></ul> <p>These OIDs will not contain WDI headers. To identify the adapter's port that the request came in on, use **NdisPortNumber** in the NDIS\_OID\_REQUEST and match it to the one in [WDI\_TASK\_CREATE\_PORT](./oid-wdi-task-create-port.md).</p> |
| UINT8 | Specifies whether the Fast Transition is supported. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether Mu-MIMO is supported. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies if the interface cannot support Miracast Sink. Valid values are 0 (supported) and 1 (not supported). |
| UINT8 | Specifies if 802.11v BSS transition is supported. Valid values are 0 (not supported) and 1 (supported). |
| UINT8 |  Specifies if the device supports IP docking capability. Valid values are 0 (not supported) and 1 (supported). <p>Added in Windows 10, version 1607, WDI version 1.0.21.</p> |
| UINT8 | Specifies if the device supports SAE authentication. Valid values are 0 (not supported) and 1 (supported). <p>Added in Windows 10, version 1903, WDI version 1.1.8.</p> |
| UINT8 | Specifies if the device supports Multiband Operation (MBO). Valid values are 0 (not supported) and 1 (supported). <p>Added in Windows 10, version 1903, WDI version 1.1.8.</p> |
| UINT8 | Specifies if the adapter implements beacon report measurements. Valid values are 0 (the adapter does not implement beacon report measurements) and 1 (the adapter implements its own 11k beacon report). <p>Added in Windows 10, version 1903, WDI version 1.1.8.</p> |

## Requirements

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

 

