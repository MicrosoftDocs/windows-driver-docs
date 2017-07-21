---
title: OID_WDI_SET_TCP_OFFLOAD_PARAMETERS
author: windows-driver-content
description: OID_WDI_SET_TCP_OFFLOAD_PARAMETERS is sent down to the device from the OS to set the TCP offload parameters.
ms.assetid: B615066B-3871-4445-8397-B41CB66EEF35
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_SET_TCP_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS


OID\_WDI\_SET\_TCP\_OFFLOAD\_PARAMETERS is sent down to the device from the OS to set the TCP offload parameters.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

This command is sent in some cases such as when there is a need to turn off the offloads due to a performance issue.

The lower edge driver (LE) must use the contents of [**WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898071) to update the currently reported TCP offload capabilities. After the update, the LE must report the current task offload capabilities with [NDIS\_STATUS\_WDI\_INDICATION\_TASK\_OFFLOAD\_CURRENT\_CONFIG](ndis-status-wdi-indication-task-offload-current-config.md). This status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description                           |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------|
| [**WDI\_TLV\_TCP\_SET\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898071) |                                |          | The TCP offload parameters to be set. |

 

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_TCP_OFFLOAD_PARAMETERS%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


