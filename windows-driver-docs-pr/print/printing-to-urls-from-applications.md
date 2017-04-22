---
title: Printing to URLs from Applications
author: windows-driver-content
description: Printing to URLs from Applications
ms.assetid: bc9aedb4-1d64-4b70-b14b-1392f914a635
keywords:
- Internet printing WDK , printing to URLs
- URL-identified print queue WDK
- friendly names WDK printer
- printing to URLs WDK
- print Web pages WDK , printing to URLs
- Web pages WDK printer , printing to URLs
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printing to URLs from Applications


## <a href="" id="ddk-printing-to-urls-from-applications-gg"></a>


From an application's perspective, printing to a URL-identified print queue is identical to printing to a UNC-identified print queue. The application is typically unaware that the print queue is accessed by means of a URL.

By [viewing print Web pages](viewing-print-web-pages.md), a user can install and connect to a URL-identified print queue. When this happens, the print queue is assigned the same "friendly name" that it has on the print server, and this friendly name is listed in the user's print folder.

Applications generally refer to the print queue by its friendly name, as they do for UNC-identified print queues. Calls to the **OpenPrinter** function in the local print provider (caused, for example, by the application making GDI calls), include the friendly name. The local print provider, in turn, calls **OpenPrinter** in the HTTP print provider (Inetpp.dll), specifying the print queue's URL.

Applications that refer to print queues by friendly names are generally unaware of whether the print queue is local or on a network, or whether the network protocol is RPC, SMB, or HTTP. However applications can, if necessary, call **OpenPrinter** directly, specifying a URL. When specifying a URL to **OpenPrinter**, the following URL format must be used:

http://&lt;ServerName&gt;/printers/&lt;ShareName&gt;/.printer

where &lt;ServerName&gt; is the server name (either a DNS name for Internet connections, or a WINS name for intranet connections), "printers" represents a virtual directory on the server, and &lt;ShareName&gt; is the print queue's share name, as specified in its property sheet. (Virtual directories are discussed in the Microsoft Windows SDK documentation.)

When a client spooler component or application calls **OpenPrinter** and specifies a URL, subsequent calls to spooler functions, such as **StartDocPrinter**, **WritePrinter**, and so on, are handled by the client's HTTP print provider. The HTTP print provider appends arguments to the URL and sends the resulting URL string to the print server.

For a Microsoft Windows 2000 print server to accept print requests containing URLs, it must be running either:

-   Windows 2000 Server software with Microsoft Internet Information Server (IIS), or

-   Windows 2000 Professional software with Microsoft Peer Web Server

For a Windows XP print server to accept print requests containing URLs, it must be running either:

-   Microsoft Windows Server 2003 software with Microsoft Internet Information Server (IIS), or

-   Windows XP Professional software with Microsoft Peer Web Server

**Note**   A Windows XP Home Edition print server cannot accept requests containing URLs.

 

On the print server, IIS or the Peer Web Server receives the URL string. Arguments appended to the string by Inetpp.dll on the client system cause the server to call the HTTP print server, which is contained in Msw3prt.dll. The HTTP print server accepts RAW-formatted printer data and sends it to the local print spooler.

Printer data is sent from client to server using the Internet Printing Protocol (IPP 1.0), defined by the Printer Working Group (PWG) of the Internet Engineering Task Force (IETF).

The following figure illustrates the path that print data takes from a client application to a print server spooler, if the client prints to a URL-identified print queue.

![diagram illustrating printing to a url-identified print queue](images/prntpath.png)

If both the client and server are Windows 2000 or later systems, as illustrated, RPC protocol is typically (but not always) used for client-server communication. (For more information, see [Installing Print Drivers from a Web Page](installing-print-drivers-from-a-web-page.md).) If the client and server are not both Windows 2000 or later systems, HTTP is used. HTTP is also used for printers that contain internal network cards and support IPP 1.0, and are therefore not connected to a server.

Print server security is provided by IIS, which executes on the print server. Security mechanisms supported by IIS are described in the *IIS Resource Guide*, which is contained in the **

*Microsoft Windows 2000 Server Resource Kit*. Additionally, the resource kit describes specifically how system administrators can control security methods associated with printing to URLs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printing%20to%20URLs%20from%20Applications%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


