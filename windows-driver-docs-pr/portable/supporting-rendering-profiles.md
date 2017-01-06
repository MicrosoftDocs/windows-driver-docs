---
Description: Supporting Rendering Profiles
MS-HAID: 'wpddk.supporting\_rendering\_profiles'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting Rendering Profiles
---

# Supporting Rendering Profiles


An audio or video device may support specific rendering profiles. For example, an audio streaming device may stream a particular type of content at a specific bitrate over multiple channels. The content type, streaming bitrate, and channel count are referred to as a *rendering profile*.

WPD applications will often retrieve a rendering profile from the driver. For more information about how an application retrieves a rendering profile, see the [Retrieving the Rendering Capabilities Supported by a Device](http://go.microsoft.com/fwlink/p/?linkid=150363) topic in the WPD SDK.

This topic describes how the WpdWudfSampleDriver driver implements support for audio streaming in the *Helpers.cpp* module.

When an application requests a rendering profile, the driver receives a WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET command with a command category of WPD\_CATEGORY\_OBJECT\_PROPERTIES and a WPD\_PROPERTY\_OBJECT\_PROPERTIES\_OBJECT\_ID of RenderingInformation. In the sample driver, the receipt of this command triggers a call to the SetRenderingProfile function in the *Helpers.cpp* module.

```ManagedCPlusPlus
HRESULT SetRenderingProfiles(
    IPortableDeviceValues*          pValues)
{
    HRESULT hr = S_OK;
    CComPtr<IPortableDeviceValues> pPreferredProfile;
    CComPtr<IPortableDeviceValues> pProfile2;

    CComPtr<IPortableDeviceValuesCollection> pProfiles;

    if(pValues == NULL)
    {
        hr = E_POINTER;
        CHECK_HR(hr, ("Cannot have NULL parameter"));
        return hr;
    }

    // Create the collection to hold the profiles
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValuesCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValuesCollection,
                              (VOID**) &pProfiles);
        CHECK_HR(hr, "Failed to CoCreateInstance CLSID_PortableDeviceValuesCollection");
    }

    // Get the preferred audio profile
    if (hr == S_OK)
    {
        hr = GetPreferredAudioProfile(&pPreferredProfile);
        CHECK_HR(hr, "Failed to get preferred audio profile properties");
    }

    // Add the profile
    if (hr == S_OK)
    {
        hr = pProfiles->Add(pPreferredProfile);
        CHECK_HR(hr, "Failed to add preferred audio profile to profile collection");
    }

    // Get the second audio profile
    if (hr == S_OK)
    {
        hr = GetAudioProfile2(&pProfile2);
        CHECK_HR(hr, "Failed to get second audio profile properties");
    }

    // Add the profile
    if (hr == S_OK)
    {
        hr = pProfiles->Add(pProfile2);
        CHECK_HR(hr, "Failed to add second audio profile to profile collection");
    }

    // Set the WPD_RENDERING_INFORMATION_PROFILES
    if (hr == S_OK)
    {
        hr = pValues->SetIPortableDeviceValuesCollectionValue(WPD_RENDERING_INFORMATION_PROFILES, pProfiles);
        CHECK_HR(hr, "Failed to set WPD_RENDERING_INFORMATION_PROFILES");
    }

    return hr;
}
```

The **SetRenderingProfiles** function, in turn, calls the GetPreferredAudioProfile helper function, which returns the actual profile information in an IPortableDeviceValues object.

```ManagedCPlusPlus
HRESULT GetPreferredAudioProfile(
    IPortableDeviceValues** ppProfile)
{
    HRESULT hr = S_OK;
    CComPtr<IPortableDeviceValues> pProfile;

    if(ppProfile == NULL)
    {
        hr = E_POINTER;
        CHECK_HR(hr, ("Cannot have NULL parameter"));
        return hr;
    }

    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pProfile);
        CHECK_HR(hr, "Failed to CoCreateInstance CLSID_PortableDeviceValues");
    }

    // Set the value for WPD_OBJECT_FORMAT to indicate this profile applies to WMA objects
    if (hr == S_OK)
    {
        hr = pProfile->SetGuidValue(WPD_OBJECT_FORMAT, WPD_OBJECT_FORMAT_WMA);
        CHECK_HR(hr, "Failed to set WPD_OBJECT_FORMAT");
    }

    // Set the preferred value for WPD_MEDIA_TOTAL_BITRATE
    if (hr == S_OK)
    {
        hr = pProfile->SetUnsignedIntegerValue(WPD_MEDIA_TOTAL_BITRATE, 192000);
        CHECK_HR(hr, "Failed to set WPD_MEDIA_TOTAL_BITRATE");
    }

    // Set the preferred value for WPD_AUDIO_CHANNEL_COUNT
    if (hr == S_OK)
    {
        hr = pProfile->SetUnsignedIntegerValue(WPD_AUDIO_CHANNEL_COUNT, 2);
        CHECK_HR(hr, "Failed to set WPD_AUDIO_CHANNEL_COUNT");
    }

    // Set the preferred value for WPD_AUDIO_FORMAT_CODE
    if (hr == S_OK)
    {
        hr = pProfile->SetUnsignedIntegerValue(WPD_AUDIO_FORMAT_CODE, WAVE_FORMAT_MSAUDIO3);
        CHECK_HR(hr, "Failed to set WPD_AUDIO_FORMAT_CODE");
    }

    // Set the output result
    if (hr == S_OK)
    {
        hr = pProfile->QueryInterface(IID_PPV_ARGS(ppProfile));
        CHECK_HR(hr, "Failed to QI for IPortableDeviceValues");
    }

    return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20Rendering%20Profiles%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



