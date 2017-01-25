---
Description: 'Command-Option Retrieval'
MS-HAID: 'wpddk.command\_option\_retrieval'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Command-Option Retrieval'
---

# Command-Option Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetCommandOptions** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetCommandOptions** method in the sample driver. The latter method creates an **IPortableDeviceValues** object into which the driver would store any supported options. Because the sample driver does not support command options, the collection returned by this method is empty.

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetCommandOptions(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT     hr      = S_OK;
    PROPERTYKEY Command = WPD_PROPERTY_NULL;
    CComPtr<IPortableDeviceValues> pOptions;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the command whose options have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetKeyValue(WPD_PROPERTY_CAPABILITIES_COMMAND, &Command);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_COMMAND");
    }

    // CoCreate a collection to store the command options.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pOptions);
        CHECK_HR(hr, "Failed to CoCreateInstance CLSID_PortableDeviceValues");
    }

    // Add command options to the collection
    if (hr == S_OK)
    {
        // If your driver supports command options, then they should be added here
        // to the command options collection &#39;pOptions&#39;.
    }

    // Set the WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS, pOptions);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_COMMAND_OPTIONS");
    }

    return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Command-Option%20Retrieval%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



