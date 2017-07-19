---
title: WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY
author: windows-driver-content
description: WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY is a TLV that contains an ASP2 Service Information Discovery Entry.
ms.assetid: 67F1CDE2-8003-44D3-B338-FE7C5EA48C29
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY


WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY is a TLV that contains an ASP2 Service Information Discovery Entry.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x12D

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                         |
|-------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)                          |                                |          | Name of the service (UTF-8), up to 21 bytes.                                                                        |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME**](wdi-tlv-p2p-instance-name.md)                        |                                |          | Instance name of the service (UTF-8), up to 63 bytes.                                                               |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md)            |                                | X        | Request service information to be used for the ANQP query request to download service information for this Service. |
| [**WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR**](wdi-tlv-p2p-service-update-indicator.md) |                                | X        | Service Update indicator to be used for the ANQP query request.                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_TRANSACTION\_ID**](wdi-tlv-p2p-service-transaction-id.md)     |                                | X        | Service transaction ID to be used for the ANQP query request.                                                       |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


