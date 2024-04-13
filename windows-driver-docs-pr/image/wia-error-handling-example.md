---
title: WIA Error Handling Example
description: WIA Error Handling Example
ms.date: 05/29/2020
---

# WIA Error Handling Example

For an example of a driver that sends device status messages, please see the *Extended WIA 2.0 Monster Driver* sample in the [Windows Image Acquisition (WIA) Driver Samples](/samples/microsoft/windows-driver-samples/windows-image-acquisition-wia-driver-samples). The sample illustrates how a simple error handler can be implemented.

## Example: Error Handling Extension

The following code snippet shows how a simple error handing extension can be implemented. This error handling extension only handles the WIA\_ERROR\_COVER\_OPEN device status error and shows a modal dialog box. Note that some of the code has been omitted to simplify this example.

```cpp
STDMETHODIMP

CErrHandler::ReportStatus(

IN LONG lFlags,

IN HWND hwndParent,

IN IWiaItem2 *pWiaItem2,

IN HRESULT hrStatus,

IN LONG lPercentComplete)

{

    HRESULT hr = WIA_STATUS_NOT_HANDLED;

    if (WIA_ERROR_COVER_OPEN == hrStatus)

    {

        int i;

        i = MessageBox(hwndParent,

        ERROR_COVER_OPEN_STR,

        TEXT("Driver UI Extension"),

        MB_RETRYCANCEL|MB_TASKMODAL|MB_ICONERROR);

        if (IDOK == i)

        {

            hr = S_OK;

        }

        else

        {

            hr = WIA_ERROR_COVER_OPEN;

        }

    }

    return hr;

}

STDMETHODIMP

CErrHandler::GetStatusDescription(

IN LONG lFlags,

IN IWiaItem2 *pWiaItem2,

IN HRESULT hrStatus,

OUT BSTR *pbstrDescription)

{

    HRESULT hr = pbstrDescription ? WIA_STATUS_NOT_HANDLED :

    E_INVALIDARG;

    if (WIA_ERROR_COVER_OPEN == hrStatus)

    {

        BSTR bstrDescription = NULL;

        bstrDescription = SysAllocString(ERROR_COVER_OPEN_STR);

        if (bstrDescription)

        {

            *pbstrDescription = bstrDescription;

            hr = S_OK;

        }

        else

        {

            hr = E_OUTOFMEMORY;

        }

    }

    return hr;

}
```
