---
title: Cancellation of Data Transfers in Windows XP
description: Cancellation of Data Transfers in Windows XP
ms.assetid: 971979a5-950b-49d4-9adb-cd4589a00426
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cancellation of Data Transfers in Windows XP


In Microsoft Windows XP and Windows Me, there were two ways for a WIA application to cancel a data transfer:

-   Return S\_FALSE from the transfer callback routine, **IWiaDataCallback::BandedDataCallback**.

-   Call **IWiaItemExtras::CancelPendingIO**. We do not recommend this method and it is not used by any in-box drivers or samples.

There were also two ways for a WIA driver to be notified that the application had canceled a transfer:

-   Receive S\_FALSE when it called into [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946).

-   Receive a call to its [**IWiaMiniDrv::drvNotifyPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) with a WIA\_EVENT\_CANCEL\_IO event.

One problem with the Windows XP implementation is that there is no connection between the two notification methods; that is, if a user calls **IWiaItemExtras::CancelPendingIO** but the driver does not support asynchronous canceling of a data transfer through **IWiaMiniDrv::drvNotifyPnPEvent**, the application will also have to return S\_FALSE from **IWiaMiniDrvCallBack::MiniDrvCallback**<em>.</em>

The **IWiaDataCallback** and **IWiaItemExtras** interfaces are described in the Microsoft Windows SDK documentation.

 

 




