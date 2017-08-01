---
title: WDI_TLV_LINK_STATE_CHANGE_PARAMETERS
author: windows-driver-content
description: WDI_TLV_LINK_STATE_CHANGE_PARAMETERS is a TLV that contains link state change parameters for NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE.
ms.assetid: 808C2E69-B713-41A3-AFB9-7441D2A96867
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_LINK_STATE_CHANGE_PARAMETERS Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_LINK_STATE_CHANGE_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


