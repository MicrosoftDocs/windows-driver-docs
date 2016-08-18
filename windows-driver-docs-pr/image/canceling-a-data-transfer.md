---
title: Canceling a Data Transfer
author: windows-driver-content
description: Canceling a Data Transfer
MS-HAID:
- 'WIA\_db\_trans\_71507fc7-a019-47db-ae49-de6037143aba.xml'
- 'image.canceling\_a\_data\_transfer'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a7900968-df57-41d9-abb1-4d2c97517362
---

# Canceling a Data Transfer


## <a href="" id="ddk-canceling-a-data-transfer-si"></a>


WIA applications and WIA minidrivers can cancel a data transfer at any time. A WIA minidriver can determine whether an application canceled the data transfer by checking the value returned by the [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946) method. If the method returns S\_FALSE, the data transfer has been canceled. The WIA minidriver must stop all acquisition activity and return to an idle state. It is then ready for the next data transfer.

A WIA minidriver can signal that the data transfer was canceled by returning S\_FALSE from the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method. Some devices have a cancel button on the hardware that can abort the data transfer. In such cases, the WIA minidriver should return S\_FALSE.

**Note**   It is possible to cancel a WIA scan without declaring an error and returning S\_FALSE. However, this is only possible in Windows XP and later operating systems; it is not possible in Windows Millennium Edition.

 

All return codes received from the **IWiaMiniDrvCallBack::MiniDrvCallback** method should be returned in the **IWiaMiniDrv::drvAcquireItemData** method. If an application returns an error code in the **IWiaMiniDrvCallBack::MiniDrvCallback** method, the WIA minidriver must stop the data transfer, return to an idle state, and then return that error code to the WIA service.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Canceling%20a%20Data%20Transfer%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


