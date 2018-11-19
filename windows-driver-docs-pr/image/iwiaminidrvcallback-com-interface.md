---
title: IWiaMiniDrvCallBack COM Interface
description: IWiaMiniDrvCallBack COM Interface
ms.assetid: a535d718-e34f-4cd0-9137-83d28d0b8e9c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IWiaMiniDrvCallBack COM Interface





The [IWiaMiniDrvCallBack Interface](https://msdn.microsoft.com/library/windows/hardware/ff543943) provides one link in a communication chain between a minidriver and an application. Because a minidriver cannot communicate directly with an application, and vice versa, any communication between the two must go through an intermediary: the WIA service. To enable this communication, the application implements the **IWiaDataCallback** interface (described in the Microsoft Windows SDK documentation). This interface includes the **IWiaDataCallback::BandedDataCallback** method, which the WIA service can call. If an application provides this callback routine, the WIA service creates another callback, the [**IWiaMiniDrvCallBack::MiniDrvCallback**](https://msdn.microsoft.com/library/windows/hardware/ff543946) method, which it provides for use by the minidriver.

When the minidriver is ready to send image data from the imaging device or to transfer status messages (the percentage of data transferred, for example), it calls the WIA service's **IWiaMiniDrvCallBack**::**MiniDrvCallback**. The WIA service then passes the data or messages along to the application when it calls the application's callback.

 

 




