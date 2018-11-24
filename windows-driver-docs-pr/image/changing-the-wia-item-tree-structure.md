---
title: Changing the WIA Item Tree Structure
description: Changing the WIA Item Tree Structure
ms.assetid: fa6c9d25-4435-43ee-a262-9e267b9a0a69
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing the WIA Item Tree Structure





A WIA minidriver has the ability to change the WIA item tree structure at any time. When the minidriver makes a change to the WIA item tree, the minidriver must notify the WIA service. The WIA service then notifies all connected WIA applications. After the notification is received, the WIA application must enumerate the WIA item tree to determine the result of any changes.

A minidriver uses the WIA service utility function, [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296), to communicate changes in the tree structure to the WIA service. A WIA minidriver can queue only those events that were reported in [**IWiaMiniDrv::drvGetCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff543977). For more information about reporting WIA events, see [Event Reporting](event-reporting.md).

### Explanation of the IWiaMiniDrv::drvDeleteItem Implementation

The WIA service calls the [**IWiaMiniDrv::drvDeleteItem**](https://msdn.microsoft.com/library/windows/hardware/ff543961) method when a WIA application calls the **IWiaItem::DeleteItem** method (described in the Microsoft Windows SDK documentation) to delete a WIA item.

The WIA service verifies the following before calling this method:

-   The item is not a root item.

-   The item is has no children.

-   The access rights of the item allow deletion.

Because the WIA service verifies these criteria, it is not necessary for the WIA driver to do so as well.

The following code example shows an implementation of **IWiaMiniDrv::drvDeleteItem**:

```cpp
HRESULT _stdcall CWIADevice::drvDeleteItem(BYTE *pWiasContext,
                                           LONG lFlags,
                                           LONG *plDevErrVal)
{
    //
    // If the caller did not pass in the correct parameters,
    // then fail the call with E_INVALIDARG.
    //

    if ((!pWiasContext) || (!plDevErrVal))
    {
        return E_INVALIDARG;
    }

    *plDevErrVal = 0;

    HRESULT hr = S_OK;

    //
    // Two pieces of information are needed to queue an event:
    // 1. Full item name
    // 2. Device ID (passed in from drvInitializeWia,
    //    or read from the ROOT item's property set)
    //

    BSTR bstrFullItemName = NULL;
    hr = wiasReadPropStr(pWiasContext,
                         WIA_IPA_FULL_ITEM_NAME,
                         &bstrFullItemName,NULL,TRUE);
    if (hr == S_OK)
    {
        hr = HARDWARE_DELETE_DATA_FOR_ITEM();
        if (hr == S_OK)
        {
            //
            // Use m_bstrDeviceID cached from the
            // drvInitializeWia method call.
            //

            hr = wiasQueueEvent(m_bstrDeviceID,
                                &WIA_EVENT_ITEM_DELETED,
                                bstrFullItemName);
        }

        //
        // Free item's full item name, read above.
        //

        if (bstrFullItemName)
        {
            SysFreeString(bstrFullItemName);
            bstrFullItemName = NULL;
        }
    }

    //
    // Returning S_OK will instruct the WIA service to remove the WIA
    // item from the item tree. The WIA minidriver should only remove
    // any associated data corresponding to the target item.
    //

    return hr;
}
```

 

 




