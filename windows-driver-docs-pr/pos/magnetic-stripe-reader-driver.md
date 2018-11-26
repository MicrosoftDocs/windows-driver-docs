---
title: Magnetic stripe reader driver sample
description: This sample demonstrates how to create a universal driver for a magnetic stripe reader and is intended as a template for creating a new driver.
ms.assetid: 92A8C116-F71F-4A74-A453-44C14297BCDD
ms.date: 09/07/2018
ms.localizationpriority: medium
---

# Magnetic stripe reader driver sample

The magnetic stripe reader driver sample demonstrates how to create a universal driver for a magnetic stripe reader and is intended to be used as a template for creating a new driver. The sample uses the User-Mode Driver Framework (UMDF) 2.0 and demonstrates basic functionality such as claiming the device for exclusive access. The sample driver can be compiled and deployed on x86, amd64, and ARM platforms.

## Requirements

-   Windows 10
-   [Microsoft Visual Studio 2015](https://go.microsoft.com/fwlink/p/?LinkId=533470) (any version)
-   [Windows Driver Kit (WDK) 10](https://go.microsoft.com/fwlink/p/?LinkId=733614)

The Windows Software Development Kit (SDK) 10 is also required, but this is installed as part of Microsoft Visual Studio 2015.

> [!NOTE]
> The sample driver does not require any magnetic stripe reader hardware to function because it operates on a software device. If you have a hardware device you wish to use with the sample, you can still use the driver by adding the device's hardware ID to the INF file.

## Download and extract the sample

Starting with Windows 10, Windows driver samples are available on GitHub and can be downloaded from the [Windows driver samples repository project page](http://go.microsoft.com/fwlink/p/?LinkId=616507).

1.  Download **Windows-driver-samples-master.zip** from [GitHub](http://go.microsoft.com/fwlink/p/?LinkID=623296). This file contains all of the Windows driver samples.
2.  Extract **Windows-driver-samples-master.zip** to the location of your choice on your development machine. This location will be referred to as *&lt;sample\_root&gt;* throughout the remainder of this article.

## Open the driver solution in Visual Studio

1.  In Windows Explorer, navigate to the `<sample_root>\pos\drivers\MagneticStripeReader\` folder.
2.  Double-click the solution file, **MagneticStripeReader.sln** to open the solution with Visual Studio 2015.
3.  The project zip file was downloaded from the Internet so you may see a security warning when you open the solution. If you do, click **OK** to finish loading the project.
4.  In Visual Studio, locate **Solution Explorer**. If this is not already open, select **Solution Explorer** from the **View** menu. In **Solution Explorer**, you can see the project and the source files it contains.

## Build the sample using Visual Studio

1.  From the *Standard* toolbar in Visual Studio, select the *Solution Platform* that matches your operating system platform. For example, if you are using a 64-bit version of Windows, select x64.
    > [!NOTE]
    > If targeting the ARM platform, you will need to use the configuration manager to add ARM to your list of targets.

2.  Select **Build Solution** from the **Build** menu.

## Install the driver

1.  When built, the driver was signed with a test certification. In order to install the driver for testing, you need to change your boot configuration to allow drivers signed with a test certificate to load. To change the setting, open up an elevated command prompt and enter the command:

    `bcdedit.exe /set TESTSIGNING on`

2.  Reboot your machine.
    > [!NOTE]
    > If test-signing had been enabled previously, a reboot is not necessary.

     

3.  From an elevated command prompt, navigate to the folder where your project was built. If you created an x64 debug build, this folder will be `<project_root>\x64\Debug\SampleMagneticStripeReaderDrv`.

    In that folder, you will see the following files:

    | File                              | Description                                                                  |
    |-----------------------------------|------------------------------------------------------------------------------|
    | SampleMagneticStripeReaderDrv.dll | The driver file.                                                             |
    | SampleMagneticStripeReaderDrv.inf | An INF file that contains information needed to install the driver.          |
    | samplemagneticstripereaderdrv.cat | A signed catalog file, which serves as the signature for the entire package. |

     

4.  Identify the path to the Device Console utility (devcon.exe) that matches your OS and driver platform. The default locations for the x64 version is `C:\Program Files (x86)\Windows Kits\10\Tools\x64`.
5.  Type the following command, replacing &lt;devcon\_path&gt; with the path to the devcon.exe file that you located in the previous step.

    `"<devcon_path>\devcon.exe" install SampleMagneticStripeReaderDrv.inf Root\SampleMagneticStripeReaderDrv`

6.  You will see a **Windows Security** dialog informing you that the publisher of the driver can't be verified. This is because the driver was signed with a test certificate. Click **Install this driver software anyway**. In a moment, you will see confirmation that your driver was installed correctly.

If the Device Console utility wasn't able to install the driver, confirm that you were using the one that matches your current OS platform and the platform of the driver.

## View the device in Device Manager

1.  Open Device Manager. This can be done many ways, but if you're still in a command prompt then type `devmgmt`.
2.  In Device Manager, choose **Devices by type** from the **View** menu.
3.  Your device is listed under the **Samples** node.
