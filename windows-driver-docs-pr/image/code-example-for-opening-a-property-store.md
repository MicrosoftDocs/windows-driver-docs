---
title: Code Example for Opening a Property Store
author: windows-driver-content
description: Code Example for Opening a Property Store
MS-HAID:
- 'WIA\_wsd\_scan\_c59cb22d-0665-495b-ba0d-64ac31000f81.xml'
- 'image.code\_example\_for\_opening\_a\_property\_store'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4d63ea52-f3f5-4af7-ad6f-0bbd57b76c52
---

# Code Example for Opening a Property Store


The following code example shows how to open a Property Store for the current Function Instance object. The procedure for obtaining the current Function Instance object is described in [Obtaining a Function Instance Object](obtaining-a-function-instance-object.md).

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Code%20Example%20for%20Opening%20a%20Property%20Store%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


