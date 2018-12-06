---
Description: Closing a Resource
title: Closing a Resource
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closing a Resource


After an application has completed a read or write operation by using the given **IStream** object, it closes the stream by calling **IStream::Release** or **IStream::Commit** (to save changes for resource write requests). The close request at the application level triggers the **WpdObjectResources::OnCloseResource** method for the driver.

The primary job of the **WpdObjectResources::OnCloseResource** method is to remove the resource context data from the client context map and free any associated memory.

```ManagedCPlusPlus
HRESULT WpdObjectResources::OnCloseResource(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT     hr                 = S_OK;
    LPWSTR      wszResourceContext = NULL;
    ContextMap* pContextMap        = NULL;

    UNREFERENCED_PARAMETER(pResults);

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the resource context identifier for this resource operation.  We will
    // need this to look up the specific resource context in the client context map.
    hr = pParams->GetStringValue(WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT, &wszResourceContext);
    if (hr != S_OK)
    {
        hr = E_INVALIDARG;
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT");
    }

    // Get the client context map so we can retrieve the resource context for this resource
    // operation by using the WPD_PROPERTY_OBJECT_RESOURCES_CONTEXT property value obtained previously.
    if (hr == S_OK)
    {
        hr = pParams->GetIUnknownValue(PRIVATE_SAMPLE_DRIVER_CLIENT_CONTEXT_MAP, (IUnknown**)&pContextMap);
        CHECK_HR(hr, "Failed to get PRIVATE_SAMPLE_DRIVER_CLIENT_CONTEXT_MAP");
    }

    // Destroy any data, either allocated or associated, with the resource context and then remove it from the context map.
    // We no longer need to keep this context around because the resource operation has ended.
    if (hr == S_OK)
    {
        pContextMap->Remove(wszResourceContext);
    }

    // Free the memory.  CoTaskMemFree ignores NULLs so no need to check.
    CoTaskMemFree(wszResourceContext);

    SAFE_RELEASE(pContextMap);

    return hr;
}
```

 

 




