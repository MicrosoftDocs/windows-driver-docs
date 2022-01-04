---
title: Managing IRP Resources for NDIS Selective Suspend
description: Managing IRP Resources for NDIS Selective Suspend
ms.date: 04/20/2017
---

# Managing IRP Resources for NDIS Selective Suspend


If a miniport driver supports and enables NDIS selective suspend, NDIS calls [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) to issue an idle notification to the driver if the network adapter becomes inactive. When the miniport driver handles this notification, it may need to issue I/O request packets (IRPs) to the underlying bus driver. These IRPs notify the bus driver about the adapter's idle state and request confirmation that the adapter can transition to a low-power state.

IRPs that are issued by the miniport driver are bus-specific. For example, when NDIS calls [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification), the USB miniport issues an USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) IRP to the underlying USB bus driver.

NDIS may issue the idle notification to the miniport driver many times after the driver has been initialized. Therefore, we recommend that the driver allocate the resources for the USB idle request IRP in the context of the call to the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

The following example shows how the miniport driver allocates the IRP resources.

```C++
//
// MiniportInitializeEx()
//
// In the miniport's initialization routine, the miniport should allocate
// an IRP.  It can also set up the USB_IDLE_CALLBACK_INFO structure that
// will be used with each successive USB idle request.
//
NDIS_STATUS MiniportInitializeEx(
    _In_ NDIS_HANDLE MiniportAdapterHandle,
    _In_ NDIS_HANDLE MiniportDriverContext,
    _In_ PNDIS_MINIPORT_INIT_PARAMETERS MiniportInitParameters
    )
    {
    PIRP UsbSsIrp;
    USB_IDLE_CALLBACK_INFO UsbSsCallback;
    ...

    UsbSsIrp = IoAllocateIrp(Adapter->Fdo->StackSize, FALSE);
    if (!UsbSsIrp)
       {
       // Handle failure
       return NDIS_STATUS_RESOURCES;
       }

    UsbSsCallback.IdleCallback = MiniportUsbIdleRequestCallback;
    UsbSsCallback.IdleContext = Adapter;

    // Save these in the adapter structure for later use
    Adapter->UsbSsIrp = UsbSsIrp;
    Adapter->UsbSsCallback = UsbSsCallback;
    ...
    }
```

If the miniport driver allocates the IRP resources during the call to [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize), the driver must free those resources during the call to [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt).

The following example shows how the miniport driver frees the IRP resources.

```C++
//
// MiniportHaltEx
//
// During halt (or when the miniport performs its cleanup from 
// MiniportInitializeEx) the miniport should free the IRP allocated 
// earlier.
//
VOID MiniportHaltEx(
     _In_  NDIS_HANDLE MiniportAdapterContext,
     _In_  NDIS_HALT_ACTION HaltAction
    )
    {
    ...
    if (Adapter->UsbSsIrp)
        {
        IoFreeIrp(Adapter->UsbSsIrp);
        Adapter->UsbSsIrp = NULL;
        }
    ...
    }

```
