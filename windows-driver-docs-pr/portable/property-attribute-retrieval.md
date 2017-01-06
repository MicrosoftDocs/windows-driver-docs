---
Description: 'Property-Attribute Retrieval'
MS-HAID: 'wpddk.property\_attribute\_retrieval'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Property-Attribute Retrieval'
---

# Property-Attribute Retrieval


When a WPD application calls the **IPortableDeviceProperties::GetPropertyAttributes** method, this method, in turn, triggers a call to the **WpdObjectProperties::OnGetPropertyAttributes** method in the sample driver. The latter method creates an **IPortableDeviceValues** object into which the driver stores the attributes for the given property.

```ManagedCPlusPlus
HRESULT WpdObjectProperties::OnGetPropertyAttributes(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT     hr          = S_OK;
    LPWSTR      wszObjectID = NULL;
    PROPERTYKEY Key         = WPD_PROPERTY_NULL;
    CComPtr<IPortableDeviceValues>  pAttributes;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the object identifier whose property attributes have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetStringValue(WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID, &wszObjectID);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID");
    }

    // Get the list of property keys whose attributes are being requested
    if (hr == S_OK)
    {
        hr = pParams->GetKeyValue(WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS, &Key);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS");
    }

    // CoCreate a collection to store the property attributes.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pAttributes);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDeviceValues");
    }

    // Get the attributes for the specified properties on the specified object and add them
    // to the collection.
    if (hr == S_OK)
    {
        hr = GetPropertyAttributesForObject(wszObjectID, Key, pAttributes);
        CHECK_HR(hr, "Failed to get property attributes");
    }

    if (SUCCEEDED(hr))
    {
        // Set the WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES value in the results
        HRESULT hrTemp = S_OK;
        hrTemp = pResults->SetIPortableDeviceValuesValue(WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES, pAttributes);
        CHECK_HR(hrTemp, ("Failed to set WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_ATTRIBUTES"));

        if(FAILED(hrTemp))
        {
            hr = hrTemp;
        }
    }

    // Free the memory.  CoTaskMemFree ignores NULLs so no need to check.
    CoTaskMemFree(wszObjectID);

    return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Property-Attribute%20Retrieval%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



