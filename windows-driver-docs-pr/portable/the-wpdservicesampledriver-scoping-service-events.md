---
Description: Scoping Service Events
title: Scoping Service Events
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





