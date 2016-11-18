---
title: WIA Error Handler Return Values
author: windows-driver-content
description: WIA Error Handler Return Values
MS-HAID:
- 'WIA\_error\_f07c3cd5-691c-4d2e-b965-c84be0faa11c.xml'
- 'image.wia\_error\_handler\_return\_values'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9b8efcd7-e767-4344-b3a1-96b1898e102f
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Error%20Handler%20Return%20Values%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


