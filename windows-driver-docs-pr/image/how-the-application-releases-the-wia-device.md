---
title: How the Application Releases the WIA Device
author: windows-driver-content
description: How the Application Releases the WIA Device
MS-HAID:
- 'WIA\_drv\_basic\_66c11c75-ca8f-422e-978c-f2fcf806cb32.xml'
- 'image.how\_the\_application\_releases\_the\_wia\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 694daed4-d794-4835-a052-27cc498baa10
---

# How the Application Releases the WIA Device


## <a href="" id="ddk-how-the-application-releases-the-wia-device-si"></a>


When an application has no further need of a WIA device, it calls the **IWiaItem::Release** method (described in the Microsoft Windows SDK documentation). When the last reference to any WIA item is released, the WIA service calls the [**IWiaMiniDrv::drvUnInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff545010) method. A WIA minidriver should use this method primarily to manage resources associated with all connected applications. When an application closes, the resources associated with its item tree are no longer needed. The WIA minidriver should keep track of all connected applications by incrementing a reference counter in [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986) and decrementing that reference counter in **IWiaMiniDrv::drvUnInitializeWia**. Freeing resources at this point can cause problems for other connected applications. When the reference counter reaches zero there are no more applications connected to the WIA minidriver. The minidriver should clean up any allocated resources it acquired during application connections.

**Note**  **** The **IWiaMiniDrv::drvUnInitializeWia** method does not unload the driver. The driver may be called again to process events, or when an application intends to communicate with it. A call to this method does not mean that all clients are disconnected. There should be one call per client disconnect.
Each call to the **IWiaMiniDrv::drvUnInitializeWia** method should be paired with a corresponding call to the **IWiaMiniDrv::drvInitializeWia** method.

The WIA driver should *not* free any driver resources in this method call unless it can safely determine that *no* applications are currently connected.

To determine the current application connection count, the WIA driver should increment a class member variable as a reference counter to keep track of the method calls to **IWiaMiniDrv::drvInitializeWia** (incrementing the counter) and **IWiaMiniDrv::drvUnInitializeWia** (decrementing the counter).

 

The following example shows an implementation of the **IWiaMiniDrv::drvUnInitializeWia** method.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20How%20the%20Application%20Releases%20the%20WIA%20Device%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


