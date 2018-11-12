---
Description: Supported Command Retrieval
title: Supported Command Retrieval
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supported Command Retrieval


When a WPD application calls the **IPortableDeviceCapabilities::GetSupportedCommands** method, this method, in turn, triggers a call to the **WpdCapabilities::OnGetSupportedCommands** method in the sample driver. The latter method creates an **IPortableDeviceKeyCollection** object into which the driver stores the list of commands it supports. In the case of the sample driver, there are 22 supported commands in four categories.

```ManagedCPlusPlus
const PROPERTYKEY g_SupportedCommands[] =
{
    // WPD_CATEGORY_OBJECT_ENUMERATION
    WPD_COMMAND_OBJECT_ENUMERATION_START_FIND,
    WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT,
    WPD_COMMAND_OBJECT_ENUMERATION_END_FIND,

    // WPD_CATEGORY_OBJECT_PROPERTIES
    WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED,
    WPD_COMMAND_OBJECT_PROPERTIES_GET,
    WPD_COMMAND_OBJECT_PROPERTIES_GET_ALL,
    WPD_COMMAND_OBJECT_PROPERTIES_SET,
    WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES,
    WPD_COMMAND_OBJECT_PROPERTIES_DELETE,

    // WPD_CATEGORY_OBJECT_RESOURCES
    WPD_COMMAND_OBJECT_RESOURCES_GET_SUPPORTED,
    WPD_COMMAND_OBJECT_RESOURCES_OPEN,
    WPD_COMMAND_OBJECT_RESOURCES_READ,
    WPD_COMMAND_OBJECT_RESOURCES_CLOSE,
    WPD_COMMAND_OBJECT_RESOURCES_GET_ATTRIBUTES,

    // WPD_CATEGORY_CAPABILITIES
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS,
    WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS,
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES,
    WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS,
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES,
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS,
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMAT_PROPERTIES,
    WPD_COMMAND_CAPABILITIES_GET_FIXED_PROPERTY_ATTRIBUTES,
};
```

The following excerpt from the *WpdCapabilities.cpp* file contains the code for the **OnGetSupportedCommands** method.

```ManagedCPlusPlus
HRESULT WpdCapabilities::OnGetSupportedCommands(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr = S_OK;
    CComPtr<IPortableDeviceKeyCollection> pCommands;
    UNREFERENCED_PARAMETER(pParams);

    // CoCreate a collection to store the supported commands.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceKeyCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceKeyCollection,
                              (VOID**) &pCommands);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDeviceKeyCollection");
    }

    // Add the supported commands to the collection.
    if (hr == S_OK)
    {
        for (DWORD dwIndex = 0; dwIndex < ARRAYSIZE(g_SupportedCommands); dwIndex++)
        {
            hr = pCommands->Add(g_SupportedCommands[dwIndex]);
            CHECK_HR(hr, "Failed to add supported command at index %d", dwIndex);
            if (FAILED(hr))
            {
                break;
            }
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS, pCommands);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_SUPPORTED_COMMANDS");
    }

    return hr;
}
```

 

 




