---
title: ASP Variables for Print Web Pages
author: windows-driver-content
description: ASP Variables for Print Web Pages
ms.assetid: eab0d5e0-0e20-443c-b714-a2b2327894e4
keywords: ["customized print Web pages WDK , ASP variables", "ASP variables WDK printer", "session variables WDK printer", "print Web pages WDK , ASP variables", "Web pages WDK printer , ASP variables"]
---

# ASP Variables for Print Web Pages


## <a href="" id="ddk-asp-variables-for-print-web-pages-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ASP%20Variables%20for%20Print%20Web%20Pages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


