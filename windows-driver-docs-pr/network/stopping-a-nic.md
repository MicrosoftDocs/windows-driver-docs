---
title: Stopping a NIC
description: Stopping a NIC
ms.assetid: 033b45bd-fbe9-4a40-84e6-b9447370b17f
keywords:
- NICs WDK networking , stopping
- network interface cards WDK networking , stopping
- Plug and Play WDK NDIS miniport , stopping NIC
- stopping NICs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stopping a NIC





The PnP manager stops a NIC so that it can reconfigure or rebalance the hardware resources that it assigned to the NIC. The following steps describe how NDIS participates in the stopping of a NIC:

1.  The PnP manager issues an [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725) request.

2.  When NDIS receives this IRP, it calls the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function of the lowest filter driver that is attached to the NIC in the driver stack. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for filter drivers that advertise an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function. A filter driver advertises this entry point when it calls the [**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608) function.

     

3.  Within the context of the call to its [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function, the filter driver must call [**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828) to forward the **NetEventQueryRemoveDevice** event up to the next filter driver in the driver stack. This causes NDIS to call that filter driver's *FilterNetPnPEvent* function with an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for the next filter driver in the driver stack that advertises an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

4.  Each filter driver in the driver stack repeats the previous step until the highest filter driver in the stack has forwarded the **NetEventQueryRemoveDevice** event.

    When this happens, NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of all protocol drivers that are bound to the NIC. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

5.  If a protocol driver fails the **NetEventQueryRemoveDevice** event by returning a failure code from *ProtocolNetPnPEvent*, NDIS or the PnP manager might ignore the failure and subsequently succeed the IRP\_MN\_QUERY\_STOP\_DEVICE request. A protocol driver must, therefore, be prepared to handle the removal of the NIC even though the protocol driver failed the **NetEventQueryRemoveDevice** event.

6.  The PnP manager issues an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request to stop the device or an [**IRP\_MN\_CANCEL\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550826) request to cancel the pending stop.

7.  If the PnP manager issues an IRP\_MN\_CANCEL\_STOP\_DEVICE request, NDIS calls the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function of the lowest filter driver that is attached to the NIC in the driver stack. In this call, NDIS specifies an event code of **NetEventCancelRemoveDevice**.

    **Note**  NDIS performs this step only for filter drivers that advertise an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

8.  Within the context of the call to its [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function, the filter driver must call [**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828) to forward the **NetEventCancelRemoveDevice** event up to the next filter driver in the driver stack. This causes NDIS to call that filter driver's *FilterNetPnPEvent* function with an event code of **NetEventCancelRemoveDevice**.

    **Note**  NDIS performs this step only for the next filter driver in the driver stack that advertises an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

9.  Each filter driver in the driver stack repeats the previous step until the highest filter driver in the stack has forwarded the **NetEventCancelRemoveDevice** event.

    When this happens, NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of all protocol drivers that are bound to the NIC. In this call, NDIS specifies an event code of **NetEventCancelRemoveDevice**.

10. If the PnP manager issues an IRP\_MN\_STOP\_DEVICE request, NDIS performs these steps:

    1.  It pauses all protocol drivers that are bound to the NIC.

    2.  It pauses all filter drivers that are attached to the NIC.

    3.  It pauses the miniport driver for the NIC.

    4.  It calls the [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function of all protocol drivers that are bound to the NIC.

    5.  It calls the [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function of all filter modules that are attached to the NIC.

11. After all protocol and filter drivers are unbound and detached from the NIC, NDIS calls the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function. NDIS sets the *HaltAction* parameter of *MiniportHaltEx* to **NdisHaltDeviceStopped**.

12. When processing an IRP\_MN\_STOP\_DEVICE request, NDIS does not destroy the functional device object (FDO) that it created for the NIC when the *AddDevice* routine was called. NDIS destroys the device object only after receiving an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request for the NIC.

    If the PnP manager issues an IRP\_MN\_START\_DEVICE to restart the NIC, NDIS will reuse the FDO that was previously created for the NIC. NDIS will then restart the NIC. For more information on this procedure, see [Starting a NIC](starting-a-nic.md).

 

 





