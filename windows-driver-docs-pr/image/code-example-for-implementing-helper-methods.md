---
title: Code Example for Implementing Helper Methods
author: windows-driver-content
description: Code Example for Implementing Helper Methods
MS-HAID:
- 'WIA\_wsd\_scan\_9967e57f-50cd-481c-8ead-0b40b9f1780b.xml'
- 'image.code\_example\_for\_implementing\_helper\_methods'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4f9710c2-3741-4048-9b6c-b21241b72c91
---

# Code Example for Implementing Helper Methods


The following code example shows the implementation of the helper methods that are used to initialize the WSD Challenge interface and register the device challenge.

```
/**************************************************************************\
* CWSDDevice::InitializeChallengeInterface
*
* Initializes the WSD challenge API interface
*
* Arguments:
*
*    None
*
* Return Value:
*
*    S_OK if operation is successful, an error HRESULT otherwise
*
\**************************************************************************/

HRESULT
CWSDDevice::InitializeChallengeInterface()
{
    HRESULT hr = S_OK;
    DWORD dwErr = NO_ERROR; 
    WCHAR wszDllPath[MAX_PATH + 1] = {0} ;

    //
    // Reset the previous initialization, if any
    //
    if (m_pfnRegisterDeviceToChallenge)
    {
        UnInitializeChallengeInterface();
    }

    //
    // Set up the path name for the WSD Challenge DLL
    //
    if (!GetSystemDirectory(wszDllPath, sizeof(wszDllPath) / sizeof(wszDllPath[0])))
    {
        dwErr = ::GetLastError();
        hr = HRESULT_FROM_WIN32(dwErr);
        if (SUCCEEDED(hr))
        {
            hr = E_FAIL;
        }
        WIAS_ERROR((g_hInst, "GetSystemDirectory failed (0x%08X), hr = 0x%08X", dwErr, hr));
    }
    if (SUCCEEDED(hr))
    {
        hr = StringCbCat(wszDllPath, sizeof(wszDllPath), WSDCHNGR_DLL_NAME);
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "StringCbCat(%ws, %ws) failed, hr = 0x%08X", wszDllPath, WSDCHNGR_DLL_NAME, hr));
        }
    }

    //
    // Load the WSD Challenge DLL
    //
    if (SUCCEEDED(hr))
    {
        m_hChallengeDll = LoadLibrary(wszDllPath);
        if (!m_hChallengeDll)
        {
            dwErr = ::GetLastError();
            hr = HRESULT_FROM_WIN32(dwErr);
            if (SUCCEEDED(hr))
            {
                hr = E_FAIL;
            }
            WIAS_ERROR((g_hInst, "LoadLibrary(%ws) failed (0x%08X), hr = 0x%08X", wszDllPath, dwErr, hr));
        }
    }

    //
    // Find the WSDCHNGRInitialize API
    //
    if (SUCCEEDED(hr))
    {
        m_pfnInitializeChallenge = (PFN_WSDCHNR_INITIALIZE)GetProcAddress(m_hChallengeDll, WSDCHNR_INITIALIZE);
        if (!m_pfnInitializeChallenge)
        {
            dwErr = ::GetLastError();
            hr = HRESULT_FROM_WIN32(dwErr);
            if (SUCCEEDED(hr))
            {
                hr = E_FAIL;
            }
            WIAS_ERROR((g_hInst, "GetProcAddress(%s) failed (0x%08X), hr = 0x%08X", WSDCHNR_INITIALIZE, dwErr, hr));
        }
    }

    //
    // Find the WSDCHNGRShutdown API
    //
    if (SUCCEEDED(hr))
    {
        m_pfnShutdownChallenge = (PFN_WSDCHNR_SHUTDOWN)GetProcAddress(m_hChallengeDll, WSDCHNR_SHUTDOWN);
        if (!m_pfnShutdownChallenge)
        {
            dwErr = ::GetLastError();
            hr = HRESULT_FROM_WIN32(dwErr);
            if (SUCCEEDED(hr))
            {
                hr = E_FAIL;
            }
            WIAS_ERROR((g_hInst, "GetProcAddress(%s) failed (0x%08X), hr = 0x%08X", WSDCHNR_SHUTDOWN, dwErr, hr));
        }
    }

    //
    // Find the WSDCHNGRRegisterDeviceToChallenge API
    //
    if (SUCCEEDED(hr))
    {
        m_pfnRegisterDeviceToChallenge = (PFN_WSDCHNR_REGISTER_DEVICE_TO_CHALLENGE)
            GetProcAddress(m_hChallengeDll, WSDCHNR_REGISTER_DEVICE_TO_CHALLENGE);

        if (!m_pfnRegisterDeviceToChallenge)
        {
            dwErr = ::GetLastError();
            hr = HRESULT_FROM_WIN32(dwErr);
            if (SUCCEEDED(hr))
            {
                hr = E_FAIL;
            }
            WIAS_ERROR((g_hInst, "GetProcAddress(%s) failed (0x%08X), hr = 0x%08X", WSDCHNR_REGISTER_DEVICE_TO_CHALLENGE, dwErr, hr));
        }
    }
 
    //
    // Call WSDCHNGRInitialize
    // 
    if (SUCCEEDED(hr))
    {
        hr = (*m_pfnInitializeChallenge)();
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "WSDCHNGRInitialize failed, hr = 0x%08X", hr));
        }
    }

    if (FAILED(hr))
    {
        UnInitializeChallengeInterface();
    }

    return hr;
}

/**************************************************************************\
* CWSDDevice::UnInitializeChallengeInterface
*
* Uninitializes the WSD challenge API interface
*
* Arguments:
*
*    None
*
* Return Value:
*
*    S_OK if operation is successful, an error HRESULT otherwise
*
\**************************************************************************/

void
CWSDDevice::UnInitializeChallengeInterface()
{
    HRESULT hr = S_OK;

    if ((m_hChallengeDll) && (m_pfnShutdownChallenge))
    {
        hr = (*m_pfnShutdownChallenge)();
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "WSDCHNGRShutdown failed, hr = 0x%08X", hr));
        }
    }

    if (m_hChallengeDll)
    {
        FreeLibrary(m_hChallengeDll);
        m_hChallengeDll = NULL;

    }

    m_pfnRegisterDeviceToChallenge = NULL;
    m_pfnInitializeChallenge = NULL;
    m_pfnShutdownChallenge = NULL;

    return;
}

/**************************************************************************\
* CWSDDevice::RegisterDeviceToChallenge
*
* Registers the device to be challenged by WSDCHNGR.DLL
*
* Arguments:
*
*    None
*
* Return Value:
*
*    S_OK if operation is successful or the challenge interface is disabled, 
*    S_FALSE if the device is already registered, an error HRESULT otherwise
*
\**************************************************************************/

HRESULT
CWSDDevice::RegisterDeviceToChallenge()
{
    HRESULT hr = S_OK;
    if (!m_pFunctionInstance)
    {
        hr = E_POINTER;
        WIAS_ERROR((g_hInst, "Invalid IFunctionInstance pointer, hr = 0x%08X", hr));    
    }

    if (SUCCEEDED(hr))
    {
        if (m_pfnRegisterDeviceToChallenge)
        {
            WIAS_TRACE((g_hInst, "Registering device to challenge.."));
 
            hr = (*m_pfnRegisterDeviceToChallenge)(m_pFunctionInstance);    
            if (FAILED(hr))
            {
                WIAS_ERROR((g_hInst, "WSDCHNGRRegisterDeviceToChallenge failed, hr = 0x%08X", hr));
            }
        }
        else 
        {
            WIAS_TRACE((g_hInst, "Challenge interface disabled or not initialized, hr = 0x%08X", hr));
        }
    }

    if (S_OK == hr)
    {
        //
        // WSDCHNGRRegisterDeviceToChallenge returns S_FALSE when the device is already registered
        //
        WIAS_TRACE((g_hInst, "Device registered to challenge"));
        DoTraceMessage(WSDSCDRV_TRC, L"Device registered to challenge");
    }

    return hr;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Code%20Example%20for%20Implementing%20Helper%20Methods%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


