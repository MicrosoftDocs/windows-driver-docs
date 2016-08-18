---
title: Properties for All WIA Minidrivers
author: windows-driver-content
description: Properties for All WIA Minidrivers
MS-HAID:
- 'WIA\_arch\_caf9b7e9-2b61-4d91-b26b-fce76a21228c.xml'
- 'image.properties\_for\_all\_wia\_minidrivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ba85dbbd-2333-4f4f-b12a-84985773eef6
---

# Properties for All WIA Minidrivers


## <a href="" id="ddk-properties-for-all-wia-minidrivers-si"></a>


### Required Properties on Root or Child Items

The WIA service supplies the following properties:

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551561)

[**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585)

[**WIA\_IPA\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551590)

[**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581)

A WIA minidriver supplies the following property:

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518)

### Required Properties on Root Items

The WIA service supplies the following root item properties:

[**WIA\_DIP\_BAUDRATE**](https://msdn.microsoft.com/library/windows/hardware/ff550244)

[**WIA\_DIP\_DEV\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff550247)

[**WIA\_DIP\_DEV\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff550250)

[**WIA\_DIP\_DEV\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff550256)

[**WIA\_DIP\_DEV\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff550260)

[**WIA\_DIP\_DRIVER\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff550263)

[**WIA\_DIP\_HW\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff550268)

[**WIA\_DIP\_PORT\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff550278)

[**WIA\_DIP\_REMOTE\_DEV\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff550282)

[**WIA\_DIP\_SERVER\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff550285)

[**WIA\_DIP\_STI\_GEN\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff550288)

[**WIA\_DIP\_UI\_CLSID**](https://msdn.microsoft.com/library/windows/hardware/ff550291)

[**WIA\_DIP\_VEND\_DESC**](https://msdn.microsoft.com/library/windows/hardware/ff550293)

[**WIA\_DIP\_WIA\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff550296)

### Optional Properties on Root Items

A WIA minidriver supplies the following optional properties on root items:

[**WIA\_DPA\_CONNECT\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff550299)

[**WIA\_DPA\_DEVICE\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff550303)

[**WIA\_DPA\_FIRMWARE\_VERSION**](https://msdn.microsoft.com/library/windows/hardware/ff550309)

### Required Properties on Child Items Able to Transfer Data

The WIA service supplies the following property on child items:

[**WIA\_IPA\_ICM\_PROFILE\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551571)

A WIA minidriver supplies the following properties on child items:

[**WIA\_IPA\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551526)

[**WIA\_IPA\_BUFFER\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551527)

[**WIA\_IPA\_BYTES\_PER\_LINE**](https://msdn.microsoft.com/library/windows/hardware/ff551531)

[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](https://msdn.microsoft.com/library/windows/hardware/ff551535)

[**WIA\_IPA\_COMPRESSION**](https://msdn.microsoft.com/library/windows/hardware/ff551540)

[**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543)

[**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546)

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549)

[**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553)

[**WIA\_IPA\_ITEM\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551594)

[**WIA\_IPA\_NUMBER\_OF\_LINES**](https://msdn.microsoft.com/library/windows/hardware/ff551611)

[**WIA\_IPA\_PIXELS\_PER\_LINE**](https://msdn.microsoft.com/library/windows/hardware/ff551615)

[**WIA\_IPA\_PLANAR**](https://msdn.microsoft.com/library/windows/hardware/ff551617)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551623)

[**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656)

### Optional Properties on Child Items Able to Transfer Data

A WIA minidriver supplies the following properties:

[**WIA\_IPA\_APP\_COLOR\_MAPPING**](https://msdn.microsoft.com/library/windows/hardware/ff551521)

[**WIA\_IPA\_COLOR\_PROFILE**](https://msdn.microsoft.com/library/windows/hardware/ff551536)

[**WIA\_IPA\_GAMMA\_CURVES**](https://msdn.microsoft.com/library/windows/hardware/ff551568)

[**WIA\_IPA\_ITEM\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff551601)

[**WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551628)

[**WIA\_IPA\_REGION\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551646)

[**WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE**](https://msdn.microsoft.com/library/windows/hardware/ff551653)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Properties%20for%20All%20WIA%20Minidrivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


