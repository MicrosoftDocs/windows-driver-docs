---
title: Attestation Sign Windows Drivers
description: Sign a Windows driver by using attestation signing, create and sign the CAB file, submit and validate the signed file in the Partner Center, and test your driver on Windows.
ms.date: 07/15/2025
---

# Attestation sign Windows drivers

This article describes how to sign a driver by using attestation signing. For detailed information and requirements for attestation signing, see [Windows 10 attestation signed drivers](code-signing-reqs.md#windows-10-attestation-signed-drivers-for-testing-scenarios).

> [!IMPORTANT]
> As of March 1, 2023, attestation signed drivers that target retail audiences are no longer published on Windows Update. Support continues for attestation-signed drivers when testing scenarios with the **CoDev** or **Test Registry Key / Surface SSRK** options.

## Prerequisites

- Read and understand the requirements for [Windows 10 attestation signed drivers](code-signing-reqs.md#windows-10-attestation-signed-drivers-for-testing-scenarios) for testing scenarios.

- Register for the Hardware Developer program. If you aren't registered, follow the steps in [Register for the Microsoft Windows Hardware Developer Program](hardware-program-register.md).

- You must have an extended validation (EV) code signing certificate. Check whether your organization already has a code signing certificate.

   - If you have an existing certificate, make the certificate available.
   
   - If your organization doesn't have a certificate, [purchase an EV certificate](code-signing-reqs.md#ev-certificate-signed-drivers).

- Download and install the Windows Assessment and Deployment Kit (Windows ADK) by following the process described in [Download and install the Windows ADK](/windows-hardware/get-started/adk-install).

- (Optional) Download the [Echo driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/echo/kmdf/driver/AutoSync) used in this article, which is available on GitHub.

## Create the CAB file

The following procedure creates a CAB files submission by using the [Echo driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/general/echo/kmdf/driver/AutoSync) to illustrate the steps.

A typical CAB file submission must contain the following components:

- The driver itself, for example *Echo.sys*.

- The driver INF (*.inf*) file used by the dashboard to facilitate the signing process.

- The symbol file used for debugging information, such as *Echo.pdb*. The *.pdb* file is required for Microsoft's automated crash analysis tools.

- Catalog *.CAT* files are required and used for company verification only. Microsoft regenerates catalog files and replaces any catalog files submitted previously.

> [!NOTE]
> Each driver folder in your CAB file must support the same set of architectures. For example, they must support x86, x64, or they must all support both x86 and x64.
>
> Don't use UNC file share paths when you reference your driver locations (`\server\share`). You must use a mapped drive letter for the CAB to be valid.

To create the CAB file, follow these steps:

1. Gather the binaries to be signed into a single directory. This example uses the `C:\Echo` folder.

1. Open a Command Prompt window with Administrator privileges.

1. Enter the `MakeCab /?` command to see the command options:

   ```cmd
   C:\Echo> MakeCab /?
   Cabinet Maker - Lossless Data Compression Tool

   MAKECAB [/V[n]] [/D var=value ...] [/L dir] source [destination]
   MAKECAB [/V[n]] [/D var=value ...] /F directive_file [...]

   source         File to compress.
   destination    File name to give compressed file. If omitted, the
                  last character of the source file name is replaced
                  with an underscore (_) and used as the destination.
   /F directives  A file with MakeCAB directives (may be repeated). Refer to
                  Microsoft Cabinet SDK for information on directive_file.
   /D var=value   Defines variable with specified value.
   /L dir         Location to place destination (default is current directory).
   /V[n]          Verbosity level (1..3).
   ```

1. Prepare a cab file DDF input file. For the Echo driver in this example, the input might be similar to the following code:

   ```ddf
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

1. Enter the following command to create the CAB file:

   ```cmd
   C:\Echo> MakeCab /f "C:\Echo\Echo.ddf
   ```

   The output of the `MakeCab` command should display the number of files in the created CAB file. In this case, there should be two files.

   ```cmd
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

1. Locate the CAB file in the `Disk1` subdirectory. You can select the CAB file in File Explorer to verify it contains the expected files.

## Sign the CAB file with your EV certificate

The next procedure step is to sign the CAB file with your EV certificate.

Use the process recommended by your EV certificate provider. For example, to sign your CAB file with an SHA256 Certificate/Digest Algorithm/Timestamp, enter the following command:

```cmd
C:\Echo> SignTool sign /s MY /n "Company Name" /fd sha256 /tr http://sha256timestamp.ws.symantec.com/sha256/timestamp /td sha256 /v "C:\Echo\Disk1\Echo.cab"
```

> [!IMPORTANT]
> Remember to use industry best practices to manage the security of the EV code signing process.

## Submit the EV signed Cab file in the Partner Center

After you sign the CAB file, you're ready to submit the file in the Partner Center:

1. Go to the [Partner Center hardware dashboard](https://partner.microsoft.com/dashboard/hardware/Search) and sign in with your credentials.

1. Select **Submit new hardware**:

   :::image type="content" source="./images/code-signing-attestation/hardware-list.png" alt-text="Screenshot of the list of hardware submissions.":::

1. In the **Packages and signing properties** section, enter a product name for your driver submission. This name can be used to search for and organize your driver submissions.

   > [!NOTE]
   > The name is visible when you share your driver with another company.

1. Leave both test-signing options unchecked (not selected).

1. For the **Requested Signatures** option, select the signatures to include in your driver package:

   :::image type="content" source="./images/code-signing-attestation/attestation-flow.png" alt-text="Screenshot showing the options for submitting the Echo driver for signing.":::

1. Select **Submit** at the bottom of the page.

1. After the signing process completes, download your signed driver from the hardware dashboard.

## Validate the driver is properly signed

Confirm your driver was properly signed with these steps:

1. After you download the submission file, extract the driver file.

1. Open a Command Prompt window with Administrator privileges.

1. Enter the following command to verify the driver is signed as expected:

   ```cmd
   C:\Echo> SignTool verify Echo.Sys
   ```

1. To list other information and have SignTool verify all signatures in a file with multiple signatures, enter the following command:

   ```cmd
    C:\Echo> SignTool verify /pa /ph /v /d Echo.Sys
   ```

1. To confirm the EKUs of the driver complete the following steps:

   1. Open Windows Explorer and locate the binary file. Right-click the file and select **Properties**.

   1. On the **Digital Signatures** tab, select the listed item in the Signature list.

   1. Select **Details**, and then select **View Certificate**.

   1. On the **Details** tab, select **Enhanced Key Usage**.

The driver uses the following process when it resigns the driver:

1. Append a Microsoft SHA2 embedded signature.

1. If the driver binaries are embedded signed by the customer with their own certificates, overwrite the signatures.

1. Create and sign a new catalog file with an SHA2 Microsoft certificate. The catalog replaces any existing catalog provided by the customer.

## Test your driver on Windows

Install the sample driver and test it on Windows:

1. Open a Command Prompt window with Administrator privileges.

1. Go to your driver package folder, and enter the following command.

   ```cmd
   C:\Echo> devcon install echo.inf root\ECHO
   ```

1. Confirm the driver install process doesn't show the following error message:

   > _Windows can't verify the publisher of this driver software_ message._

## Create a submission with multiple drivers

Submit multiple drivers at the same time by following these steps:

1. Create a subdirectory for each driver:

   :::image type="content" source="./images/code-signing-attestation/multiple-driver-signing.png" border="false" alt-text="Diagram showing an example driver signing directory structure.":::

1. Prepare a CAB file DDF input file that references the subdirectories. For this example, the input might be similar to the following code:

   ```ddf
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
