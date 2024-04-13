---
title: Cancel Pending I/O Operations
description: Cancel pending I/O operations
ms.date: 04/20/2017
---

# Cancel pending I/O operations

WIA applications can use the **IWiaItemExtras::CancelPendingIO** method (described in the Microsoft Windows SDK documentation) to cancel any pending I/O operations that the WIA minidriver may currently be processing. The **IWiaItemExtras::CancelPendingIO** method calls the [**IWiaMiniDrv::drvNotifyPnpEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) method with a WIA_EVENT_CANCEL_IO event. The WIA minidriver should cancel all current I/O operations and return to an idle state.

The **IWiaItemExtras::CancelPendingIO** method can be called at any time. It is recommended that all kernel-mode read or write operations use [overlapped I/O](../kernel/handling-overlapped-i-o-operations.md). This allows an immediate cancellation to occur. WIA applications that are experiencing unexpected delays, or appear to be hanging, can call the **IWiaItemExtras::CancelPendingIO** method to attempt to return control back to the end user.
