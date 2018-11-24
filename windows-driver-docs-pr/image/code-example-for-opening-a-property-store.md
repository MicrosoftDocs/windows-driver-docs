---
title: Code Example for Opening a Property Store
description: Code Example for Opening a Property Store
ms.assetid: 4d63ea52-f3f5-4af7-ad6f-0bbd57b76c52
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code Example for Opening a Property Store


The following code example shows how to open a Property Store for the current Function Instance object. The procedure for obtaining the current Function Instance object is described in [Obtaining a Function Instance Object](obtaining-a-function-instance-object.md).

```cpp
/**************************************************************************\
* CWSDDevice::OpenPropertyStore
*
* Opens the Property Store that is associated with the current Function Instance. 
*
* Arguments:
*
*    pPropertyStore - returns the IPropertyStore interface. The caller must
*                     release it by calling IPropertyStore::Release
* Return Value:
*
*     S_OK if operation is successful, an error HRESULT otherwise
*
\**************************************************************************/

HRESULT
CWSDDevice::OpenPropertyStore(
    __out IPropertyStore **ppPropertyStore)
{
    HRESULT hr = S_OK;

    if (!ppPropertyStore)
    {
        hr = E_INVALIDARG;
        WIAS_ERROR((g_hInst, "Invalid argument, hr = 0x%08X", hr));
    }

    if (!m_pFunctionInstance)
    {
        hr = E_UNEXPECTED;
        WIAS_ERROR((g_hInst, "Communication interface not initialized, hr = 0x%08X", hr));
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pFunctionInstance->OpenPropertyStore(STGM_READ, ppPropertyStore);
        if ((SUCCEEDED(hr)) && (!(*ppPropertyStore)))
        {
            hr = E_POINTER;
            WIAS_ERROR((g_hInst, 
                "IFunctionInstance::OpenPropertyStore returned hr = 0x%08X with a NULL property store interface, hr = 0x%08X", hr));
        }
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "IFunctionInstance::OpenPropertyStore failed, hr = 0x%08X", hr));
        }
    }

    return hr;
}
```

 

 




