---
Description: Reading Resource Data
MS-HAID: 'wpddk.reading\_resource\_data'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Reading Resource Data
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Reading%20Resource%20Data%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



