---
title: Processing the Surprise Removal of a NIC (Windows Vista)
description: Processing the Surprise Removal of a NIC (Windows Vista)
ms.assetid: 940E6109-0A4C-4F4C-8201-F28BB789D7AE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing the Surprise Removal of a NIC (Windows Vista)





The following steps describe how NDIS participates in the surprise removal of a NIC in Windows Vista and Windows Server 2008:

1.  The PnP manager issues an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request to the device stack for the NIC.

2.  When NDIS receives this IRP, it calls the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function of the lowest filter driver that is attached to the NIC in the driver stack. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice**.

    **Note**  NDIS performs this step only for filter drivers that advertise an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function. A filter driver advertise this entry point when it calls the [**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608) function.

     

3.  Within the context of the call to its [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function, the filter driver must call [**NdisFNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561828) to forward the **NetEventQueryRemoveDevice** event up to the next filter driver in the driver stack. This causes NDIS to call that filter driver's *FilterNetPnPEvent* function with an event code of **NetEventQueryRemoveDevice.**.

    **Note**  NDIS performs this step only for the next filter driver in the driver stack that advertises an entry point for the [*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952) function.

     

4.  Each filter driver in the driver stack repeats the previous step until the highest filter driver in the stack has forwarded the **NetEventQueryRemoveDevice.** event.

    When this happens, NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of all protocol drivers that are bound to the NIC. In this call, NDIS specifies an event code of **NetEventQueryRemoveDevice.**.

5.  If the miniport driver was successfully initialized, NDIS calls the [*MiniportDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff559369) function with an event code of **NdisDevicePnPEventSurpriseRemoved**. The miniport driver should note that the device has been physically removed. If the miniport driver is an NDIS-WDM driver, it should cancel any pending IRPs that it sent down to the underlying bus driver. If the miniport driver was not successfully initialized, processing continues.

6.  NDIS sends the IRP\_MN\_SURPRISE\_REMOVAL request to the next-lower device object in the stack. After receiving the returned IRP\_MN\_SURPRISE\_REMOVAL request from the next-lower device object in the stack, NDIS completes the IRP\_MN\_SURPRISE\_REMOVAL request.

7.  The PnP manager issues an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to remove the software representation (device objects, and so forth) for the NIC.

8.  NDIS performs the following steps:

    1.  It pauses all protocol drivers that are bound to the NIC.

    2.  It pauses all filter drivers that are attached to the NIC.

    3.  It pauses the miniport driver for the NIC.

    4.  It calls the [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function of all protocol drivers that are bound to the NIC.

    5.  It calls the [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function of all filter modules that are attached to the NIC.

9.  After all protocol and filter drivers are unbound and detached from the NIC, NDIS calls the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function. NDIS sets the *HaltAction* parameter of *MiniportHaltEx* to **NdisHaltDeviceSurpriseRemoved**.

10. NDIS sends the IRP\_MN\_REMOVE\_DEVICE request to the next lower device object in the stack.

11. When NDIS receives the completed IRP\_MN\_REMOVE\_DEVICE request from the next lower device object in the stack, NDIS destroys the functional device object (FDO) that it created for the NIC.

 

 





