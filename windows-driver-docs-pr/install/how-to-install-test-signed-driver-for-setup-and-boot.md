---
title: How to Install a Test-signed Driver Package Required for Windows Setup and Boot
description: Describes how to install a test-signed driver package on a computer running Windows Server or after Windows Setup
ms.date: 03/03/2022
---

# How to Install a Test-signed Driver Package Required for Windows Setup and Boot

This page describes how to install a test-signed driver package on a computer running Windows Server 2019 (or Windows Server 2016), or on a computer starting for the first time after Windows Setup. You should only use a test-signed driver package in a test environment.

For more info, see [Introduction to Test-Signing](introduction-to-test-signing.md).

Before you begin, ensure that you have:
* [Windows Assessment and Deployment Kit (ADK)](/windows-hardware/get-started/adk-install) and Windows PE add-on for the ADK
* Windows Server 2019 or 2016 Installation Media ISO file

## Creating the ISO file

Use the following steps to create an ISO file and install Windows from it:
1. In the ADK Start Menu options, choose **Deployment and Imaging Tools Environment**, right-click, and select **Run as administrator**.
2. Run **copype** to create a working copy of the Windows PE files: `copype amd64 C:\WinPE_amd64`
3. Enable **testsigning**. On a non-UEFI (legacy) computer, use:

```cmd
cd C:\WinPE_amd64\media\Boot
bcdedit /store .\BCD /enum all
bcdedit /store .\BCD /set {default} testsigning on
```

On a UEFI platform, use:

```cmd
cd C:\WinPE_amd64\media\EFI\Microsoft\Boot
bcdedit /store .\BCD /enum all
bcdedit /store .\BCD /set {default} testsigning on
```

4. To verify that `testsigning Yes` now appears for the {default} identifier, under Windows Boot Loader, run `bcdedit /store .\BCD /enum all` a second time.

5.	Mount the Windows Server 2016 Installation Media ISO file to a drive, for example, `G`, and manually copy all files under the sources folder, for example `G:\sources`, to the sources folder of the WinPE system files, for example `C:\WinPE_amd64\media\sources`.

> [!NOTE]
> Do not overwrite the existing `boot.wim` file in the folder `C:\WinPE_amd64\media\sources`. We'll use the original WinPE environment later.

Now we have all the files including WinPE and Windows Server 2016.

6. Optionally copy a test-signed driver package to the folder `C:\WinPE_amd64\media`. Files copied might include the driver package's .cat, .cer, .inf, and .sys files.
Use the following commands to import the test-signed driver package to the WIM file:

```cmd
Dism /Get-WimInfo /wimfile:C:\WinPE_amd64\media\sources\install.wim
Dism /Mount-Image /imagefile:C:\WinPE_amd64\media\sources\install.wim /index:4 /mountdir:C:\WinPE_amd64\mount
Dism /image:C:\WinPE_amd64\mount /Add-Driver /driver:C:\WinPE_amd64\media\DriverSample
Dism /unmount-image /mountdir:C:\WinPE_amd64\mount /commit
```

7.	Create a new ISO file: `Makewinpemedia /iso C:\winpe_amd64 C:\WS2016_amd64.iso`. While the default application in the ISO file is the cmd.exe, you'll launch the setup.exe manually to configure boot settings after installation.  

8. Install Windows Server 2016 from `WS2016_amd64.iso`. Optionally, customize the installation source to import more driver packages.

## Installing the driver package

Use these steps to install the driver package:

1. Turn off **Secure Boot** on the test computer and then start the WinPE system.
2. After the machine boots with the ISO file, a command prompt appears.
3. To identify the letter of the drive with the mounted ISO file, use `diskpart`, then `list volume`. Find the volume with **Type** of `DVD-ROM`. Type `exit`.
4. Navigate to the ISO drive and switch to the driver pacakge sample directory, for example `D:\DriverSample`.
5. Use the following commands to install the test driver package:
```cmd
certmgr.exe -add DriverSample.cer -s -r localmachine root
certmgr.exe -add DriverSample.cer -s -r localmachine trustedpublisher
pnputil.exe /add-driver DriverSample.inf /install
```
6. Optionally, confirm the installation by reviewing the `%windir%\inf\setupapi.dev.log` log.
7. Run `setup.exe /NoReboot`, for example from `D:\sources`.
8. After installation, a message appears indicating that the setup application can be closed. Exit the application to return to the WinPE command prompt.
9. Type `diskpart`. Identify the OS boot partition and the drive letter for that boot partition (The only FAT32 partition and the size is about 100MB)
10. Navigate to the boot partition drive and switch directory to the location of the BCD file, for example `E:\EFI\Microsoft\Boot`.
11. Turn on **testsigning**: `bcdedit /store BCD /set {default} testsigning on` and reboot the computer.
12. To confirm that the computer is in test mode, look for a **Test Mode** watermark in the lower right of the desktop.

The computer must be in Test Mode to load a test-signed driver package. If there is a boot device requiring the test-signed driver package, the test-signed driver package must be imported to the WIM file (use the optional Dism steps above) to avoid PnP installation later. If you turn off the **testsigning** setting, the machine may fail to boot.
