---
title: Processing the surprise removal of a NIC (Windows 7 and later)
description: Processing the Surprise Removal of a NIC (Windows 7 and Later Versions)
ms.date: 04/20/2017
---

# Processing the Surprise Removal of a NIC (Windows 7 and Later Versions)





In Windows 7 and Windows Server 2008 R2 and later, NDIS may participate in the surprise removal of a network interface card (NIC) differently than it had in previous versions of Windows. NDIS performs a revised surprise removal procedure if *any* of the following conditions are true:

-   The operating system is Windows 8 / Windows Server 2012 or later.
-   The operating system is Windows 7, and the hotfix for KB2471472 has been installed.
-   The operating system is Windows 7, and the network adapter is a mobile broadband (MBB) device.

If none of these conditions are met, NDIS participates in the surprise removal process as it did in previous versions of Windows. For more information about this procedure, see [Processing the Surprise Removal of a NIC (Windows Vista)](processing-the-surprise-removal-of-a-nic--windows-vista-.md).

The following steps describe the revised way in which NDIS participates in the surprise removal of a NIC:

1.  The PnP manager issues an [**IRP\_MN\_SURPRISE\_REMOVAL**](../kernel/irp-mn-surprise-removal.md) request to the device stack for the NIC.

2.  When NDIS receives this IRP, it calls the [*FilterNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event) function of the lowest filter driver that is attached to the NIC in the driver stack. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for filter drivers that advertise an entry point for the [*FilterNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event) function. A filter driver advertise this entry point when it calls the [**NdisFRegisterFilterDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver) function.

     

3.  Within the context of the call to its [*FilterNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event) function, the filter driver must call [**NdisFNetPnPEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfnetpnpevent) to forward the **NetEventQueryRemoveDevice** event up to the next filter driver in the driver stack. This causes NDIS to call that filter driver's *FilterNetPnPEvent* function with an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for the next filter driver in the driver stack that advertises an entry point for the [*FilterNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event) function.

     

4.  Each filter driver in the driver stack repeats the previous step until the highest filter driver in the stack has forwarded the **NetEventQueryRemoveDevice** event.

    When this happens, NDIS calls the [*ProtocolNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event) function of all protocol drivers that are bound to the NIC. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

5.  NDIS calls the [*MiniportDevicePnPEventNotify*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_device_pnp_event_notify) function with an event code of **NdisDevicePnPEventSurpriseRemoved**. The miniport driver should note that the device has been physically removed. If the miniport driver is an NDIS-WDM driver, it should cancel any pending IRPs that it sent down to the underlying bus driver.

6.  NDIS performs the following steps:

    1.  It pauses all protocol drivers that are bound to the NIC.

    2.  It pauses all filter drivers that are attached to the NIC.

    3.  It pauses the miniport driver for the NIC.

    4.  It calls the [*ProtocolUnbindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex) function of all protocol drivers that are bound to the NIC.

    5.  It calls the [*FilterDetach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_detach) function of all filter modules that are attached to the NIC.

7.  After all protocol and filter drivers are unbound and detached from the NIC, NDIS calls the miniport driver's [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function. NDIS sets the *HaltAction* parameter of *MiniportHaltEx* to **NdisHaltDeviceSurpriseRemoved**.

8.  NDIS sends the IRP\_MN\_SURPRISE\_REMOVAL request to the next-lower device object in the stack. After receiving the returned IRP\_MN\_SURPRISE\_REMOVAL request from the next-lower device object in the stack, NDIS completes the IRP\_MN\_SURPRISE\_REMOVAL request.

9.  The PnP manager issues an [**IRP\_MN\_REMOVE\_DEVICE**](../kernel/irp-mn-remove-device.md) request to remove the software representation (device objects, and so forth) for the NIC.

10. NDIS sends the IRP\_MN\_REMOVE\_DEVICE request to the next lower device object in the stack.

11. When NDIS receives the completed IRP\_MN\_REMOVE\_DEVICE request from the next lower device object in the stack, NDIS destroys the functional device object (FDO) that it created for the NIC.

 

