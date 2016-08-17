---
title: Color Management for Still Image Devices
description: Color Management for Still Image Devices
MS-HAID:
- 'stillimg\_57feac67-c585-44ad-abde-f643d5e72c1d.xml'
- 'image.color\_management\_for\_still\_image\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dfc4afad-221a-436c-9124-981a74f70ee3
---

# Color Management for Still Image Devices


## <a href="" id="ddk-color-management-for-still-image-devices-si"></a>


Vendors should provide one or more color profiles for each still image device. Color profile file names should be included in the vendor-supplied INF file. If your device generates sRGB data, you can specify the system-supplied standard color profile, *sRGB Color Space Profile.icm*. The installer copies the supplied file names to one of the [registry entries for still image devices](registry-entries-for-still-image-devices.md).

If the device generates images using another color space, you will need to use a different color profile. Whether your device generates sRGB data or data in another color space, you will obtain the best results if you use a single color space consistently.

A still-image device must be made aware of the color space it sends its data to. For example, suppose that a user resets the gamma level (on a system that allows modification of the data source). The application will not be aware of this change.

For more information about color management, see the Microsoft Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Color%20Management%20for%20Still%20Image%20Devices%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




