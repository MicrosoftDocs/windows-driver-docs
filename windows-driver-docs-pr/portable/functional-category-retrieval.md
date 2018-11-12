---
Description: Functional-Category Retrieval
title: Functional-Category Retrieval
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Functional-Category Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetFunctionalCategories** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetFunctionalCategories** method in the sample driver. The method creates an **IPortableDevicePropVariantCollection** object into which the driver stores the two supported categories (WPD\_FUNCTIONAL\_CATEGORY\_DEVICE and WPD\_FUNCTIONAL\_CATEGORY\_STORAGE).

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetFunctionalCategories(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr = S_OK;
    CComPtr<IPortableDevicePropVariantCollection> pFunctionalCategories;

    UNREFERENCED_PARAMETER(pParams);

    // CoCreate a collection to store the supported functional categories.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pFunctionalCategories);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Add the supported functional categories to the collection.
    if (hr == S_OK)
    {
        for (DWORD dwIndex = 0; dwIndex < ARRAYSIZE(g_SupportedFunctionalCategories); dwIndex++)
        {
            PROPVARIANT pv = {0};
            PropVariantInit(&pv);
            // Don&#39;t call PropVariantClear, since we did not allocate the memory for these GUIDs

            pv.vt    = VT_CLSID;
            pv.puuid = (GUID*) &g_SupportedFunctionalCategories[dwIndex];

            hr = pFunctionalCategories->Add(&pv);
            CHECK_HR(hr, "Failed to add supported functional category at index %d", dwIndex);
            if (FAILED(hr))
            {
                break;
            }
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES, pFunctionalCategories);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORIES");
    }

    return hr;
}
```

 

 




