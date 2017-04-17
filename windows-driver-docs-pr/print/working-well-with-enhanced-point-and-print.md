---
title: Working well with enhanced Point and Print
author: windows-driver-content
description: The updated printer sharing mechanism is referred to as enhanced Point and Print, and it allows print clients to print to v4 shares without downloading the manufacturer-provided device driver from the print server.
ms.assetid: AD01AAD1-B209-419A-B73B-CA746F1B772A
---

# Working well with enhanced Point and Print


The updated printer sharing mechanism is referred to as enhanced Point and Print, and it allows print clients to print to v4 shares without downloading the manufacturer-provided device driver from the print server.

Because client machines do not download the entire driver package when they connect with a print server that has enhanced Point and Print and v4 printer drivers, it is important to be aware of the following architectures. This information should help you to develop and package your v4 printer driver appropriately.

## Windows 8 Client Connection Behavior


When a Windows 8 client connects to a shared print queue that is using a v4 printer driver, the client will try to obtain a driver that supports client side rendering. The client searches the local DriverStore for a driver with a HardwareID that matches the server driver’s PrinterDriverID. If one is found, that driver will be installed locally. Otherwise, the client will connect using the enhanced Point and Print driver.

In both cases, the client downloads configuration data from the server using GetPrinterDataEx calls. The configuration data includes data files like generic printer description (GPD) files, PostScript printer description (PPD) files, the driver property bag, JavaScript constraints and a resource DLL. The client also downloads the CAT file that was associated with the server’s driver.

The print system then examines the client and validates that the resource DLL contains no executable code. The print system also verifies that the downloaded files are valid and signed by the CAT file downloaded from the server. Any files that are untrusted will be deleted. The following diagram illustrates this configuration-related communication between a Windows 8 client and shared print servers that use the v4 printer driver.

![configuration-related communication between a windows 8 print client and a print server with a v4 print driver. configuration information is downloaded using getprinterdataex calls.](images/win8and-epp.png)

## Windows 7 and Windows Vista Client Connection Behavior


Windows 7 and Windows Vista clients may also connect to shared print queues that use a v4 printer driver. In this case, however, the client will always download the enhanced Point and Print driver from the server. This driver uses server side rendering to ensure that the proper printer description language (PDL) is generated for the printer.

Configuration data is downloaded from the server in the same way for Windows 7 and Windows Vista client connections, using GetPrinterDataEx calls. If any downloaded files fail validation against the server’s CAT file, they are deleted. The following diagram illustrates this configuration-related communication between a Windows 7 or a Windows Vista client and shared print servers that use the v4 printer driver.

![configuration-related communication between a windows 7 or windows vista print client and a print server with a v4 print driver. configuration information is downloaded using getprinterdataex calls.](images/win7and-epp.png)

Shared printers that are backed by a v3 printer driver will continue to work using the existing Point and Print system.

## Related topics
[V4 Printer Driver Development Best Practices](v4-printer-driver-development-best-practices.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Working%20well%20with%20enhanced%20Point%20and%20Print%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


