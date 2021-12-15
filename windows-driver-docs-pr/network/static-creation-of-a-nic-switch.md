---
title: Static Creation of a NIC Switch
description: Static Creation of a NIC Switch
ms.date: 04/20/2017
---

# Static Creation of a NIC Switch


A network adapter that supports single root I/O virtualization (SR-IOV) must be able to create a NIC switch. For some adapters, the NIC switch can be created statically within the context of the call to [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize).

Only the miniport driver for the PCI Express (PCIe) Physical Function (PF) of the SR-IOV adapter can create a NIC switch on the adapter.

**Note**  Starting with Windows Server 2012, the SR-IOV interface supports only one NIC switch on the network adapter. This switch is known as the *default NIC switch*, and is referenced by the NDIS\_DEFAULT\_SWITCH\_ID identifier.

 

The parameters for the default NIC switch are defined through standardized keyword settings in the registry. For more information on these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

The PF miniport driver statically creates the NIC switch when NDIS calls the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. Typically, the driver creates and configures the NIC switch as part of its initialization sequence before it enables SR-IOV on the network adapter.

The PF miniport driver follows these steps when it statically creates the NIC switch and enables SR-IOV on the network adapter in the context of the call to [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize):

1.  The PF miniport driver must read the SR-IOV standardized keywords to determine whether SR-IOV is enabled and obtain the NIC switch configuration parameters.

    **Note**  If the PF miniport driver registered an entry point to a [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function, the driver may have previously obtained these parameters from the registry when NDIS called *MiniportSetOptions*.

     

2.  If SR-IOV is enabled, the PF miniport driver configures the network adapter with the NIC switch parameters from the registry. The driver must verify that the parameters are valid before it configures the network adapter. For example, the miniport driver must verify that the maximum number of PCIe Virtual Functions (VFs) assigned to the NIC switch does not exceed the number of VFs supported by the network adapter.

3.  The miniport driver calls [**NdisMEnableVirtualization**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismenablevirtualization) to enable SR-IOV and set the number of VFs on the network adapter. This function configures the SR-IOV Extended Capability in adapter's PCI configuration space. If this function returns NDIS\_STATUS\_SUCCESS, SR-IOV is enabled and the VFs are exposed over the PCIe interface.

**Note**  If the PF miniport driver statically creates the NIC switch, the switch cannot be used until NDIS issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md). If the PF miniport driver statically created the NIC switch, it must verify that the switch parameters are specified in the OID request. These parameters, as contained within the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure associated with the OID request, must be identical to the parameters the driver used to create the switch.

 

For more information on how to handle the [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) request, see [Handling the OID\_NIC\_SWITCH\_CREATE\_SWITCH Request](handling-the-oid-nic-switch-create-switch-request.md).

For more information on the initialization sequence and requirements for PF miniport drivers, see [Initializing a PF Miniport Driver](initializing-a-pf-miniport-driver.md).

 

