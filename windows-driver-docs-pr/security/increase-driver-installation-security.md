---
title: Increase driver installation security
description: Evaluate how and where the driver installs to decrease the risk of tampering. Design default settings so that users are protected out of the box and have to opt in to taking on more risk.
ms.assetid: CD1A121D-59B5-4C21-88E9-5C3D5FE5157C
---

# Increase driver installation security


**Last updated:**

-   December 2016

Evaluate how and where the driver installs to decrease the risk of tampering. Design default settings so that users are protected out of the box and have to opt in to taking on more risk.

## <span id="Driver_installation"></span><span id="driver_installation"></span><span id="DRIVER_INSTALLATION"></span>Driver installation


During installation, copy driver files to secure locations and set security descriptors if necessary. The system subdirectories of the Windows directory (%windir%) automatically inherit the security settings of their parent directory, which protects system files. Vendors must not override these defaults. Therefore, if your installation procedure copies files only to %windir%\\system32\\drivers and other subdirectories of the Windows directory, the appropriate security descriptors are in place by default; you do not need to specify a security descriptor in the INF **CopyFiles** directive.

However, if you install files in a different location, you should set a security descriptor that has access control entries (ACEs) that allow access by the local system and by built-in administrators but deny write access to nonprivileged users. The local system and built-in administrators require write access to install and upgrade devices, drivers, and system service packs. For example:

(A;;GA;;;SY) grants all access to the local system.

(A;;GA;;;BA) grants all access to built-in administrators.

For most drivers, the INF file should specify device characteristics and security settings for device objects. The values in the INF file override the defaults for the security descriptor for the device class.

For WDM drivers, specifying device object security settings in the INF file is the preferred method. Before starting a WDM device stack, the PnP manager propagates the security settings that are specified in the INF file to the security descriptors for the drivers in the stack.

For more information, see [Creating Secure Device Installations](https://msdn.microsoft.com/library/windows/hardware/ff540212) and [Device and Driver Installation](https://msdn.microsoft.com/library/windows/hardware/dn653558).

## <span id="Use_Secure_Default_Settings"></span><span id="use_secure_default_settings"></span><span id="USE_SECURE_DEFAULT_SETTINGS"></span>Use Secure Default Settings


Most users accept default settings during product installation. Therefore, a default setting that can be exploited by a security attack is both highly reproducible and can affect many users. Whenever possible, make defaults restrictive and allow system administrators to change them if necessary. Do not define nonrestrictive defaults and assume that users or administrators will study your documentation to learn how to tighten them.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Increase%20driver%20installation%20security%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




