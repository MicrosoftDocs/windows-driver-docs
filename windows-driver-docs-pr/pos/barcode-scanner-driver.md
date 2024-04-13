---
title: Barcode Scanner Driver Sample
description: The barcode scanner driver sample demonstrates how to create a universal driver for a barcode scanner and is intended to be used as a template for creating a new barcode scanner driver.
ms.date: 03/17/2023
---

# Barcode scanner driver sample

The barcode scanner driver sample demonstrates how to create a universal driver for a barcode scanner and is intended to be used as a template for creating a new barcode scanner driver. The sample uses the User-Mode Driver Framework (UMDF) 2.0 and demonstrates basic functionality such as claiming the device for exclusive access. The sample driver can be compiled and deployed on x86, amd64, and Arm platforms. For more information on universal drivers, go to [Getting Started with Universal Windows drivers](../develop/getting-started-with-windows-drivers.md).

## Requirements

- Windows 10

- [Microsoft Visual Studio](https://visualstudio.microsoft.com) (any version)

- [Windows Driver Kit (WDK) 10](../download-the-wdk.md)

The Windows Software Development Kit (SDK) 10 is also required, but this is installed as part of Microsoft Visual Studio.

The sample driver does not require any barcode scanner hardware to function because it operates on a software device. If you have a hardware device you wish to use with the sample, you can still use the driver by adding the device hardware ID to the INF file.

## Download and extract the sample

The [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) are available on GitHub.

1. Download [**Windows-driver-samples-master.zip**](https://github.com/microsoft/Windows-driver-samples/archive/master.zip). This file contains all Windows Driver Kit (WDK) samples.

1. Extract **Windows-driver-samples-master.zip** to the location of your choice on your development machine. This location will be referred to as `<sample_root>` throughout the remainder of this article.

## Open the driver solution in Visual Studio

1. In Windows Explorer, navigate to the `<sample_root>\pos\drivers\barcodescanner` folder.

1. Double-click the solution file, **BarcodeScanner.sln** to open the solution with Visual Studio.

1. The project zip file was downloaded from the Internet so you may see a security warning when you open the solution. If you do, select **OK** to finish loading the project.

1. In Visual Studio, locate **Solution Explorer**. If this is not already open, select **Solution Explorer** from the **View** menu. In **Solution Explorer**, you can see the project and the source files it contains.

## Build the sample using Visual Studio

1. From the *Standard* toolbar in Visual Studio, select the *Solution Platform* that matches your operating system platform. For example, if you are using a 64-bit version of Windows, select x64. If targeting the Arm platform, you will need to use the configuration manager to add Arm to your list of targets.

1. Select **Build Solution** from the **Build** menu.

## Install the driver

1. When built, the driver was signed with a test certification. In order to install the driver for testing, you need to change your boot configuration to allow drivers signed with a test certificate to load. To change the setting, open up an elevated command prompt and enter the command:

    `bcdedit.exe /set TESTSIGNING on`

1. Reboot your machine. If test-signing had been enabled previously, a reboot is not necessary.

1. From an elevated command prompt, navigate to the folder where your project was built. If you created an x64 debug build, this folder will be `<project_root>\x64\Debug\SampleBarcodeScannerDrv`.

    In that folder, you will see the following files:

    | File | Description |
    |--|--|
    | SampleBarcodeScannerDrv.dll | The driver file. |
    | SampleBarcodeScannerDrv.inf | An INF file that contains information needed to install the driver. |
    | samplebarcodescannerdrv.cat | A signed catalog file, which serves as the signature for the entire package. |

1. Identify the path to the Device Console utility (devcon.exe) that matches your OS and driver platform. The default locations for the x64 version is `C:\Program Files (x86)\Windows Kits\10\Tools\x64`.

1. Type the following command, replacing `<devcon\_path>` with the path to the devcon.exe file that you located in the previous step.

    `<devcon_path>\devcon.exe install SampleBarcodeScannerDrv.inf Root\SampleBarcodeScannerDrv`

1. You will see a **Windows Security** dialog informing you that the publisher of the driver can not be verified. This is because the driver was signed with a test certificate. Select **Install this driver software anyway**. In a moment, you will see confirmation that your driver was installed correctly.

If the Device Console utility was not able to install the driver, confirm that you were using the one that matches your current OS platform and the platform of the driver.

## View the device in Device Manager

1. Open Device Manager. This can be done many ways, but if you are still in a command prompt, type `devmgmt`.

1. In Device Manager, choose **Devices by type** from the **View** menu.

1. Your device is listed under the **Samples** node.
