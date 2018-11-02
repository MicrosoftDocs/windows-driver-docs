---
title: Dynamic Creation of a NIC Switch
description: Dynamic Creation of a NIC Switch
ms.assetid: 16B2D94A-AF30-434F-8F14-2F535501A52F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamic Creation of a NIC Switch


A network adapter that supports single root I/O virtualization (SR-IOV) must be able to create a NIC switch. For some adapters, the NIC switch can be created dynamically after the miniport driver has returned from the call to [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389).

Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of the SR-IOV adapter can create a NIC switch on the adapter.

**Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

NDIS issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815) to create a NIC switch on the SR-IOV network adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451587) structure that contains the parameters for the switch.

If the PF miniport driver supports dynamic NIC switch creation, it must follow these steps when it handles this OID request:

1.  The PF miniport driver allocates the necessary hardware and software resources for the NIC switch based on these parameters. The driver also configures the network adapter with these parameters.

    **Note**  PF miniport drivers that support dynamic NIC switch creation do not have to read the switch parameters through the standardized SR-IOV keyword settings in the registry. NDIS reads these keywords to initialize the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451587) structure before it issues the [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815) request. For more information on these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

     

2.  The miniport driver calls [**NdisMEnableVirtualization**](https://msdn.microsoft.com/library/windows/hardware/hh451481) to enable SR-IOV and set the number of VFs on the network adapter. This function configures the SR-IOV Extended Capability in adapter's PCI configuration space. If this function returns NDIS\_STATUS\_SUCCESS, SR-IOV is enabled and the VFs are exposed over the PCIe interface.

For more information on how to handle the [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815) request, see [Handling the OID\_NIC\_SWITCH\_CREATE\_SWITCH Request](handling-the-oid-nic-switch-create-switch-request.md).

 

 





