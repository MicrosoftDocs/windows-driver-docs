---
Description: Property Deletion
title: Property Deletion
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Deletion


When a Windows Portable Devices (WPD) application calls the **IPortableDeviceProperties::Delete** method, this method, in turn, triggers a call to the **WpdObjectProperties::OnDelete** method in the sample driver. Because none of the object properties in the sample driver can be deleted, this method simply returns E\_ACCESSDENIED.

```ManagedCPlusPlus
HRESULT WpdObjectProperties::OnDeleteProperties(
    IPortableDeviceValues*  pParams,
    IPortableDeviceValues*  pResults)
{
    HRESULT hr = E_ACCESSDENIED;

    UNREFERENCED_PARAMETER(pParams);
    UNREFERENCED_PARAMETER(pResults);

    // This driver has no properties which can be deleted.

    return hr;
}
```

 

 




