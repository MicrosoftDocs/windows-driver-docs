---
Description: Driver Capabilities
title: Driver Capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Capabilities


The *WpdCapabilities.cpp* and *WpdCapabilities.h* files contain the command handlers that retrieve supported commands, command options, function categories, and so on.

When a Windows-based application calls one of the methods in the **IPortableDeviceCapabilities** interface, this call, in turn, triggers one of eight command handlers in the **WpdCapabilities** class. The following table identifies the mapping of **IPortableDeviceCapabilities** methods to **WpdCapabilities** command handlers.

|                                                               |                                    |
|---------------------------------------------------------------|------------------------------------|
| **IPortableDeviceCapabilities Method**                        | **WpdCapabilities Event Handler**  |
| **IPortableDeviceCapabilities::GetCommandOptions**            | **OnGetCommandOptions**            |
| **IPortableDeviceCapabilities::GetFixedPropertyAttributes**   | **OnGetFixedPropertyAttributes**   |
| **IPortableDeviceCapabilities::GetFunctionalCategories**      | **OnGetFunctionalCategories**      |
| **IPortableDeviceCapabilities::GetFunctionalObjects**         | **OnGetFunctionalObjects**         |
| **IPortableDeviceCapabilities::GetSupportedCommands**         | **OnGetSupportedCommands**         |
| **IPortableDeviceCapabilities::GetSupportedContentTypes**     | **OnGetSupportedContentTypes**     |
| **IPortableDeviceCapabilities::GetSupportedFormatProperties** | **OnGetSupportedFormatProperties** |
| **IPortableDeviceCapabilities::GetSupportedFormats**          | **OnGetSupportedFormats**          |
| **IPortableDeviceCapabilities::GetSupportedEvents**           | **OnGetSupportedEvents**           |
| **IPortableDeviceCapabilities::GetEventOptions**              | **OnGetEventOptions**              |

 

The WpdCapabilities command handlers are invoked by the **WpdCapabilities::DispatchMessage** method. The following excerpt from the sample driver contains the code for **WpdCapabilities::DispatchMessage**.

```ManagedCPlusPlus
HRESULT WpdCapabilities::DispatchWpdMessage(const PROPERTYKEY&      Command,
                                            IPortableDeviceValues*  pParams,
                                            IPortableDeviceValues*  pResults)
{
    HRESULT hr = S_OK;

    if (hr == S_OK)
    {
        if (Command.fmtid != WPD_CATEGORY_CAPABILITIES)
        {
            hr = E_INVALIDARG;
            CHECK_HR(hr, "This object does not support this command category %ws",CComBSTR(Command.fmtid));
        }
    }

    if (hr == S_OK)
    {
        if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS))
        {
            hr = OnGetSupportedCommands(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported commands");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS))
        {
            hr = OnGetCommandOptions(pParams, pResults);
            CHECK_HR(hr, "Failed to get command options");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES))
        {
            hr = OnGetFunctionalCategories(pParams, pResults);
            CHECK_HR(hr, "Failed to get functional categories");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS))
        {
            hr = OnGetFunctionalObjects(pParams, pResults);
            CHECK_HR(hr, "Failed to get functional objects");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES))
        {
            hr = OnGetSupportedContentTypes(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported content types");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS))
        {
            hr = OnGetSupportedFormats(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported formats");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES))
        {
            hr = OnGetSupportedFormatProperties(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported format properties");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES))
        {
            hr = OnGetFixedPropertyAttributes(pParams, pResults);
            CHECK_HR(hr, "Failed to get fixed property attributes");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS))
        {
            hr = OnGetSupportedEvents(pParams, pResults);
            CHECK_HR(hr, "Failed to get supported events");
        }
        else if (IsEqualPropertyKey(Command, WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS))
        {
            hr = OnGetEventOptions(pParams, pResults);
            CHECK_HR(hr, "Failed to get event options");
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

 

 




