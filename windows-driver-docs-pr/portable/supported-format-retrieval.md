---
Description: Supported Format Retrieval
title: Supported Format Retrieval
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supported Format Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetSupportedFormats** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetSupportedFormats** method in the sample driver. The latter method creates an **IPortableDevicePropVariantCollection** object into which the driver stores the formats supported for a given content type.

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetSupportedFormats(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr              = S_OK;
    GUID    guidContentType = GUID_NULL;
    CComPtr<IPortableDevicePropVariantCollection> pFormats;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the content type whose supported formats have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE, &guidContentType);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE");
    }

    // CoCreate a collection to store the supported formats.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pFormats);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Add the supported formats for the specified content type to the collection.
    if (hr == S_OK)
    {
        PROPVARIANT pv = {0};
        PropVariantInit(&pv);
        // Don&#39;t call PropVariantClear, since we did not allocate the memory for these GUIDs

        if ((guidContentType   == WPD_CONTENT_TYPE_DOCUMENT) ||
            ((guidContentType  == WPD_CONTENT_TYPE_ALL)))
        {
            // Add WPD_OBJECT_FORMAT_TEXT to the supported formats collection
            pv.vt    = VT_CLSID;
            pv.puuid = (CLSID*)&WPD_OBJECT_FORMAT_TEXT;
            hr = pFormats->Add(&pv);
            CHECK_HR(hr, "Failed to add WPD_OBJECT_FORMAT_TEXT");
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_FORMATS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_FORMATS, pFormats);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_FORMATS");
    }

    return hr;
}
```

 

 




