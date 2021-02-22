---
title: Creating Callback Objects Example
description: Creating Callback Objects Example
keywords:
- callback objects WDK UMDF , example of creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Callback Objects Example


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The following code example shows how a driver creates a device callback object in the implementation of its [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method and then passes a pointer to the device callback interface in its call to the [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice) method to create the device.

```cpp
   HRESULT CMyDriver::OnDeviceAdd(
              IWDFDriver*           pDriver,
              IWDFDeviceInitialize* pDeviceInit
              ) {
      IUnknown *pDeviceCallback = NULL;
      ...
      HRESULT hr;
      // Create callback object
      hr = CMyDevice::CreateInstance( &pDeviceCallback,
                                      pDeviceInit,
                                      completionPort );
      ...
      // Create WDF device
      hr = pDriver->CreateDevice( pDeviceInit, 
                                  pDeviceCallback,
                                  &pIWDFDevice );
      ...
   }
```

 

