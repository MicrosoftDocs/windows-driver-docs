---
title: Property Validation for RAW Format Transfers
description: Property Validation for RAW Format Transfers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Validation for RAW Format Transfers


The driver must validate the WIA property settings prior to a RAW format data transfer. The WIA properties must be set as follows:

<a href="" id="wia-ips-xpos--wia-ips-ypos"></a>[**WIA\_IPS\_XPOS**](./wia-ips-xpos.md), [**WIA\_IPS\_YPOS**](./wia-ips-ypos.md)  
These properties are set the same for RAW as they are for other image formats. These properties contain the coordinates, in pixels, of the upper-left corner of the selected image

<a href="" id="wia-ips-xres--wia-ips-yres"></a>[**WIA\_IPS\_XRES**](./wia-ips-xres.md), [**WIA\_IPS\_YRES**](./wia-ips-yres.md)  
These properties are set the same for RAW as they are for other image formats. These properties contain the current horizontal and vertical (respectively) resolution, in pixels per inch, for the device

<a href="" id="wia-ips-xextent--wia-ips-yextent"></a>[**WIA\_IPS\_XEXTENT**](./wia-ips-xextent.md), [**WIA\_IPS\_YEXTENT**](./wia-ips-yextent.md)  
These properties are set by the application and are read by and updated by the driver. Because the properties might be changed from their original values, the application must read the value stored in these properties when it processes the RAW stream.

<a href="" id="wia-ipa-depth"></a>[**WIA\_IPA\_DEPTH**](./wia-ipa-depth.md)  
This property contains the number of bits per pixel. The driver sets the value of this property when the application sets [**WIA\_IPA\_FORMAT**](./wia-ipa-format.md) to **WiaImgFmt\_RAW**. The sum of all of the entries in the WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL property must equal the number stored in the WIA\_IPA\_DEPTH property. WIA\_IPA\_DEPTH is writable if the driver supports multiple configurations. For example, for a driver that supports 32 bits per pixel and 48 bits per pixel configurations, the application can choose one setting, and the driver should set WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL and the associated properties accordingly.

<a href="" id="wia-ipa-raw-bits-per-channel"></a>[**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](./wia-ipa-raw-bits-per-channel.md)  
This property is set by the driver in response to a value of **WiaImgFmt\_RAW** in the WIA\_IPA\_FORMAT property and is updated when WIA\_IPA\_DATATYPE is changed. All entries for WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL must equal the number of bits per pixel stored in WIA\_IPA\_DEPTH.

<a href="" id="wia-ipa-channels-per-pixel"></a>[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](./wia-ipa-channels-per-pixel.md)  
This property is set by the driver to the number of channels per pixel of the selected RAW subtype in WIA\_IPA\_DATATYPE.

<a href="" id="wia-ipa-datatype"></a>[**WIA\_IPA\_DATATYPE**](./wia-ipa-datatype.md)  
When WIA\_IPA\_FORMAT is set to **WiaImgFmt\_RAW**, the driver sets this property to a default value. The driver also determines a list of allowable values from which the application can select to change the default value. The WIA\_IPA\_DATATYPE default value is selected by the driver; it can be any value that the device allows.

<a href="" id="wia-ipa-bytes-per-line"></a>[**WIA\_IPA\_BYTES\_PER\_LINE**](./wia-ipa-bytes-per-line.md)  
Must be updated by the minidriver according to the WIA\_IPA\_FORMAT and WIA\_IPA\_DATATYPE settings.

<a href="" id="wia-ipa-item-size"></a>[**WIA\_IPA\_ITEM\_SIZE**](./wia-ipa-item-size.md)  
Must be zero.

 

