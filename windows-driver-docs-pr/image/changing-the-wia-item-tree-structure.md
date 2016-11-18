---
title: Changing the WIA Item Tree Structure
author: windows-driver-content
description: Changing the WIA Item Tree Structure
MS-HAID:
- 'WIA\_tree\_6e7a0162-0067-44cc-b5be-8c724d2593c2.xml'
- 'image.changing\_the\_wia\_item\_tree\_structure'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fa6c9d25-4435-43ee-a262-9e267b9a0a69
---

# Changing the WIA Item Tree Structure


## <a href="" id="ddk-changing-the-wia-item-tree-structure-si"></a>


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

```
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
    //    or read from the ROOT item&#39;s property set)
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
        // Free item&#39;s full item name, read above.
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Changing%20the%20WIA%20Item%20Tree%20Structure%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


