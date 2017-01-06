---
Description: Opening a Resource and Retrieving an IStream object
MS-HAID: 'wpddk.opening\_a\_resource\_and\_retrieving\_an\_istream\_object'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Opening a Resource and Retrieving an IStream object
---

# Opening a Resource and Retrieving an IStream object


When an application has to read resource data from or write resource data to a device, it begins by calling the **IPortableDeviceResources::GetStream** method. This method retrieves an **IStream** interface that the application uses for the corresponding read and write operations. (The **IStream** interface is returned by the WPD API, not the driver.)

The call to the **IPortableDeviceResources::GetStream** method triggers a call to the **WpdObjectResources::OnOpenResource** command handler in the sample driver. This handler creates a resource context that is used by the driver for read operations. In this particular case, the resource context includes the following items:

-   The object identifier for the object that contains the resource
-   The resource PROPERTYKEY
-   A count of bytes transferred (used for read operations)
-   A size of the entire resource, in bytes

```ManagedCPlusPlus
HRESULT WpdObjectResources::OnOpenResource(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT     hr              = S_OK;
    LPWSTR      wszObjectID     = NULL;
    PROPERTYKEY Key             = WPD_PROPERTY_NULL;
    DWORD       dwMode          = STGM_READ;
    CAtlStringW strStrObjectID;
    CAtlStringW strResourceContext;
    ContextMap* pContextMap     = NULL;

    // Get the Object identifier of the object which contains the specified resource
    hr = pParams->GetStringValue(WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID, &wszObjectID);
    if (hr != S_OK)
    {
        hr = E_INVALIDARG;
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_OBJECT_ID");
    }

    // Get the resource key
    if (hr == S_OK)
    {
        hr = pParams->GetKeyValue(WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS, &Key);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_RESOURCE_KEYS");
    }

    // Get the access mode
    if (hr == S_OK)
    {
        hr = pParams->GetUnsignedIntegerValue(WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE, &dwMode);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_ACCESS_MODE");
    }

    // Validate whether the params given to us are correct.  In this case, we need to check that the object
    // supports the resource requested, and can be opened in the requested access mode.
    if (hr == S_OK)
    {
        // In this sample, we only have one object (README_FILE_OBJECT_ID) which supports a
        // resource (WPD_RESOURCE_DEFAULT) for reading only.
        // So if any other Object ID or any other resource is specified, it must be invalid.
        strStrObjectID = wszObjectID;
        if(strStrObjectID.CompareNoCase(README_FILE_OBJECT_ID) != 0)
        {
            hr = E_INVALIDARG;
            CHECK_HR(hr, "Object [%ws] does not support resources", wszObjectID);
        }
        if (hr == S_OK)
        {
            if (!IsEqualPropertyKey(Key, WPD_RESOURCE_DEFAULT))
            {
                hr = E_INVALIDARG;
                CHECK_HR(hr, "Only WPD_RESOURCE_DEFAULT is supported in this sample driver");
            }
        }
        if (hr == S_OK)
        {
            if ((dwMode & STGM_WRITE) != 0)
            {
                hr = E_ACCESSDENIED;
                CHECK_HR(hr, "This resource is not available for write access");
            }
        }
    }

    // Get the context map which the driver stored in pParams for convenience
    if (hr == S_OK)
    {
        hr = pParams->GetIUnknownValue(PRIVATE_SAMPLE_DRIVER_CLIENT_CONTEXT_MAP, (IUnknown**)&pContextMap);
        CHECK_HR(hr, "Failed to get PRIVATE_SAMPLE_DRIVER_CLIENT_CONTEXT_MAP");
    }

    // Create a new resource operation context, initialize it, and add it to the client context map.
    if (hr == S_OK)
    {
        WpdObjectResourceContext* pResourceContext = new WpdObjectResourceContext();
        if (pResourceContext != NULL)
        {
            // Initialize the resource context with ...
            pResourceContext->m_strObjectID      = wszObjectID;
            pResourceContext->m_Resource         = Key;
            pResourceContext->m_BytesTransferred = 0;
            pResourceContext->m_BytesTotal       = GetObjectSize(wszObjectID);

            // Add the resource context to the context map
            pContextMap->Add(pResourceContext, strResourceContext);
        }
        else
        {
            hr = E_OUTOFMEMORY;
            CHECK_HR(hr, "Failed to allocate resource context");
        }
    }

    if (hr == S_OK)
    {
        hr = pResults->SetStringValue(WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT, strResourceContext);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT");
    }

    // Set the optimal buffer size
    if (hr == S_OK)
    {
        hr = pResults->SetUnsignedIntegerValue(WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE, FILE_OPTIMAL_READ_BUFFER_SIZE_VALUE);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_OBJECT_RESOURCES_OPTIMAL_TRANSFER_BUFFER_SIZE value");
    }

    // Free the memory.  CoTaskMemFree ignores NULLs so no need to check.
    CoTaskMemFree(wszObjectID);

    SAFE_RELEASE(pContextMap);

    return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Opening%20a%20Resource%20and%20Retrieving%20an%20IStream%20object%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



