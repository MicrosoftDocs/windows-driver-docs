---
title: Cancel a data transfer
description: Cancel a data transfer
ms.date: 03/28/2023
---

# Cancel a data transfer

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

WIA applications and WIA minidrivers can cancel a data transfer at any time. A WIA minidriver can determine whether an application canceled the data transfer by checking the value returned by the [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback) method. If the method returns S_FALSE, the data transfer has been canceled. The WIA minidriver must stop all acquisition activity and return to an idle state. It is then ready for the next data transfer.

A WIA minidriver can signal that the data transfer was canceled by returning S_FALSE from the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method. Some devices have a cancel button on the hardware that can abort the data transfer. In such cases, the WIA minidriver should return S_FALSE.

It is possible to cancel a WIA scan without declaring an error and returning S_FALSE. However, this is only possible in Windows XP and later operating systems; it is not possible in Windows Millennium Edition.

All return codes received from the **IWiaMiniDrvCallBack::MiniDrvCallback** method should be returned in the **IWiaMiniDrv::drvAcquireItemData** method. If an application returns an error code in the **IWiaMiniDrvCallBack::MiniDrvCallback** method, the WIA minidriver must stop the data transfer, return to an idle state, and then return that error code to the WIA service.
