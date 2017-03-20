---
Description: Resources
MS-HAID: 'wpddk.resources'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Resources
---

# Resources


The *WpdObjectResources.cpp* and *WpdObjectResources.h* files contain the member functions that open or close a given resource, read the contents of a resource, retrieve the attributes that are supported by a resource, and retrieve the resources that are supported by a given object.

In the case of the sample driver, there is a single resource (a sample readme text file) that resides within the Documents Folder object.

When a Windows-based application calls one of the methods in the **IPortableDeviceResources** interface, this call, in turn, triggers one of several command handlers in the WpdObjectResources class. The following table identifies the mapping of application methods to WpdObjectResource methods.

| WpdObjectResources Command Handler           | Description                                                                                                                            |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| WpdObjectResources::OnCloseResource          | Called in response to a close operation on the **IStream** object that **OnOpenResource** returned.                                    |
| WpdObjectResources::OnGetResourceAttributes. | Called in response to an application invoking the **IPortableDeviceResources::GetResourceAttributes** method.                          |
| WpdObjectResources::OnGetSupportedResources  | Called in response to an application invoking the **IPortableDeviceResources::GetSuportedResources** method.                           |
| WpdObjectResources::OnOpenResource           | Called in response to an application invoking the **IPortableDeviceResources::GetStream** method.                                      |
| WpdObjectResources::OnReadResource           | Called in response to an application invoking the **IStream::Read** method on the **IStream** object that **OnOpenResource** returned. |

 

The WpdObjectResources command handlers are invoked by the **WpdObjectResources::DispatchWpdMessage** method. The following excerpt from the sample driver contains the code for **WpdObjectResources::DispatchWpdMessage**.

```ManagedCPlusPlus
HRESULT WpdObjectResources::DispatchWpdMessage(
    const PROPERTYKEY&     Command,
    IPortableDeviceValues* pParams,
    IPortableDeviceValues* pResults)
{
    HRESULT hr = S_OK;

    if (hr == S_OK)
    {
        if (Command.fmtid != WPD_CATEGORY_OBJECT_RESOURCES)
        {
            hr = E_INVALIDARG;
            CHECK_HR(hr, "This object does not support this command category %ws",CComBSTR(Command.fmtid));
        }
    }

    if (hr == S_OK)
    {
        if (IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED))
        {
            hr = OnGetSupportedResources(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported resources");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_RESOURCES_OPEN))
        {
            hr = OnOpenResource(pParams, pResults);
            CHECK_HR(hr, "Failed to open resource");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_RESOURCES_READ))
        {
            hr = OnReadResource(pParams, pResults);
            CHECK_HR(hr, "Failed to read resource");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_RESOURCES_CLOSE))
        {
            hr = OnCloseResource(pParams, pResults);
            CHECK_HR(hr, "Failed to close resource");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES))
        {
            hr = OnGetResourceAttributes(pParams, pResults);
            CHECK_HR(hr, "Failed to get resource attributes");
        }
        else
        {
            hr = E_NOTIMPL;
            CHECK_HR(hr, "This object does not support this command id %d", Command.pid);
        }
    }
    return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Resources%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



