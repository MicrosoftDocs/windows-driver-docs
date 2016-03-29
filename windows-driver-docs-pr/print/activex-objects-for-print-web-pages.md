---
title: ActiveX Objects for Print Web Pages
description: ActiveX Objects for Print Web Pages
ms.assetid: 85c37895-542f-4399-bf87-517eaab99a09
keywords: ["print Web pages WDK , ActiveX objects", "Web pages WDK printer , ActiveX objects", "customized print Web pages WDK , ActiveX objects", "ActiveX objects WDK printer"]
---

# ActiveX Objects for Print Web Pages


## <a href="" id="ddk-activex-objects-for-print-web-pages-gg"></a>


Three ActiveX objects, [Iasphelp](https://msdn.microsoft.com/library/windows/hardware/ff550742), [IOleCvt](https://msdn.microsoft.com/library/windows/hardware/ff551819), and [ISNMP](https://msdn.microsoft.com/library/windows/hardware/ff554396), are provided for print Web pages. ASP files can access each object through an Automation interface, by using a scripting language such as VBScript. The objects and interfaces are implemented in Oleprn.dll.

The following list contains a brief description of each interface:

-   The [Iasphelp Automation Interface](https://msdn.microsoft.com/library/windows/hardware/ff550742) allows you to obtain properties associated with a specified printer.

    This interface provides access to information that is not available from ASP session variables, and allows an ASP page to obtain information about printers other than the one for which the page was invoked.

-   The [IOleCvt Automation Interface](https://msdn.microsoft.com/library/windows/hardware/ff551819) allows you to convert strings from ANSI to Unicode, and vice versa, to convert strings to UTF8 format, and to convert Unicode strings using a different code page.

-   The [ISNMP Automation Interface](https://msdn.microsoft.com/library/windows/hardware/ff554396) allows you to set and retrieve values associated with SNMP OIDs, if RFC 1759 is supported for a printer.

    The [ISNMP](https://msdn.microsoft.com/library/windows/hardware/ff554396) interface can only be used with printers that use Microsoft's TCIP/IP port monitor. This interface is essentially an OLE automation wrapper for SNMP Management API functions. For more information about these functions, see the Microsoft Windows SDK documentation.

    Object IDs (OIDs) can be specified using numeric strings, and by including text name strings for the Management Information Base (MIB) specified by RFC 1759. Additional MIB names can be used if you define, compile, and install customized MIBs, as described in the Windows SDK documentation.

For information about ActiveX and Automation, see the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ActiveX%20Objects%20for%20Print%20Web%20Pages%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




