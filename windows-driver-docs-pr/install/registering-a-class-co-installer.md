---
title: Registering a Class Co-installer
description: Registering a Class Co-installer
ms.assetid: a86a4302-ec37-4117-aa5c-4fa84fbb7902
keywords: ["class co-installers WDK", "registering class co-installers", "setup-class-GUID WDK device installations", "CoDeviceInstallers"]
---

# Registering a Class Co-installer


## <a href="" id="ddk-registering-a-class-co-installer-dg"></a>


To register a co-installer for every device of a particular setup class, create a registry entry like the following under the **HKLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers** subkey:

```
{setup-class-GUID}: REG_MULTI_SZ : "XyzCoInstall.dll,XyzCoInstallEntryPoint\0\0"
```

The system creates the **CoDeviceInstallers** key. *Setup-class-GUID* specifies the GUID for the [device setup class](device-setup-classes.md). If the co-installer applies to more than one class of devices, create a separate value entry for each setup class.

You must not overwrite other co-installers that have been previously written to the *setup-class-GUID* key. Read the key, append your co-installer string to the REG\_MULTI\_SZ list, and write the key back to the registry.

If you omit the *CoInstallEntryPoint*, the default is CoDeviceInstall.

The co-installer DLL must also be copied to the system directory.

The class co-installer is available to be called for relevant devices and services once the file has been copied and the registry entry is made.

Rather than manually creating the registry entry to register a class co-installer, you can register it using an INF file like the following:

```
[version]
signature = "$Windows NT$"
 
[DestinationDirs]
DefaultDestDir = 11    // DIRID_SYSTEM
 
[DefaultInstall]
CopyFiles = @classXcoinst.dll
AddReg = CoInstaller_AddReg
 
[CoInstaller_AddReg]
HKLM,System\CurrentControlSet\Control\CoDeviceInstallers, \
 {setup-class-GUID},0x00010008, "classXcoinst.dll,classXCoInstaller"
; above line uses the line continuation character ()
```

This sample INF copies the file *classXcoinst.dll* to the system directory and makes an entry for the *setup-class-GUID* class under the **CoDeviceInstallers** key. The entry in the *Xxx*\_AddReg section specifies two flags: the "00010000" flag specifies that the entry is a REG\_MULTI\_SZ, and the "00000008" flag specifies that the new value is to be appended to any existing value (if the new value is not already present in the string).

Such an INF that registers a class co-installer can be activated by a right-click install or through an application that calls **SetupInstallFromInfSection**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Registering%20a%20Class%20Co-installer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




