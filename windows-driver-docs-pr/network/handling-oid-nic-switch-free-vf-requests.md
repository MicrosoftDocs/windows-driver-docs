---
title: Handling OID_NIC_SWITCH_FREE_VF Requests
description: Handling OID_NIC_SWITCH_FREE_VF Requests
ms.assetid: 56134421-6D3C-4A40-B7EE-FDB729D46DEB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling OID\_NIC\_SWITCH\_FREE\_VF Requests


When the miniport driver for the PCI Express (PCIe) Physical Function (PF) on the network adapter handles the object identifier (OID) set request of [OID\_NIC\_SWITCH\_FREE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451822), it does the following:

-   The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the OID request contains a pointer to an [**NDIS\_NIC\_SWITCH\_FREE\_VF\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451579) structure. The PF miniport driver must verify that the identifier of the PCIe Virtual Function (VF), which is specified by the **VFId** member, is valid. If this is not true, the driver must fail the OID set request by returning NDIS\_STATUS\_INVALID\_PARAMETER.

-   The PF miniport driver must verify that resources for the VF have been previously allocated through an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814). If this is not true, the driver must fail the OID set request by returning NDIS\_STATUS\_INVALID\_PARAMETER.

-   The PF miniport driver must verify that no virtual ports (VPorts) are currently attached to the VF. If this is not true, the driver must fail the set request by returning NDIS\_STATUS\_INVALID\_PARAMETER.

-   The PF miniport driver must free all software resources that were allocated for the specified VF.

-   The PF miniport driver must detach the VF from the NIC switch on the network adapter.

If the PF miniport driver can successfully free the allocated software resources and detach the VF from the NIC switch, the driver completes the OID request with NDIS\_STATUS\_SUCCESS.

**Note**  NDIS guarantees that all the VFs allocated on the miniport are freed before NDIS issues an OID set request of [OID\_NIC\_SWITCH\_DELETE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451817) to the PF miniport driver. When it handles this OID, the driver deletes a NIC switch on the network adapter.

 

 

 





