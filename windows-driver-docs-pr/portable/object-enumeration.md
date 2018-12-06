---
Description: Object Enumeration
title: Object Enumeration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Object Enumeration


The *WpdObjectEnum.cpp* and *WpdObjectEnum.h* files contain the member functions that enumerate objects that are supported by the device.

When a Windows-based application invokes**IPortableDeviceContent::EnumObject** or one of the two methods of the **IEnumPortableDeviceObjectIDs** interface, this call, in turn, triggers one of three command handlers in the **WpdObjectEnumerator** class. The following table identifies the mapping of application methods to **WpdObjectEnumerator** driver methods.

|                                           |                                         |
|-------------------------------------------|-----------------------------------------|
| **IPortableDeviceContent Method**         | **WpdObjectEnumerator Command Handler** |
| **IPortableDeviceContent::EnumObjects**   | **OnStartFind**                         |
| **IEnumPortableDeviceObjectIDs::Next**    | **OnFindNext**                          |
| **IEnumPortableDeviceObjectIDs::Release** | **OnEndFind**                           |

 

The **WpdObjectEnumerator** command handlers are invoked by the **WpdObjectEnumerator::DispatchWpdMessage** method. The following excerpt from the sample driver contains the code for **WpdObjectEnumerator::DispatchWpdMessage.**

```ManagedCPlusPlus
HRESULT WpdObjectEnumerator::DispatchWpdMessage(const PROPERTYKEY&     Command,
                                                IPortableDeviceValues* pParams,
                                                IPortableDeviceValues* pResults)
{
    HRESULT hr = S_OK;

    if (hr == S_OK)
    {
        if (Command.fmtid != WPD_CATEGORY_OBJECT_ENUMERATION)
        {
            hr = E_INVALIDARG;
            CHECK_HR(hr, "This object does not support this command category %ws",CComBSTR(Command.fmtid));
        }
    }

    if (hr == S_OK)
    {
        if (Command.pid == WPD_COMMAND_OBJECT_ENUMERATION_START_FIND.pid)
        {
            hr = OnStartFind(pParams, pResults);
            CHECK_HR(hr, "Failed to begin enumeration");
        }
        else if (Command.pid == WPD_COMMAND_OBJECT_ENUMERATION_FIND_NEXT.pid)
        {
            hr = OnFindNext(pParams, pResults);
            if(FAILED(hr))
            {
                CHECK_HR(hr, "Failed to find next object");
            }
        }
        else if (Command.pid == WPD_COMMAND_OBJECT_ENUMERATION_END_FIND.pid)
        {
            hr = OnEndFind(pParams, pResults);
            CHECK_HR(hr, "Failed to end enumeration");
        }
        else
        {
            hr = E_NOTIMPL;
            CHECK_HR(hr, "This object does not support this command id %d", Command.pid);
        }
    }

    return hr;
}
```

 

 




