---
Description: Supported Content-Type Retrieval
title: Supported Content-Type Retrieval
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supported Content-Type Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetSupportedContentTypes** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetSupportedContentTypes** method in the sample driver. The latter method creates an **IPortableDevicePropVariantCollection** object into which the driver stores the content types that it supports for the specified functional category. (If the driver does not support content types for a given functional category, it returns an empty collection.)

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetSupportedContentTypes(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr                     = S_OK;
    GUID    guidFunctionalCategory = GUID_NULL;
    CComPtr<IPortableDevicePropVariantCollection> pContentTypes;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the functional category whose supported content types have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY, &guidFunctionalCategory);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY");
    }

    // CoCreate a collection to store the supported content types.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pContentTypes);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Add the supported content types for the specified functional
    // category to the collection.
    if (hr == S_OK)
    {
        PROPVARIANT pv = {0};
        PropVariantInit(&pv);
        // Don&#39;t call PropVariantClear, since we did not allocate the memory for these GUIDs

        // Add supported content types for known functional categories
        if (guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_STORAGE)
        {
            // Add WPD_CONTENT_TYPE_DOCUMENT to the supported content type collection
            pv.vt    = VT_CLSID;
            pv.puuid = (CLSID*)&WPD_CONTENT_TYPE_DOCUMENT;
            hr = pContentTypes->Add(&pv);
            CHECK_HR(hr, "Failed to add WPD_CONTENT_TYPE_DOCUMENT");

            if (hr == S_OK)
            {
                // Add WPD_CONTENT_TYPE_FOLDER to the supported content type collection
                pv.vt    = VT_CLSID;
                pv.puuid = (CLSID*)&WPD_CONTENT_TYPE_FOLDER;
                hr = pContentTypes->Add(&pv);
                CHECK_HR(hr, "Failed to add WPD_CONTENT_TYPE_FOLDER");
            }
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES, pContentTypes);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES");
    }

    return hr;
}
```

 

 




