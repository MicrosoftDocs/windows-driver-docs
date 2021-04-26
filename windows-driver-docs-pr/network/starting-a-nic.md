---
title: Starting a NIC
description: Starting a NIC
keywords:
- NICs WDK networking , starting
- network interface cards WDK networking , starting
- Plug and Play WDK NDIS miniport , starting NIC
- starting NICs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a NIC





The following steps describe how NDIS participates in the starting of a NIC:

1.  The PnP manager issues an [**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md) request. This IRP contains information that informs NDIS about the resources that the PnP manager has allocated for the NIC.

2.  NDIS sets an [**IoCompletion**](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine and passes the IRP\_MN\_START\_DEVICE request down the device stack to the next lowest driver, which is typically the bus driver. When the bus driver receives the IRP\_MN\_START\_DEVICE request, the bus driver performs its start operations on the device and passes the completed IRP\_MN\_START\_DEVICE request back up the device stack.

3.  When NDIS receives the completed IRP\_MN\_START\_DEVICE request (that is, when NDIS's [**DispatchPnP**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine gains control after all lower drivers have finished with the IRP), NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

4.  If the *MiniportInitializeEx* function returns NDIS\_STATUS\_SUCCESS, NDIS schedules an event to call the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function of all protocol drivers that are supposed to bind to the adapter, as indicated by the binding information in the registry. Note that the miniport driver has no information about bindings.

5.  NDIS completes the IRP\_MN\_START\_DEVICE request.

 

