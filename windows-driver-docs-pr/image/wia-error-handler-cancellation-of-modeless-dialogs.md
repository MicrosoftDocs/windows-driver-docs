---
title: WIA Error Handler Cancellation of Modeless Dialogs
description: WIA Error Handler Cancellation of Modeless Dialogs
ms.assetid: eca6c3a3-c196-4d28-925a-c8f5d5d8601b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Error Handler Cancellation of Modeless Dialogs


Much of the complexity in the error handler revolves around how cancellation and dismissal of modeless dialog boxes are handled.

In particular, the WIA proxy code ensures that a lower-level error handler (in other words a handler other than that application's error handler) gets the chance to communicate a cancel request back from a modeless dialog to the driver; this ensures that a lower level handler gets a chance to dismiss its modeless dialog box.

In order to allow an error handler to cancel a data transfer operation from a modeless dialog, a driver should keep sending WIA\_TRANSFER\_MSG\_DEVICE\_STATUS messages with the same *hrErrorStatus* code, possibly updating the *lPercentComplete* parameter to allow an error handler UI to show progress. For example, if a driver can give an estimate of how long "warming up" really takes, it can send a number of device messages with *hrErrorStatus* set to WIA\_STATUS\_WARMING\_UP. This will allow the error handler to show a progress dialog as well as giving the user a chance to cancel the transfer from this dialog box. The *lPercentComplete* parameter passed into [**IWiaErrorHandler::ReportStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543909) is the exact same *lPercentComplete* parameter that the driver sets in the **IWiaTransferCallback::WiaTransferParams** method. For an example of this, see the Extended WIA Monster Driver on the WDK CD.

To allow an error handler to dismiss a modeless dialog, Microsoft introduced the device status code WIA\_STATUS\_CLEAR. This message is sent by the WIA proxy to the error handler that is currently displaying a modeless UI when the WIA proxy receives a different device message from the one that is currently being displayed. The proxy also sends the WIA\_STATUS\_CLEAR message when:

The driver sends out the WIA\_TRANSFER\_MESSAGE\_STATUS message,

during calls to the **IWiaTransferCallback::GetNextStream** method

at the end of stream/transfer (if there is currently an error handler displaying a modeless UI).

Drivers should not send the WIA\_STATUS\_CLEAR message themselves.

The **IWiaTransferCallback** interface is described in the Microsoft Windows SDK documentation.

 

 




