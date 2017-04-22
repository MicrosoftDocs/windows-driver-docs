---
title: Cancellation of Data Transfers in Windows Vista
author: windows-driver-content
description: Cancellation of Data Transfers in Windows Vista
ms.assetid: 0cdc02bf-23fe-4122-8d5f-f42c3c07da8b
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cancellation of Data Transfers in Windows Vista


In Windows Vista, there is a new interface, **IWiaTransfer** (which is described in the Windows SDK documentation) that applications use to perform stream-based data transfers. This interface, in addition to the new transfer methods, contains a **Cancel** method that an application can use to cancel data transfers, including [multi-item transfers](multipage-istream-transfers.md). With this method, you can asynchronously cancel a data transfer. We recommended that you use this procedure to cancel a data transfer. However, a Windows Vista application can also return S\_FALSE from its callback routine to cancel a transfer.

Thus, there are two ways for a WIA application in Windows Vista to cancel a transfer:

-   Return S\_FALSE from its callback routine.

-   Call **IWiaTransfer::Cancel**.

A Windows Vista driver can be notified in two different ways that the application has canceled the transfer:

-   The driver receives a call to its [**IWiaMiniDrv::drvNotifyPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) with a WIA\_EVENT\_CANCEL\_IO event. We recommend that all kernel-mode read or write operations use OVERLAPPED I/O. Only with this procedure can you guarantee *immediate* cancellation.

-   S\_FALSE is returned from two callback functions: **IWiaMiniDrvTransferCallback::GetNextStream** and [**IWiaMiniDrvTransferCallback::SendMessage**](https://msdn.microsoft.com/library/windows/hardware/jj151552).

When an application calls **IWiaTransfer::Cancel**, the **IWiaMiniDrv::drvNotifyPnPEvent** method should be called into the driver with WIA\_EVENT\_CANCEL\_IO. In addition, the [**IWiaMiniDrvTransferCallback::GetNextStream**](https://msdn.microsoft.com/library/windows/hardware/jj151551) and **IWiaMiniDrvTransferCallback::SendMessage** callback functions must always return S\_FALSE after the transfer has been canceled.

If **IWiaTransferCallback::GetNextStream** returns WIA\_STATUS\_SKIP\_ITEM during a [multi-item transfer](multipage-istream-transfers.md), an application is skipping (that is, not transferring) the current item. A return value of S\_FALSE still means that the whole transfer should be canceled.

The **IWiaTransfer** and **IWiaTransferCallback** interfaces are described in the Microsoft Windows SDK documentation.

## Related topics
[**IWiaMiniDrvTransferCallback**](https://msdn.microsoft.com/library/windows/hardware/jj151550)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Cancellation%20of%20Data%20Transfers%20in%20Windows%20Vista%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


