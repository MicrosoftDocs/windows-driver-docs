---
title: Attestation signing a kernel driver for public release
description: This topic describes how to sign a driver using attestation signing.
ms.assetid: A292B15D-37FD-407E-998C-728D9423E712
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attestation signing a kernel driver for public release

This topic describes how to sign a driver using attestation signing.

> [!Note]
> Attestation signing has the following properties.
> -   Attestation signing supports Windows 10 Desktop kernel mode and user mode drivers. Although user mode drivers do not need to be signed by Microsoft for Windows 10, the same attestation process can be used for both user and kernel mode drivers.
> -   Attestation signing will not return the proper PE Level for **ELAM** or **Windows Hello** PE binaries.  These must be tested and submitted as .hlkx packages to receive the additional signature attributes.
> -   Attestation signing requires the use of an EV Certificate to submit the driver to the Hardware Dev Center dashboard.
> -   An attestation signed driver will only work for Windows 10. It will not work for other versions of Windows, such as Windows Server 2016,Windows 8.1, or Windows 7.
> -   Attestation signing requires driver folder names to contain no special characters, and to be less than 40 characters long.
 
## Attestation signing a kernel mode driver

To attestation sign a kernel mode driver complete the following steps:

1. Acquire an EV Code Signing Certificate
2. Register your company for the Hardware Dev Center
3. Download and install the Windows Driver Kit
4. Create a CAB files submission
5. Sign the CAB file submission with your EV Cert
6. Submit the EV signed Cab file using the Hardware Dev Center dashboard
7. Validate that the driver was properly signed
8. Test your driver on Windows 10 for Desktop

## Acquire an EV code signing certificate

Before you can submit binaries to the dashboard for signing, you need to acquire an [extended validation (EV) code signing certificate](get-a-code-signing-certificate.md) to secure your digital information. EV certificates are the accepted standard for establishing ownership of the code you submit.

## Allowable PE signatures and binaries

The following PE levels and binaries can be processed through Attestation:

- **PeTrust**
- **DrmLevel**
- **HAL**
- .exe
- .cab
- .dll
- .ocx
- .msi
- .xpi
- .xap

## Register your company for Hardware Dev Center (Sysdev) Dashboard Services

To sign your drivers through the Hardware dashboard you first need to register your organization and get a code signing certificate.

Follow the process described in [Register for the hardware program](register-for-the-hardware-program.md) to set up the account you will use for the hardware dashboard.

## Download and install the Windows Driver Kit

You will need to download and install the Windows Driver Kit (WDK) to gain access to tools used to sign your driver binary files.

Follow the process described in [Download kits and tools for Windows 10](https://msdn.microsoft.com/windows/hardware/dn913721.aspx) to download and install the WDK.

## Create a CAB Files Submission

To create a CAB file that can be submitted to the dashboard, complete the following steps:

1. Gather the binaries that you will submit to be signed in a single directory. In this example, we will use C:\\Echo. The steps described here will reference the [echo driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/echo/kmdf/driver/AutoSync) available from GitHub.

Typical CAB file submissions contain the following:

- The driver itself, for example Echo.sys
- The driver INF file that is used by the dashboard to facilitate the signing process.
- The symbol file that is used for debugging information. For example, Echo.pdb.
- Catalog .CAT files are not required. Microsoft regenerates catalog files and replaces any catalog files that were submitted.

  > [!NOTE]
  > All driver folders in your CAB file must support the same set of architectures. For example, they all must support x86, x64, or they all must support both x86 and x64.

2. Use MakeCab.exe to process the DDF file and create a cab file.

Open a Command Prompt window as Administrator. Then enter the following command to view the MakeCab options:

MakeCab /?

```cpp
C:\Echo> MakeCab /?
Cabinet Maker - Lossless Data Compression Tool

MAKECAB [/V[n]] [/D var=value ...] [/L dir] source [destination]
MAKECAB [/V[n]] [/D var=value ...] /F directive_file [...]

  source         File to compress.
  destination    File name to give compressed file.  If omitted, the
                 last character of the source file name is replaced
                 with an underscore (_) and used as the destination.
  /F directives  A file with MakeCAB directives (may be repeated). Refer to
                 Microsoft Cabinet SDK for information on directive_file.
  /D var=value   Defines variable with specified value.
  /L dir         Location to place destination (default is current directory).
  /V[n]          Verbosity level (1..3).
```

3. Prepare a cab file DDF input file. For our Echo driver it might look something like this.

```cpp
;*** Echo.ddf example
;
.OPTION EXPLICIT     ; Generate errors
.Set CabinetFileCountThreshold=0
.Set FolderFileCountThreshold=0
.Set FolderSizeThreshold=0
.Set MaxCabinetSize=0
.Set MaxDiskFileCount=0
.Set MaxDiskSize=0
.Set CompressionType=MSZIP
.Set Cabinet=on
.Set Compress=on
;Specify file name for new cab file
.Set CabinetNameTemplate=Echo.cab
; Specify the subdirectory for the files.  
; Your cab file should not have files at the root level,
; and each driver package must be in a separate subfolder.
.Set DestinationDir=Echo
;Specify files to be included in cab file
C:\Echo\Echo.Inf
C:\Echo\Echo.Sys
```
 

4. Call the makecab utility and provide the ddf file as input using the /f option.

```cpp
C:\Echo> MakeCab /f "C:\Echo\Echo.ddf
```

The output of makecab should display the number of files in the created cabinet, in our example 2.

```cpp
C:\Echo> MakeCab /f Echo.ddf
Cabinet Maker - Lossless Data Compression Tool

17,682 bytes in 2 files
Total files:              2
Bytes before:        17,682
Bytes after:          7,374
After/Before:            41.70% compression
Time:                     0.20 seconds ( 0 hr  0 min  0.20 sec)
Throughput:              86.77 Kb/second
```

5. Locate the cab file in the Disk1 subdirectory. You can click the cab file in File Explorer to verify that it contains the expected files.

## Sign the submission CAB file with your EV certificate

1. Use the process recommended by the EV cert provider to sign the cab file with your EV cert. For example, you might use the signtool and if you are using Verisign, you might specify their timestamp server.

```cpp
C:\Echo> SignTool sign /v /ac "C:\MyEVCert.cer" /s MY /n "Company Name" /t http://timestamp.verisign.com/scripts/timstamp.dll "C:\Echo\Disk1\Echo.cab"
```

> [!IMPORTANT]
> Remember to use industry best practices to manage the security of the EV code signing process.

## Submit the EV signed Cab file using the Hardware Dev Center dashboard

1. Submit the EV signed CAB file using the Hardware Dev Center. See [Driver Signing Properties](https://msdn.microsoft.com/windows/hardware/drivers/develop/driver-signing-properties) for more information.

   * As part of the submission process, you must specify whether you are submitting [universal drivers](https://msdn.microsoft.com/windows/hardware/drivers/develop/getting-started-with-universal-drivers).

   * The following screen shot shows the options for submitting the echo driver for signing.
    ![a screenshot showing the options for submitting the echo driver for signing](images/attestation-driver-signing-submission-dashboard.png)

2. When the signing process is complete, download your signed driver from the hardware dashboard.

## Validate that the driver was properly signed

Complete the following steps to ensure that the driver was properly signed.

1. After you have downloaded the submission file, extract the driver file.

2. Open a Command Prompt window as Administrator. Then enter the following command to verify that the driver was signed as expected.

```cpp
C:\Echo> SignTool verify Echo.Sys
```

3.To list additional information and have signtool verify all signatures in a file with multiple signatures, type the following.

```cpp
C:\Echo> SignTool verify /pa /ph /v /d Echo.Sys
```

4. To confirm the EKUs of the driver complete the following steps.
a. Open Windows Explorer and locate the binary file. Right-click the file and select **Properties**.
b. On the **Digital Signatures** tab, select the listed item in the Signature list.
c. Select the **Details** button, and then select **View Certificate**.
d. On the **Details** tab, select the **Enhanced Key Usage** field.
When the driver is resigned by the dashboard the following process is used.

- Appends a Microsoft SHA2 embedded signature.
- If the driver binaries are embedded signed by the customer with their own certificates, those signatures will not be overwritten.
- Creates and signs a new catalog file with a SHA2 Microsoft certificate. This catalog replaces any existing catalog provided by the customer.

## Test your driver on Windows 10

Use the following instructions to install the sample driver.

1. Open Device Manager, right click on the computer icon and select "Add legacy Hardware". Follow the prompts to complete the install of the driver.

2. Alternatively, open a Command Prompt window as Administrator and use devcon to install the driver. Navigate to your driver package folder, and enter the following command.

```cpp
C:\Echo> devcon install echo.inf root\ECHO
```

3. Confirm that the driver install process does not display the "Windows can't verify the publisher of this driver software." Windows security dialog box.

## Create a submission with multiple drivers

To submit multiple drivers at the same time create a sub directory for each driver as shown below.

![An image showing an example driver signing directory structure.](images/multiple-driversigning.png)

Prepare a CAB file DDF input file that references the subdirectories. It might look something like this:

```cpp
;*** Submission.ddf multiple driver example
;
.OPTION EXPLICIT     ; Generate errors
.Set CabinetFileCountThreshold=0
.Set FolderFileCountThreshold=0
.Set FolderSizeThreshold=0
.Set MaxCabinetSize=0
.Set MaxDiskFileCount=0
.Set MaxDiskSize=0
.Set CompressionType=MSZIP
.Set Cabinet=on
.Set Compress=on
;Specify file name for new cab file
.Set CabinetNameTemplate=Echo.cab
;Specify files to be included in cab file
; First Driver
.Set DestinationDir=DriverPackage1
C:\DriverFiles\DriverPackage1\Driver1.sys
C:\DriverFiles\DriverPackage1\Driver1.inf
; Second driver
.Set DestinationDir=DriverPackage2
C:\DriverFiles\DriverPackage2\Driver2.sys
C:\DriverFiles\DriverPackage2\Driver2.inf
```

You can follow these steps to sign, submit and test the other driver files you wish to submit.
