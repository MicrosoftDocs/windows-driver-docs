---
title: Apply WIA Property Settings to the Hardware
description: Apply WIA Property Settings to the Hardware
ms.date: 03/27/2023
---

# Apply WIA Property Settings to the Hardware

When a WIA application initiates a data transfer, the WIA service gives the WIA minidriver the opportunity to apply current WIA property settings, and to apply any device-specific settings to the hardware. The WIA service then calls the [**IWiaMiniDrv::drvWriteItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties) method before it calls the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method. The latter method is called only when a WIA application initiates a data transfer. The WIA minidriver should use the WIA service functions to read the properties in its own driver item tree.

## Implement IWiaMiniDrv::drvWriteItemProperties

The WIA service calls the **IWiaMiniDrv::drvWriteItemProperties** method after the client requests a data transfer. The WIA service calls this method before it makes a call to [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata). The WIA minidriver should commit any settings it needs to the hardware before returning from this method.

When this method is called, the WIA minidriver has been committed to performing a data transfer. The WIA service will fail any application that attempts to acquire data at this time with a WIA\_ERROR\_BUSY error code.

The following example shows an implementation of the [**IWiaMiniDrv::drvWriteItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties) method:

```cpp
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
