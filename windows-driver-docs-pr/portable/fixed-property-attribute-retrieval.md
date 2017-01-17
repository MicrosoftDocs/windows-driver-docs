---
Description: 'Fixed Property-Attribute Retrieval'
MS-HAID: 'wpddk.fixed\_property\_attribute\_retrieval'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Fixed Property-Attribute Retrieval'
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Fixed%20Property-Attribute%20Retrieval%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



