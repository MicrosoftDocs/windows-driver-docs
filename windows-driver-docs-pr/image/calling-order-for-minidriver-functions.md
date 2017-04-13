---
title: Calling Order for Minidriver Functions
author: windows-driver-content
description: Calling Order for Minidriver Functions
ms.assetid: 0e51d29c-964d-44d5-86be-095601286f94
---

# Calling Order for Minidriver Functions


## <a href="" id="ddk-calling-order-for-minidriver-functions-si"></a>


When a minidriver is started, it calls some of the older STI entry points, such as [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824), and [**IStiUSD::GetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543823). As soon as the first application attempts to communicate with the device, the WIA service calls [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986). It is in this function that the minidriver should construct the item tree.

The WIA service next calls [**IWiaMiniDrv::drvInitItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff544989) for each item in the tree. The minidriver should create all the properties relevant to the item. In some situations, it might be wise to create an empty property and fill in its data later. For example, for better performance, image thumbnails on cameras should be read in only when the WIA service specifically asks for them, as described below.

The next function to be called depends on the application and device type. Typically, an application's most common operation is transferring data. For scanners, the application first sets up the properties (for example, data type and extent) that define the image it wants to get from the device. The WIA service calls [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017) when the application changes any properties. The minidriver should check that the properties are valid, communicating with the device, if necessary. The minidriver should generally avoid setting the properties in that function, because another application could set the properties to different values before the data transfer takes place.

To transfer data, the WIA service calls [**IWiaMiniDrv::drvLockWiaDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544995), [**IWiaMiniDrv::drvWriteItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545020), [**IWiaMiniDrv::drvAcquireItemData**](https://msdn.microsoft.com/library/windows/hardware/ff543956), and [**IWiaMiniDrv::drvUnLockWiaDevice**](https://msdn.microsoft.com/library/windows/hardware/ff545012), in that order. The calls to lock and unlock the device guarantee that no other application accesses the device during the transfer. For scanners, **IWiaMiniDrv::drvWriteItemProperties** should send properties such as position, extent, and resolution to the device. Camera drivers typically do not need to send any properties to the device. **IWiaMiniDrv::drvAcquireItemData** should retrieve the image data from the device and send it back to the application via the WIA service, using the [IWiaMiniDrvCallback COM interface](iwiaminidrvcallback-com-interface.md).

For cameras, if an application wants to display thumbnails for the images, the WIA service calls [**IWiaMiniDrv::drvReadItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545005) on each image. The minidriver should read the thumbnail at that point and cache it in the driver item context. It is important to cache the thumbnail, because multiple applications might ask for the thumbnail, resulting in multiple calls to **IWiaMiniDrv::drvReadItemProperties**. If the minidriver reads the thumbnail each time an application asks for it, performance suffers.

One other special consideration for cameras is root item properties that affect settings on the camera (shutter speed, for example). When the application changes these properties, the WIA service calls [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017). The minidriver can communicate with the camera, if necessary, to validate the property settings. This function, however, is not the best place to change settings on the camera, because another application also can change the properties. The minidriver should update all of the camera settings from the root item properties when the [**IWiaMiniDrv::drvDeviceCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543967) function is called to capture a new image.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Calling%20Order%20for%20Minidriver%20Functions%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


