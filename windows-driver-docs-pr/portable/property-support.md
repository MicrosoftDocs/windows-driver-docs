---
Description: Property Support
title: Property Support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Support


The *WpdObjectProperties.cpp* and *WpdObjectProperties.h* files contain the member functions that set and retrieve object properties on the device.

When a Windows application calls one of the five methods in the **IPortableDeviceProperties** interface, this call, in turn, triggers one of five command handlers in the **WpdObjectProperty** class. The following table identifies the mapping of application methods to **WpdObjectProperties** driver methods.

|                                                       |                                                   |
|-------------------------------------------------------|---------------------------------------------------|
| **IPortableDeviceProperties Method**                  | **WpdObjectProperties Command Handler**           |
| **IPortableDeviceProperties::Delete**                 | **OnDelete**                                      |
| **IPortableDeviceProperties::GetPropertyAttributes**  | **OnGetPropertyAttributes**                       |
| **IPortableDeviceProperties::GetSupportedProperties** | **OnGetSupportedProperties**                      |
| **IPortableDeviceProperties::GetValues**              | **OnGetPropertyValues or OnGetAllPropertyValues** |
| **IPortableDeviceProperties::SetValues**              | **OnSetPropertyValues**                           |

 

The WpdObjectProperties command handlers are invoked by the **WpdObjectProperty::DispatchWpdMessage** method. The following excerpt from the sample driver contains the code for **WpdObjectProperty::DispatchWpdMessage:**

```ManagedCPlusPlus
HRESULT WpdObjectProperties::DispatchWpdMessage(
    const PROPERTYKEY&     Command,
    IPortableDeviceValues* pParams,
    IPortableDeviceValues* pResults)
{
    HRESULT hr = S_OK;

    if (hr == S_OK)
    {
        if (Command.fmtid != WPD_CATEGORY_OBJECT_PROPERTIES)
        {
            hr = E_INVALIDARG;
            CHECK_HR(hr, "This object does not support this command category %ws",CComBSTR(Command.fmtid));
        }
    }

    if (hr == S_OK)
    {
        if (IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED))
        {
            hr = OnGetSupportedProperties(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported properties");
        }
        else if(IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_PROPERTIES_GET))
        {
            hr = OnGetPropertyValues(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to get properties");
            }
        }
        else if(IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL))
        {
            hr = OnGetAllPropertyValues(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to get all properties");
            }
        }
        else if(IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_PROPERTIES_SET))
        {
            hr = OnSetPropertyValues(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to set properties");
            }
        }
        else if(IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES))
        {
            hr = OnGetPropertyAttributes(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to get property attributes");
            }
        }
        else if(IsEqualPropertyKey(Command, WPD_COMMAND_OBJECT_PROPERTIES_DELETE))
        {
            hr = OnDeleteProperties(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to delete properties");
            }
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

 

 




