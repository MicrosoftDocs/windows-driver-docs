---
title: Install Rollo USB Printer drivers on Windows
description: Step-by-step instructions for installing the Rollo USB thermal label printer driver on Windows 11, Windows 10, Windows 7, and legacy Windows XP.
ms.topic: tutorial
ms.date: 08/27/2025
ms.service: windows-driver-docs
ms.author: christianrollo
---

# Install Rollo USB Printer drivers on Windows

The **Rollo USB Printer** is a compact thermal label printer used for shipping labels and barcodes.  
This article provides step-by-step guidance to install the Rollo USB printer driver on Windows 11, Windows 10, Windows 7, and legacy Windows XP.

> [!NOTE]
> The Rollo **wireless** model does **not** require drivers on Windows. This tutorial applies only to the **USB** model.

## Prerequisites

- A Rollo **USB** thermal label printer  
- Rollo labels (4 × 6 recommended)  
- Administrative rights on the Windows device  
- Internet access to download the driver package  

## Install the driver on Windows 11 or Windows 10

1. Download the current **Rollo USB printer driver** package.  
2. Extract the `.zip` file to a local folder.  
3. Run `setup.exe` and follow the on-screen instructions.  
4. Connect the printer with the supplied USB cable.  
5. Open **Settings > Bluetooth & devices > Printers & scanners** and confirm the Rollo printer appears.  
6. Print a test label to verify setup.  

## Install the driver on Windows 7

1. Download the driver package and extract the `.zip`.  
2. Open **Control Panel > Devices and Printers** and select **Add a printer**.  
3. Choose **Have Disk**, then browse to the extracted driver folder.  
4. Complete the installation wizard and print a test page.  

## Install the driver on Windows XP (manual install)

Windows XP supports the Rollo driver, but does not support the automated installer. Use Device Manager for a manual install:

1. Download the legacy driver package from the Rollo Support article linked below.  
2. Right-click the `.zip` file and select **Extract All**.  
3. Select **Start**, right-click **My Computer**, and choose **Manage**.  
4. In **Computer Management**, select **Device Manager**.  
5. Expand the appropriate device category, right-click the device, and choose **Update Driver** to open the Hardware Update Wizard.  
6. When prompted for Windows Update, select **No, not this time**, then **Next**.  
7. Select **Install from a list or specific location (Advanced)**, then **Next**.  
8. Select **Search for the best driver in these locations**, check **Include this location in the search**, and choose **Browse**.  
9. Navigate to the extracted driver folder and select **OK**.  
10. Select **Next** to install the driver, then **Finish**.  

## Troubleshooting

- **Printer not detected**: Try a different USB port or cable; avoid hubs during setup.  
- **Installer fails**: Re-run `setup.exe` as an administrator.  
- **Misaligned or blank prints**: In printer preferences, set media size to **4 × 6 in** and confirm application settings match.  

## Additional resources

- [Rollo Support guide for installing drivers on Windows](https://support.rollo.com/support/solutions/articles/29000001096-installing-rollo-driver-on-windows)
