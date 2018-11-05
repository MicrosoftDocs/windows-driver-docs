---
title: Verifying the Signature of a Test-Signed Driver File
description: Verifying the Signature of a Test-Signed Driver File
ms.assetid: 21f4c42c-3d6e-453c-acff-f4b8acc3e20b
keywords:
- test signing driver files WDK
- verifying test signatures
- checking test signatures
- test signatures WDK
- validating test certificates WDK
- driver file test signing WDK
- test signing driver packages WDK , driver files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying the Signature of a Test-Signed Driver File


To verify a test signature that is embedded in a driver file, use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```cpp
SignTool verify /v /pa DriverFileName.sys
```

Where:

-   The **verify** command configures SignTool to verify the signature that is embedded in the driver file *DriverFileName.sys.*

-   The **/v** option configures SignTool to print the execution and warning messages.

-   The **/pa** option configures SignTool to verify that the signature that is embedded in *DriverFileName.sys* complies with the PnP device installation signing requirements.

-   *DriverFileName.sys* is the name of the driver file.

Be aware that the SignTool **verify** command does not explicitly specify the test certificate that was used to sign the driver file. For the verify operation to succeed, you must first install the test certificate in the [Trusted Root Certification Authorities certificate store](trusted-root-certification-authorities-certificate-store.md) of the local computer that you use to verify the signature. For more information about how to install the test certificate in the Trusted Root Certification Authorities certificate store of a local computer, see [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md). The installation procedure is the same on both the signing computer and a test computer.

For example, the following command verifies the embedded signature in *Toaster.sys*, which is in the *amd64* subdirectory under the directory in which the command is run.

```cpp
SignTool verify /v /pa amd64\toaster.sys
```

 

 





