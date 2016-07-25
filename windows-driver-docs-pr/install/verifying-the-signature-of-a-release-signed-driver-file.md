---
title: Verifying the Signature of a Release-Signed Driver File
description: Verifying the Signature of a Release-Signed Driver File
ms.assetid: 70876389-6493-4c16-8a82-ca72fc23325c
---

# Verifying the Signature of a Release-Signed Driver File


To verify an embedded signature in a driver file that is created by a [Software Publisher Certificate (SPC)](software-publisher-certificate.md), use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command:

```
SignTool verify /v /kp DriverFileName.sys
```

Where:

-   The **verify** command configures SignTool to verify the signature that is embedded in the driver file *DriverFileName.sys.*

-   The **/v** option configures SignTool to print execution and warning messages.

-   The **/kp** option configures SignTool to verify that the signature that is embedded in *DriverFileName.sys* complies with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) for Windows Vista and later versions of Windows.

-   *DriverFileName.sys* is the name of the driver file.

For example, the following command verifies that *Toaster.sys* has a valid embedded signature. In this example, T*oaster.sys* is in the *amd64* subdirectory under the directory in which the command is run.

```
SignTool verify /kp amd64\toaster.sys
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Verifying%20the%20Signature%20of%20a%20Release-Signed%20Driver%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




