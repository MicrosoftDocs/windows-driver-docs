---
title: Code Example for Challenging a Potentially Disconnected Device
author: windows-driver-content
description: Code Example for Challenging a Potentially Disconnected Device
MS-HAID:
- 'WIA\_wsd\_scan\_86c08f57-176b-4929-8b45-9e0fb2b194ab.xml'
- 'image.code\_example\_for\_challenging\_a\_potentially\_disconnected\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 74633481-229f-4074-a84e-cc515eaaacd0
---

# Code Example for Challenging a Potentially Disconnected Device


The following code example shows a call to the **RegisterDeviceToChallenge** function (which is listed in the code example in [Sample Code for Implementing Helper Methods](code-example-for-implementing-helper-methods.md)) to challenge a potentially disconnected device.

```
HRESULT hr = S_OK;

if (SUCCEEDED(hr))
{
    //
    // Activate ScanProxy to retrieve the IScanService interface for it
    //
    hr = m_pFunctionInstance->QueryService(__uuidof(WSDScanProxy),
                                           __uuidof(IScanService),
                                           (void**) &m_pScanProxy);
    if (FAILED(hr))
    {
        WIAS_ERROR((g_hInst, "IFunctionInstance::QueryService(WSDScanProxy, IScanService) failed, cannot activate ScanProxy, hr = 0x%08X", hr));
 
        if (WSD_COMMUNICATION_ERROR(hr))
        {
            RegisterDeviceToChallenge();
        }
    }
}

if (SUCCEEDED(hr))
{
    //
    // Retrieve the IScanServiceEvents interface from the ScanProxy
    //
    hr = m_pScanProxy->QueryInterface(__uuidof(IScanServiceEvents), (void**)&m_pScanEvents);
    if (FAILED(hr))
    {
        WIAS_ERROR((g_hInst, "IScanService::QueryInterface(IScanServiceEvents) failed, hr = 0x%08X", hr));
 
        if (WSD_COMMUNICATION_ERROR(hr))
        {
            RegisterDeviceToChallenge();
        }
    }
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Code%20Example%20for%20Challenging%20a%20Potentially%20Disconnected%20Device%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


