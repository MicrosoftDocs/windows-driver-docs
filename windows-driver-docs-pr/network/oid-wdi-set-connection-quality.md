---
title: OID_WDI_SET_CONNECTION_QUALITY
author: windows-driver-content
description: OID_WDI_SET_CONNECTION_QUALITY provides a hint to the IHV component to enforce connection quality for a given virtualized port. This hint allows the port to optimize channel usage in different scenarios.
ms.assetid: 753e25c5-44b5-4afa-8769-49f693472aa9
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_SET_CONNECTION_QUALITY Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_CONNECTION_QUALITY%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


