---
title: MSI-X Pre-Registration
description: MSI-X Pre-Registration
keywords:
- MSI-X WDK networking , resource-requirements filter function
- message-signaled interrupts WDK networking , resource-requirements filter function
- MSIs WDK networking , resource-requirements filter function
- resource-requirements filter function WDK net
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MSI-X Pre-Registration





To support changing interrupt affinities for MSI-X or to remove message interrupt resources, a miniport driver must establish a resource-requirements filter function. This pre-registration step occurs before NDIS calls the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

To establish a resource-requirements filter function, the miniport driver must provide a [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. When the miniport driver calls the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function from the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, the driver passes the entry point for *MiniportSetOptions* in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure. NDIS calls the *MiniportSetOptions* function in the context of **NdisMRegisterMiniportDriver**.

From *MiniportSetOptions*, the miniport driver calls the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function and specifies an [**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_pnp_characteristics) structure. This structure defines the entry points for the [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device), [*MiniportRemoveDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device), [*MiniportStartDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), and [*MiniportFilterResourceRequirements*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp) functions.

When NDIS receives an add-device request from the Plug and Play (PnP) manager, NDIS calls the miniport driver's *MiniportAddDevice* function. The handle that NDIS passes to *MiniportAddDevice* in the *MiniportAdapterHandle* parameter is the handle that NDIS later passes to the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

In [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device), the driver initializes an [**NDIS\_MINIPORT\_ADD\_DEVICE\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_add_device_registration_attributes) structure and passes this structure to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function. The NDIS\_MINIPORT\_ADD\_DEVICE\_REGISTRATION\_ATTRIBUTES structure contains the **MiniportAddDeviceContext** member that is a handle to a miniport driver-allocated context area for the device. NDIS later provides this context handle to the [*MiniportRemoveDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device), [*MiniportFilterResourceRequirements*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), [*MiniportStartDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), and [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) functions. For *MiniportInitializeEx*, the context handle is passed in the **MiniportAddDeviceContext** member of the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure that the *MiniportInitParameters* parameter points to.

After NDIS calls [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) and *MiniportAddDevice* returns NDIS\_STATUS\_SUCCESS, NDIS calls the *MiniportFilterResourceRequirements* function every time that it receives the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](../kernel/irp-mn-filter-resource-requirements.md) I/O request packet (IRP). *MiniportFilterResourceRequirements* can change the interrupt affinity for each MSI-X message, add message interrupt resources, or remove message interrupt resources if the driver will register for line-based interrupts in the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. For more information about establishing an interrupt affinity policy, see [MSI-X Resource Filtering](msi-x-resource-filtering.md).

When NDIS receives a remove-device request from the PnP manager, NDIS calls the miniport driver's [*MiniportRemoveDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device) function. The *MiniportRemoveDevice* function should undo the operations that the [*MiniportAddDevice*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) function performed.

 

