---
title: OID\_SWITCH\_PORT\_UPDATED
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_UPDATED to notify extensible switch extensions about the update of an extensible switch port.
ms.assetid: 7FDC963A-92E4-49B2-AB77-FA9C92EEBC25
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_SWITCH_PORT_UPDATED Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_PORT\_UPDATED


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_PORT\_UPDATED to notify extensible switch extensions about the update of an extensible switch port. The OID will only be issued for ports that have already been created, and have not yet begun the teardown/delete process. Currently, only the **PortFriendlyName** field is subject to update after creation.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](ndis-oid-request.md) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](ndis-switch-nic-save-state.md) structure.

Remarks
-------

The **PortId** member of the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure specifies the extensible switch port for which the update notification is being made.

The extension must follow these guidelines for handling OID set requests of OID\_SWITCH\_PORT\_UPDATED:

-   The extension must not modify the [**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md) structure that is associated with the OID request.

-   The extension must always forward this OID set request to underlying extensions. The extension must not fail the request.

**Note**  Extensible switch extensions must not issue OID set requests of OID\_SWITCH\_PORT\_UPDATED.

 

For more information about the states of extensible switch ports and network adapter connections, see [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID set request of OID\_SWITCH\_PORT\_UPDATED and returns the following status code.

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
[*DereferenceSwitchNic*](dereferenceswitchnic.md)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NDIS\_SWITCH\_PORT\_PARAMETERS**](ndis-switch-port-parameters.md)

[**NdisFOidRequest**](ndisfoidrequest.md)

[OID\_SWITCH\_NIC\_DELETE](oid-switch-nic-delete.md)

[OID\_SWITCH\_PORT\_ARRAY](oid-switch-port-array.md)

[*ReferenceSwitchNic*](referenceswitchnic.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_PORT_UPDATED%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


