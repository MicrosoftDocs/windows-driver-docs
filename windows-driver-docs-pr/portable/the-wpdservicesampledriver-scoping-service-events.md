---
Description: Scoping Service Events
MS-HAID: 'wpddk.the\_wpdservicesampledriver\_scoping\_service\_events'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Scoping Service Events
---

# Scoping Service Events


By default, WPD broadcasts service events to all client applications (even clients that are connected to other services). To limit the scope of the broadcast, a driver must set the WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID event parameter to the ObjectID of the service to which the broadcast should be limited.

The following code example shows how **WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBEJCT\_ID** is added to the event parameters in **FakeDevice::SetPropertyValues**, to indicate that an object has been updated:

```ManagedCPlusPlus
        if (SUCCEEDED(hr) && (*pbObjectChanged)) 
        {
            HRESULT hrEvent = pEventParams->SetGuidValue(WPD_EVENT_PARAMETER_EVENT_ID, WPD_EVENT_OBJECT_UPDATED);
            CHECK_HR(hrEvent, "Failed to add WPD_EVENT_PARAMETER_EVENT_ID");

        . . .

            if (hrEvent == S_OK)
            {
                // Adding this event parameter will allow WPD to scope this event to the container functional object
                hrEvent = pEventParams->SetStringValue(WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID, pContent->ContainerFunctionalObjectID);
                CHECK_HR(hrEvent, "Failed to add WPD_OBJECT_CONTAINER_FUNCTIONAL_OBJECT_ID");
            }
        }
```

For objects within the Contact Service, *pContent-&gt;ContainerFunctionalObjectID* contains the Contact Service’s object identifier. If this parameter is specified, WPD matches this event parameter and filters the event so that only other clients that connect to the same Contacts Service will receive this event.

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Scoping%20Service%20Events%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




