---
title: Installing Scanning Functionality in an MFP with a Single PDO
description: Installing Scanning Functionality in an MFP with a Single PDO
ms.date: 03/24/2023
---

# Installing Scanning Functionality in an MFP with a Single PDO

> [!IMPORTANT]
> Starting with the WDK for Windows 11, version 22H2, WDF redistributable co-installers are no longer supported.
> To learn how to work around this change, see [WDF redistributable co-installers don't work](/windows-hardware/drivers/wdk-known-issues#wdf-redistributable-co-installers-dont-work) in the *WDK known issues* article.

A special procedure is required to install scanning functionality in multifunction printers having only a single physical device object (PDO). If the device identifies itself as a printer, the printer's INF file can call the WIA co-installer in order to install the scanning functionality.

Microsoft recommends that each logical function of a multifunction printer should have its own PDO, if at all possible. Associating multiple functions of a device with a single PDO should be avoided.

If you register the WIA co-installer as the co-installer of your device, Setup always calls the WIA co-installer to process the installation before and after the Printer class installer. The WIA co-installer creates an Image class device interface on the printer's PDO and stores all required information in the device interface registry key. The current location in the registry of this key is:

**HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceClasses\\{6bdd1fc6-810f-11d0-bec7-08002be2092f}\\&lt;*device symbolic link*&gt;**

This key isn't guaranteed to remain in this location In future operating system versions. To open this key, call [**SetupDiOpenDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey).

The WIA service enumerates all Image class PDOs and device interfaces. Therefore, the newly created device interface is enumerated as a WIA device.

The Windows DDK ships with an example INF that installs scanning functionality in a multifunction printer with only a single PDO. The name of this file is *mfpoemprn.inf*, and it's located in the *\\src\\print\\infs* directory.

## To install scanning functionality in an MFP

1. Specify *sti\_ci.dll* as the entry value for the **CoInstallerEntry** entry.

    The INF for your device must have an [**INF DDInstall.CoInstallers Section**](../install/inf-ddinstall-coinstallers-section.md) to be able to register the co-installer for device installation. This section should appear similar to the following example:

    ```INF
    [OEMMFP.GPD.CoInstallers]
    AddReg=WIA.CoInstallers.AddReg

    [WIA.CoInstallers.AddReg]
    HKR,,CoInstallers32,0x00010000,"sti_ci.dll, CoInstallerEntry"
    ```

1. Include a **WIASection** entry in the [**INF DDInstall Section**](../install/inf-ddinstall-section.md) that refers to the section containing all of the WIA-related settings. The section containing the WIA-related settings must appear in the same INF file.

    ```INF
    [OEMMFP.GPD]
    CopyFiles=@OEMMFP.DLL,@OEMPRT1.DLL,@OEMUI.DLL,OEMMFP.GPD.WIA.CopyFiles
    WIASection=OEMMFP.GPD.WIA

    [OEMMFP.GPD.WIA]
    Description=%OEM_MFP_SCANNER%
    SubClass=StillImage
    DeviceType=1
    Capabilities=0x00000011
    AddReg=OEMMFP.GPD.WIA.AddReg
    DeviceData=OEMMFP.GPD.WIA.DeviceData
    ICMProfiles="sRGB Color Space Profile.icm"
    USDClass="{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}"
    ```

    By including a **WIASection** entry, the Image class installer doesn't create a devnode for the device, but instead creates an additional device interface. Accordingly, it uses the previously mentioned device interface registry key to store STI-/WIA-related information.

1. Make sure that the [**INF DDInstall section**](../install/inf-ddinstall-section.md) copies all required files.

    Alternatively, you can list the files to copy in the **WIASection**, but they won't be listed in Device Manager.

The **Include** and **Needs** entries can't be used in the **WIASection** section.

All kernel-mode portions must be installed by the original [**INF DDInstall Section**](../install/inf-ddinstall-section.md).

If the device is hot-pluggable, and requires its own kernel-mode component, it must create and enable an Image class device interface. This interface is in addition to any other class device interfaces, such as the Print class device interface.

The kernel-mode component enables an Image class device interface on the device's devnode with a call to the [**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate) function. When the Image class device interface is enabled, a Plug and Play event is fired, notifying the WIA service that the device is connected.
