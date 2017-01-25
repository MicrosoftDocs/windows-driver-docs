---
Description: 'Supported Content-Type Retrieval'
MS-HAID: 'wpddk.supported\_content\_type\_retrieval'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Supported Content-Type Retrieval'
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supported%20Content-Type%20Retrieval%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



