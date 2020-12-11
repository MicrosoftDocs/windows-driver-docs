---
title: Handling OID_NIC_SWITCH_FREE_VF Requests
description: Handling OID_NIC_SWITCH_FREE_VF Requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling OID\_NIC\_SWITCH\_FREE\_VF Requests


When the miniport driver for the PCI Express (PCIe) Physical Function (PF) on the network adapter handles the object identifier (OID) set request of [OID\_NIC\_SWITCH\_FREE\_VF](./oid-nic-switch-free-vf.md), it does the following:

-   The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure for the OID request contains a pointer to an [**NDIS\_NIC\_SWITCH\_FREE\_VF\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_free_vf_parameters) structure. The PF miniport driver must verify that the identifier of the PCIe Virtual Function (VF), which is specified by the **VFId** member, is valid. If this is not true, the driver must fail the OID set request by returning NDIS\_STATUS\_INVALID\_PARAMETER.

-   The PF miniport driver must verify that resources for the VF have been previously allocated through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](./oid-nic-switch-allocate-vf.md). If this is not true, the driver must fail the OID set request by returning NDIS\_STATUS\_INVALID\_PARAMETER.

-   The PF miniport driver must verify that no virtual ports (VPorts) are currently attached to the VF. If this is not true, the driver must fail the set request by returning NDIS\_STATUS\_INVALID\_PARAMETER.

-   The PF miniport driver must free all software resources that were allocated for the specified VF.

-   The PF miniport driver must detach the VF from the NIC switch on the network adapter.

If the PF miniport driver can successfully free the allocated software resources and detach the VF from the NIC switch, the driver completes the OID request with NDIS\_STATUS\_SUCCESS.

**Note**  NDIS guarantees that all the VFs allocated on the miniport are freed before NDIS issues an OID set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](./oid-nic-switch-delete-switch.md) to the PF miniport driver. When it handles this OID, the driver deletes a NIC switch on the network adapter.

 

 

