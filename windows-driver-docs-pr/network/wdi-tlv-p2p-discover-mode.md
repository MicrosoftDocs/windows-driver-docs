---
title: WDI_TLV_P2P_DISCOVER_MODE
author: windows-driver-content
description: WDI_TLV_P2P_DISCOVER_MODE is a TLV that contains Wi-Fi Direct discovery mode information for OID_WDI_TASK_P2P_DISCOVER.
ms.assetid: 430DDDBE-C861-4E85-BFAB-31670F77696D
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_P2P_DISCOVER_MODE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DISCOVER\_MODE


WDI\_TLV\_P2P\_DISCOVER\_MODE is a TLV that contains Wi-Fi Direct discovery mode information for [OID\_WDI\_TASK\_P2P\_DISCOVER](https://msdn.microsoft.com/library/windows/hardware/dn925955).

## TLV Type


0xA9

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                                       | Description                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_DISCOVER\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926093) (UINT32)                    | The type of discovery to be performed by the port.                                                                                                                                                                              |
| UINT8                                                                                      | A flag that indicates if a complete device discovery is required. Valid values are 0 (not required) and 1 (required). If this flag is set to 0, a partial discovery may be performed.                                           |
| [**WDI\_P2P\_SCAN\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926099) (UINT32)                            | The type of scan to be performed by the port in scan phase.                                                                                                                                                                     |
| [**WDI\_P2P\_SERVICE\_DISCOVERY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926101) (UINT32) | The type of Service Discovery to be performed.                                                                                                                                                                                  |
| UINT8                                                                                      | The scan repeat count. Specifies if the full scan procedure should be repeated. If set to 0, the scan should be repeated until the task is aborted by the host.                                                                 |
| UINT32                                                                                     | The time between scans. If the scan repeat count is not set to 1, this time specifies how long (in milliseconds) device should wait before repeating the scan procedure after completing a full scan of the requested channels. |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_DISCOVER_MODE%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


