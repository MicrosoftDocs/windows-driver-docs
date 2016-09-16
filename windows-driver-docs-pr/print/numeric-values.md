---
title: Numeric Values
author: windows-driver-content
description: Numeric Values
MS-HAID:
- 'nt5gpd\_28e2faad-c428-4c64-bb4b-350dae45d780.xml'
- 'print.numeric\_values'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4f1f4145-aeda-4770-9a49-d8fe701763c8
keywords: ["GPD file entries WDK Unidrv , numeric values", "numeric values WDK GPD files"]
---

# Numeric Values


## <a href="" id="ddk-numeric-values-gg"></a>


All numeric values that you specify as entry values or parameter values in a GPD file must be integers. Decimal points are not allowed, except within text strings.

Numeric values are assumed to be positive unless preceded by a minus sign.

Numeric values are assumed to be decimal unless preceded by 0x, in which case they are unsigned hexadecimal values.

The asterisk character (\*) can be used to indicate either an infinite value or a "don't care" value, if applicable within the context of a particular GPD file entry.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Numeric%20Values%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


