---
title: Print Driver Packages
description: Print Driver Packages
ms.assetid: 902e1634-e705-4902-baab-a93818288b08
keywords:
- installing drivers WDK printer , packages
- printer driver installations WDK , packages
- packages WDK print
- driver pacakges WDK print
- printer driver packages WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Driver Packages


In Windows Vista, Setup and the printing infrastructure use complete driver packages whenever possible. A driver package consists of all the hardware and software components you must supply in order for your device to be supported under Windows.

The driver package options for printer installation include the following:

-   **Local printer installation.** When a user installs a new printer driver on a Windows Vista machine, Setup automatically adds the complete print driver package to the driver store and then installs the driver.

-   **Remote printer installation.** When a user installs a print driver on a remote Windows Vista machine, Setup adds the print driver package to the driver store on the remote machine and then installs the print driver from the driver store on the remote machine.

-   **Package point and print.** When a Windows Vista client connects to a shared printer on another machine that is running Windows Vista and it needs to download the driver, package point and print copies the driver package from the driver store on the remote print server to the driver store on the client. Then package point and print installs the driver on the local machine from the local driver store.

-   **Web package point and print.** When a Windows Vista client uses Hypertext Transfer Protocol (HTTP) to connect to a shared printer that is hosted by a Windows Vista print server and has a driver package, web package point and print installs the driver in the same way as package point and print.

This section includes:

[Point and Print with Driver Packages](point-and-print-with-driver-packages.md)

[Package-Aware Print Drivers](package-aware-print-drivers.md)

[Using Updated Core Print Drivers](using-updated-core-print-drivers.md)

 

 




