---
title: WDI_TLV_GET_AUTO_POWER_SAVE
author: windows-driver-content
description: WDI_TLV_GET_AUTO_POWER_SAVE is a TLV that contains auto power save information for OID_WDI_GET_AUTO_POWER_SAVE.
ms.assetid: E57AD1CE-A252-4BB5-B983-11D3E46B7EC1
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_GET_AUTO_POWER_SAVE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_GET\_AUTO\_POWER\_SAVE


WDI\_TLV\_GET\_AUTO\_POWER\_SAVE is a TLV that contains auto power save information for [OID\_WDI\_GET\_AUTO\_POWER\_SAVE](https://msdn.microsoft.com/library/windows/hardware/dn925840).

## TLV Type


0xB3

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                               | Description                                                                                                        |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| UINT8                                                                              | The firmware current AutoPSM state.                                                                                |
| UINT8                                                                              | Reserved.                                                                                                          |
| UINT16                                                                             | Reserved.                                                                                                          |
| UINT16                                                                             | The beacon interval in milliseconds.                                                                               |
| UINT8                                                                              | The listen interval, in the unit of the beacon interval (for example, 1).                                          |
| UINT8                                                                              | The listen interval in the last low power state (for example, 5). If there is no last low power state, set to 255. |
| [**WDI\_POWER\_SAVE\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/dn926107) (UINT32)              | The power mode.                                                                                                    |
| [**WDI\_POWER\_SAVE\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/dn926107) (UINT32)              | The power mode in Dx.                                                                                              |
| [**WDI\_POWER\_MODE\_REASON\_CODE**](https://msdn.microsoft.com/library/windows/hardware/dn926106) (UINT32) | The reason for entering the Power Save state and listen interval.                                                  |
| UINT64                                                                             | Milliseconds since start.                                                                                          |
| UINT64                                                                             | Milliseconds in power save mode.                                                                                   |
| UINT64                                                                             | Number of received multicast packets, including broadcast.                                                         |
| UINT64                                                                             | Number of sent multicast packets, including broadcast.                                                             |
| UINT64                                                                             | Number of received unicast packets.                                                                                |
| UINT64                                                                             | Number of sent unicast packets.                                                                                    |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_GET_AUTO_POWER_SAVE%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


