---
Description: Fixed Property-Attribute Retrieval
title: Fixed Property-Attribute Retrieval
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Fixed Property-Attribute Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetFixedPropertyAttributes** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetFixedPropertyAttributes** method in the sample driver. The latter method creates an **IPortableDeviceValues** object into which the driver stores the requested attributes.

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetFixedPropertyAttributes(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT     hr               = S_OK;
    GUID        guidObjectFormat = GUID_NULL;
    PROPERTYKEY key              = WPD_PROPERTY_NULL;
    CComPtr<IPortableDeviceValues> pAttributes;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the object format whose fixed property attributes have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_FORMAT, &guidObjectFormat);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_FORMAT");
    }

    // Get the property whose fixed property attributes have been requested
    if(hr == S_OK)
    {
        hr = pParams->GetKeyValue(WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS, &key);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_PROPERTY_KEYS");
    }

    // CoCreate a collection to store the fixed property attributes.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pAttributes);
        CHECK_HR(hr, "Failed to CoCreateInstance CLSID_PortableDeviceValues");
    }

    // Add the fixed property attributes for the specified object format and property
    if (hr == S_OK)
    {
        hr = GetFixedPropertyAttributesForFormat(guidObjectFormat, key, pAttributes);
        CHECK_HR(hr, "Failed to get fixed property attributes");
    }

    // Set the WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIPortableDeviceValuesValue(WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES, pAttributes);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_PROPERTY_ATTRIBUTES");
    }

    return hr;
}
```

 

 




