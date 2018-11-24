---
title: WIA Error Handler Return Values
description: WIA Error Handler Return Values
ms.assetid: 9b8efcd7-e767-4344-b3a1-96b1898e102f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Error Handler Return Values


All error handlers must adhere to a number of rules regarding their return value.

The following are all the valid return values:

<a href="" id="s-ok"></a>S\_OK  
Device status code was successfully handled. No more error handlers will be invoked.

In case of an error status code (modal dialog), this means that appropriate action was taken to correct the error such as a paper jam for an ADF.

In case of an informational status code, this only means that the appropriate action was taken to provide the user with a modeless dialog and that the device message should not be forwarded to any other error handlers down the line.

<a href="" id="wia-status-not-handled"></a>WIA\_STATUS\_NOT\_HANDLED  
No action was taken to handle the error or report status to the user. Next handler (if any) in the list will be invoked.

This should be the default return value from the error handler.

<a href="" id="s-false"></a>S\_FALSE  
The user canceled the transfer from the handler's modeless dialog. This return value can be returned at any point by the error handler no matter what the device status code is (handled, unhandled, error, or informational).

<a href="" id="other-error-codes"></a>Other Error Codes  
If a device error cannot be recovered from, or if the user chooses to stop the transfer in response to the displayed modal dialog box, the error handler should return the device status code itself (see examples in Examples section). This of course implies that the error handler does handle the device status code.

Additionally, an error handler must be consistent in handling device status codes. That is, an instance of the error handler cannot choose to handle status code WIA\_STATUS\_XYZ (or WIA\_ERROR\_XYZ) at time t0 and then decide not to handle it at time t1.

The following code is an example of an invalid error handler:

```cpp
STDMETHODIMP
CErrHandler::ReportStatus(
    IN  LONG        lFlags,
    IN  HWND        hwndParent,
    IN  IWiaItem2   *pWiaItem2,
    IN  HRESULT     hrStatus,
    IN  LONG        lPercentComplete)
{
    HRESULT hr = WIA_STATUS_NOT_HANDLED;
    if ((hrStatus == WIA_ERROR_PAPER_JAM) && HandleMessageNow())
    {
        ...
    }
    return hr;
}
```

Removing the *HandleMessageNow* routine would make this a valid error handler.

 

 




