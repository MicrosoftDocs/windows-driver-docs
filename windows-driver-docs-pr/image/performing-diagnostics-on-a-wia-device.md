---
title: Performing Diagnostics on a WIA Device
author: windows-driver-content
description: Performing Diagnostics on a WIA Device
MS-HAID:
- 'WIA\_drv\_basic\_e3b9e8a1-4878-450c-8bd3-46812f69d8e3.xml'
- 'image.performing\_diagnostics\_on\_a\_wia\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 15962c49-f03c-409b-b138-033893a50ec2
---

# Performing Diagnostics on a WIA Device


## <a href="" id="ddk-performing-diagnostics-on-a-wia-device-si"></a>


The WIA service can test a device's functionality status by calling the [**IStiUSD::Diagnostic**](https://msdn.microsoft.com/library/windows/hardware/ff543814) method. The WIA minidriver should check the hardware's current functional state and report the results. The **IStiUSD::Diagnostic** method is also called when the "Test Device" button is pressed on the WIA device's default property page (the Microsoft-provided property page).

The following example shows an implementation of the **IStiUSD::Diagnostic** method.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Performing%20Diagnostics%20on%20a%20WIA%20Device%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


