---
title: Verifying the Signature of a Release-Signed Driver File
description: Verifying the Signature of a Release-Signed Driver File
ms.date: 04/20/2017
---

# Verifying the Signature of a Release-Signed Driver File


To verify an embedded signature in a driver file that is created by a [Software Publisher Certificate (SPC)](./deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md), use the following [**SignTool**](../devtest/signtool.md) command:

```cpp
SignTool verify /v /kp DriverFileName.sys
```

Where:

-   The **verify** command configures SignTool to verify the signature that is embedded in the driver file *DriverFileName.sys.*

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/kp** option configures SignTool to verify that the signature that is embedded in *DriverFileName.sys* complies with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) for Windows Vista and later versions of Windows.

-   *DriverFileName.sys* is the name of the driver file.

For example, the following command verifies that *Toaster.sys* has a valid embedded signature. In this example, T*oaster.sys* is in the *amd64* subdirectory under the directory in which the command is run.

```cpp
SignTool verify /kp amd64\toaster.sys
```