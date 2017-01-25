---
Description: Mapping Object Identifiers
MS-HAID: 'wpddk.mapping\_object\_identifiers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Mapping Object Identifiers
---

# Mapping Object Identifiers


The mapping function, **WpdBaseDriver::OnGetObjectIDsFromPersistentUniqueIDs**, handles the mapping of object identifiers to persistent identifiers. In the WPD driver model, an object identifier is an identifier that is only valid for a given device session. A persistent identifier is valid across all device sessions.

The following excerpt from the sample driver contains the code for **WpdBaseDriver::OnGetObjectIDsFromPersistentUniqueIDs.**

```ManagedCPlusPlus
HRESULT WpdBaseDriver::OnGetObjectIDsFromPersistentUniqueIDs(
    IPortableDeviceValues* pParams,
    IPortableDeviceValues* pResults)
{

    HRESULT hr      = S_OK;
    DWORD   dwCount = 0;
    CComPtr<IPortableDevicePropVariantCollection> pPersistentIDs;
    CComPtr<IPortableDevicePropVariantCollection> pObjectIDs;

    if((pParams    == NULL) ||
       (pResults   == NULL))
    {
        hr = E_POINTER;
        CHECK_HR(hr, "Cannot have NULL parameter");
        return hr;
    }

    // Get the list of Persistent IDs
    if (hr == S_OK)
    {
        hr = pParams->GetIPortableDevicePropVariantCollectionValue(WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS, &pPersistentIDs);
        CHECK_HR(hr, "Failed to get WPD_PROPERTY_COMMON_PERSISTENT_UNIQUE_IDS");
    }

    // Create the collection to hold the ObjectIDs
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pObjectIDs);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Iterate through the persistent ID list and add the equivalent object ID for each element.
    if (hr == S_OK)
    {
        hr = pPersistentIDs->GetCount(&dwCount);
        CHECK_HR(hr, "Failed to get count from persistent ID collection");

        if (hr == S_OK)
        {
            DWORD       dwIndex        = 0;
            PROPVARIANT pvPersistentID = {0};
            PROPVARIANT pvObjectID     = {0};

            PropVariantInit(&pvPersistentID);
            PropVariantInit(&pvObjectID);

            for(dwIndex = 0; dwIndex < dwCount; dwIndex++)
            {
                pvObjectID.vt = VT_LPWSTR;
                hr = pPersistentIDs->GetAt(dwIndex, &pvPersistentID);
                CHECK_HR(hr, "Failed to get persistent ID at index %d", dwIndex);

                // Because our persistent unique identifiers are identical to our object
                // identifiers, we just return it back to the caller.
                if (hr == S_OK)
                {
                    pvObjectID.pwszVal = AtlAllocTaskWideString(pvPersistentID.pwszVal);
                }

                if (hr == S_OK)
                {
                    hr = pObjectIDs->Add(&pvObjectID);
                    CHECK_HR(hr, "Failed to add next Object ID");
                }

                PropVariantClear(&pvPersistentID);
                PropVariantClear(&pvObjectID);

                if(FAILED(hr))
                {
                    break;
                }
            }
        }
    }

    if (hr == S_OK)
    {
        hr = pResults->SetIPortableDevicePropVariantCollectionValue(WPD_PROPERTY_COMMON_OBJECT_IDS, pObjectIDs);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_COMMON_OBJECT_IDS");
    }

    return hr;
}
```

Some devices might store the persistent identifiers in an object, some might generate a persistent identifier based on a hash of object data, and others might treat their object identifiers as persistent identifiers (because they will never change). The WpdHelloWorldDriver sample implements this latter case.

When a client application calls the **IPortableDeviceContent::GetObjectIDsFromPersistentUniqueIDs** method, the driver, in turn, calls **WpdBaseDriver::OnGetObjectIDsFromPersistentUniqueIDs**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Mapping%20Object%20Identifiers%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



