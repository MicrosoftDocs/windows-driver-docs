---
title: OID_SWITCH_NIC_UPDATED
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_UPDATED to the extensible switch driver stack.
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_UPDATED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_UPDATED


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_UPDATED to the extensible switch driver stack. This OID request notifies underlying extensible switch extensions about the update of the parameters of a network adapter. The OID will only be issued for NICs that have already been connected, and have not yet begun the disconnect process. These run-time configuration changes can include **NicFriendlyName**, **NetCfgInstanceId**, **MTU**, **NumaNodeId**, **PermanentMacAddress**, **VMMacAddress**, **CurrentMacAddress**, and **VFAssigned**.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure.

## Remarks

The **PortId** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure specifies the port for which the update notification is being made. The extensible switch extension can obtain the parameter information for this and other ports on the extensible switch by issuing OID query requests of [OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md).

The **Index** member of the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure specifies the index of a network adapter for which the update notification is being made. The network adapter with the specified **Index** value is connected to the extensible switch port specified by the **PortId** member. For more information on these index values, see [Network Adapter Index Values](./network-adapter-index-values.md).

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_NIC\_UPDATED:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters) structure that is associated with the OID request.
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

 

## Requirements

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
[*DereferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_nic)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_SWITCH\_NIC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_nic_parameters)

[OID\_SWITCH\_NIC\_DISCONNECT](oid-switch-nic-disconnect.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchNic*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_nic)

 

