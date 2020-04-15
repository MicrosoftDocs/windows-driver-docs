---
ms.assetid: E109BD80-F9CB-4F1F-A6FD-1142E27EC6AD
title: Getting Started with Windows Drivers
description: Windows drivers allow you to create one driver that runs on multiple device types, from embedded systems to tablets and PCs.
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# Getting Started with Windows Drivers

Starting at some point *after* Windows 10, version 2004, drivers that run on Windows will be classified as **Windows Drivers** or **Windows Desktop Drivers**. 

Windows Drivers will run on *all Windows offerings*, including **Windows 10X** and **Windows 10 Desktop editions**.  Windows Desktop Drivers will *only* run on **Windows 10 Desktop editions**.  

The *Windows Driver* classification will extend and replace the current *Universal Driver* classification. 

This page provides a preview of the upcoming requirements for Windows Drivers.  

> [!NOTE]
> This distinction between Windows Drivers and Windows Desktop Drivers **does not impact any driver being submitted and certified for Windows 10 Version 2004**.  Changes in certification and submission processes that reflect the distinction between Windows Drivers and Windows Desktop Drivers will happen at a later date.  Appropriate guidance and documentation will be provided ahead of any changes made.


## Windows 10X and Windows Drivers

While it won't be required for a driver running only on Windows 10 Desktop to meet the additional requirements for a Windows Driver, it will still be beneficial for the driver from a serviceability and reliability standpoint.

In addition, the driver is also prepared for when certification of drivers for Windows 10X systems becomes available.

## Windows Drivers vs. Windows Desktop Drivers

This table highlights the differences that will apply when Windows Drivers become a certification option:

|                                                                     |Windows Drivers|Windows Desktop Drivers |
| --------------------------------------------------------------------|:-------------:|:----------------------:|
| Run on Windows 10 Desktop                                           | Yes           | Yes                    |
| Run on Windows 10X                                                  | Yes           | No                     |
| Must be certified with WHCP                                         | Yes           | No                     |
| WDK & HLK are primary vehicles for developing and certifying drivers| Yes           | Yes                    |
| Reliability and serviceability requirements     | Yes           | No                     |

For info about WHCP, see [Windows Hardware Compatibility Program Certification Process](https://docs.microsoft.com/windows-hardware/design/compatibility/whcp-certification-process).

## Windows Drivers Requirements

Windows Drivers will have the following requirements:

- Compliant with [**DCH Design Principles**](dch-principles-best-practices.md)
- Follow the principles of [**Driver Package Isolation**](driver-isolation.md)
- Follow [**API Layering Requirements**](api-layering.md)
- Certified with [Windows Hardware Compatibility Program Certification Process](https://docs.microsoft.com/windows-hardware/design/compatibility/whcp-certification-process) using the [Hardware Lab Kit](https://docs.microsoft.com/windows-hardware/test/hlk/) as the main certification vehicle

