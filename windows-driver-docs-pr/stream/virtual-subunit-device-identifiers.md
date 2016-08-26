---
title: Virtual Subunit Device Identifiers
author: windows-driver-content
description: Virtual Subunit Device Identifiers
MS-HAID:
- 'AVCguide\_f7139b81-fbe2-452c-af33-eac6da5d20a8.xml'
- 'stream.virtual\_subunit\_device\_identifiers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c2018560-f9f4-4aaa-b2b2-8ac5195b892f
keywords: ["AV/C WDK , identifiers", "identifiers WDK AV/C", "device IDs WDK AV/C", "Avc.sys function driver WDK , identifiers", "virtual subunit device identifiers WDK AV/C", "subunit support WDK AV/C"]
---

# Virtual Subunit Device Identifiers


Similar to the format of device identifier (ID) fields for [peer subunits](peer-subunit-device-identifiers.md), the format that *Avc.sys* uses to generate virtual subunit device identifier strings, based on the format described in [AV/C Device IDs](av-c-device-identifiers.md), is as follows:

-   Hardware identifier

<a href="" id="vavc-vendor-model-subunittype-subunitid"></a>**VAVC\\*Vendor*&*Model*&*SubunitType*&*SubunitID***  
This hardware identifier is the most complete, but this is seldom specified in an INF file because the subunit identifier (the last ampersand-delimited portion of the device identifier) is not usually of interest.

-   Compatible identifiers

<a href="" id="vavc-subunittype-subunitid"></a>**VAVC\\*SubunitType*&*SubunitID***  
While *Avc.sys* does not provide this kind of compatible identifier for peer subunits, it does provide this kind of compatible identifier for virtual subunits.

<a href="" id="vavc-subunittype"></a>**VAVC\\*SubunitType***  
While *Avc.sys* does not provide this kind of compatible identifier for peer subunits, it does provide this kind of compatible identifier for virtual subunits.

<a href="" id="vavc-generic"></a>**VAVC\\GENERIC**  
A "universal" unit driver includes this entry in its INF file.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Virtual%20Subunit%20Device%20Identifiers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


