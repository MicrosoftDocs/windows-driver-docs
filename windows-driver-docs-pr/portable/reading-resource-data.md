---
Description: Reading Resource Data
title: Reading Resource Data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading Resource Data


After an application has retrieved an **IStream** object, it can perform the required read or write operations by using the **IStream::Read** or **IStream::Write** methods. (In the case of the sample driver, only read operations are supported). When the application calls the **IStream::Read** method, this method, in turn, triggers a call to the device driver's **WpdObjectResources::OnReadResource** method, which performs the actual read operation.

The **WpdObjectResources::OnReadResource** method reads the requested number of bytes into the destination buffer and then updates the resource context with the count of bytes that were transferred.

```ManagedCPlusPlus
HRESULT WpdObjectResources::OnReadResource(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT                   hr                 = S_OK;
    LPWSTR                    wszResourceContext = NULL;
    DWORD                     dwNumBytesToRead   = 0;
    DWORD                     dwNumBytesRead     = 0;
    BYTE*                     pBuffer            = NULL;
    DWORD                     cbBuffer           = 0;
    WpdObjectResourceContext* pResourceContext   = NULL;
    ContextMap*               pContextMap        = NULL;

    // Get the enumeration context identifier for this enumeration operation.  We will
    // need this to look up the specific enumeration context in the client context map.
    hr = pParams->GetStringValue(WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT, &wszResourceContext);
    if (hr != S_OK)
    {
        hr = E_INVALIDARG;
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT");
    }

    // Get the number of bytes to read
    if (hr == S_OK)
    {
        hr = pParams->GetUnsignedIntegerValue(WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ, &dwNumBytesToRead);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_TO_READ");
    }

    // Get the destination buffer
    if (hr == S_OK)
    {
        hr = pParams->GetBufferValue(WPD_PROPERTY_OBJECT_RESOURCES_DATA, &pBuffer, &cbBuffer);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_DATA");
    }

    // Get the client context map so we can retrieve the resource context for this resource
    // operation using the WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT property value obtained above.
    if (hr == S_OK)
    {
        hr = pParams->GetIUnknownValue(PRIVATE_SAMPLE_DRIVER_CLIENT_CONTEXT_MAP, (IUnknown**)&pContextMap);
        CHECK_HR(hr, "Failed to get PRIVATE_SAMPLE_DRIVER_CLIENT_CONTEXT_MAP");
    }

    if (hr == S_OK)
    {
        pResourceContext = (WpdObjectResourceContext*)pContextMap->GetContext(wszResourceContext);
        if (pResourceContext == NULL)
        {
            hr = E_INVALIDARG;
            CHECK_HR(hr, "Missing resource context");
        }
    }

    // Read the next chunk of data for this request
    if (hr == S_OK)
    {
        hr = ReadDataFromResource(pResourceContext, pBuffer, dwNumBytesToRead, &dwNumBytesRead);
        CHECK_HR(hr, "Failed to read %d bytes from resource", dwNumBytesToRead);
    }

    if (hr == S_OK)
    {
        hr = pResults->SetBufferValue(WPD_PROPERTY_OBJECT_RESOURCES_DATA, pBuffer, dwNumBytesRead);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_OBJECT_RESOURCES_DATA");
    }

    if (hr == S_OK)
    {
        hr = pResults->SetUnsignedIntegerValue(WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ, dwNumBytesRead);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_OBJECT_RESOURCES_NUM_BYTES_READ");
    }

    // Free the memory.  CoTaskMemFree ignores NULLs so no need to check.
    CoTaskMemFree(wszResourceContext);

    // Free the memory.  CoTaskMemFree ignores NULLs so no need to check.
    CoTaskMemFree(pBuffer);

    SAFE_RELEASE(pContextMap);

    return hr;
}
```

 

 




