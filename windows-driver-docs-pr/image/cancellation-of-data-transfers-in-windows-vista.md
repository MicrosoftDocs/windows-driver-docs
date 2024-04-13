---
title: Cancellation of Data Transfers in Windows Vista
description: Cancellation of data transfers in Windows Vista
ms.date: 03/28/2023
---

# Cancellation of data transfers in Windows Vista

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

In Windows Vista, there is a new interface, **IWiaTransfer** (which is described in the Windows SDK documentation) that applications use to perform stream-based data transfers. This interface, in addition to the new transfer methods, contains a **Cancel** method that an application can use to cancel data transfers, including [multi-item transfers](multipage-istream-transfers.md). With this method, you can asynchronously cancel a data transfer. We recommended that you use this procedure to cancel a data transfer. However, a Windows Vista application can also return S_FALSE from its callback routine to cancel a transfer.

Thus, there are two ways for a WIA application in Windows Vista to cancel a transfer:

- Return S_FALSE from its callback routine.

- Call **IWiaTransfer::Cancel**.

A Windows Vista driver can be notified in two different ways that the application has canceled the transfer:

- The driver receives a call to its [**IWiaMiniDrv::drvNotifyPnPEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) with a WIA_EVENT_CANCEL_IO event. We recommend that all kernel-mode read or write operations use OVERLAPPED I/O. Only with this procedure can you guarantee *immediate* cancellation.

- S_FALSE is returned from two callback functions: **IWiaMiniDrvTransferCallback::GetNextStream** and [**IWiaMiniDrvTransferCallback::SendMessage**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvtransfercallback-sendmessage).

When an application calls **IWiaTransfer::Cancel**, the **IWiaMiniDrv::drvNotifyPnPEvent** method should be called into the driver with WIA_EVENT_CANCEL_IO. In addition, the [**IWiaMiniDrvTransferCallback::GetNextStream**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvtransfercallback-getnextstream) and **IWiaMiniDrvTransferCallback::SendMessage** callback functions must always return S_FALSE after the transfer has been canceled.

If **IWiaTransferCallback::GetNextStream** returns WIA_STATUS_SKIP_ITEM during a [multi-item transfer](multipage-istream-transfers.md), an application is skipping (that is, not transferring) the current item. A return value of S_FALSE still means that the whole transfer should be canceled.

The **IWiaTransfer** and **IWiaTransferCallback** interfaces are described in the Microsoft Windows SDK documentation.

## Related topics

[**IWiaMiniDrvTransferCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvtransfercallback)
