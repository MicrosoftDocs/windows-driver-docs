---
Description: Object Enumeration
MS-HAID: 'wpddk.object\_enumeration'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Object Enumeration
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Object%20Enumeration%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



