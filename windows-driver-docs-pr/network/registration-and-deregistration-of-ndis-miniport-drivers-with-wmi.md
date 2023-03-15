---
title: Registration and Deregistration of NDIS Miniport Drivers with WMI
description: Registration and Deregistration of NDIS Miniport Drivers with WMI
keywords:
- miniport adapters WDK networking , registering
- adapters WDK networking , registering
- WMI WDK networking , registering miniport adapters
- registering miniport drivers
- registering miniport adapters
- miniport adapters WDK networking , WMI
- adapters WD
ms.date: 03/02/2023
---

# Registration and Deregistration of NDIS Miniport Drivers with WMI





NDIS automatically registers each miniport adapter with WMI. A miniport driver does not have to explicitly register with WMI, because NDIS automatically registers for the associated miniport adapter after the miniport driver returns from the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

After NDIS registers a miniport adapter as a data provider with WMI, WMI clients can send it query and set requests and register to receive status indications.

Before NDIS calls the miniport driver's [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function, NDIS automatically deregisters the miniport adapter with WMI so that WMI will no longer send WMI requests to the miniport driver.

For each miniport adapter that NDIS registers with WMI, NDIS registers GUIDs that correspond to particular OIDs or status indications. NDIS registers GUIDs for a miniport adapter's supported set of standard OIDs and status indications. For more information about these standard GUIDs, see [Standard Miniport Driver OIDs Registered with WMI](standard-miniport-driver-oids-registered-with-wmi.md) and [Standard Miniport Driver Status Registered with WMI](standard-miniport-driver-status-indications-registered-with-wmi.md).

NDIS can also register custom GUIDs for custom OIDs and status indications. If the miniport driver supports custom OIDs, it must provide the associated custom GUIDs. For more information about customized OIDs and status indications, see [Customized OIDs and Status Indications](customized-oids-and-status-indications.md).

For connection-oriented miniport drivers, NDIS also registers any named virtual connections (VCs). WMI clients can work only with VCs that a stand-alone call manager, or connection-oriented client, has named with the [**NdisCoAssignInstanceName**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscoassigninstancename) function. For more information about NDIS WMI support for named VCs, see [Support for Named VCs](support-for-named-vcs.md).

 

