---
Description: Setting Property Values
MS-HAID: 'wpddk.setting\_property\_values'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Setting Property Values
---

# Setting Property Values


When a WPD application calls the **IPortableDeviceProperties::SetValues** method, this method, in turn, triggers a call to the **WpdObjectProperties::OnSetPropertyValues** method in the sample driver. This method creates an **IPortableDeviceValues** object into which the new values are written. However, because the sample driver does not allow updates to any of its properties, this method writes E\_ACCESSDENIED to each entry in the **IPortableDeviceValues** object.

```ManagedCPlusPlus
HRESULT WpdObjectProperties::OnSetPropertyValues(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr          = S_OK;
    LPWSTR  wszObjectID = NULL;
    DWORD   cValues     = 0;
    CComPtr<IPortableDeviceValues> pValues;
    CComPtr<IPortableDeviceValues> pWriteResults;
    CComPtr<IPortableDeviceValues> pEventParams;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the object identifier whose property values are being set
    if (hr == S_OK)
    {
        hr = pParams->GetStringValue(WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID, &wszObjectID);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_PROPERTIES_OBJECT_ID");
    }

    // Get the caller-supplied property values requested to be set on the object
    if (hr == S_OK)
    {
        hr = pParams->GetIPortableDeviceValuesValue(WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES, &pValues);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_VALUES");
    }

    // CoCreate a collection to store the property set operation results.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pWriteResults);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDeviceValues");
    }

    // Set the property values on the specified object
    if (hr == S_OK)
    {
        // Since this driver does not support setting any properties, all property set operation
        // results will be set to E_ACCESSDENIED.
        if (hr == S_OK)
        {
            hr = pValues->GetCount(&cValues);
            CHECK_HR(hr, "Failed to get total number of values");
        }

        if (hr == S_OK)
        {
            for (DWORD dwIndex = 0; dwIndex < cValues; dwIndex++)
            {
                PROPERTYKEY Key = WPD_PROPERTY_NULL;
                hr = pValues->GetAt(dwIndex, &Key, NULL);
                CHECK_HR(hr, "Failed to get PROPERTYKEY at index %d", dwIndex);

                if (hr == S_OK)
                {
                    hr = pWriteResults->SetErrorValue(Key, E_ACCESSDENIED);
                    CHECK_HR(hr, "Failed to set error result value at index %d", dwIndex);
                }
            }
        }

        // Since we have set failures for the property set operations we must let the application
        // know by returning S_FALSE. This will instruct the application to look at the
        // property set operation results for failure values.
        if (hr == S_OK)
        {
            hr = S_FALSE;
        }
    }

    if (SUCCEEDED(hr))
    {
        // Set the WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS value in the results
        HRESULT hrTemp = pResults->SetIPortableDeviceValuesValue(WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS, pWriteResults);
        CHECK_HR(hrTemp, ("Failed to set WPD_PROPERTY_OBJECT_PROPERTIES_PROPERTY_WRITE_RESULTS"));

        if (FAILED(hrTemp))
        {
            hr = hrTemp;
        }
    }

    // Free the memory.  CoTaskMemFree ignores NULLs so no need to check.
    CoTaskMemFree(wszObjectID);

    return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Setting%20Property%20Values%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



