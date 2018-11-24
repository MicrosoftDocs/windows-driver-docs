---
Description: Support for property commands (WpdBasicHardwareDriverSample)
title: Support for property commands (WpdBasicHardwareDriverSample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for property commands (WpdBasicHardwareDriverSample)


The sample driver supports six property commands. These commands are processed initially by the **WpdObjectProperties::DispatchMessage** method that, in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are all found in the *WpdObjectProperties.cpp file*.

The following table describes each of the supported property commands, together with the names of the handlers that **DispatchMessage** calls when it processes a given command.

| Command                                           | Handler                  | Description                                                                                                   |
|---------------------------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_SUPPORTED  | OnGetSupportedProperties | Returns an array of property keys for the given object.                                                       |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET             | OnGetPropertyValues      | Returns a collection of property values that correspond to the property keys that are supplied to the driver. |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ALL        | OnGetAllProperties       | Returns all the property values for a given object.                                                           |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_SET             | OnSetPropertyValues      | Sets the specified property value on the device.                                                              |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_ATTRIBUTES | OnGetPropertyAttributes  | Returns a collection of attributes for one or more properties on a given object.                              |
| WPD\_COMMAND\_OBJECT\_PROPERTIES\_DELETE          | OnDeleteProperties       | Deletes the properties that are identified by the given property keys.                                        |



## <span id="Using_Access_Scope_when_Setting_and_Retrieving_Properties_"></span><span id="using_access_scope_when_setting_and_retrieving_properties_"></span><span id="USING_ACCESS_SCOPE_WHEN_SETTING_AND_RETRIEVING_PROPERTIES_"></span>Using Access Scope when Setting and Retrieving Properties


The code that is found in the six property handlers in the WpdServiceSampleDriver is almost identical to the code that is found in the WpdHelloWorld driver. The exception is *service-level access scoping*, which is a new concept for Windows 7.

Service-level access scoping enables a driver to limit an enumeration to only those objects that are found under a given parent service. When a driver supports access scoping and an application calls the **IPortableDeviceService::Open** method (by passing the Plug and Play identifier for a given service), the application can only access the device, the given service, and the child objects of that service. The access scoping implementation may vary depending on the driver. WpdServiceSampleDriver shows this concept by using a bitmask to define two basic levels of scoping, device-level (less restrictive), and service-level (more restrictive). The following code example shows the difference between these levels:

```ManagedCPlusPlus
// Access Scope is a bit mask, where each bit enables access to a particular scope
// for example, contacts service is bit 1.   
// The next scope, if any, will be in bit 2
// Full device access is a combination of all, requires all bits to be set
typedef enum tagACCESS_SCOPE
{
    CONTACTS_SERVICE_ACCESS = 1,
    FULL_DEVICE_ACCESS = 0xFFFFFFFF
}ACCESS_SCOPE;
```

When the driver populates the enumeration tree with fake objects, the **FakeContent::RequiredScope** member for each content object is initialized with the appropriate scope. For example, a Contacts object can be initialized to be restricted to only Contacts Service-level access.

```ManagedCPlusPlus
class FakeContactContent : public FakeContent
{
public:
    FakeContactContent()
    {
        Format              = WPD_OBJECT_FORMAT_ABSTRACT_CONTACT;
        ContentType         = WPD_CONTENT_TYPE_CONTACT;
        RequiredScope       = CONTACTS_SERVICE_ACCESS;
    ...
    }
  ...
}
```

The following code example from the **OnGetSupportedProperties** handler function shows how access scoping was used to ensure that the correct property keys were returned:

```ManagedCPlusPlus
    // Add supported property keys for the specified object to the collection
    if (hr == S_OK)
    {
        ACCESS_SCOPE Scope = m_pDevice->GetAccessScope(pParams);
        hr = m_pDevice->GetSupportedProperties(Scope, wszObjectID, pKeys);
        CHECK_HR(hr, "Failed to add supported property keys for object &#39;%ws&#39;", wszObjectID);
    }
```

The code in the previous example calls the **FakeDevice::GetSupportedProperties** method, which is found in the file *FakeDevice.cpp*.

```ManagedCPlusPlus
HRESULT FakeDevice::GetSupportedProperties(
            ACCESS_SCOPE                  Scope,
    __in    LPCWSTR                       wszObjectID,
    __out   IPortableDeviceKeyCollection* pKeys)
{
    HRESULT      hr       = S_OK;
    FakeContent* pContent = NULL;

    if ((wszObjectID == NULL) ||
        (pKeys       == NULL))
    {
        hr = E_POINTER;
        CHECK_HR(hr, "Cannot have NULL parameter");
        return hr;
    }

    hr = GetContent(Scope, wszObjectID, &pContent);
    CHECK_HR(hr, "Failed to get content &#39;%ws&#39;", wszObjectID);

    if (hr == S_OK)
    {
        hr = pContent->GetSupportedProperties(pKeys);
        CHECK_HR(hr, "Failed to get supported properties for &#39;%ws&#39;", wszObjectID);
    }

    return hr;
}
```

This method first tries to retrieve the content for the given object. Then, if the method is able to retrieve the content, it retrieves the requested property keys.**FakeContent::GetContent** checks the scope and denies access if an application provides a less restrictive access scope (such as Device-wide access).

```ManagedCPlusPlus
HRESULT FakeContent::GetContent(
            ACCESS_SCOPE   Scope,
    __in    LPCWSTR        wszObjectID,
    __out   FakeContent**  ppContent)
{
    HRESULT hr = HRESULT_FROM_WIN32(ERROR_NOT_FOUND);

    if (CanAccess(Scope))
    {
    // Within access scope, proceed . . .
    }
    else
    {
        hr = E_ACCESSDENIED;
        CHECK_HR(hr, "GetContent: &#39;%ws&#39; was found but falls outside scope", wszObjectID);
    }

    return hr;
} 

bool FakeContent::CanAccess(
    ACCESS_SCOPE Scope)
{
    return ((Scope & RequiredScope) == RequiredScope);
}
```

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)









