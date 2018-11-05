---
Description: Support for enumeration commands (WpdBasicHardwareDriverSample)
title: Support for enumeration commands (WpdBasicHardwareDriverSample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for enumeration commands (WpdBasicHardwareDriverSample)


The sample driver supports three enumeration commands. These commands are processed initially by the **WpdObjectEnumerator::DispatchMessage** method that, in turn, invokes a corresponding command handler. The **DispatchMessage** method and the individual handlers are all found in the *WpdObjectEnum.cpp* file.

The information in the following table shows each of the supported property commands, together with the names of the handlers that **DispatchMessage** calls when it processes a given command. These commands are issued when an application calls one of several methods in the **IPortableDeviceContent** or the **IEnumPortableDeviceObjectIDs** interfaces.

| Command                                        | Handler     | Description                                                                |
|------------------------------------------------|-------------|----------------------------------------------------------------------------|
| WPD\_COMMAND\_OBJECT\_ENUMERATION\_START\_FIND | OnStartFind | Creates a new enumeration context and stores it in the client context map. |
| WPD\_COMMAND\_OBJECT\_ENUMERATION\_FIND\_NEXT  | OnFindNext  | Returns an object identifier for the requested object.                     |
| WPD\_COMMAND\_OBJECT\_ENUMERATION\_END\_FIND   | OnEndFind   | Performs necessary cleanup at the conclusion of an enumeration.            |

 

For the sample driver, the code remains intact for the WPD\_COMMAND\_OBJECT\_ENUMERATION\_FIND\_NEXT and WPD\_COMMAND\_OBJECT\_ENUMERATION\_END\_FIND handlers. However, a portion of the code was modified for the WPD\_COMMAND\_OBJECT\_ ENUMERATION\_START\_FIND handler.

## <span id="WPD_COMMAND_OBJECT_ENUMERATION_START_FIND"></span><span id="wpd_command_object_enumeration_start_find"></span>WPD\_COMMAND\_OBJECT\_ENUMERATION\_START\_FIND


The driver calls the **WpdObjectEnumerator::OnStartFind** handler in response to the WPD\_COMMAND\_OBJECT\_ENUMERATION\_START\_FIND command. The handler, in turn, creates, initializes, and adds a new enumeration context to the client context map. For the sample driver, the **InitializeEnumerationContext** helper function that is called from within the **OnStartFind** handler was modified.

The modifications to both the **OnStartFind** handler and the **InitializeEnumerationContext** helper function included removing support for objects that were no longer supported (the storage, folder, and file objects) and adding support for the sensor object. The following is the code for the **InitalizeEnumerationContext** helper function:

```cpp
VOID WpdObjectEnumerator::InitializeEnumerationContext(
    WpdObjectEnumeratorContext* pEnumeratorContext,
    CAtlStringW                 strParentObjectID)
{
    if (pEnumeratorContext == NULL)
    {
        return;
    }

    // Initialize the enumeration context with the parent object identifier
    pEnumeratorContext->m_strParentObjectID = strParentObjectID;

    // Our sample driver has a very simple object structure where we know
    // how many children are under each parent.
    // The eumeration context is initialized below with this information.
    if (strParentObjectID.CompareNoCase(L"") == 0)
    {
        // Clients passing an &#39;empty&#39; string for the parent are asking for the
        // &#39;DEVICE&#39; object.  We should return 1 child in this case.
        pEnumeratorContext->m_TotalChildren = 1;
    }
    else if (strParentObjectID.CompareNoCase(WPD_DEVICE_OBJECT_ID) == 0)
    {
        // The device object contains 1 child (the sensor object).
        pEnumeratorContext->m_TotalChildren = 1;
    }
    // If the sensor objects have children, add them here...
    else 
    {
        // The sensor object contains 0 children.
        pEnumeratorContext->m_TotalChildren = 0;
    }
}
```

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





