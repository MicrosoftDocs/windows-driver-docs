---
title: IWiaMiniDrvCallBack COM Interface
description: IWiaMiniDrvCallBack COM Interface
ms.date: 04/20/2017
---

# IWiaMiniDrvCallBack COM Interface





The [IWiaMiniDrvCallBack Interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrvcallback) provides one link in a communication chain between a minidriver and an application. Because a minidriver cannot communicate directly with an application, and vice versa, any communication between the two must go through an intermediary: the WIA service. To enable this communication, the application implements the **IWiaDataCallback** interface (described in the Microsoft Windows SDK documentation). This interface includes the **IWiaDataCallback::BandedDataCallback** method, which the WIA service can call. If an application provides this callback routine, the WIA service creates another callback, the [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback) method, which it provides for use by the minidriver.

When the minidriver is ready to send image data from the imaging device or to transfer status messages (the percentage of data transferred, for example), it calls the WIA service's **IWiaMiniDrvCallBack**::**MiniDrvCallback**. The WIA service then passes the data or messages along to the application when it calls the application's callback.

 

