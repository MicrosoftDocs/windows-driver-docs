---
title: Reading WIA Item Properties by an Application
description: Reading WIA Item Properties by an Application
ms.assetid: e09f604e-451e-40dc-bc12-a077d4d263ee
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading WIA Item Properties by an Application





When an application makes a request to read WIA item properties, the WIA service calls the [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005) method.

The **IWiaMiniDrv::drvReadItemProperties** method should perform the following tasks:

1.  Determine whether the properties being read need run-time updates. To determine which WIA properties are being read, the WIA minidriver can use the PROPSPEC array (defined in the Microsoft Windows SDK documentation). It is recommended that the WIA minidriver determine the item type before processing the PROPSPEC array. This reduces the need to traverse the array on every **IWiaMiniDrv::drvReadItemProperties** call. If you have no run-time properties on the child items of this device, only root item property read requests will be processed.

2.  Update the current value by calling the [**wiasWriteMultiple**](https://msdn.microsoft.com/library/windows/hardware/ff549475) or **wiasWriteProp***Xxx* service functions, using the WIA property's ID. This updates the WIA property set that is stored in the driver item, and the WIA service returns the new value to the application.

If the WIA minidriver does not perform any run-time adjustments to WIA properties in this function, the WIA service automatically returns only the current WIA property value to the application. This function should be used only for properties such as device clocks, or WIA properties that require hardware-specific checks, such as document feeder status.

### <a href="" id="implementing-iwiaminidrv--drvreaditemproperties-"></a>Implementing IWiaMiniDrv::drvReadItemProperties

The **IWiaMiniDrv::drvReadItemProperties** method is called when an application tries to read a WIA item's properties. The WIA service first notifies the driver by calling this method. The WIA driver should verify that the property being read is correct. This is a good place to access the hardware for properties that require device status (such as [**WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff551386), or [**WIA\_DPA\_DEVICE\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff550303) if your device supports a clock).

It is important to note that a WIA driver should communicate with the hardware only on rare occasions. WIA drivers that communicate with hardware too much in this call will appear sluggish and slow.

The following example shows an implementation of the [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005) method:

```cpp
HRESULT _stdcall CWIADevice::drvReadItemProperties(
  BYTE           *pWiasContext,
  LONG           lFlags,
  ULONG          nPropSpec,
  const PROPSPEC *pPropSpec,
  LONG           *plDevErrVal)
{

  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if (!pWiasContext) {
      return E_INVALIDARG;
  }

  if (!plDevErrVal) {
      return E_INVALIDARG;
  }

  if (!pPropSpec) {
      return E_INVALIDARG;
  }

  *plDevErrVal = 0;

  LONG lWIAItemType = 0;
  HRESULT hr = wiasGetItemType(pWiasContext,&lWIAItemType);
  if(S_OK == hr) {
    //
    // perform custom operations depending on the type of
    // WIA item that was passed to drvReadItemProperties
    //

      if(lWIAItemType & WiaItemTypeRoot) {
      //
      // If the WIA_DPA_CONNECT_STATUS property ID is in the PROPSPEC
      // array, then read the latest "Connect Status".
      // If it is NOT then do nothing. (skip access to the hardware)
      //
      // NOTE: only read properties contained in the PROPSPEC array
      //     from the hardware that need device updates.
      //     If the property in PROPSPEC does not need to be read
      //     from the hardware, or updated, do nothing. The WIA service
      //     will supply the caller with the current value in the
      //     the WIA property set.
      //

          BOOL bReadLatestConnectStatus = FALSE;

      //
      // traverse the WIA PROPSPEC array, looking for known WIA
      // properties that require run-time updates, or needs to be
      // updated with hardware access.
      //

          for(ULONG ulIndex = 0; ulIndex < nPropSpec; ulIndex++) {

        //
        // look for WIA property IDs that really need hardware
        // access, or run-time adjusting.
        //

              if(pPropSpec[ulIndex].propid == WIA_DPA_CONNECT_STATUS) {
                  bReadLatestConnectStatus = TRUE;
              }
          }

        //
        // The item passed in is a ROOT item
        //

         if(bReadLatestConnectStatus) {

            //
            // WIA_DPA_CONNECT_STATUS should be updated from the
            // hardware
            //

 LONG lConnectStatus = HARDWARE_READ_ConnectStatus();

            //
            // update WIA_DPA_CONNECT_STATUS property value using
            // wiasWritePropLong ().  The pWiasContext passed in
            // already represents the current item to be written to.
            //

              hr = wiasWritePropLong(pWiasContext,WIA_DPA_CONNECT_STATUS,lConnectStatus);
              if(S_OK == hr) {

                //
                // The WIA_DPA_CONNECT_STATUS property was successfully updated
                //

              } else {

                //
                //  wiasWritePropLong() failed to write the WIA 
                //  property.  The WIA_DPA_CONNECT_STATUS
                //  property was NOT updated
                //

              }
          }

      } else {

        //
        // The item passed in is any other child item
        //

      }
  } else {

    //
    // wiasGetItemType() failed to get the current item type
    //
  }

  return hr;
}
```

 

 




