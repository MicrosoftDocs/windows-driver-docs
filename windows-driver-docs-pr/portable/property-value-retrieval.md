---
Description: 'Property-Value Retrieval'
MS-HAID: 'wpddk.property\_value\_retrieval'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Property-Value Retrieval'
---

# Property-Value Retrieval


When a WPD application calls the **IPortableDeviceProperties::GetValues** method, this method, in turn, triggers a call to the either the **WpdObjectProperties::OnGetPropertyValues** or the **WpdObjectProperties::OnGetAllPropertyValues** method in the sample driver. The latter method is called if the second argument to **IPortableDeviceProperties::GetValues** is **NULL**. These methods in the sample driver create an **IPortableDeviceValues** object into which the driver stores the property values for the requested properties. The following example from the sample driver contains the code for the **WpdObjectProperties::OnGetPropertyValues** method.

```ManagedCPlusPlus
HRESULT WpdObjectProperties::OnGetPropertyValues(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr          = S_OK;
    LPWSTR  wszObjectID = NULL;
    CComPtr<IPortableDeviceValues>        pValues;
    CComPtr<IPortableDeviceKeyCollection> pKeys;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the object identifier whose property values have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetStringValue(WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID, &wszObjectID);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID");
    }

    // Get the list of property keys for the property values the caller wants to retrieve from the specified object
    if (hr == S_OK)
    {
        hr = pParams->GetIPortableDeviceKeyCollectionValue(WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS, &pKeys);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_KEYS");
    }

    // CoCreate a collection to store the property values.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pValues);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDeviceValues");
    }

    // Read the specified properties on the specified object and add the property values to the collection.
    if (hr == S_OK)
    {
        hr = GetPropertyValuesForObject(wszObjectID, pKeys, pValues);
        CHECK_HR(hr, "Failed to get property values for object &#39;%ws&#39;", wszObjectID);
    }

    // S_OK or S_FALSE can be returned from GetPropertyValuesForObject( ).
    // S_FALSE means that 1 or more property values could not be retrieved successfully.
    // The value for the specified property should be set to an error HRESULT of
    // the reason why the property could not be read.
    // (e.g. If the property being requested is not supported on the object then an error of
    // HRESULT_FROM_WIN32(ERROR_NOT_SUPPORTED) should be set as the value.
    if (SUCCEEDED(hr))
    {
        // Set the WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES value in the results.
        HRESULT hrTemp = S_OK;
        hrTemp = pResults->SetIPortableDeviceValuesValue(WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES, pValues);
        CHECK_HR(hrTemp, ("Failed to set WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES"));

        if(FAILED(hrTemp))
        {
            hr = hrTemp;
        }
    }
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Property-Value%20Retrieval%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



