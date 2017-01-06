---
Description: Supporting the Enumeration Commands
MS-HAID: 'wpddk.the\_wpdservicesampledriver\_supporting\_wpd\_enumeration\_commands'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting the Enumeration Commands
---

# Supporting the Enumeration Commands


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20the%20Enumeration%20Commands%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




