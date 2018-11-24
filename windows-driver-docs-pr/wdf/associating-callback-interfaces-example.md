---
title: Associating Callback Interfaces Example
description: Associating Callback Interfaces Example
ms.assetid: 6156730b-394c-451c-beea-1b25ba5a1fe3
keywords:
- callback objects WDK UMDF
- callback interfaces WDK UMDF
- associating callback interfaces WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Associating Callback Interfaces Example


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The following code example shows how a driver implements a create-instance method that the driver uses to [create the device callback object](creating-callback-objects-example.md). The driver allocates the callback context and associates the supplied **IUnknown** with one or more callback interfaces. The framework can subsequently use **QueryInterface** to discover the callback interfaces supported by the driver.

```cpp
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

 

 





