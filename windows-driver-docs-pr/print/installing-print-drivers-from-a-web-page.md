---
title: Installing Print Drivers from a Web Page
author: windows-driver-content
description: Installing Print Drivers from a Web Page
ms.assetid: 44da45f7-687c-4c54-9ee6-79c91fce3947
keywords: ["Internet printing WDK , installing drivers from Web pages", "print Web pages WDK , installing print drivers from", "Web pages WDK printer , installing print drivers from", "installing drivers WDK printer , Web pages"]
---

# Installing Print Drivers from a Web Page


## <a href="" id="ddk-installing-print-drivers-from-a-web-page-gg"></a>


Before a user can send a job to a print queue that is visible by means of print Web pages, driver files must be sent from the print server and installed on the user's system. This installation operation occurs when a user views a print queue's Web page and then selects its installation page. (The installation page cannot be replaced with a customized page.)

If the client can connect to the server using RPC, which is likely for intranet connections, the printer is installed in the usual, non-HTTP manner. Otherwise the installation page calls the HTTP print server, which creates a cabinet file (described in the Microsoft Windows SDK documentation) containing the printer's setup information (INF) file and all required installation files. The server sends the cabinet file to the client, where it is expanded. It starts the client's Add Printer Wizard, which completes the installation and adds the printer to the user's print folder.

As an alternative to selecting a print queue's installation page, a user can install a URL-identified printer by running the Add Printer Wizard explicitly. When a user specifies a URL to the Add Printer Wizard, the client always connects to the server using HTTP.

**Note**  This installation method must be used when installing printers that contain their own network cards and are therefore not connected to a server.

 

The installation process is not customizable beyond specifying the contents of the [printer INF file](printer-inf-files.md), which is the same INF file used to install the printer on the print server.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20Print%20Drivers%20from%20a%20Web%20Page%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


