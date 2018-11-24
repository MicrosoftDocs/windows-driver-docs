---
Description: Resources
title: Resources
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




