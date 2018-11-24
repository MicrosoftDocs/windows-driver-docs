---
Description: Support for WPD infrastructure (WpdBasicHardwareDriverSample)
title: Support for WPD infrastructure (WpdBasicHardwareDriverSample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for WPD infrastructure (WpdBasicHardwareDriverSample)


The WPD infrastructure is command driven. When a WPD application calls one of the methods in a given interface, the WPD serializer (an in-process COM server) converts the method call into one or more commands that it sends to the driver. The driver then processes these commands and returns a response. For more information about the infrastructure, see the [Architecture Overview](architecture-overview.md) topic.

The following image of the *WpdMon.exe* tool shows the result of an application calling the **IPortableDeviceProperties::GetPropertyAttributes** method to retrieve the property attributes for the temperature and humidity sensor.

![the wpd monitor ](images/wpdmon_get_attributes.png)

In the previous image, the WPD serializer converted the **GetPropertyAttributes** call into the WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ATTRIBUTES command and the corresponding parameters. The driver processed this command and issued a response to the WPD API.

The WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ATTRIBUTES command is first handled in the **WpdObjectProperties::DispatchWpdMessage** method. This method, in turn, invokes the **WpdObjectProperties::OnGetPropertyAttributes** method. Both of these methods are found in the *WpdObjectProperties.cpp* source file.

The following excerpt from the **WpdObjectProperties::DispatchWpdMessage** method in *WpdObjectProperties.cpp* shows the call to the **WpdObjectProperties::OnGetPropertyAttributes** handler for the retrieval of property attributes. The **DispatchWpdMessage** method passes the command parameters to the handler. These parameters include an object identifier for the object whose properties the driver should retrieve. Additionally, the parameters include a collection of property keys that identify the attributes to be retrieved.

```cpp
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
            CHECK_HR(hr, 
                     "This object does not support this command category %ws",
                     CComBSTR(Command.fmtid));
        }
    }

    if (hr == S_OK)
    {
     …
        else if(IsEqualPropertyKey(Command, 
                                   WPD_COMMAND_OBJECT_PROPERTIES_GET_ATTRIBUTES))
        {
            hr = OnGetPropertyAttributes(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to get property attributes");
            }
        }
        …
    return hr;
}
```

The **WpdObjectProperties::OnGetPropertyAttributes** method returns the collection of requested attributes in a collection of device values (IPortableDeviceValues).

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





