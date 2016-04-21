---
title: Associating Callback Interfaces Example
author: windows-driver-content
description: Associating Callback Interfaces Example
ms.assetid: 6156730b-394c-451c-beea-1b25ba5a1fe3
keywords: ["callback objects WDK UMDF", "callback interfaces WDK UMDF", "associating callback interfaces WDK UMDF"]
---

# Associating Callback Interfaces Example


\[This topic applies to UMDF 1.*x*.\]

The following code example shows how a driver implements a create-instance method that the driver uses to [create the device callback object](creating-callback-objects-example.md). The driver allocates the callback context and associates the supplied **IUnknown** with one or more callback interfaces. The framework can subsequently use **QueryInterface** to discover the callback interfaces supported by the driver.

```
static HRESULT CreateInstance(
                  IUnknown **ppUnknown, 
                  IWDFDeviceInitialize *pDeviceInit,
                  HANDLE CompletionPort 
                  ) {
   ...
   // Allocate the callback context
   CMyDevice *pMyDevice = new CMyDevice();
   ...
   HRESULT hr;
   // Discover the callback interface
   hr = pMyDevice->QueryInterface( 
                      __uuidof(IUnknown), 
                      (void **) ppUnknown
                      );
   ...
   return hr;
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Associating%20Callback%20Interfaces%20Example%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




