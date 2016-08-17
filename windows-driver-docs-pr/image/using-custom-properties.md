---
title: Using Custom Properties
description: Using Custom Properties
MS-HAID:
- 'WIA\_drv\_basic\_1d962c5c-055d-4788-9acc-d59e3f133530.xml'
- 'image.using\_custom\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cf4e728f-7900-4849-ab1c-135f9fec9713
---

# Using Custom Properties


## <a href="" id="ddk-using-custom-properties-si"></a>


A WIA driver can define its own custom properties. Callers can manipulate custom properties just as they would normal WIA properties. However, only your application or custom UI module can access these custom properties.

WIA drivers should define the custom properties to have property identifiers that are offset by WIA\_PRIVATE\_DEVPROP for device properties, and use WIA\_PRIVATE\_ITEMPROP for normal item properties, such as inside [**IWiaMiniDrv::drvInitItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff544989). For more information, see [Defining Custom Properties](defining-custom-properties.md).

There are two ways to pass custom parameters to WIA drivers.

The first option is to use the **IWiaItemExtras::Escape** method (described in the Microsoft Windows SDK documentation). This is similar to the [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) method, but it allows callers to use WIA directly, instead of using STI methods. Using **IWiaItemExtras::Escape**, you can pass any information to the driver, and the driver can pass any information back. The WIA service manages only those buffers passed between the caller and the driver.

The second option is to use custom properties. Using the **IWiaItemExtras::Escape** method is more flexible than using custom WIA properties, but custom WIA properties allow you to store information in the item's property stream so that the driver can read the information at another time.

The following two sample code snippets show how to use custom properties to pass custom parameters to and from your driver.

[Sample Code to Create Custom Properties](sample-code-to-create-custom-properties.md)

[Sample Code to Set Custom Properties](sample-code-to-set-custom-properties.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Using%20Custom%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




