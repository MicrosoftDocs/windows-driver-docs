---
title: End of servicing plan for third-party printer drivers on Windows
description: This article provides information on the end of servicing plan for third-party printer drivers on Windows.
keywords:
- print devices WDK
- print WDK See printer driver
- print WDK See printing
ms.date: 09/05/2023
---

# End of servicing plan for third-party printer drivers on Windows

This article provides information on the end of servicing plan for third-party printer drivers on Windows.

## Overview

With the release of Windows 10 21H2, Windows offers inbox support for Mopria compliant printer devices over network and USB interfaces via the Microsoft IPP Class Driver. This removes the need for print device manufacturers to provide their own installers, drivers, utilities, and so on.  Device experience customization is now available via the [**Print Support Apps**](../devapps/print-support-app-design-guide.md) that are distributed and automatically installed via the Windows Store. This framework improves reliability and performance by moving customization from the Win32 framework to the UWP software development framework. Finally, print device manufacturers no longer have to rebuild their software since this solution is supported across all Windows versions and editions.

With these advancements in the Windows print platform, we are announcing the end of servicing of the legacy v3 and v4 Windows printer drivers. As this is an impactful change, end of servicing will be staged over multiple years. See the following Timeline and FAQ sections for guidance on the end of servicing roadmap.  

## Timeline

| Timeline * | Plan |
|--|--|
| **September 2023** | **Announce legacy third-party printer driver for Windows end of servicing plan.** |
| **2025** | **No new printer drivers will be published to Windows Update.**<br><br>Existing printer drivers on Windows Update can still be updated. |
| **2026** | **Printer driver ranking order modified to always prefer Windows IPP inbox class driver.** |
| **2027** | **Except for security-related fixes, third-party printer driver updates will no longer be allowed**.<br><br>Existing third-party printer drivers can be installed from Windows Update or users can install printer drivers by using a print device manufacturer-provided installation program. |

**\* Dates are subject to change.**

## FAQ

**Q: Will vendor-supplied drivers be signed by WHCP (Windows Hardware Compatibility Program)?**

**A:** Printer manufacturers can continue to submit printer drivers through the [**Partner Center**](https://partner.microsoft.com/dashboard/home) hardware tool for driver validation and signing. However, in 2025 new printer drivers will no longer be published to Windows Update. Manufacturers and independent software vendors will need to provide customers with an alternative means to download and install those printer drivers.

**Q: Will Windows prevent installation of new printer drivers?**

**A:** Windows will continue to allow vendor-supplied printer drivers to be installed via separate installation packages.

**Q: Will installation of Microsoft-signed printer drivers already released to the market be prevented from installing on Windows?**

**A:** Existing printer drivers can be installed on Windows PCs even after the end of servicing.

**Q: Does end of servicing apply to all versions of Windows?**

**A:** This change applies to all versions of Windows.

**Q: Will supporting Mopria certification be a mandatory requirement for HLK (Hardware Lab Kit)?**

**A:** Yes.

**Q: Will Microsoft continue to address security-related issues related to the legacy driver platform after the end of servicing?**

**A:** Microsoft will continue to issue security fixes related to the legacy printer driver platform while the Windows OS version is still within [**Microsoft Support Lifecycle**](/lifecycle/products/?products=windows).

**Q: Does Microsoft have plans to remove existing features supported by v3 and v4 printer drivers as part of the end of servicing plan?**

**A:** There are no plans to disable print features specifically related to the legacy printer driver platform.

**Q: Can print vendors continue to add printer Hardware IDs (HWID) to existing third-party driver packages?**

**A:** Once driver enforcement policies are live, adding new HWID will be approved on a case-by-case basis.

**Q: Will multi-function devices (print, scan, fax) work over IPP?**

**A:** Yes, they will.  For network devices, the Print and Fax endpoints will work via IPP and IPP Fax Out, respectively, while the Scan endpoint will work via WS-Scan or eSCL.  For USB devices, the endpoints will only be accessible when the USB interface is in IPP Over USB mode which means IPP for Print, IPP Fax Out for Fax, and only eSCL for Scan.  
