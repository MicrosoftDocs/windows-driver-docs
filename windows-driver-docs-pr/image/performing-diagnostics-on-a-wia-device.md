---
title: Performing Diagnostics on a WIA Device
description: Performing Diagnostics on a WIA Device
ms.assetid: 15962c49-f03c-409b-b138-033893a50ec2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Diagnostics on a WIA Device





The WIA service can test a device's functionality status by calling the [**IStiUSD::Diagnostic**](https://msdn.microsoft.com/library/windows/hardware/ff543814) method. The WIA minidriver should check the hardware's current functional state and report the results. The **IStiUSD::Diagnostic** method is also called when the "Test Device" button is pressed on the WIA device's default property page (the Microsoft-provided property page).

The following example shows an implementation of the **IStiUSD::Diagnostic** method.

```cpp
STDMETHODIMP CWIADevice::Diagnostic(LPSTI_DIAG pBuffer)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if(!pBuffer){
     return E_INVALIDARG;
  }

  //
  // initialize response buffer
  //

  memset(&pBuffer->sErrorInfo,0,sizeof(pBuffer->sErrorInfo));

  pBuffer->sErrorInfo.dwGenericError = NOERROR;
  pBuffer->sErrorInfo.dwVendorError  = 0;

  HRESULT hr = S_OK;
  if(!TestMyDeviceFunctionalty()) {
    pBuffer->sErrorInfo.dwGenericError = E_FAIL; // win32 generic error code
    pBuffer->sErrorInfo.dwVendorError  = 1234;   // device specific vendor error code
  }
  return hr;
}
```

 

 




