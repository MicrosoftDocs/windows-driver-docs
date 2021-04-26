---
title: DriverEntry Guidelines for PF Miniport Drivers
description: DriverEntry Guidelines for PF Miniport Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DriverEntry Guidelines for PF Miniport Drivers


This topic describes the guidelines for writing a [**DriverEntry**](./initializing-a-miniport-driver.md) function for the miniport driver of the PCI Express (PCIe) Physical Function (PF). The PF is a component of a network adapter that supports single root I/O virtualization (SR-IOV).

**Note**  These guidelines only apply to PF miniport drivers. For initialization guidelines for the miniport driver of a PCIe Virtual Function (VF) of the adapter, see [Initializing a VF Miniport Driver](initializing-a-vf-miniport-driver.md).

 

The SR-IOV network adapter must implement a hardware bridge that forwards network traffic over the physical port on the adapter and internal virtual ports (VPorts). This bridge is known as the *NIC switch*. For more information, see [NIC Switches](nic-switches.md).

If the PF miniport driver supports the static creation of the NIC switch on the SR-IOV network adapter, it may need to allocate switch resources when the functional device object (FDO) is created for the network adapter in the device stack. In this case, the driver must allocate those resources before NDIS calls [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize). To do this, the driver must register optional Plug-and-Play (PnP) handlers so that it can participate in the process when the adapter's FDO is added or removed from the device stack.

The miniport driver must provide a [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function to register these PnP handler functions. To do this, the driver follows these steps from the context of the call to its [**DriverEntry**](./initializing-a-miniport-driver.md) function:

1.  The miniport driver initializes an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure with the entry points of the *MiniportXxx* functions. In particular, the driver sets the **SetOptionsHandler** member to the entry point of the driver's [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function.

2.  The miniport driver calls the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function to register its entry points. From the context of this call, NDIS calls the driver's [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function

3.  When NDIS calls [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options), the miniport driver calls the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function and specifies an [**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_pnp_characteristics) structure. This structure defines the entry points for the [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device), [*MiniportRemoveDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device), [*MiniportStartDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), and [*MiniportFilterResourceRequirements*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp) functions. NDIS calls these handler functions when it handles PnP I/O request packets (IRPs) issued by the PCI bus driver.

    If the PF miniport driver must allocate additional software resources for the NIC switch before NDIS calls the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the driver must register a [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) function. When NDIS calls the *MiniportAddDevice* function, the PF miniport driver can call [**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration) to read the NIC switch configuration keyword settings from the registry. For more information about these keywords, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md).

    For more information about guidelines for the [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) function, see [*MiniportAddDevice* Guidelines for PF Miniport Drivers](miniportadddevice-guidelines-for-pf-miniport-drivers.md).

For more information on how NIC switches are created, see [Creating a NIC Switch](creating-a-nic-switch.md).

 

