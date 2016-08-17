---
title: About Item Properties
description: About Item Properties
MS-HAID:
- 'WIA\_tree\_ad54e741-817c-469b-8f2e-319886cad5e5.xml'
- 'image.about\_item\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f8d00e29-ce7d-4949-a713-07755f495d6a
---

# About Item Properties


## <a href="" id="ddk-about-item-properties-si"></a>


Each application item tree contains a collection of item properties. (This property collection is also known as a property stream.) The application item model provides each application with its own copy of the item tree, allowing applications to modify properties independent of each other.

Drivers specify the properties they support and define the initial values of those properties. When an application reads a property, the driver updates any properties that must be refreshed with their current values. For example, if the application is reading the device time, then the driver can ask the device for its current time and update the device time property. When an application writes a new value to the property, the WIA service asks the driver to validate and write this value to the property.

Certain properties are mandatory for some device types. For example, a device with an automatic document feeder (ADF) must support the ADF properties.

**Note**   If you are more familiar with TWAIN than you are with WIA, it may be helpful to know that WIA properties are synonymous with TWAIN capabilities.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20About%20Item%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




