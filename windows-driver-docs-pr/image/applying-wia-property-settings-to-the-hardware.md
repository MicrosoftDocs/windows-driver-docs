---
title: Applying WIA Property Settings to the Hardware
author: windows-driver-content
description: Applying WIA Property Settings to the Hardware
ms.assetid: adb85f77-1814-427b-8b75-0bfce4c8ca06
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Applying WIA Property Settings to the Hardware


## <a href="" id="ddk-applying-wia-property-settings-to-the-hardware-si"></a>


When a WIA application initiates a data transfer, the WIA service gives the WIA minidriver the opportunity to apply current WIA property settings, and to apply any device-specific settings to the hardware. The WIA service then calls the [**IWiaMiniDrv::drvWriteItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545020) method before it calls the [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956) method. The latter method is called only when a WIA application initiates a data transfer. The WIA minidriver should use the WIA service functions to read the properties in its own driver item tree.

### <a href="" id="implementing-iwiaminidrv-drvwriteitemproperties"></a>Implementing IWiaMiniDrv::drvWriteItemProperties

The WIA service calls the **IWiaMiniDrv::drvWriteItemProperties** method after the client requests a data transfer. The WIA service calls this method before it makes a call to [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956). The WIA minidriver should commit any settings it needs to the hardware before returning from this method.

When this method is called, the WIA minidriver has been committed to performing a data transfer. The WIA service will fail any application that attempts to acquire data at this time with a WIA\_ERROR\_BUSY error code.

The following example shows an implementation of the [**IWiaMiniDrv::drvWriteItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545020) method:

```
HRESULT _stdcall CWIADevice::drvWriteItemProperties(
  BYTE                      *pWiasContext,
  LONG                      lFlags,
  PMINIDRV_TRANSFER_CONTEXT pmdtc,
  LONG                      *plDevErrVal)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if (!pWiasContext) {
      return E_INVALIDARG;
  }

 if (!pmdtc) {
      return E_INVALIDARG;
  }

  if (!plDevErrVal) {
      return E_INVALIDARG;
  }

  HRESULT hr = S_OK;
  *plDevErrVal = 0;
  PROPVARIANT pv[2];
  PROPSPEC ps[2] = {
      {PRSPEC_PROPID, WIA_IPS_XRES},
      {PRSPEC_PROPID, WIA_IPS_YRES}
  };

  //
  // initialize propvariant structures
  //

  pv[0].vt = VT_I4;   // X resolution is a LONG value
  pv[1].vt = VT_I4;   // Y resolution is a LONG value

  //
  // read 2 WIA item properties (X and Y resolution)
  //

  hr = wiasReadMultiple(pWiasContext, 2, ps, pv, NULL);

  if (hr == S_OK) {

    //
    // write current X and Y resolution values, read from the
    // the WIA property set, and write them to the device.
    //

      hr = SetMyDeviceXResolution(pv[0].lVal);
      if(S_OK == hr) {
          hr = SetMyDeviceYResolution(pv[1].lVal);
          if(FAILED(hr)) {

            //
            // could not set Y resolution to device
            //

          }
   } else {

        //
        // could not set X resolution to device
        //

      }
  }
  return hr;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Applying%20WIA%20Property%20Settings%20to%20the%20Hardware%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


