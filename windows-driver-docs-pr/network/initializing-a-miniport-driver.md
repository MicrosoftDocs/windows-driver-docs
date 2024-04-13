---
title: Initializing a Miniport Driver
description: Initializing a Miniport Driver
keywords:
- miniport drivers WDK networking , initializing
- initializing miniport drivers
- NDIS miniport drivers WDK , initializing
ms.date: 04/20/2017
---

# Initializing a Miniport Driver



When a networking device becomes available, the system loads the NDIS miniport driver to manage the device (if the driver is not already loaded). Every miniport driver must provide a [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. The system calls **DriverEntry** after it loads the driver. **DriverEntry** registers the miniport driver's characteristics with NDIS (including the supported NDIS version and the driver entry points).

The system passes two arguments to [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize):

-   A pointer to the driver object, which was created by the I/O system.

-   A pointer to the registry path, which specifies where driver-specific parameters are stored.

In [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), miniport drivers pass both of these pointers in a call to the [NdisMRegisterMiniportDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function. Miniport drivers export a set of standard *MiniportXxx* functions by storing their entry points in an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure and passing that structure to **NdisMRegisterMiniportDriver**. 

**DriverEntry** for miniport drivers returns the value that is returned by the call to **NdisMRegisterMiniportDriver**.

A miniport driver also performs any other driver-specific initialization that it requires in [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize). The driver performs adapter-specific initialization in the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. For more information about adapter initialization, see [Initializing an Adapter](initializing-a-miniport-adapter.md).

[DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) can allocate the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure on the stack because the NDIS library copies the relevant information to its own storage. **DriverEntry** should clear the memory for this structure with [NdisZeroMemory](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiszeromemory) before setting any driver-supplied values in its members. The **MajorNdisVersion** and **MinorNdisVersion** members must contain the major and minor versions of NDIS that the driver supports. In each Xxx**Handler** member of the characteristics structure, **DriverEntry** must set the entry point of a driver-supplied *MiniportXxx* function, or the member must be **NULL**.

To enable a miniport driver to configure optional services, NDIS calls the [MiniportSetOptions](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function within the context of the miniport driver's call to [NdisMRegisterMiniportDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver). For more information about optional services, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

Drivers that call [NdisMRegisterMiniportDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) must be prepared for NDIS to call their [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) functions any time after **DriverEntry** returns. Such a driver must have sufficient installation and configuration information stored in the registry or available from calls to an **NdisXxx** bus-type-specific configuration function to set up any NIC-specific resources the driver will need to carry out network I/O operations.

The miniport driver must eventually call [**NdisMDeregisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterminiportdriver) to release resources that it allocated by calling [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver). If the driver initialization fails after the call to **NdisMRegisterMiniportDriver** succeeded, the driver can call **NdisMDeregisterMiniportDriver** from within [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize). Otherwise, the miniport driver must release the driver-specific resources that it allocates in its [*MiniportDriverUnload*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload) function. In other words, if NdisMRegisterMiniportDriver does not return NDIS_STATUS_SUCCESS, **DriverEntry** must release any resources that it allocated before it returns control. The driver will not be loaded if this occurs. For more information, see [Unloading a Miniport Driver](unloading-a-miniport-driver.md).

 

