---
title: Code Example for Challenging a Potentially Disconnected Device
description: Code example for challenging a potentially disconnected device
ms.date: 03/28/2023
---

# Code example for challenging a potentially disconnected device

> [!IMPORTANT]
> WSD Challenger functionality has been deprecated and all WSD Challenger-related documentation will be archived to previous versions documentation.

The following code example shows a call to the **RegisterDeviceToChallenge** function (which is listed in the code example in [Sample Code for Implementing Helper Methods](code-example-for-implementing-helper-methods.md)) to challenge a potentially disconnected device.

```cpp
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
