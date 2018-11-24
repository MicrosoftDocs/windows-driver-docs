---
title: ActiveX Objects for Print Web Pages
description: ActiveX Objects for Print Web Pages
ms.assetid: 85c37895-542f-4399-bf87-517eaab99a09
keywords:
- print Web pages WDK , ActiveX objects
- Web pages WDK printer , ActiveX objects
- customized print Web pages WDK , ActiveX objects
- ActiveX objects WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ActiveX Objects for Print Web Pages





Three ActiveX objects, [Iasphelp](https://msdn.microsoft.com/library/windows/hardware/ff550742), [IOleCvt](https://msdn.microsoft.com/library/windows/hardware/ff551819), and [ISNMP](https://msdn.microsoft.com/library/windows/hardware/ff554396), are provided for print Web pages. ASP files can access each object through an Automation interface, by using a scripting language such as VBScript. The objects and interfaces are implemented in Oleprn.dll.

The following list contains a brief description of each interface:

-   The [Iasphelp Automation Interface](https://msdn.microsoft.com/library/windows/hardware/ff550742) allows you to obtain properties associated with a specified printer.

    This interface provides access to information that is not available from ASP session variables, and allows an ASP page to obtain information about printers other than the one for which the page was invoked.

-   The [IOleCvt Automation Interface](https://msdn.microsoft.com/library/windows/hardware/ff551819) allows you to convert strings from ANSI to Unicode, and vice versa, to convert strings to UTF8 format, and to convert Unicode strings using a different code page.

-   The [ISNMP Automation Interface](https://msdn.microsoft.com/library/windows/hardware/ff554396) allows you to set and retrieve values associated with SNMP OIDs, if RFC 1759 is supported for a printer.

    The [ISNMP](https://msdn.microsoft.com/library/windows/hardware/ff554396) interface can only be used with printers that use Microsoft's TCIP/IP port monitor. This interface is essentially an OLE automation wrapper for SNMP Management API functions. For more information about these functions, see the Microsoft Windows SDK documentation.

    Object IDs (OIDs) can be specified using numeric strings, and by including text name strings for the Management Information Base (MIB) specified by RFC 1759. Additional MIB names can be used if you define, compile, and install customized MIBs, as described in the Windows SDK documentation.

For information about ActiveX and Automation, see the Windows SDK documentation.

 

 




