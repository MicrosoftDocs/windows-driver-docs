---
Description: Support for capability commands (WpdServiceSampleDriver sample)
title: Support for capability commands (WpdServiceSampleDriver sample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for capability commands (WpdServiceSampleDriver sample)


The sample driver supports ten capability commands for a device and 14 capability commands for a service. The code that supports the device-capability commands is found in *WpdCapabilities.cpp*. The code that supports the service-capability commands is found in *WpdServiceCapabilities.cpp*. WPD invokes these commands when an application retrieves device-capability or service-capability data. For example, when an application calls **IPortableDeviceServiceCapabilities::GetSupportedFormats**, WPD issues a corresponding WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_FORMATS command to the driver to retrieve the supported formats for a given service.

## <span id="The_Device-Capability_Commands"></span><span id="the_device-capability_commands"></span><span id="THE_DEVICE-CAPABILITY_COMMANDS"></span>The Device-Capability Commands


The device-capability commands are issued when an application calls one of several methods in the **IPortableDeviceCapabilities** interface. These commands are processed initially by the **WpdCapabilities::DispatchMessage** method that in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are found in the *WpdCapabilities.cpp* file.The following table describes each of the device-capability commands together with the names of the handlers that **DispatchMessage** calls when it processes a given command.

| Command                                                            | Handler                        | Description                                                                                                                                  |
|--------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_COMMANDS               | OnGetSupportedCommands         | Issued when an application tries to retrieve the set of commands that are supported by the device.                                           |
| WPD\_COMMAND\_CAPABILITIES\_GET\_COMMAND\_OPTIONS                  | OnGetCommandOptions            | Issued when an application tries to retrieve the options that are supported by a given command.                                              |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FUNCTIONAL\_CATEGORIES | OnGetFunctionalCategories      | Issued when an application tries to retrieve the set of functional categories that are supported by the device.                              |
| WPD\_COMMAND\_CAPABILITIES\_GET\_FUNCTIONAL\_OBJECTS               | OnGetFunctionalObjects         | Issued when an application tries to retrieve the set of functional objects that are supported by a given functional category.                |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_CONTENT\_TYPES         | OnGetSupportedContentTypes     | Issued when an application tries to retrieve the content types that are supported by a given functional category.                            |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMATS                | OnGetSupportedFormats          | Issued when an application tries to retrieve the set of formats that are supported by a given content type.                                  |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_FORMAT\_PROPERTIES     | OnGetSupportedFormatProperties | Issued when an application tries to retrieve the set of properties that are supported by a given format.                                     |
| WPD\_COMMAND\_CAPABILITIES\_GET\_FIXED\_PROPERTY\_ATTRIBUTES       | OnGetFixedPropertyAttributes   | Issued when an application tries to retrieve the set of property attributes that are identical (or fixed) for all objects of a given format. |
| WPD\_COMMAND\_CAPABILITIES\_GET\_EVENT\_OPTIONS                    | OnGetEventOptions              | Issued when an application tries to retrieve the options that are associated with a given event.                                             |
| WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_EVENTS                 | OnGetSupportedEvents           | Issued when an application tries to retrieve the set of events that are supported by a device.                                               |

 

## <span id="The_Service-Capability_Commands"></span><span id="the_service-capability_commands"></span><span id="THE_SERVICE-CAPABILITY_COMMANDS"></span>The Service-Capability Commands


The service-capability commands are issued when an application calls one of several methods in the **IPortableDeviceServiceCapabilities** interface. These commands are processed initially by the **WpdServiceCapabilities::DispatchMessage** method that, in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are found in the *WpdServiceCapabilities.cpp* file.The following table describes each of the device-capability commands together with the names of the handlers that **DispatchMessage** calls when it processes a given command.

| Command                                                                     | Handler                        | Description                                                                                                            |
|-----------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_COMMANDS               | OnGetSupportedCommands         | Issued when an application tries to retrieve the set of commands that are supported by the given service.              |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_COMMAND\_OPTIONS                  | OnGetCommandOptions            | Issued when an application tries to retrieve the options that are supported by a given command.                        |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_METHODS                | OnGetSupportedMethods          | Issued when an application tries to retrieve the methods that are supported by the given service.                      |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_METHODS\_BY\_FORMAT    | OnGetSupportedMethodsByFormat  | Issued when an application tries to retrieve the methods that are supported by a given format on the given service.    |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_METHOD\_ATTRIBUTES                | OnGetMethodAttributes          | Issued when an application tries to retrieve the attributes for a given method.                                        |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_METHOD\_PARAMETER\_ATTRIBUTES     | OnGetMethodParameterAttributes | Issued when an application tries to retrieve the attributes for a given method parameter.                              |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_FUNCTIONAL\_CATEGORIES | OnGetFunctionalCategories      | Issued when an application tries to retrieve the set of functional categories that are supported by the given service. |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_FORMATS                | OnGetSupportedFormats          | Issued when an application tries to retrieve the formats that are supported by a given service.                        |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_FORMAT\_ATTRIBUTES                | OnGetFormatAttributes          | Issued when an application tries to retrieve the attributes of a given format that is supported by the service.        |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_FORMAT\_PROPERTIES     | OnGetSupportedFormatProperties | Issued when an application tries to retrieve the set of properties that are supported by a given format.               |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_FORMAT\_PROPERTY\_ATTRIBUTES      | OnGetFormatPropertyAttributes  | Issued when an application tries to retrieve the set of property attributes for a given format on the service.         |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_SUPPORTED\_EVENTS                 | OnGetSupportedEvents           | Issued when an application tries to retrieve the events that are supported by the given service.                       |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_EVENT\_ATTRIBUTES                 | OnGetEventAttributes           | Issued when an application tries to retrieve the attributes for a given event on the service.                          |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_EVENT\_PARAMETER\_ATTRIBUTES      | OnGetEventParameterAttributes  | Issued when an application tries to retrieve the parameter attributes for a given event on the service.                |
| WPD\_COMMAND\_SERVICE\_CAPABILITIES\_GET\_INHERITED\_SERVICES               | OnGetInheritedServices         | Issued when an application tries to retrieve the services that are inherited by the given service.                     |

 

## <span id="related_topics"></span>Related topics


****
[The WpdServiceSampleDriver](the-wpdservicesampledriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





