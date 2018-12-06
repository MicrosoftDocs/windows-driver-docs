---
Description: Support for enumeration commands (WpdServiceSampleDriver)
title: Support for enumeration commands (WpdServiceSampleDriver)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for enumeration commands (WpdServiceSampleDriver)


The sample driver supports three enumeration commands. These commands are processed initially by the **WpdObjectEnumerator::DispatchMessage** method that, in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are all found in the *WpdObjectEnum.cpp* file.

Each enumeration request is associated with an enumeration context, which identifies the access scope that a given application receives. For example, an application that calls **IPortableDevice::Open** has device-wide access and receives all objects within the hierarchy, while an application that calls **IPortableDeviceService::Open** has service-level access and only receives the Device Object, the Service Object, and all children within the Service Object hierarchy.

The following table shows each of the supported enumeration commands, together with the names of the handlers that **DispatchMessage** calls when it processes a given command. These commands are issued when an application calls one of several methods in the **IPortableDeviceContent** or the **IEnumPortableDeviceObjectIDs** interfaces.

| Command                                        | Handler     | Description                                                                |
|------------------------------------------------|-------------|----------------------------------------------------------------------------|
| WPD\_COMMAND\_OBJECT\_ENUMERATION\_START\_FIND | OnStartFind | Creates a new enumeration context and stores it in the client context map. |
| WPD\_COMMAND\_OBJECT\_ENUMERATION\_FIND\_NEXT  | OnFindNext  | Returns an object identifier for the requested object.                     |
| WPD\_COMMAND\_OBJECT\_ENUMERATION\_END\_FIND   | OnEndFind   | Performs necessary cleanup when the enumeration is complete.               |

 

For the sample driver, the code intact for the WPD\_COMMAND\_OBJECT\_ENUMERATION\_END\_FIND handler is almost identical to the code that is found in the WpdHellowWorldDriver sample. However, we modified a portion of the code for the WPD\_COMMAND\_OBJECT\_ ENUMERATION\_START\_FIND and the WPD\_OBJECT\_ENUMERATION\_FIND\_NEXT handlers to support service-level access.

## <span id="WPD_COMMAND_OBJECT_ENUMERATION_START_FIND"></span><span id="wpd_command_object_enumeration_start_find"></span>WPD\_COMMAND\_OBJECT\_ENUMERATION\_START\_FIND


The driver calls the **WpdObjectEnumerator::OnStartFind** handler in response to the WPD\_COMMAND\_OBJECT\_ENUMERATION\_START\_FIND command. The handler, in turn, creates, initializes, and adds a new enumeration context to the client context map.

For the sample driver, each client enumeration request is associated with an enumeration context, and this context identifies the access scope for that client.

```ManagedCPlusPlus
        if (pEnumeratorContext != NULL)
        {
            ACCESS_SCOPE Scope = m_pDevice->GetAccessScope(pParams);
            m_pDevice->InitializeEnumerationContext(Scope, wszParentID, pEnumeratorContext);

            // Add the enumeration context to the client context map.  This calls AddRef() on pEnumeratorContext
            hr = pContextMap->Add(pEnumeratorContext, strEnumContext);
            CHECK_HR(hr, "Failed to add the enumeration context");
        }
```

For more information about access scoping and its purpose, see the [Supporting the Property Commands](the-wpdservicesampledriver-supporting-wpd-property-commands.md) topic.

## <span id="WPD_OBJECT_ENUMERATION_FIND_NEXT"></span><span id="wpd_object_enumeration_find_next"></span>WPD\_OBJECT\_ENUMERATION\_FIND\_NEXT


The driver calls the **WpdObjectEnumerator::OnFindNext** handler in response to the WPD\_COMMAND\_OBJECT\_ENUMERATION\_FIND\_NEXT command. The handler, in turn, calls the **FakeDevice::FindNext** method, and this method, in turn, calls the **FakeContent::FindNext** method.

The following code example shows the **OnFindNext** handler calling the **FakeDevice::FindNext** method:

```ManagedCPlusPlus
    if ((hr == S_OK) && (pEnumeratorContext != NULL))
    {
        hr = m_pDevice->FindNext(dwNumObjectsRequested, pEnumeratorContext, pObjectIDCollection, &dwNumObjectsEnumerated);
        CHECK_HR(hr, "Failed to get the next object");
    }
```

The following code example shows the **FakeDevice::FindNext** method calling the **FakeContent::FindNext** method:

```ManagedCPlusPlus
                    FakeContent* pChild = NULL;
                    if (pContent->FindNext(pEnumContext->m_Scope, dwStartIndex, &pChild))
                    {
                        hr = AddStringValueToPropVariantCollection(pObjectIDCollection, pChild->ObjectID);
                        CHECK_HR(hr, "Failed to add object [%ws]", pChild->ObjectID);

                        if (hr == S_OK)
                        {
                            // Update the number of children we are returning for this enumeration call
                            dwStartIndex++;
                            NumObjectsEnumerated++;
                        }
                    }
```

## <span id="related_topics"></span>Related topics


****
[The WpdServiceSampleDriver](the-wpdservicesampledriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





