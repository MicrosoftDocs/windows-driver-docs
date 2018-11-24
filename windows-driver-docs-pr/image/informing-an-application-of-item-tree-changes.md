---
title: Informing an Application of Item Tree Changes
description: Informing an Application of Item Tree Changes
ms.assetid: 6b3cb1d0-ab9f-4895-8c3f-f66c398960bb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Informing an Application of Item Tree Changes





A minidriver for a WIA device must be able to inform applications associated with WIA devices of any changes to the device's item tree. For example, if an application displays a user interface showing thumbnails of the pictures on a camera, a WIA minidriver should be able to notify an application's user interface to not display thumbnails of pictures that the user has already deleted.

The following sample implementation of the [**IWiaMiniDrv::drvDeviceCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543967) method shows how a WIA minidriver can respond to a command sent to it by the WIA service, and pass the command on to the device. After the WIA minidriver issues the command to the device, the minidriver informs applications that the device item tree has changed. In this implementation, the method determines that the WIA service has issued the "Take Picture" command (WIA\_CMD\_TAKE\_PICTURE). The method calls the **TakePicture** method on the root item (the item for the device), and informs any connected applications that the item tree now contains the new picture. (Both WIA\_CMD\_TAKE\_PICTURE and **TakePicture** are described in the Microsoft Windows SDK documentation.) The minidriver does this by calling the [**wiasQueueEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549296) function.

Note that when the minidriver sends out the event that indicates that the tree has been updated, *all* listening applications are informed of the change, not just the caller. For example, if a user has the Explorer view of the camera open, and uses Microsoft Paint to acquire a new picture, the Explorer window also shows the new picture when it arrives, because it listens for such events.

The following example shows an implementation of the **IWiaMiniDrv::drvDeviceCommand** method.

```cpp
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

 

 




