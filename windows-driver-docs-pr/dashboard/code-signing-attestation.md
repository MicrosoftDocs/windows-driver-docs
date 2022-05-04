---
title: Attestation sign Windows 10+ drivers
description: Attestation sign Windows 10+ drivers
ms.topic: article
ms.date: 04/20/2022
---

# Attestation sign Windows 10+ drivers

This article describes how to sign a driver using attestation signing. For detailed information and requirements for attestation signing, see [Windows 10 attestation signed drivers](code-signing-reqs.md#windows-10-attestation-signed-drivers).

## Prerequisites

- Read and understand the requirements for [Windows 10 attestation signed drivers](code-signing-reqs.md#windows-10-attestation-signed-drivers).

- Register for the Hardware Developer program. If you're not yet registered, follow the steps in [How to register for the Microsoft Windows Hardware Developer Program](hardware-program-register.md).

- You must have an Extended Validation (EV) code signing certificate. Check whether your organization already has a code signing certificate. If your company already has a certificate, have the certificate available. If your organization doesn't have a certificate, you'll need to [purchase an EV certificate](code-signing-reqs.md#ev-certificate-signed-drivers).

- Follow the process described in [Download kits and tools for Windows 10](/windows-hardware/get-started/adk-install) to download and install the Windows Driver Kit (WDK).

- (Optional)  Download the [echo driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/echo/kmdf/driver/AutoSync) that is used in this article.


### Create the CAB file

In this section, we'll step through the process of creating a CAB files submission.  We'll be using the [echo driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/echo/kmdf/driver/AutoSync) to illustrate the process.

A typical CAB file submission must contain the following:

- The driver itself, for example Echo.sys
- The driver INF file that is used by the dashboard to facilitate the signing process.
- The symbol file that is used for debugging information. For example, Echo.pdb.
- Catalog .CAT files are required and used for company verification only. Microsoft regenerates catalog files and replaces any catalog files that were submitted.

> [!NOTE]
> Each driver folder in your CAB file must support the same set of architectures. For example, they must support x86, x64, or they all must support both x86 and x64.
>
> Do not use UNC file share paths when referencing your driver locations (`\\\server\share`).  You must use a mapped drive letter for the CAB to be valid.

To create the CAB file:

   1. Gather the binaries to be signed into a single directory. In this example, we'll use `C:\\Echo`.

   1. Open a Command Prompt window as Administrator.

   1. Enter `MakeCab /?` to view the MakeCab options:

      ```cmd
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

   1. Prepare a cab file DDF input file. For our Echo driver it might look something like this.

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

   1. Enter the following to create the CAB file.

      ```cmd
      C:\Echo> MakeCab /f "C:\Echo\Echo.ddf
      ```

      The output of MakeCab should display the number of files in the created CAB file. In this case, there should be two files.

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

   1. Locate the CAB file in the `Disk1` subdirectory. You can select the CAB file in File Explorer to verify that it contains the expected files.

### Sign the CAB file with your EV certificate

1. Use the process recommended by the EV certificate provider to sign the CAB file with your EV certificate. For example, to sign your CAB file with a SHA256 Certificate/Digest Algorithm/Timestamp, enter the following command: 

   ```cmd
   C:\Echo> SignTool sign /ac "C:\MyEVCert.cer" /s MY /n "Company Name" /fd sha256 /tr http://sha256timestamp.ws.symantec.com/sha256/timestamp /td sha256 /v "C:\Echo\Disk1\Echo.cab"
   ```

   > [!IMPORTANT]
   > Remember to use industry best practices to manage the security of the EV code signing process.

### Submit the EV signed Cab file using the Partner Center

1. Go to [Partner Center hardware dashboard](https://partner.microsoft.com/dashboard/hardware/Search) and sign in using your credentials.

1. Select **Submit new hardware**.

    :::image type="content" source="./images/code-signing-attestation/hardware-list.png" alt-text="Screenshot of the the list of submitted hardware.":::

1. In the **Packages and signing properties** section, enter a product name for your driver submission. This name can be used to search for and organize your driver submissions.

    >[!NOTE]
    >If you share your driver with another company, they will see this name.

1. Leave both test-signing options unchecked.

1. For **Requested Signatures**, select which signatures you wish to include in your driver package.

    :::image type="content" source="./images/code-signing-attestation/attestation-flow.png" alt-text="A screenshot showing the options for submitting the echo driver for signing.":::

1. Move down through the page, and select **Submit**.

1. When the signing process is complete, download your signed driver from the hardware dashboard.

### Validate that the driver was properly signed

Complete the following steps to ensure that the driver was properly signed.

1. After you've downloaded the submission file, extract the driver file.

1. Open a Command Prompt window as Administrator.

1. Enter the following command to verify that the driver was signed as expected.

   ```cmd
   C:\Echo> SignTool verify Echo.Sys
   ```

1. To list additional information and have signtool verify all signatures in a file with multiple signatures, enter the following command:

   ```cmd
    C:\Echo> SignTool verify /pa /ph /v /d Echo.Sys
   ```

1. To confirm the EKUs of the driver complete the following steps.

   1. Open Windows Explorer and locate the binary file. Select and hold (or right-click) the file and select **Properties**.

   1. On the **Digital Signatures** tab, select the listed item in the Signature list.

   1. Select **Details**, and then select **View Certificate**.

   1. On the **Details** tab, select **Enhanced Key Usage**.

When the driver is resigned by the dashboard the following process is used.

- Appends a Microsoft SHA2 embedded signature.
- If the driver binaries are embedded signed by the customer with their own certificates, those signatures won't be overwritten.
- Creates and signs a new catalog file with a SHA2 Microsoft certificate. This catalog replaces any existing catalog provided by the customer.

### Test your driver on Windows 10

Use the following instructions to install the sample driver.

1. Open a Command Prompt window as Administrator. Go to your driver package folder, and enter the following command.

   ```cmd
   C:\Echo> devcon install echo.inf root\ECHO
   ```

1. Confirm that the driver install process doesn't display the "Windows can't verify the publisher of this driver software." Windows security dialog box.

## Create a submission with multiple drivers

To submit multiple drivers at the same time:

1. Create a subdirectory for each driver as shown below.

   :::image type="content" source="./images/code-signing-attestation/multiple-driver-signing.png" alt-text="A diagram showing an example driver signing directory structure.":::

1. Prepare a CAB file DDF input file that references the subdirectories. It might look something like this:

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
