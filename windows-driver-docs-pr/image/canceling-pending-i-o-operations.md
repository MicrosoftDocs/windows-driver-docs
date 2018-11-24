---
title: Canceling Pending I/O Operations
description: Canceling Pending I/O Operations
ms.assetid: 58383836-5922-4499-a73d-d17d26dd2f76
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling Pending I/O Operations





WIA applications can use the **IWiaItemExtras::CancelPendingIO** method (described in the Microsoft Windows SDK documentation) to cancel any pending I/O operations that the WIA minidriver may currently be processing. The **IWiaItemExtras::CancelPendingIO** method calls the [**IWiaMiniDrv::drvNotifyPnpEvent**](https://msdn.microsoft.com/library/windows/hardware/ff544998) method with a WIA\_EVENT\_CANCEL\_IO event. The WIA minidriver should cancel all current I/O operations and return to an idle state.

The **IWiaItemExtras::CancelPendingIO** method can be called at any time. It is recommended that all kernel-mode read or write operations use [overlapped I/O](https://msdn.microsoft.com/library/windows/hardware/ff546911). This allows an immediate cancellation to occur. WIA applications that are experiencing unexpected delays, or appear to be hanging, can call the **IWiaItemExtras::CancelPendingIO** method to attempt to return control back to the end user.

 

 




