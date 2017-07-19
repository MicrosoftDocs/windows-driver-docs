---
title: WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv4ARP
author: windows-driver-content
description: WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv4ARP is a TLV that contains IPv4 ARP protocol offload parameters.
ms.assetid: 03894B22-3D4B-4262-893A-660FC88AA93D
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv4ARP Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv4ARP


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv4ARP is a TLV that contains IPv4 ARP protocol offload parameters.

## TLV Type


0x61

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32                                            | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter.                                                                   |
| UINT8\[4\]                                        | Specifies an optional IPv4 address to match with the Source Protocol Address (SPA) field of the ARP request. If the incoming ARP request has an SPA value that matches this IPv4 address, the network adapter sends an ARP response when it is in a low power state. If this is set to zero, the network adapter should respond to ARP requests from any remote IPv4 address. |
| UINT8\[4\]                                        | Specifies the host IPv4 address the network adapter uses for the Source Protocol Address (SPA) field when sending an ARP response.                                                                                                                                                                                                                                            |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | Specifies the MAC address that the network adapter must use for the Source Hardware Address (SHA) field of the ARP response packet that it generates. However, it should use the current MAC address of the network adapter as the source address in the MAC header.                                                                                                          |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_PM_PROTOCOL_OFFLOAD_IPv4ARP%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


