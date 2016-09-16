---
title: Viewing Print Web Pages
author: windows-driver-content
description: Viewing Print Web Pages
MS-HAID:
- 'inetpri\_22d62328-45e1-4986-8fb4-ee23e0ac6c32.xml'
- 'print.viewing\_print\_web\_pages'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c2cf782c-0f53-47e1-8c5e-1e2aa87613c4
keywords: ["Internet printing WDK , viewing print Web pages", "viewing print Web pages", "displaying print Web pages", "print Web pages WDK , viewing", "Web pages WDK printer , viewing", "print server pages WDK", "viewing print server pages", "print URLs WDK"]
---

# Viewing Print Web Pages


## <a href="" id="ddk-viewing-print-web-pages-gg"></a>


With any Internet browser executing on any type of client platform, users can view Web pages that display the status of a Microsoft Windows 2000 or later print server and its connected printers. Microsoft provides a set of server-resident HTML files that generate these Web pages. Web pages for the print server and for each server-installed printer can be referenced by a client browser using URLs. Additional pages can be referenced by links from these pages.

For a Windows 2000 print server to support Web pages, it must be running either Windows 2000 Server software with Microsoft Internet Information Server (IIS), or Windows 2000 Professional software with Microsoft Peer Web Server.

For a Windows XP print server to support Web pages, it must be running either Microsoft Windows Server 2003 software with Microsoft Internet Information Server (IIS), or Windows XP Professional software with Microsoft Peer Web Server. Note that the print server in Windows XP Home Edition does not support Web pages.

To view a print server page, a user specifies the following URL format:

http://&lt;ServerName&gt;/printers

where &lt;ServerName&gt; is the server name (either a DNS name for Internet connections or a WINS name for intranet connections). The URL points to an HTML file that generates the print server's page.

The server page provides a link to a print queue page for each print queue available on the server. Shared print queues can be accessed by all users. A user can also reference the print queue pages for shared printers by specifying a URL with the following format:

http://&lt;ServerName&gt;/&lt;ShareName&gt;

where &lt;ShareName&gt; is the print queue's share name, as specified in its property sheet.

If a user selects a printer's link within the print folder, Windows Internet Explorer is automatically started and the print queue page's URL is accessed. Alternatively, as already described, a user can view a print server page or a print queue page by specifying the page's URL to any HTML browser.

Print Web pages are generated from template files that can be interpreted by Microsoft Active Server Pages (ASP). These templates (called ASP files) contain standard HTML tags and ASP script tags (&lt;% and %&gt;).

When the Active Server Pages interpreter encounters text within ASP script tags, it calls an appropriate scripting language interpreter (such as JScript or VBScript) to process the text. The resulting HTML data stream is then sent to the client browser.

For more information about Microsoft Active Server Pages, see the Microsoft Windows SDK documentation.

A set of COM-based [ActiveX objects for print Web pages](activex-objects-for-print-web-pages.md), with associated Automation interfaces, is provided (in Oleprn.dll) for obtaining printer properties and SNMP information.

When a user wants to view the Web page of a particular server or printer, the following steps occur:

1.  The user employs a browser to specify an appropriate URL. The URL points to one of the template files on the specified print server.

2.  The server-resident Active Server Pages interpreter, which is part of IIS, searches for ASP script tags, invokes the appropriate scripting language interpreter to interpret the script text, and places the returned results in the HTML data stream.

3.  The ASP interpreter, on the server, sends the resulting HTML stream to the client's browser.

The following figure illustrates the process by which a printer URL is sent from a client to a print server, and how its associated HTML stream is returned to the client.

![diagram illustrating sending a print url from the client to the print server](images/prnturl.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Viewing%20Print%20Web%20Pages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


