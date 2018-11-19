---
title: OID_SWITCH_NIC_UPDATED
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_UPDATED to the extensible switch driver stack.
ms.assetid: C1B446A3-861F-41B4-99EF-C7CB45F86F39
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_UPDATED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_UPDATED


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_UPDATED to the extensible switch driver stack. This OID request notifies underlying extensible switch extensions about the update of the parameters of a network adapter. The OID will only be issued for NICs that have already been connected, and have not yet begun the disconnect process. These run-time configuration changes can include **NicFriendlyName**, **NetCfgInstanceId**, **MTU**, **NumaNodeId**, **PermanentMacAddress**, **VMMacAddress**, **CurrentMacAddress**, and **VFAssigned**.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies the port for which the update notification is being made. The extensible switch extension can obtain the parameter information for this and other ports on the extensible switch by issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md).

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure specifies the index of a network adapter for which the update notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](https://msdn.microsoft.com/library/windows/hardware/hh598258).

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_NIC\_UPDATED:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215) structure that is associated with the OID request.
-   The extension must always forward this OID set request to underlying extensions. The extension must not complete the request.
-   The extension must not issue its own OID set requests of OID\_SWITCH\_NIC\_UPDATED.

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_NIC\_UPDATED and returns the following status code.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[*DereferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598141)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598215)

[OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchNic*](https://msdn.microsoft.com/library/windows/hardware/hh598294)

 

 




