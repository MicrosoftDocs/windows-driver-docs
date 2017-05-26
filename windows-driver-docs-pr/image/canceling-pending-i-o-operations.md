---
title: Canceling Pending I/O Operations
author: windows-driver-content
description: Canceling Pending I/O Operations
ms.assetid: 58383836-5922-4499-a73d-d17d26dd2f76
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Canceling Pending I/O Operations


## <a href="" id="ddk-canceling-pending-i-o-operations-si"></a>


WIA applications can use the **IWiaItemExtras::CancelPendingIO** method (described in the Microsoft Windows SDK documentation) to cancel any pending I/O operations that the WIA minidriver may currently be processing. The **IWiaItemExtras::CancelPendingIO** method calls the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method with a WIA\_EVENT\_CANCEL\_IO event. The WIA minidriver should cancel all current I/O operations and return to an idle state.

The **IWiaItemExtras::CancelPendingIO** method can be called at any time. It is recommended that all kernel-mode read or write operations use [overlapped I/O](https://msdn.microsoft.com/library/windows/hardware/ff546911). This allows an immediate cancellation to occur. WIA applications that are experiencing unexpected delays, or appear to be hanging, can call the **IWiaItemExtras::CancelPendingIO** method to attempt to return control back to the end user.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Canceling%20Pending%20I/O%20Operations%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


