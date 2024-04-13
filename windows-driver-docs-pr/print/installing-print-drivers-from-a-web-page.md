---
title: Install Print Drivers from a Web Page
description: Provides information about how to install print drivers from a Web page.
keywords:
- Internet printing WDK, installing drivers from Web pages
- print Web pages WDK, installing print drivers from
- Web pages WDK printer, installing print drivers from
- installing drivers WDK printer, Web pages
ms.date: 09/14/2022
---

# Install print drivers from a Web page

Before a user can send a job to a print queue that is visible by means of print Web pages, driver files must be sent from the print server and installed on the user's system. This installation operation occurs when a user views a print queue's Web page and then selects its installation page. (The installation page cannot be replaced with a customized page.)

If the client can connect to the server using RPC, which is likely for intranet connections, the printer is installed in the usual, non-HTTP manner. Otherwise the installation page calls the HTTP print server, which creates a [cabinet file](/windows/win32/msi/cabinet-files) containing the printer's setup information (INF) file and all required installation files. The server sends the cabinet file to the client, where it is expanded. It starts the client's Add Printer Wizard, which completes the installation and adds the printer to the user's print folder.

As an alternative to selecting a print queue's installation page, a user can install a URL-identified printer by running the Add Printer Wizard explicitly. When a user specifies a URL to the Add Printer Wizard, the client always connects to the server using HTTP.

> [!NOTE]
> This installation method must be used when installing printers that contain their own network cards and are therefore not connected to a server.

The installation process is not customizable beyond specifying the contents of the [printer INF file](printer-inf-files.md), which is the same INF file used to install the printer on the print server.
