---
title: OID_WDI_SET_CONNECTION_QUALITY
description: OID_WDI_SET_CONNECTION_QUALITY provides a hint to the IHV component to enforce connection quality for a given virtualized port. This hint allows the port to optimize channel usage in different scenarios.
ms.assetid: 753e25c5-44b5-4afa-8769-49f693472aa9
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_CONNECTION_QUALITY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_CONNECTION\_QUALITY


OID\_WDI\_SET\_CONNECTION\_QUALITY provides a hint to the IHV component to enforce connection quality for a given virtualized port. This hint allows the port to optimize channel usage in different scenarios.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

**Note**  This property specifies data path quality of service hints, which may cause conflicts with other properties or tasks that are issued to the adapter.

 

## Set property parameters


| TLV                                                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_CONNECTION\_QUALITY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926259)                           |                                |          | The desired Wi-Fi connection quality hint.                                                                                                                                                     |
| [**WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn897843) |                                | X        | The behavior for low latency connection quality. This is only required if the connection quality is set to [**WDI\_CONNECTION\_QUALITY\_LOW\_LATENCY**](https://msdn.microsoft.com/library/windows/hardware/dn897807). |

 

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

 

 




