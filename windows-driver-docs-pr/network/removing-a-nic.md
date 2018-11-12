---
title: Removing a NIC
description: Removing a NIC
ms.assetid: eaa4b784-4375-465d-9ef5-99b38b7fd15a
keywords:
- NICs WDK networking , removing
- network interface cards WDK networking , removing
- Plug and Play WDK NDIS miniport , removing NIC
- removing NICs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Removing a NIC





The following steps describe how NDIS participates in the removal of a NIC:

1.  The PnP manager issues an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) request to query whether the NIC can be removed without disrupting the computer.

2.  When NDIS receives this IRP, it calls the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function of the lowest filter driver that is attached to the NIC in the driver stack. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for filter drivers that advertise an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function. A filter driver advertises this entry point when it calls the [**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608) function.

     

3.  Within the context of the call to its [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function, the filter driver must call [**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828) to forward the **NetEventQueryRemoveDevice** event up to the next filter driver in the driver stack. This causes NDIS to call that filter driver's *FilterNetPnPEvent* function with an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for the next filter driver in the driver stack that advertises an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

4.  Each filter driver in the driver stack repeats the previous step until the highest filter driver in the stack has forwarded the **NetEventQueryRemoveDevice** event.

    When this happens, NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of all protocol drivers that are bound to the NIC. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

5.  If a protocol driver fails the **NetEventQueryRemoveDevice** event by returning a failure code NDIS\_STATUS\_FAILURE from *ProtocolNetPnPEvent*, NDIS or the PnP manager might ignore the failure and subsequently succeed the [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705) request. A protocol driver must, therefore, be prepared to handle the removal of the NIC even though the protocol driver failed the **NetEventQueryRemoveDevice** event.

6.  The PnP manager issues an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to remove the software representation (device objects, and so on) for the NIC or an [**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550823) request to cancel the pending removal. Note that an IRP\_MN\_REMOVE\_DEVICE request is not always preceded by an IRP\_MN\_QUERY\_REMOVE\_DEVICE request.

7.  If the PnP manager issues an IRP\_MN\_CANCEL\_REMOVE\_DEVICE request, NDIS calls the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function of the lowest filter driver that is attached to the NIC in the driver stack. In this call, NDIS specifies an event code of **NetEventCancelRemoveDevice**.

    **Note**  NDIS performs this step only for filter drivers that advertise an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

8.  Within the context of the call to its [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function, the filter driver must call [**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828) to forward the **NetEventCancelRemoveDevice** event up to the next filter driver in the driver stack. This causes NDIS to call that filter driver's *FilterNetPnPEvent* function with an event code of **NetEventCancelRemoveDevice**.

    **Note**  NDIS performs this step only for the next filter driver in the driver stack that advertises an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

9.  Each filter driver in the driver stack repeats the previous step until the highest filter driver in the stack has forwarded the **NetEventCancelRemoveDevice** event.

    When this happens, NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of all protocol drivers that are bound to the NIC. In this call, NDIS specifies an event code of **NetEventCancelRemoveDevice**. This event code ends the removal sequence.

10. If the PnP manager issues an IRP\_MN\_REMOVE\_DEVICE request, NDIS performs these steps:

    1.  It pauses all protocol drivers that are bound to the NIC.

    2.  It pauses all filter drivers that are attached to the NIC.

    3.  It pauses the miniport driver for the NIC.

    4.  It calls the [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function of all protocol drivers that are bound to the NIC.

    5.  It calls the [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function of all filter modules that are attached to the NIC.

11. If the miniport driver was successfully initialized, NDIS calls the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function. NDIS sets the *HaltAction* parameter of *MiniportHaltEx* to **NdisHaltDeviceDisabled**.

12. NDIS sends the IRP\_MN\_REMOVE\_DEVICE request to the next lower device object in the stack.

13. When NDIS receives the completed IRP\_MN\_REMOVE\_DEVICE request from the next lower device object in the stack, NDIS destroys the functional device object (FDO) that it created for the NIC.

 

 





