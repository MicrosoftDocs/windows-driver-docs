---
title: NDIS_STATUS_SWITCH_NIC_STATUS
description: The NDIS_STATUS_SWITCH_NIC_STATUS status indication is used to encapsulate a status indication from a physical network adapter that is bound to the external network adapter of the Hyper-V extensible switch.
ms.assetid: 51A3BE6A-35F1-4AF0-91C0-94681640BD64
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_SWITCH_NIC_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_SWITCH\_NIC\_STATUS


The **NDIS\_STATUS\_SWITCH\_NIC\_STATUS** status indication is used to encapsulate a status indication from a physical network adapter that is bound to the external network adapter of the Hyper-V extensible switch. Through this encapsulation, the status indication is forwarded up the extensible switch driver stack.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure for this indication contains a pointer to an [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/hh598217) structure.

Remarks
-------

When an underlying physical network adapter issues an NDIS status indication, it is received by the external network adapter. When this happens, the extensible switch interface performs these steps:

1.  The interface encapsulates the status indication inside an [**NDIS\_SWITCH\_NIC\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/hh598217) structure.

2.  The interface issues an **NDIS\_STATUS\_SWITCH\_NIC\_STATUS** status indication to forward the encapsulated status indication up the extensible switch driver stack. This allows extensible switch extensions to modify the encapsulated status indication.

    Typically, the extension modifies an encapsulated status indication to change the current offload capabilities of the underlying team of physical adapters that are bound to the external network adapter.

    For more information about the different configurations in which physical network adapters can be bound to the external network adapter, see [Types of Physical Network Adapter Configurations](https://msdn.microsoft.com/library/windows/hardware/hh582274).

3.  When the **NDIS\_STATUS\_SWITCH\_NIC\_STATUS** status indication is received by the overlying extensible switch protocol driver in the stack, the interface forwards the decapsulated status indication to overlying protocol or filter drivers.

An extension can also originate encapsulated hardware offload status indications to overlying drivers in the extensible switch driver stack. This also allows the driver to change the current offload capabilities of the underlying team of physical adapters that are attached to the external network adapter. When a team of adapters are bound to the external network adapter, only the common capabilities of the team are advertised to NDIS or the overlying protocol and filter drivers. The extension can extend the advertised capabilities by originating encapsulated status indications to advertise capabilities that are supported by some adapters in the team.

For example, the extension can issue an encapsulated [**NDIS\_STATUS\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES**](ndis-status-receive-filter-current-capabilities.md) indication to change the currently-enabled receive filter capabilities for the entire team.

For more information on how to forward or originate **NDIS\_STATUS\_SWITCH\_NIC\_STATUS** indications, see [Managing NDIS Status Indications from Physical Network Adapters](https://msdn.microsoft.com/library/windows/hardware/hh598199).

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_STATUS\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES**](ndis-status-receive-filter-current-capabilities.md)

 

 




