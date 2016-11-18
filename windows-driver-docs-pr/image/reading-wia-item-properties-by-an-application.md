---
title: Reading WIA Item Properties by an Application
author: windows-driver-content
description: Reading WIA Item Properties by an Application
MS-HAID:
- 'WIA\_drv\_basic\_ff15d639-ba2a-4b34-9ce6-70813673c4e2.xml'
- 'image.reading\_wia\_item\_properties\_by\_an\_application'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e09f604e-451e-40dc-bc12-a077d4d263ee
---

# Reading WIA Item Properties by an Application


## <a href="" id="ddk-reading-wia-item-properties-by-an-application-si"></a>


When an application makes a request to read WIA item properties, the WIA service calls the [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005) method.

The **IWiaMiniDrv::drvReadItemProperties** method should perform the following tasks:

1.  Determine whether the properties being read need run-time updates. To determine which WIA properties are being read, the WIA minidriver can use the PROPSPEC array (defined in the Microsoft Windows SDK documentation). It is recommended that the WIA minidriver determine the item type before processing the PROPSPEC array. This reduces the need to traverse the array on every **IWiaMiniDrv::drvReadItemProperties** call. If you have no run-time properties on the child items of this device, only root item property read requests will be processed.

2.  Update the current value by calling the [**wiasWriteMultiple**](https://msdn.microsoft.com/library/windows/hardware/ff549475) or **wiasWriteProp***Xxx* service functions, using the WIA property's ID. This updates the WIA property set that is stored in the driver item, and the WIA service returns the new value to the application.

If the WIA minidriver does not perform any run-time adjustments to WIA properties in this function, the WIA service automatically returns only the current WIA property value to the application. This function should be used only for properties such as device clocks, or WIA properties that require hardware-specific checks, such as document feeder status.

### <a href="" id="implementing-iwiaminidrv--drvreaditemproperties-"></a>Implementing IWiaMiniDrv::drvReadItemProperties

The **IWiaMiniDrv::drvReadItemProperties** method is called when an application tries to read a WIA item's properties. The WIA service first notifies the driver by calling this method. The WIA driver should verify that the property being read is correct. This is a good place to access the hardware for properties that require device status (such as [**WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff551386), or [**WIA\_DPA\_DEVICE\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff550303) if your device supports a clock).

It is important to note that a WIA driver should communicate with the hardware only on rare occasions. WIA drivers that communicate with hardware too much in this call will appear sluggish and slow.

The following example shows an implementation of the [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005) method:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Reading%20WIA%20Item%20Properties%20by%20an%20Application%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


