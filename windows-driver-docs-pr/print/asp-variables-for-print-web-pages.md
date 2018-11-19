---
title: ASP Variables for Print Web Pages
description: ASP Variables for Print Web Pages
ms.assetid: eab0d5e0-0e20-443c-b714-a2b2327894e4
keywords:
- customized print Web pages WDK , ASP variables
- ASP variables WDK printer
- session variables WDK printer
- print Web pages WDK , ASP variables
- Web pages WDK printer , ASP variables
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ASP Variables for Print Web Pages





Microsoft provides a set of ASP session variables for use by customized print Web pages. The following table lists the session variables. Customized ASP files must not modify these variables. As indicated, some variables are only valid if Microsoft's TCP/IP port monitor is being used for the printer.

Some variables are passed in as session variables, while others are passed in using URL decoration. Session variables can be accessed by using Session("*VariableName*"). Parameters passed in by URL decoration can be accessed by using Request("*VariableName*"). If you wish to automatically refresh the status page, you might find it necessary to redecorate the URL with the variables your page requires. Since Request variables must be passed in the URL, they may require encoding and decoding to translate from ANSI to Unicode representation. A helper object, whose COM ProgID is "OlePrn.OleCvt", has been provided to enable encoding and decoding between the ANSI used in the URL and Unicode. Two methods on this object, [**IOleCvt::EncodeUnicodeName**](https://msdn.microsoft.com/library/windows/hardware/ff551829), and [**IOleCvt::DecodeUnicodeName**](https://msdn.microsoft.com/library/windows/hardware/ff551824), can be used to translate from ANSI to Unicode, and from Unicode to ANSI, respectively. This conversion does not need to be performed for Session variables.

Variable
Value
TCP/IP Port
Variable
Encoded?
Monitor Only?
Type
MS\_ASP1

Directory path to the initial Web page used for describing printer-specific details.

No

Request

No

MS\_Community

The print server's SNMP community name.

Yes

Request

No

MS\_Computer

The print server's computer name.

No

Session

No

MS\_DefaultPage

The default ASP file for printer-specific details.

No

Session

No

MS\_Device

The printer's SNMP device index.

Yes

Request

No

MS\_DHTMLEnabled

**TRUE** if the client supports dynamic HTML; otherwise **FALSE**.

No

Session

No

MS\_IPAddress

The printer's IP address.

Yes

Request

No

MS\_LocalServer

The print server's identifier. This might be either an IP address or a computer name.

No

Session

No

MS\_Model

The name of the printer driver.

No

Request

Yes

MS\_Portname

The printer's port name.

No

Request

Yes

MS\_Printer

The printer's name.

No

Request

Yes

MS\_SNMP

**TRUE** if SNMP is being used with a printer, otherwise **FALSE**.

Yes

Request

No

MS\_URLPrinter

The printer's name, in encoded URL format.

No

Request

Yes

 

The session variables specify properties of the "current" printer, that is, the printer for which an ASP page was invoked. To obtain additional printer properties for the current printer, or to obtain properties of a different printer, see [ActiveX Objects for Print Web Pages](activex-objects-for-print-web-pages.md).

 

 




