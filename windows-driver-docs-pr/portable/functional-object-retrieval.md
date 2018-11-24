---
Description: Functional-Object Retrieval
title: Functional-Object Retrieval
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Functional-Object Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetFunctionalObjects** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetFunctionalObjects** method in the sample driver. The latter method creates an **IPortableDevicePropVariantCollection** object into which the driver stores the requested functional objects. In the case of the sample driver, only two object types are supported: WPD\_DEVICE\_OBJECT\_ID or STORAGE\_OBJECT\_ID. Depending on the requested functional category, this method can return either one or both of these types.

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetFunctionalObjects(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr                     = S_OK;
    GUID    guidFunctionalCategory = GUID_NULL;
    CComPtr<IPortableDevicePropVariantCollection> pFunctionalObjects;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the functional category whose functional object identifiers have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY, &guidFunctionalCategory);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY");
    }

    // CoCreate a collection to store the supported functional object identifiers.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pFunctionalObjects);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Add the supported functional object identifiers for the specified functional
    // category to the collection.
    if (hr == S_OK)
    {
        PROPVARIANT pv = {0};
        PropVariantInit(&pv);
        // Don&#39;t call PropVariantClear, since we did not allocate the memory for these object identifiers

        // Add WPD_DEVICE_OBJECT_ID to the functional object identifiers collection
        if (hr == S_OK)
        {
            if ((guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_DEVICE) ||
                (guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_ALL))
            {
                pv.vt       = VT_LPWSTR;
                pv.pwszVal  = WPD_DEVICE_OBJECT_ID;
                hr = pFunctionalObjects->Add(&pv);
                CHECK_HR(hr, "Failed to add device object ID");
            }
        }

        // Add STORAGE_OBJECT_ID to the functional object identifiers collection
        if (hr == S_OK)
        {
            if ((guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_STORAGE) ||
                (guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_ALL))
            {
                pv.vt       = VT_LPWSTR;
                pv.pwszVal  = STORAGE_OBJECT_ID;
                hr = pFunctionalObjects->Add(&pv);
                CHECK_HR(hr, "Failed to add storage object ID");
            }
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS, pFunctionalObjects);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS");
    }

    return hr;
}
```

 

 




