---
title: Installing Scanning Functionality in an MFP with a Single PDO
description: Installing Scanning Functionality in an MFP with a Single PDO
MS-HAID:
- 'WIA\_GS\_c1fbb33e-6cf7-45c1-8430-677a40ccfc3b.xml'
- 'image.installing\_scanning\_functionality\_in\_an\_mfp\_with\_a\_single\_pdo'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 002ff319-42f9-4034-9bdd-c1e771ed2ba9
---

# Installing Scanning Functionality in an MFP with a Single PDO


## <a href="" id="ddk-installing-scanning-functionality-in-an-mfp-with-a-single-pdo-si"></a>


A special procedure is required to install scanning functionality in multifunction printers having only a single physical device object (PDO). If the device identifies itself as a printer, the printer's INF file can call the WIA co-installer in order to install the scanning functionality.

Microsoft recommends that each logical function of a multifunction printer should have its own PDO, if at all possible. Associating multiple functions of a device with a single PDO should be avoided.

If you register the WIA co-installer as the co-installer of your device, Setup always calls the WIA co-installer to process the installation before and after the Printer class installer. The WIA co-installer creates an Image class device interface on the printer's PDO and stores all required information in the device interface registry key. The current location in the registry of this key is:

**HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceClasses\\{6bdd1fc6-810f-11d0-bec7-08002be2092f}\\&lt;*device symbolic link*&gt;**

This key is not guaranteed to remain in this location In future operating system versions. To open this key, call [**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075).

The WIA service enumerates all Image class PDOs and device interfaces. Therefore, the newly created device interface will be enumerated as a WIA device.

The Windows DDK ships with an example INF that installs scanning functionality in a multifunction printer with only a single PDO. The name of this file is *mfpoemprn.inf*, and it is located in the *\\src\\print\\infs* directory.

**To install scanning functionality in an MFP**

1.  1.Specify *sti\_ci.dll* as the entry value for the **CoInstallerEntry** entry.

    The INF for your device must have an [**INF DDInstall.CoInstallers Section**](https://msdn.microsoft.com/library/windows/hardware/ff547321) to be able to register the co-installer for device installation. This section should appear similar to the following:

    ```
    [OEMMFP.GPD.CoInstallers]
    AddReg=WIA.CoInstallers.AddReg

    [WIA.CoInstallers.AddReg]
    HKR,,CoInstallers32,0x00010000,"sti_ci.dll, CoInstallerEntry"
    ```

2.  2.Include a **WIASection** entry in the [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) that refers to the section containing all of the WIA-related settings. The section containing the WIA-related settings must appear in the same INF file.

    ```
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

    By including a **WIASection** entry, the Image class installer does not create a devnode for the device, but instead creates an additional device interface. Accordingly, it uses the previously mentioned device interface registry key to store STI-/WIA-related information.

3.  3.Make sure that the [**INF DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) copies all required files.

    Alternatively, you can list the files to copy in the **WIASection**, but they will not be listed in Device Manager.

**Note**   The **Include** and **Needs** entries cannot be used in the **WIASection** section.
All kernel-mode portions must be installed by the original [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344).

If the device is hot-pluggable, and requires its own kernel-mode component, it must create and enable an Image class device interface (in addition to any other class device interfaces, such as the Print class device interface). The kernel-mode component enables an Image class device interface on the device's devnode by means of a call to the [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700) function. When the Image class device interface is enabled, a Plug and Play event is fired, notifying the WIA service that the device is connected.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Installing%20Scanning%20Functionality%20in%20an%20MFP%20with%20a%20Single%20PDO%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




