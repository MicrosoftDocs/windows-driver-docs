---
title: Creating a NIC Switch
description: Creating a NIC Switch
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a NIC Switch


This section describes the requirements and guidelines for creating the NIC switch of a network adapter that supports single root I/O virtualization (SR-IOV). The miniport driver for the PCI Express (PCIe) Physical Function (PF) of the SR-IOV network adapter creates and configures the NIC switch on the adapter.

A NIC switch can be created through one of the following methods:

<a href="" id="static-creation"></a>Static Creation  
The NIC switch is statically created on the SR-IOV network adapter by using a set of switch parameters defined by registry settings. After the NIC switch is created, its parameters cannot be changed while the driver is running.

The PF miniport driver statically creates the NIC switch within the context of the call to the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. However, the NIC switch cannot be used until NDIS issues an object identifier (OID) method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md). Even though the NIC switch was previously created, the PF miniport driver enabled the NIC switch for use when it handled this OID request.

For more information about this method, see [Static Creation of a NIC Switch](static-creation-of-a-nic-switch.md).

<a href="" id="dynamic-creation"></a>Dynamic Creation  
The NIC switch is dynamically created on the SR-IOV network adapter through the OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md). This OID request defines the NIC switch parameters through the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure. These parameters are also based on the staticallydefined registry settings but could change dynamically while the miniport driver is running.

For more information about this method, see [Dynamic Creation of a NIC Switch](dynamic-creation-of-a-nic-switch.md).

For more information on how to handle the [OID\_NIC\_SWITCH\_CREATE\_SWITCH](./oid-nic-switch-create-switch.md) request, see [Handling the OID\_NIC\_SWITCH\_CREATE\_SWITCH Request](handling-the-oid-nic-switch-create-switch-request.md).

For more information on NIC switches for SR-IOV network adapters, see [NIC Switches](nic-switches.md).

**Note**  The miniport driver for a PCIe Virtual Function (VF) on the SR-IOV network adapter does not create or configure the network adapter's hardware resources, such as the NIC switch. For more information, see [Writing SR-IOV VF Miniport Drivers](writing-sr-iov-vf-miniport-drivers.md).

 

 

