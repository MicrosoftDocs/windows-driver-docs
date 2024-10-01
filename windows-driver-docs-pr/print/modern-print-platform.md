---
title: Modern print platform
description: Describes the modern print platform and Windows protected print mode.
ms.date: 09/27/2024
---

# Modern print platform and Windows protected print mode

Modern print is Windows' preferred means of communicating to printers, including the [Internet Printing Protocol (IPP)](more-information-on-windows-protected-print-mode-for-enterprises.md#ipp-basics), eSCL scanning, and [Universal Print](/universal-print/discover-universal-print).

Modern print doesn't require the installation third-party drivers. This provides a simple, streamlined and secure printing experience compared to traditional printers, regardless of the PC's architecture. Modern print is designed to work with [Mopria certified printers](https://mopria.org/certified-products), and many existing printers are already compatible with modern print.  

## Mopria

The [Mopria](https://mopria.org/) alliance is a collection of printer manufacturers and software vendors that have come together to define the standards for [IPP printing](more-information-on-windows-protected-print-mode-for-enterprises.md#ipp-basics) and eSCL scanning. Mopria certified devices guarantee conformance to these standards.  

## Universal Print

Universal Print is a cloud print solution that eliminates the need for printer servers. For more information, see [Universal Print](/universal-print/discover-universal-print).

## Modern print vs legacy print

> [!IMPORTANT]
> We have announced an end of servicing plan for legacy v3 and v4 Windows print drivers. For more information see [End of servicing plan for third-party printer drivers on Windows.](end-of-servicing-plan-for-third-party-printer-drivers-on-windows.md)

Traditionally, PCs communicated with printers by installing drivers. Drivers are software modules created by printer manufacturers that gives PCs instructions on how to send printers information about print jobs in a way that it understands. With modern print, printers communicate to PCs without the need to install drivers, creating an experience with improved security, compatibility, and reliability.

- **Security:** Different printer models and manufacturers mean that there are thousands of drivers out there, and there's no way to verify the security of all of them. For more information about driver security, see [the driver problem.](more-information-on-windows-protected-print-mode-for-enterprises.md#the-driver-problem)

- **Compatibility:** Modern print works regardless of the a PC's architecture. Not all drivers work with ARM devices.  

- **Reliability:** After Windows Update, drivers may not work as expected. Modern print platform provides a more consistent printing experience without the daunting task of keeping drivers up to date.

### Print support applications

The modern print platform works in combination with print support applications to enable customization of the print experience for Windows 10 and 11. For more information, see [Print support app design guide.](../devapps/print-support-app-design-guide.md)

## Introducing Windows protected print mode  

Improve the security of a PC and eliminate driver issues by enabling Windows protected print mode. Windows protected print mode provides many additional print security features. It also simplifies the printing experience by allowing PCs exclusively print using the Windows modern print stack, which is designed to work with [Mopria certified printers](https://mopria.org/certified-products) only. For more information, see [Windows protected print mode](windows-protected-print-mode.md).
