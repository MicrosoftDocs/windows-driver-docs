---
title: XML Schema Linebreak Translations
author: windows-driver-content
description: XML Schema Linebreak Translations
MS-HAID:
- 'gplfiles\_5ad1f366-8ea2-4b47-abcb-18f5a0e614eb.xml'
- 'print.xml\_schema\_linebreak\_translations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c277984f-8e7a-4d17-98ab-66c3f6f80473
keywords: ["linebreak sequence WDK GDL", "GDL WDK , schemas", "schemas WDK GDL", "snapshots WDK GDL , linebreaks"]
---

# XML Schema Linebreak Translations


The XML snapshot represents linebreaks with the following two character sequence: &lt;0d&gt;&lt;0a&gt; (CR LF). However, within &lt;CDATA&gt; sections, quoted string values, and native XML data type values, the raw character sequence that is found in the GDL source file is used exactly. This usage prevents any loss of information that might be contained in the choice of linebreak sequence that the author of the GDL data uses.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XML%20Schema%20Linebreak%20Translations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


