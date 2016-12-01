---
title: Magnetic stripe reader driver sample
author: windows-driver-content
description: The magnetic stripe reader driver sample demonstrates how to create a universal driver for a magnetic stripe reader and is intended to be used as a template for creating a new driver.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 92A8C116-F71F-4A74-A453-44C14297BCDD
---

# Magnetic stripe reader driver sample


The magnetic stripe reader driver sample demonstrates how to create a universal driver for a magnetic stripe reader and is intended to be used as a template for creating a new driver. The sample uses the User-Mode Driver Framework (UMDF) 2.0 and demonstrates basic functionality such as claiming the device for exclusive access. The sample driver can be compiled and deployed on x86, amd64, and ARM platforms.

## Requirements


-   Windows 10
-   [Microsoft Visual Studio 2015](https://go.microsoft.com/fwlink/p/?LinkId=533470) (any version)
-   [Windows Driver Kit (WDK) 10](https://go.microsoft.com/fwlink/p/?LinkId=733614)

The Windows Software Development Kit (SDK) 10 is also required, but this is installed as part of Microsoft Visual Studio 2015.

**Note**  The sample driver does not require any magnetic stripe reader hardware to function because it operates on a software device. If you have a hardware device you wish to use with the sample, you can still use the driver by adding the device's hardware ID to the INF file.

 

## Download and extract the sample


Starting with Windows 10, Windows driver samples are available on GitHub and can be downloaded from the [Windows driver samples repository project page](http://go.microsoft.com/fwlink/p/?LinkId=616507).

1.  Download **Windows-driver-samples-master.zip** from <http://go.microsoft.com/fwlink/p/?LinkID=623296>. This file contains all of the Windows driver samples.
2.  Extract **Windows-driver-samples-master.zip** to the location of your choice on your development machine. This location will be referred to as *&lt;sample\_root&gt;* throughout the remainder of this article.

## Open the driver solution in Visual Studio


1.  In Windows Explorer, navigate to the `<sample_root>\pos\drivers\MagneticStripeReader\` folder.
2.  Double-click the solution file, **MagneticStripeReader.sln** to open the solution with Visual Studio 2015.
3.  The project zip file was downloaded from the Internet so you may see a security warning when you open the solution. If you do, click **OK** to finish loading the project.
4.  In Visual Studio, locate **Solution Explorer**. If this is not already open, select **Solution Explorer** from the **View** menu. In **Solution Explorer**, you can see the project and the source files it contains.

## Build the sample using Visual Studio


1.  From the *Standard* toolbar in Visual Studio, select the *Solution Platform* that matches your operating system platform. For example, if you are using a 64-bit version of Windows, select x64.
    **Note**  If targeting the ARM platform, you will need to use the configuration manager to add ARM to your list of targets.

     

2.  Select **Build Solution** from the **Build** menu.

## Install the driver


1.  When built, the driver was signed with a test certification. In order to install the driver for testing, you need to change your boot configuration to allow drivers signed with a test certificate to load. To change the setting, open up an elevated command prompt and enter the command:

    `bcdedit.exe /set TESTSIGNING on`

2.  Reboot your machine.
    **Note**  If test-signing had been enabled previously, a reboot is not necessary.

     

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20Magnetic%20stripe%20reader%20driver%20sample%20%20RELEASE:%20%289/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


