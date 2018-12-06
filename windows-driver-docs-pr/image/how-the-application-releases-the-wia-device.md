---
title: How the Application Releases the WIA Device
description: How the Application Releases the WIA Device
ms.assetid: 694daed4-d794-4835-a052-27cc498baa10
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How the Application Releases the WIA Device





When an application has no further need of a WIA device, it calls the **IWiaItem::Release** method (described in the Microsoft Windows SDK documentation). When the last reference to any WIA item is released, the WIA service calls the [**IWiaMiniDrv::drvUnInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff545010) method. A WIA minidriver should use this method primarily to manage resources associated with all connected applications. When an application closes, the resources associated with its item tree are no longer needed. The WIA minidriver should keep track of all connected applications by incrementing a reference counter in [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986) and decrementing that reference counter in **IWiaMiniDrv::drvUnInitializeWia**. Freeing resources at this point can cause problems for other connected applications. When the reference counter reaches zero there are no more applications connected to the WIA minidriver. The minidriver should clean up any allocated resources it acquired during application connections.

**Note**  **** The **IWiaMiniDrv::drvUnInitializeWia** method does not unload the driver. The driver may be called again to process events, or when an application intends to communicate with it. A call to this method does not mean that all clients are disconnected. There should be one call per client disconnect.
Each call to the **IWiaMiniDrv::drvUnInitializeWia** method should be paired with a corresponding call to the **IWiaMiniDrv::drvInitializeWia** method.

The WIA driver should *not* free any driver resources in this method call unless it can safely determine that *no* applications are currently connected.

To determine the current application connection count, the WIA driver should increment a class member variable as a reference counter to keep track of the method calls to **IWiaMiniDrv::drvInitializeWia** (incrementing the counter) and **IWiaMiniDrv::drvUnInitializeWia** (decrementing the counter).

 

The following example shows an implementation of the **IWiaMiniDrv::drvUnInitializeWia** method.

```cpp
HRESULT _stdcall CWIADevice::drvUnInitializeWia(BYTE *pWiasContext)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if (!pWiasContext) {
      return E_INVALIDARG;
  }

  InterlockedDecrement(&m_lClientsConnected);

  //
  // make sure we never decrement below zero (0)
  //

  if(m_lClientsConnected < 0){
      m_lClientsConnected = 0;
  return S_OK;
  }

  //
  // check for connected applications.
  //

  if(m_lClientsConnected == 0){

      //
      // There are no application clients connected to this WIA driver
      //

  }

  return S_OK;
}
```

 

 




