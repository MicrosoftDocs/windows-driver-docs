---
title: Using the DevCon Tool to Install a Driver Package
description: Using the DevCon Tool to Install a Driver Package
ms.assetid: d77573e0-7866-46a5-88bc-c911bbd2a165
---

# Using the DevCon Tool to Install a Driver Package


The example in this topic uses the *ToastPkg* sample [driver package](driver-packages.md). Within the WDK installation directory, the package's source files are located in the *src\\general\\toaster\\toastpkg\\toastcd* directory. After you have built and digitally-signed this driver package, copy the driver package to the directory *c:\\toaster* on the test computer.

To install the driver package through DevCon, do the following:

1.  To use the DevCon tool, the user must be a member of the Administrators group on the test computer and run DevCon from an elevated command prompt. To open an elevated Command Prompt window, create a desktop shortcut to *Cmd.exe*, right-click the *Cmd.exe* shortcut, and select **Run as administrator**.

2.  From the elevated, Command Prompt window, enter the following:

    ```
    devcon.exe install c:\toaster\toastpkg.inf {b85b7c50-6a01-11d2-b841-00c04fad5171}\mstoaster
    ```

    This command-line specifies the location of the driver package's INF file (*c:\\toaster\\toastpkg.inf*) and the toaster device's hardware identifier (ID), which is specified within the INF file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20the%20DevCon%20Tool%20to%20Install%20a%20Driver%20Package%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




