---
title: Creating Callback Objects Example
description: Creating Callback Objects Example
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 4476c2f0-12ba-4678-b20e-bde7e81df01d
keywords: ["callback objects WDK UMDF example of creating"]
---

# Creating Callback Objects Example


\[This topic applies to UMDF 1.*x*.\]

The following code example shows how a driver creates a device callback object in the implementation of its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method and then passes a pointer to the device callback interface in its call to the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to create the device.

```
   HRESULT CMyDriver::OnDeviceAdd(
              IWDFDriver*           pDriver,
              IWDFDeviceInitialize* pDeviceInit
              ) {
      IUnknown *pDeviceCallback = NULL;
      ...
      HRESULT hr;
      // Create callback object
      hr = CMyDevice::CreateInstance( &amp;pDeviceCallback,
                                      pDeviceInit,
                                      completionPort );
      ...
      // Create WDF device
      hr = pDriver->CreateDevice( pDeviceInit, 
                                  pDeviceCallback,
                                  &amp;pIWDFDevice );
      ...
   }
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20Callback%20Objects%20Example%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




