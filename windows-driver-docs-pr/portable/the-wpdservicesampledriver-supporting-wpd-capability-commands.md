---
Description: Supporting the Capability Commands
MS-HAID: 'wpddk.the\_wpdservicesampledriver\_supporting\_wpd\_capability\_commands'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting the Capability Commands
---

# Supporting the Capability Commands


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20the%20Capability%20Commands%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




