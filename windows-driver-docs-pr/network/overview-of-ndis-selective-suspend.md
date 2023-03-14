---
title: Overview of NDIS Selective Suspend
description: Overview of NDIS Selective Suspend
ms.date: 03/02/2023
---

# Overview of NDIS Selective Suspend


Starting with NDIS 6.30, the NDIS selective suspend interface enables NDIS to suspend an idle network adapter by transitioning the adapter to a low-power state. This enables the system to reduce the CPU and power overhead of the adapter.

NDIS selective suspend is especially useful for network adapters that are based on the USB v1.1 and v2.0 interface. These adapters are continuously polled for received packets regardless of whether they are active or idle. By suspending idle USB adapters, the CPU overhead can be reduced by as much as 10 percent.

NDIS selective suspend is based on the [USB selective suspend](../usbcon/usb-selective-suspend.md) technology. However, NDIS selective suspend is designed to be bus-independent. In this way, bus-independent I/O request packets (IRPs) for selective suspend are issued by NDIS. This makes the miniport driver responsible for issuing any IRPs that are required for selective suspend on a specific bus. For example, miniport drivers for USB network adapters issue the bus-specific USB idle request IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) to the USB bus driver during a selective suspend operation.

NDIS and the miniport driver participate in NDIS selective suspend in the following way:

1.  If a miniport driver has registered its support for NDIS selective suspend, NDIS monitors the I/O activity of the network adapter. I/O activity includes receive packet indications, send packet completions, and OID requests that are handled by the miniport driver.

2.  NDIS considers the network adapter to be idle if it has been inactive for longer than a specified idle time-out period. When this happens, NDIS starts a selective suspend operation by issuing an idle notification to the miniport driver in order to transition the network adapter to a low-power state.

    > [!NOTE]
    > The length of the idle time-out period is specified by the value of the **\*SSIdleTimeout** standardized INF keyword. For more information about this keyword, see [Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md).     

    For more information about how NDIS determines that a network adapter is idle, see [How NDIS Detects Idle Network Adapters](how-ndis-detects-idle-network-adapters.md).

3.  NDIS issues the idle notification to the miniport driver by calling the driver's [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function. When this function is called, the miniport driver determines whether the network adapter can transition to a low-power state. The miniport driver performs this determination in a bus-specific manner.

    For example, a USB miniport driver determines whether the network adapter can transition to a low-power state by issuing a USB idle request IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) to the underlying USB bus driver. This informs the bus driver that the network adapter is idle and confirms whether the adapter can be transitioned to a low-power state.
    
    > [!NOTE]
    > The miniport driver must specify a callback and completion routine for the USB idle request IRP.
    
    For more information about how a miniport driver handles an idle notification, see [Handling the NDIS Selective Suspend Idle Notification](handling-the-ndis-selective-suspend-idle-notification.md).

4.  After the miniport driver confirms that the network adapter can transition to a low-power state, it calls [**NdisMIdleNotificationConfirm**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationconfirm). In this call, the miniport driver specifies the lowest power state that the network adapter can transition to.

5.  When [**NdisMIdleNotificationConfirm**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationconfirm) is called, NDIS issues OID requests to the miniport driver to prepare the adapter for the transition to a low-power state. NDIS also issues IRPs to the underlying bus driver to set the adapter to a low-power state.

6.  After the network adapter has been suspended, it remains in a low power state until the outstanding idle notification is canceled.

    NDIS cancels the outstanding idle notification by calling the miniport driver's [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) handler function. NDIS calls this handler function if one or more of the following conditions are true:

    -   NDIS detects send packet requests or OID requests that are issued to the miniport driver from overlying protocol or filter drivers.

    -   The network adapter signals a wake-up event. This might occur when the adapter receives a packet or detects a change in its media connection status.

    After the network adapter has been suspended, the miniport driver can also complete the idle notification in order to resume the adapter to a full-power state. The reasons for doing this are specific to the design and requirements of the driver and adapter.

    For more information about how NDIS cancels the idle notification, see [Canceling the NDIS Selective Suspend Idle Notification](canceling-the-ndis-selective-suspend-idle-notification.md).

    For more information about how the miniport driver completes the idle notification, see [Completing the NDIS Selective Suspend Idle Notification](completing-the-ndis-selective-suspend-idle-notification.md).

7.  When the [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) handler function is called, the miniport driver determines whether the network adapter can resume to a full-power state. The driver also cancels any bus-specific IRPs that it may have previously issued for the idle notification.

    The determination that the network adapter can transition to a full-power state is bus-specific. For example, when [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) is called, the USB miniport must cancel the previously issued USB idle request IRP. As soon as the USB driver has canceled the IRP, it calls the IRP's completion routine to confirm that the IRP is canceled and the network adapter can resume to a full-power state. In the context of the completion routine, the miniport driver calls [**NdisMIdleNotificationComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationcomplete).

    When the miniport determines that the network adapter can resume to a full-power state, it calls [**NdisMIdleNotificationComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationcomplete). This call notifies NDIS that the idle notification has been completed. NDIS then proceeds with completing the selective suspend operation by transitioning the network adapter to a full-power state.

8.  When [**NdisMIdleNotificationComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationcomplete) is called, NDIS issues OID requests to the miniport driver to prepare the adapter for the transition to a full-power state. NDIS also issues IRPs to the underlying bus driver to set the adapter to a full-power state.

9.  When the network adapter resumes to a full-power state, the selective suspend operation is completed. NDIS resumes monitoring the I/O activity of the network adapter. If the adapter becomes inactive after another idle time-out period, NDIS issues an idle notification to the miniport driver in order to suspend the network adapter.
