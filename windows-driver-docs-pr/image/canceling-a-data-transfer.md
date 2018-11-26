---
title: Canceling a Data Transfer
description: Canceling a Data Transfer
ms.assetid: a7900968-df57-41d9-abb1-4d2c97517362
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling a Data Transfer





WIA applications and WIA minidrivers can cancel a data transfer at any time. A WIA minidriver can determine whether an application canceled the data transfer by checking the value returned by the [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946) method. If the method returns S\_FALSE, the data transfer has been canceled. The WIA minidriver must stop all acquisition activity and return to an idle state. It is then ready for the next data transfer.

A WIA minidriver can signal that the data transfer was canceled by returning S\_FALSE from the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method. Some devices have a cancel button on the hardware that can abort the data transfer. In such cases, the WIA minidriver should return S\_FALSE.

**Note**   It is possible to cancel a WIA scan without declaring an error and returning S\_FALSE. However, this is only possible in Windows XP and later operating systems; it is not possible in Windows Millennium Edition.

 

All return codes received from the **IWiaMiniDrvCallBack::MiniDrvCallback** method should be returned in the **IWiaMiniDrv::drvAcquireItemData** method. If an application returns an error code in the **IWiaMiniDrvCallBack::MiniDrvCallback** method, the WIA minidriver must stop the data transfer, return to an idle state, and then return that error code to the WIA service.

 

 




