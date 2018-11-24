---
Description: Opening a Resource and Retrieving an IStream object
title: Opening a Resource and Retrieving an IStream object
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




