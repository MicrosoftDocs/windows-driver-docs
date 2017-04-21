---
title: Cancellation of Data Transfers in Windows XP
author: windows-driver-content
description: Cancellation of Data Transfers in Windows XP
ms.assetid: 971979a5-950b-49d4-9adb-cd4589a00426
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cancellation of Data Transfers in Windows XP


In Microsoft Windows XP and Windows Me, there were two ways for a WIA application to cancel a data transfer:

-   Return S\_FALSE from the transfer callback routine, **IWiaDataCallback::BandedDataCallback**.

-   Call **IWiaItemExtras::CancelPendingIO**. We do not recommend this method and it is not used by any in-box drivers or samples.

There were also two ways for a WIA driver to be notified that the application had canceled a transfer:

-   Receive S\_FALSE when it called into [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946).

-   Receive a call to its [**IWiaMiniDrv::drvNotifyPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) with a WIA\_EVENT\_CANCEL\_IO event.

One problem with the Windows XP implementation is that there is no connection between the two notification methods; that is, if a user calls **IWiaItemExtras::CancelPendingIO** but the driver does not support asynchronous canceling of a data transfer through **IWiaMiniDrv::drvNotifyPnPEvent**, the application will also have to return S\_FALSE from **IWiaMiniDrvCallBack::MiniDrvCallback***.*

The **IWiaDataCallback** and **IWiaItemExtras** interfaces are described in the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Cancellation%20of%20Data%20Transfers%20in%20Windows%20XP%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


