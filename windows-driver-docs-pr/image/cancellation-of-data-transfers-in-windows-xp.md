---
title: Cancellation of Data Transfers in Windows XP
description: Cancellation of Data Transfers in Windows XP
ms.date: 04/20/2017
---

# Cancellation of Data Transfers in Windows XP


In Microsoft Windows XP and Windows Me, there were two ways for a WIA application to cancel a data transfer:

-   Return S\_FALSE from the transfer callback routine, **IWiaDataCallback::BandedDataCallback**.

-   Call **IWiaItemExtras::CancelPendingIO**. We do not recommend this method and it is not used by any in-box drivers or samples.

There were also two ways for a WIA driver to be notified that the application had canceled a transfer:

-   Receive S\_FALSE when it called into [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback).

-   Receive a call to its [**IWiaMiniDrv::drvNotifyPnPEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) with a WIA\_EVENT\_CANCEL\_IO event.

One problem with the Windows XP implementation is that there is no connection between the two notification methods; that is, if a user calls **IWiaItemExtras::CancelPendingIO** but the driver does not support asynchronous canceling of a data transfer through **IWiaMiniDrv::drvNotifyPnPEvent**, the application will also have to return S\_FALSE from **IWiaMiniDrvCallBack::MiniDrvCallback**<em>.</em>

The **IWiaDataCallback** and **IWiaItemExtras** interfaces are described in the Microsoft Windows SDK documentation.

 

