---
title: Informing an Application of Item Tree Changes
author: windows-driver-content
description: Informing an Application of Item Tree Changes
ms.assetid: 6b3cb1d0-ab9f-4895-8c3f-f66c398960bb
---

# Informing an Application of Item Tree Changes


## <a href="" id="ddk-informing-an-application-of-item-tree-changes-si"></a>


A minidriver for a WIA device must be able to inform applications associated with WIA devices of any changes to the device's item tree. For example, if an application displays a user interface showing thumbnails of the pictures on a camera, a WIA minidriver should be able to notify an application's user interface to not display thumbnails of pictures that the user has already deleted.

The following sample implementation of the [**IWiaMiniDrv::drvDeviceCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543967) method shows how a WIA minidriver can respond to a command sent to it by the WIA service, and pass the command on to the device. After the WIA minidriver issues the command to the device, the minidriver informs applications that the device item tree has changed. In this implementation, the method determines that the WIA service has issued the "Take Picture" command (WIA\_CMD\_TAKE\_PICTURE). The method calls the **TakePicture** method on the root item (the item for the device), and informs any connected applications that the item tree now contains the new picture. (Both WIA\_CMD\_TAKE\_PICTURE and **TakePicture** are described in the Microsoft Windows SDK documentation.) The minidriver does this by calling the [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296) function.

Note that when the minidriver sends out the event that indicates that the tree has been updated, *all* listening applications are informed of the change, not just the caller. For example, if a user has the Explorer view of the camera open, and uses Microsoft Paint to acquire a new picture, the Explorer window also shows the new picture when it arrives, because it listens for such events.

The following example shows an implementation of the **IWiaMiniDrv::drvDeviceCommand** method.

```
HRESULT _stdcall CWIADevice::drvDeviceCommand(
  BYTE        *pWiasContext,
  LONG        lFlags,
  const GUID  *plCommand,
  IWiaDrvItem **ppWiaDrvItem,
  LONG        *plDevErrVal)
{
  //
  // If the caller did not pass in the correct parameters, 
  // then fail the call and return E_INVALIDARG.
  //

  if ((!pWiasContext)||(!plDevErrVal)||(!plCommand)) {
    return E_INVALIDARG;
  }

  *plDevErrVal = 0;
  HRESULT hr = E_NOTIMPL;

  //
  //  Check which command was issued
  //

  if (*plCommand == WIA_CMD_TAKE_PICTURE) {

    //
    // process command here
    //

      hr = HARDWARE_SNAP_PHOTO();
  }
  return hr;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Informing%20an%20Application%20of%20Item%20Tree%20Changes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


