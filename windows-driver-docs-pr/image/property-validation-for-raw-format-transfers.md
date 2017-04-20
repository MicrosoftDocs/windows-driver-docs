---
title: Property Validation for RAW Format Transfers
author: windows-driver-content
description: Property Validation for RAW Format Transfers
ms.assetid: ad58f94e-d59e-4d04-be27-cc87f89f3d76
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Property Validation for RAW Format Transfers


The driver must validate the WIA property settings prior to a RAW format data transfer. The WIA properties must be set as follows:

<a href="" id="wia-ips-xpos--wia-ips-ypos"></a>[**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663), [**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671)  
These properties are set the same for RAW as they are for other image formats. These properties contain the coordinates, in pixels, of the upper-left corner of the selected image

<a href="" id="wia-ips-xres--wia-ips-yres"></a>[**WIA\_IPS\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff552665), [**WIA\_IPS\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff552673)  
These properties are set the same for RAW as they are for other image formats. These properties contain the current horizontal and vertical (respectively) resolution, in pixels per inch, for the device

<a href="" id="wia-ips-xextent--wia-ips-yextent"></a>[**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661), [**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669)  
These properties are set by the application and are read by and updated by the driver. Because the properties might be changed from their original values, the application must read the value stored in these properties when it processes the RAW stream.

<a href="" id="wia-ipa-depth"></a>[**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546)  
This property contains the number of bits per pixel. The driver sets the value of this property when the application sets [**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553) to **WiaImgFmt\_RAW**. The sum of all of the entries in the WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL property must equal the number stored in the WIA\_IPA\_DEPTH property. WIA\_IPA\_DEPTH is writable if the driver supports multiple configurations. For example, for a driver that supports 32 bits per pixel and 48 bits per pixel configurations, the application can choose one setting, and the driver should set WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL and the associated properties accordingly.

<a href="" id="wia-ipa-raw-bits-per-channel"></a>[**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641)  
This property is set by the driver in response to a value of **WiaImgFmt\_RAW** in the WIA\_IPA\_FORMAT property and is updated when WIA\_IPA\_DATATYPE is changed. All entries for WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL must equal the number of bits per pixel stored in WIA\_IPA\_DEPTH.

<a href="" id="wia-ipa-channels-per-pixel"></a>[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](https://msdn.microsoft.com/library/windows/hardware/ff551535)  
This property is set by the driver to the number of channels per pixel of the selected RAW subtype in WIA\_IPA\_DATATYPE.

<a href="" id="wia-ipa-datatype"></a>[**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543)  
When WIA\_IPA\_FORMAT is set to **WiaImgFmt\_RAW**, the driver sets this property to a default value. The driver also determines a list of allowable values from which the application can select to change the default value. The WIA\_IPA\_DATATYPE default value is selected by the driver; it can be any value that the device allows.

<a href="" id="wia-ipa-bytes-per-line"></a>[**WIA\_IPA\_BYTES\_PER\_LINE**](https://msdn.microsoft.com/library/windows/hardware/ff551531)  
Must be updated by the minidriver according to the WIA\_IPA\_FORMAT and WIA\_IPA\_DATATYPE settings.

<a href="" id="wia-ipa-item-size"></a>[**WIA\_IPA\_ITEM\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551594)  
Must be zero.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Property%20Validation%20for%20RAW%20Format%20Transfers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


