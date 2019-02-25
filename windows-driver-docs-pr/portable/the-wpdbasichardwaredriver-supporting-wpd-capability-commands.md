---
Description: Support for capability commands (WpdBasicHardwareDriver sample)
title: Support for capability commands (WpdBasicHardwareDriver sample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for capability commands (WpdBasicHardwareDriver sample)


The sample driver supports ten capability commands. These commands are processed initially by the **WpdCapabilities::DispatchMessage** method that, in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are found in the *WpdCapabilities.cpp* file.

The information in the following table describes each of the supported property commands together with the names of the handlers that **DispatchMessage** calls when it processes a given command.

| Command                                                            | Handler                        | Description                                                                                                                                     |
|--------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_COMMANDS               | OnGetSupportedCommands         | Issued when an application attempts to retrieve the set of commands that are supported by the device.                                           |
| WPD\_COMMAND\_CAPABILITIES\_GET\_COMMAND\_OPTIONS                  | OnGetCommandOptions            | Issued when an application attempts to retrieve the options that are supported by a given command.                                              |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FUNCTIONAL\_CATEGORIES | OnGetFunctionalCategories      | Issued when an application attempts to retrieve the set of functional categories that are supported by the device.                              |
| WPD\_COMMAND\_CAPABILITIES\_GET\_FUNCTIONAL\_OBJECTS               | OnGetFunctionalObjects         | Issued when an application attempts to retrieve the set of functional objects that are supported by a given functional category.                |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_CONTENT\_TYPES         | OnGetSupportedContentTypes     | Issued when an application attempts to retrieve the content types that are supported by a given functional category.                            |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMATS                | OnGetSupportedFormats          | Issued when an application attempts to retrieve the set of formats that are supported by a given content type.                                  |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMAT\_PROPERTIES     | OnGetSupportedFormatProperties | Issued when an application attempts to retrieve the set of properties that are supported by a given format.                                     |
| WPD\_COMMAND\_CAPABILITIES\_GET\_FIXED\_PROPERTY\_ATTRIBUTES       | OnGetFixedPropertyAttributes   | Issued when an application attempts to retrieve the set of property attributes that are identical (or fixed) for all objects of a given format. |
| WPD\_COMMAND\_CAPABILITIES\_GET\_EVENT\_OPTIONS                    | OnGetEventOptions              | Issued when an application attempts to retrieve the options that are associated with a given event.                                             |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_EVENTS                 | OnGetEventOptions              | Issued when an application attempts to retrieve the set of events that are supported by a device.                                               |

 

For the sample driver, the code remained intact for the handlers that are associated with the following commands:

-   WPD\_COMMAND\_CAPABILITIES\_GET\_COMMAND\_OPTIONS
-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMAT\_PROPERTIES
-   WPD\_COMMAND\_CAPABILITIES\_GET\_FIXED\_PROPERTY\_ATTRIBUTES
-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_ FORMAT\_PROPERTIES

However, the code was modified for the following handlers:

-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_COMMANDS
-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FUNCTIONAL\_CATEGORIES
-   WPD\_COMMAND\_CAPABILITIES\_GET\_FUNCTIONAL\_OBJECTS
-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_CONTENT\_TYPES
-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMATS
-   WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_EVENTS
-   WPD\_COMMAND\_CAPABILITIES\_GET\_EVENT\_OPTIONS

## <span id="WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS"></span><span id="wpd_command_capabilities_get_supported_commands"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_COMMANDS


The driver calls the **WpdObjectCapabilities::OnGetSupportedCommands** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_ COMMANDS command. The handler, in turn, returns an array of identifiers for the supported commands.

Although it was unnecessary to modify the handler, it was necessary to update the array of supported commands that appears at the beginning of the *WpdCapabilities.cpp* file. These modifications entailed removing the object-resource category of commands, because neither the sensor devices nor the driver support resources:

```cpp
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

    // WPD_CATEGORY_CAPABILITIES
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_COMMANDS,
    WPD_COMMAND_CAPABILITIES_GET_COMMAND_OPTIONS,
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES,
    WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS,
    WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS,  
    WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS,
};
```

## <span id="WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FUNCTIONAL_CATEGORIES"></span><span id="wpd_command_capabilities_get_supported_functional_categories"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FUNCTIONAL\_CATEGORIES


The driver calls the **WpdObjectCapabilities::OnGetFunctionalCategories** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_ FUNCTIONAL\_CATEGORIES command. The handler, in turn, returns an array of identifiers for the supported categories.

Although it was unnecessary to modify the handler, it was necessary to update the array of supported categories that appears at the beginning of the *WpdCapabilities.cpp* file. These modifications entailed removing the storage category and replacing it with the sensor category:

```cpp
const GUID g_SupportedFunctionalCategories[] =
{
    WPD_FUNCTIONAL_CATEGORY_DEVICE,
    FUNCTIONAL_CATEGORY_SENSOR_SAMPLE, // Our sensor&#39;s functional category  
};
```

The sample driver defines a custom functional category GUID (FUNCTIONAL\_CATEGORY\_SENSOR\_SAMPLE) to describe a sensor functional object.

## <span id="WPD_COMMAND_CAPABILITIES_GET_FUNCTIONAL_OBJECTS"></span><span id="wpd_command_capabilities_get_functional_objects"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_FUNCTIONAL\_OBJECTS


The driver calls the **WpdObjectCapabilities::OnGetFunctionalObjects** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_FUNCTIONAL\_ OBJECTS command. The handler, in turn, returns an array of identifiers for the supported functional objects.

The modifications to the **OnGetFunctionalObjects** handler included removing support for the storage object, which is not included in the WpdBasicHardwareDriver, and adding support for the sensor object:

```cpp
HRESULT WpdCapabilities::OnGetFunctionalObjects(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr                     = S_OK;
    GUID    guidFunctionalCategory = GUID_NULL;
    CComPtr<IPortableDevicePropVariantCollection> pFunctionalObjects;

    // First get ALL parameters for this command.  If we cannot get ALL parameters
    // then E_INVALIDARG should be returned and no further processing should occur.

    // Get the functional category whose functional object identifiers have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY, &guidFunctionalCategory);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY");
    }

    // CoCreate a collection to store the supported functional object identifiers.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pFunctionalObjects);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Add the supported functional object identifiers for the specified functional
    // category to the collection.
    if (hr == S_OK)
    {
        PROPVARIANT pv = {0};
        PropVariantInit(&pv);
        // Don&#39;t call PropVariantClear, since we did not allocate the memory for these object identifiers

        // Add WPD_DEVICE_OBJECT_ID to the functional object identifiers collection
        if (hr == S_OK)
        {
           
            if ((guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_DEVICE) ||
                (guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_ALL))
            {
                pv.vt       = VT_LPWSTR;
                pv.pwszVal  = WPD_DEVICE_OBJECT_ID;
                hr = pFunctionalObjects->Add(&pv);
                CHECK_HR(hr, "Failed to add device object ID");
            }
        }

        // Add FUNCTIONAL_CATEGORY_SENSOR_SAMPLE to the functional object 
        // identifiers collection
        if (hr == S_OK)
        {
            if ((guidFunctionalCategory  == FUNCTIONAL_CATEGORY_SENSOR_SAMPLE) ||
                (guidFunctionalCategory  == WPD_FUNCTIONAL_CATEGORY_ALL))
            {
                pv.vt       = VT_LPWSTR;
                pv.pwszVal  = SENSOR_OBJECT_ID;
                hr = pFunctionalObjects->Add(&pv);
                CHECK_HR(hr, "Failed to add sensor object ID");
            }
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS, pFunctionalObjects);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_OBJECTS");
    }

    return hr;
}
```

## <span id="WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_CONTENT_TYPES"></span><span id="wpd_command_capabilities_get_supported_content_types"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_CONTENT\_TYPES


The driver calls the **WpdObjectCapabilities::OnGetSupportedContentTypes** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_ SUPPORTED\_CONTENT\_TYPES command. Because the sensor devices do not support any content types, this handler returns an empty collection.

The modifications to the **OnGetSupportedContentTypes** handler included removing the code in the WpdHelloWorldSample driver that added the document and folder content types to the returned collection:

```cpp
HRESULT WpdCapabilities::OnGetSupportedContentTypes(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr                     = S_OK;
    GUID    guidFunctionalCategory = GUID_NULL;
    CComPtr<IPortableDevicePropVariantCollection> pContentTypes;

    // First get ALL parameters for this command. If we cannot get ALL parameters
    // then E_INVALIDARG should be returned 
    // and no further processing should occur.

    // Get the functional category whose supported content types 
    // have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY, 
                                   &guidFunctionalCategory);
        CHECK_HR(hr, 
                 "Missing value for 
                  WPD_PROPERTY_CAPABILITIES_FUNCTIONAL_CATEGORY");
    }

    // CoCreate a collection to store the supported content types.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pContentTypes);
        CHECK_HR(hr, 
                 "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Set the WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES, 
                                        pContentTypes);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_CONTENT_TYPES");
    }

    return hr;
}
```

## <span id="WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_FORMATS"></span><span id="wpd_command_capabilities_get_supported_formats"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMATS


The driver calls the **WpdObjectCapabilities::OnGetSupportedFormats** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_ FORMATS command. Because the sensor devices do not support any content types, there are no supported formats either. As a result, this handler also returns an empty collection.

The modifications to the **OnGetSupportedContentTypes** handler involves removing the code in the WpdHelloWorldSample driver that added the text format to the collection. The text format was supported for the document content type:

```cpp
HRESULT WpdCapabilities::OnGetSupportedFormats(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr              = S_OK;
    GUID    guidContentType = GUID_NULL;
    CComPtr<IPortableDevicePropVariantCollection> pFormats;

    // First get ALL parameters for this command. If we cannot get ALL parameters
    // then E_INVALIDARG should be returned 
    // and no further processing should occur.

    // Get the content type whose supported formats have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE, 
                                   &guidContentType);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_CONTENT_TYPE");
    }

    // CoCreate a collection to store the supported formats.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pFormats);
        CHECK_HR(hr, "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Set the WPD_PROPERTY_CAPABILITIES_FORMATS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_FORMATS, 
                                        pFormats);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_FORMATS");
    }

    return hr;
}
```

## <span id="WPD_COMMAND_CAPABILITIES_GET_SUPPORTED_EVENTS"></span><span id="wpd_command_capabilities_get_supported_events"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_EVENTS


The driver calls the **WpdObjectCapabilities::OnGetSupportedEvents** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_EVENTS command. Because the sensor devices support the custom sensor-reading updated event (EVENT\_ SENSOR\_READING\_ UPDATED), it was necessary to update the source file.

The first modification involved adding a g\_SupportedEvents array that contains the identifier for the one supported event:

```cpp
const GUID g_SupportedEvents[] =
{
    EVENT_SENSOR_READING_UPDATED,
};
```

The second modification, to the **OnGetSupportedEvents** handler, involved adding code that populated the supported events collection:

```cpp
HRESULT WpdCapabilities::OnGetSupportedEvents(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr = S_OK;
    CComPtr<IPortableDevicePropVariantCollection> pEvents;
    UNREFERENCED_PARAMETER(pParams);

    // CoCreate a collection to store the supported events.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDevicePropVariantCollection,
                              (VOID**) &pEvents);
        CHECK_HR(hr, 
                 "Failed to CoCreate CLSID_PortableDevicePropVariantCollection");
    }

    // Add the supported events to the collection.
    if (hr == S_OK)
    {
        // populate the supported events collection
        for (DWORD dwIndex = 0; dwIndex < ARRAYSIZE(g_SupportedEvents); dwIndex++)
        {
            PROPVARIANT pv = {0};
            PropVariantInit(&pv);
            // Don&#39;t call PropVariantClear, 
            // since we did not allocate the memory for these GUIDs

            pv.vt    = VT_CLSID;
            pv.puuid = (GUID*) &g_SupportedEvents[dwIndex];

            hr = pEvents->Add(&pv);
            CHECK_HR(hr, "Failed to add supported event at index %d", dwIndex);
            if (FAILED(hr))
            {
                break;
            }
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS value in the results.
    if (hr == S_OK)
    {
        hr = pResults-> 
             SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS, 
                              pEvents);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_SUPPORTED_EVENTS");
    }

    return hr;
}
```

## <span id="WPD_COMMAND_CAPABILITIES_GET_EVENT_OPTIONS"></span><span id="wpd_command_capabilities_get_event_options"></span>WPD\_COMMAND\_CAPABILITIES\_GET\_EVENT\_OPTIONS


The driver calls the **WpdObjectCapabilities::OnGetEventOptions** handler in response to the WPD\_COMMAND\_CAPABILITIES\_GET\_EVENT\_OPTIONS command. Because the sensor devices support the reading updated event, which is a broadcast event, it was necessary to add a flag indicating that this option (WPD\_EVENT\_OPTION\_IS\_BROADCAST\_EVENT) is **TRUE**:

```cpp
HRESULT WpdCapabilities::OnGetEventOptions(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr    = S_OK;
    GUID    Event = GUID_NULL;
    CComPtr<IPortableDeviceValues> pOptions;

    // First get ALL parameters for this command. If we cannot get ALL parameters
    // then E_INVALIDARG should be returned 
    // and no further processing should occur.

    // Get the event whose options have been requested
    if (hr == S_OK)
    {
        hr = pParams->GetGuidValue(WPD_PROPERTY_CAPABILITIES_EVENT, &Event);
        CHECK_HR(hr, "Missing value for WPD_PROPERTY_CAPABILITIES_EVENT");
    }

    // CoCreate a collection to store the event options.
    if (hr == S_OK)
    {
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &pOptions);
        CHECK_HR(hr, "Failed to CoCreateInstance CLSID_PortableDeviceValues");
    }

    // Add event options to the collection
    if (hr == S_OK)
    {
        //  Check for the events we support
        if (Event == EVENT_ SENSOR_READING_UPDATED)
        {
            // These events are broadcast events
            hr = pOptions->SetBoolValue(WPD_EVENT_OPTION_IS_BROADCAST_EVENT, 
                                        TRUE);
            CHECK_HR(hr, "Failed to set WPD_EVENT_OPTION_IS_BROADCAST_EVENT");
        }
    }

    // Set the WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS value in the results.
    if (hr == S_OK)
    {
        hr = pResults->SetIUnknownValue(WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS, 
                                        pOptions);
        CHECK_HR(hr, "Failed to set WPD_PROPERTY_CAPABILITIES_EVENT_OPTIONS");
    }

    return hr;
}
```

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





