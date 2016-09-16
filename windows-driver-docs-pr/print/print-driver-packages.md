---
title: Print Driver Packages
author: windows-driver-content
description: Print Driver Packages
MS-HAID:
- 'prtinst\_80659023-3f68-43a4-b0c2-d5b7a32c16e0.xml'
- 'print.print\_driver\_packages'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 902e1634-e705-4902-baab-a93818288b08
keywords: ["installing drivers WDK printer , packages", "printer driver installations WDK , packages", "packages WDK print", "driver pacakges WDK print", "printer driver packages WDK print"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Driver%20Packages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


