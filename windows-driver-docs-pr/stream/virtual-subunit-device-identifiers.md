---
title: Virtual Subunit Device Identifiers
description: Virtual Subunit Device Identifiers
ms.assetid: c2018560-f9f4-4aaa-b2b2-8ac5195b892f
keywords:
- AV/C WDK , identifiers
- identifiers WDK AV/C
- device IDs WDK AV/C
- Avc.sys function driver WDK , identifiers
- virtual subunit device identifiers WDK AV/C
- subunit support WDK AV/C
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




