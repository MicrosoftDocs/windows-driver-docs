---
title: WDI_TLV_LINK_STATE_CHANGE_PARAMETERS
description: WDI_TLV_LINK_STATE_CHANGE_PARAMETERS is a TLV that contains link state change parameters for NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE.
ms.assetid: 808C2E69-B713-41A3-AFB9-7441D2A96867
ms.date: 07/18/2017
keywords:
 - WDI_TLV_LINK_STATE_CHANGE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_LINK\_STATE\_CHANGE\_PARAMETERS


WDI\_TLV\_LINK\_STATE\_CHANGE\_PARAMETERS is a TLV that contains link state change parameters for [NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE](https://msdn.microsoft.com/library/windows/hardware/dn925638).

## TLV Type


0x56

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Specifies the MAC address of the remote peer.                                                                                                                                   |
| UINT32                                            | Specifies the current TX link speed. This is a value, in kilobits per second, that is the current TX link speed for this virtualized port. The conversion is 1 kbps = 1000 bps. |
| UINT32                                            | Specifies the current RX link speed. This is a value, in kilobits per second, that is the current RX link speed for this virtualized port. The conversion is 1 kbps = 1000 bps. |
| UINT8                                             | Specifies the current link quality. This is a value between 0 and 100 that is the current link quality for this virtualized port.                                               |

 

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

 

 




