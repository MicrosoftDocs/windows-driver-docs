---
title: MSI-X Pre-Registration
description: MSI-X Pre-Registration
ms.assetid: 93a09ebd-8a50-4c96-a926-54bb4686a618
keywords:
- MSI-X WDK networking , resource-requirements filter function
- message-signaled interrupts WDK networking , resource-requirements filter function
- MSIs WDK networking , resource-requirements filter function
- resource-requirements filter function WDK net
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MSI-X Pre-Registration





To support changing interrupt affinities for MSI-X or to remove message interrupt resources, a miniport driver must establish a resource-requirements filter function. This pre-registration step occurs before NDIS calls the [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

To establish a resource-requirements filter function, the miniport driver must provide a [*MiniportSetOptions*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. When the miniport driver calls the [**NdisMRegisterMiniportDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function from the [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, the driver passes the entry point for *MiniportSetOptions* in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure. NDIS calls the *MiniportSetOptions* function in the context of **NdisMRegisterMiniportDriver**.

From *MiniportSetOptions*, the miniport driver calls the [**NdisSetOptionalHandlers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function and specifies an [**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_pnp_characteristics) structure. This structure defines the entry points for the [*MiniportAddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device), [*MiniportRemoveDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device), [*MiniportStartDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), and [*MiniportFilterResourceRequirements*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp) functions.

When NDIS receives an add-device request from the Plug and Play (PnP) manager, NDIS calls the miniport driver's *MiniportAddDevice* function. The handle that NDIS passes to *MiniportAddDevice* in the *MiniportAdapterHandle* parameter is the handle that NDIS later passes to the [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

In [*MiniportAddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device), the driver initializes an [**NDIS\_MINIPORT\_ADD\_DEVICE\_REGISTRATION\_ATTRIBUTES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_add_device_registration_attributes) structure and passes this structure to the [**NdisMSetMiniportAttributes**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function. The NDIS\_MINIPORT\_ADD\_DEVICE\_REGISTRATION\_ATTRIBUTES structure contains the **MiniportAddDeviceContext** member that is a handle to a miniport driver-allocated context area for the device. NDIS later provides this context handle to the [*MiniportRemoveDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device), [*MiniportFilterResourceRequirements*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), [*MiniportStartDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pnp_irp), and [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) functions. For *MiniportInitializeEx*, the context handle is passed in the **MiniportAddDeviceContext** member of the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure that the *MiniportInitParameters* parameter points to.

After NDIS calls [*MiniportAddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) and *MiniportAddDevice* returns NDIS\_STATUS\_SUCCESS, NDIS calls the *MiniportFilterResourceRequirements* function every time that it receives the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mn-filter-resource-requirements) I/O request packet (IRP). *MiniportFilterResourceRequirements* can change the interrupt affinity for each MSI-X message, add message interrupt resources, or remove message interrupt resources if the driver will register for line-based interrupts in the [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. For more information about establishing an interrupt affinity policy, see [MSI-X Resource Filtering](msi-x-resource-filtering.md).

When NDIS receives a remove-device request from the PnP manager, NDIS calls the miniport driver's [*MiniportRemoveDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_remove_device) function. The *MiniportRemoveDevice* function should undo the operations that the [*MiniportAddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_add_device) function performed.

 

 





