---
title: Vendor-Extended Properties
author: windows-driver-content
description: Vendor-Extended Properties
MS-HAID:
- 'WIA\_drv\_cam\_fb85aa18-6730-4c51-b20f-0e986f18986b.xml'
- 'image.vendor\_extended\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bcc89272-c14d-4d46-a2ca-7da0fb188111
---

# Vendor-Extended Properties


## <a href="" id="ddk-vendor-extended-properties-si"></a>


A **PropCode** entry in the **DeviceData** INF file section (see the example in [Vendor-Extended Features](vendor-extended-features.md)) lists all the vendor-extended property codes, separated by commas. For each property code, an entry of the form **PropCode***XXXX* must be present, where XXXX is the code value in uppercase hexadecimal. The entry should list the WIA property code and text description (which does not need to be localized) enclosed in quotes.

The WIA property codes should be between 0x9802 and 0x11802, which is the range defined for vendor-defined WIA device properties. The properties can be accessed through the **IWiaPropertyStorage::GetPropertyStream** and **IWiaPropertyStorage::SetPropertyStream** methods, which are described in the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Vendor-Extended%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


