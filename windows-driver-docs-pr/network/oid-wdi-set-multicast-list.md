---
title: OID_WDI_SET_MULTICAST_LIST
description: OID_WDI_SET_MULTICAST_LIST specifies the multicast address list for a given port. This command can be set at any time.
ms.assetid: dee41a49-2be2-4364-877c-b2b3bf29e78d
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_MULTICAST_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_MULTICAST\_LIST


OID\_WDI\_SET\_MULTICAST\_LIST specifies the multicast address list for a given port. This command can be set at any time.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

The IHV component should only fail the command if the list size exceeds the limit specified in [**WDI\_TLV\_INTERFACE\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn897835).

After the host enables multicast packet filtering on the port using [OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER](oid-wdi-set-receive-packet-filter.md), the device must indicate received multicast frames with a destination address matching an address in the port’s multicast list to the host. The device must clear the multicast list as part of processing of [OID\_WDI\_TASK\_DOT11\_RESET](oid-wdi-task-dot11-reset.md). When the command is sent with no multicast list specified, the driver must clear its multicast list. In this case, no packets should be indicated up unless OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER has the WDI\_PACKET\_FILTER\_ALL\_MULTICAST bit set.

## Set property parameters


| TLV                                                              | Multiple TLV instances allowed | Optional | Description                                                  |
|------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------|
| [**WDI\_TLV\_MULTICAST\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn897849) |                                | X        | List of multicast MAC addresses. The list must not be empty. |

 

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

 

 




