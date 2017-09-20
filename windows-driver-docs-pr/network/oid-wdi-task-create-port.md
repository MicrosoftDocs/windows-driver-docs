---
title: OID_WDI_TASK_CREATE_PORT
author: windows-driver-content
description: OID_WDI_TASK_CREATE_PORT requests that a new 802.11 entity is created by the IHV component.
ms.assetid: e1a03a97-608f-42af-bd39-37a7eb9ad5b7
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_TASK_CREATE_PORT Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TASK\_CREATE\_PORT


OID\_WDI\_TASK\_CREATE\_PORT requests that a new 802.11 entity is created by the IHV component.

| Object  | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|---------|---------------|---------------------------------------|---------------------------------|
| Adapter | No            | 6                                     | 1                               |

 

The operation mode of the created port is set to **WDI\_OPERATION\_MODE\_STA** unless it has been specified in the task parameters.

If the MAC is to function as a Wi-Fi Direct device port, **uOpmodeMask** contains **WDI\_OPERATION\_MODE\_P2P\_DEVICE**. In this case, the IHV component driver must assign the MAC address reserved for the Wi-Fi Direct Device to this port and return it in the request completion indication.

## Task parameters


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>WDI_TLV_CREATE_PORT_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926273)</td>
<td></td>
<td></td>
<td>Parameters for port creation.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_CREATE_PORT_MAC_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926270)</td>
<td></td>
<td>X</td>
<td><p>This TLV is used when the UE recreates the non-primary port during resume from hibernation. When this TLV is present, the firmware must use this MAC address to create the port. This MAC address is guaranteed to be the MAC address that the firmware created for the port type prior to hibernation.</p>
<p>The goal is to use the same NDIS port number and MAC address in order to match the states of the upper layers. Note that the WFC_PORT_ID can be different at recreation, but the port ID should not collide with any port ID of an existing port. This information is only used between the UE and LE/firmware.</p></td>
</tr>
</tbody>
</table>

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_CREATE\_PORT\_COMPLETE](ndis-status-wdi-indication-create-port-complete.md)
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_TASK_CREATE_PORT%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


