---
ms.assetid: E109BD80-F9CB-4F1F-A6FD-1142E27EC6AD
title: Getting Started with Windows Drivers
description: Windows drivers allow you to create one driver that runs on multiple device types, from embedded systems to tablets and PCs.
ms.date: 04/20/2018
ms.localizationpriority: medium
---

# Getting Started with Windows Drivers

In future releases of Windows 10, drivers in the Windows ecosystem will be classified as one of two types: **Windows Drivers** or **Windows Desktop Drivers**. 

Windows Drivers are intended to run on *all Windows offerings* including **Windows 10X** and **Windows 10 Desktop editions**.  Windows Desktop Drivers will *only* run on **Windows 10 Desktop editions**.  

Windows Drivers are the next stage in the evolution of drivers in the Windows ecosystem.  Windows Drivers inherit the same principles from what were previously known as "Universal Drivers" and additionally adopt new requirements.  Windows Drivers implement the latest best practices in driver development and as a result are **easier to update**, **more resilient to external changes**, and **more straightforward to install**. 

The documentation in this section is intended to detail the motivation for introducing the distinction between Windows Drivers and Windows Desktop Drivers, illustrate the differences between the two types of drivers, and detail the requirements for Windows Drivers.  

> [!NOTE]
> There is no change to driver certification and submission for Windows 10 Version 2004.
> Details regarding certification and submission to the [Windows Hardware Developer Center Dashboard](https://msdn.microsoft.com/windows/hardware/gg236587.aspx) for Windows Drivers and Windows Desktop Drivers will come at a later date.


## Windows 10X and Windows Drivers

Windows 10X does not replace Windows 10, but is a part of the Windows 10 family. 

Windows Drivers were introduced in order to ensure the drivers running on Windows 10X systems guarantee the security, serviceability, and reliability promises that come with the Windows 10X operating system.

Windows Drivers have the benefit of being able to run on both Windows 10X and Windows 10 Desktop editions, while Windows Desktop Drivers will only run on Windows 10 Desktop editions.  

**A Windows Driver running on Windows 10 Desktop editions will benefit from adhering to Windows Drivers requirements**.  

A Windows Driver running on Windows 10 Desktop benefits from improved serviceability and reliability.  Additionally, Windows Drivers running on Windows 10 Desktop follow all of the best practices that are *required* for drivers on Windows 10X, preparing the driver for when certification of drivers for Windows 10X systems becomes generally available at a future date. 

## Windows Drivers vs. Windows Desktop Drivers

|                                                                     |Windows Drivers|Windows Desktop Drivers |
| --------------------------------------------------------------------|:-------------:|:----------------------:|
| Run on Windows 10 Desktop                                           | Yes           | Yes                    |
| Run on Windows 10X                                                  | Yes           | No                     |
| Must be certified with WHCP                                         | Yes           | No                     |
| WDK & HLK are primary vehicles for developing and certifying drivers| Yes           | Yes                    |
| Requirements introduced to improve reliability and serviceability   | Yes           | No                     |

## Windows Drivers Requirements

Windows Drivers must adhere to the following requirements:

- Compliant with [**DCH Design Principles**](dch-principles-best-practices.md)
- Follow the principles of [**Driver Package Isolation**](driver-isolation.md)
- Adhere to [**API Layering Requirements**](api-layering.md)

Additionally, all Windows Drivers **must be [WHCP certified](https://docs.microsoft.com/windows-hardware/design/compatibility/whcp-certification-process) using the [Hardware Lab Kit](https://docs.microsoft.com/windows-hardware/test/hlk/)** as the main certification vehicle.

## Driver Certification and Submission for Windows 10 Version 2004

This distinction between Windows Drivers and Windows Desktop Drivers **does not impact any driver being submitted and certified for Windows 10 Version 2004**.  Changes in certification and submission processes that reflect the distinction between Windows Drivers and Windows Desktop Drivers will happen at a later date.  Appropriate guidance and documentation will be provided ahead of any changes made.



