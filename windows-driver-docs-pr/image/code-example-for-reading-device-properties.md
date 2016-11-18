---
title: Code Example for Reading Device Properties
author: windows-driver-content
description: Code Example for Reading Device Properties
MS-HAID:
- 'WIA\_wsd\_scan\_0f336f3c-dbc6-4697-9544-00634ee4e134.xml'
- 'image.code\_example\_for\_reading\_device\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9ff3f30d-fd1c-4241-a068-1af2160e9296
---

# Code Example for Reading Device Properties


The following code example shows how to read device properties from a Property Store. For an example of how to open a Property Store for the current Function Instance object, see [Code Example for Opening a Property Store](code-example-for-opening-a-property-store.md).

```
/**************************************************************************\
* CWSDDevice::ReadDeviceProperty
*
* Reads a LPWTSR device property from the device metadata and returns 
* a copy of its value as a BSTR character string. 
*
*
* Arguments:
*
*    pPropertyStore        - IPropertyStore interface, optional
*                            (if not specified a new property store
*                            Is opened and closed for each call)
*    pPropertyKey          - property key (for example, PKEY_PNPX_FirmwareVersion)
*    pbstrPropertyValue    - Returns the property value; this valuemust be 
*                            freed by caller using SysFreeString
*
* Return Value:
*
*     S_OK if operation is successful, an error HRESULT otherwise
*
\**************************************************************************/

HRESULT
CWSDDevice::ReadDeviceProperty(
    __in_opt IPropertyStore *pPropertyStore,
    __in const PROPERTYKEY  *pPropertyKey,
    __out BSTR              *pbstrPropertyValue)
{
    HRESULT hr = S_OK;
    IPropertyStore *pThisPropertyStore = NULL;
    BOOL bClosePropertyStore = FALSE;
    PROPVARIANT propvar = {0};

    if ((!pbstrPropertyValue) || (!pPropertyKey))
    {
        hr = E_INVALIDARG;
        WIAS_ERROR((g_hInst, "Invalid argument, hr = 0x%08X", hr));
    }

    if ((!m_pFunctionInstance) || (!m_pScanProxy))
    {
        hr = E_UNEXPECTED;
        WIAS_ERROR((g_hInst, "ScanProxy not initialized, hr = 0x%08X", hr));
    }

    if (SUCCEEDED(hr))
    {
        pThisPropertyStore = pPropertyStore;
 
        if (!pThisPropertyStore)
        {
            hr = m_pFunctionInstance->OpenPropertyStore(STGM_READ, &pThisPropertyStore);
            if ((SUCCEEDED(hr)) && (!pThisPropertyStore))
            {
                hr = E_POINTER;
                WIAS_ERROR((g_hInst, 
                    "IFunctionInstance::OpenPropertyStore returned hr = 0x%08X with a NULL property store interface, hr = 0x%08X", hr));
            }
            if (FAILED(hr))
            {
                WIAS_ERROR((g_hInst, "IFunctionInstance::OpenPropertyStore failed, hr = 0x%08X", hr));
            }

            if (pThisPropertyStore)
            {
                bClosePropertyStore = TRUE;
            }
        }    
    }
 
    PropVariantInit(&propvar);

    if (SUCCEEDED (hr))
    {
        hr = pThisPropertyStore->GetValue(*pPropertyKey, &propvar);
        if (FAILED(hr))
        {
            WIAS_ERROR((g_hInst, "IPropertyStore::GetValue failed, hr = 0x%08X", hr));
        }
    }

    if ((SUCCEEDED(hr)) && (VT_EMPTY == propvar.vt))
    {
        hr = E_FAIL;
        WIAS_ERROR((g_hInst, "IPropertyStore::GetValue returned no value (VT_EMPTY), hr = 0x%08X", hr));
    }

    if ((SUCCEEDED(hr)) && (VT_LPWSTR != propvar.vt))
    {
        hr = E_UNEXPECTED;
        WIAS_ERROR((g_hInst, "IPropertyStore::GetValue returned an unexpected PROPVARIANT type, hr = 0x%08X", hr));
    }

    if (SUCCEEDED (hr))
    {
        *pbstrPropertyValue = SysAllocString(propvar.pwszVal);
        if (!(*pbstrPropertyValue))
        {
            hr = E_OUTOFMEMORY;
            WIAS_ERROR((g_hInst, 
                "Cannot make a copy of the value returned by IPropertyStore::GetValue, %ws, hr = 0x%08X", propvar.pwszVal, hr));
        }
    }

    PropVariantClear(&propvar);

    if ((bClosePropertyStore) && (pThisPropertyStore))
    {
        pThisPropertyStore->Release();
        pThisPropertyStore = NULL;
    }

    return hr;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Code%20Example%20for%20Reading%20Device%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


