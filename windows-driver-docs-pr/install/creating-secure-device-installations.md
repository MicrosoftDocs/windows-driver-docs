---
title: Creating Secure Device Installations
description: Creating Secure Device Installations
ms.assetid: e92488c4-1383-4493-b229-61c646546c82
keywords: ["Device setup WDK device installations , security", "device installations WDK , security", "installing devices WDK , security", "security WDK device installations", "security descriptors WDK device installations", "INF files WDK device installations", "testing security settings WDK device installations", "registry WDK device installations", "WMI security WDK device installations"]
---

# Creating Secure Device Installations


## <a href="" id="ddk-creating-secure-device-installations-dg"></a>


When you create a [driver package](driver-packages.md), you must make sure that the installation of your device will always be performed in a secure manner. A secure device installation is one that does the following:

-   limits access to the device and its device interface classes

-   limits access to the driver services that were created for the device

-   protects driver files from modification or deletion

-   limits access to the device's registry entries

-   limits access to the device's WMI classes

-   uses SetupAPI functions correctly

Device installation security is controlled by [*security descriptors*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-security-descriptor). The primary medium for specifying security descriptors is the INF file. The system provides default security descriptors, and under most circumstances you do not have to override these descriptors.

### Security Settings for Devices and Interfaces

The system supplies default security descriptors for all [system-supplied device setup classes](https://msdn.microsoft.com/library/windows/hardware/ff553419). Generally, these descriptors allow full access for system administrators and read/write/execute access for users. (The security descriptors that control access to a device also control access to the device's [device interface classes](device-interface-classes.md), if any.)

INF files for WDM drivers can specify security settings, either per class or per device, that override the system's default settings. Vendors who create a new device setup class should specify a security descriptor for the class. Generally, specifying a device-specific security descriptor is not necessary. It might be useful to supply a device-specific security descriptor if different types of devices that belong to the same class have significantly different types of users.

To specify a security descriptor for all devices that belong to a WDM device setup class, use an [**INF AddReg directive**](inf-addreg-directive.md) within an [**INF ClassInstall32 section**](inf-classinstall32-section.md) of the class installer's INF file. The **AddReg** directive must point to an *add-registry-section* that sets values for **DeviceType** and **Security** registry entries. These registry values specify a security descriptor for all devices of the specified device type.

To specify a security descriptor for a single device that belongs to a WDM device setup class, use an [**INF AddReg directive**](inf-addreg-directive.md) within an [**INF DDInstall.HW section**](inf-ddinstall-hw-section.md) of the device's INF file. The **AddReg** directive must point to an *add-registry-section* that sets values for **DeviceType** and **Security** registry entries. These registry values specify a security descriptor for all devices that match the [hardware ID](hardware-ids.md) or [compatible IDs](compatible-ids.md) specified by an associated [**INF Models section**](inf-models-section.md).

By default, the system applies the security descriptor set for a device to a request to open the device object that represents the device (for example, a request to open the device whose NT device name is *\\Device\\DeviceName*).

However, the system does not by default apply the security descriptor set for a device to a request to open an object in the namespace of the device, where the device namespace includes all objects whose names have the form *\\Device\\DeviceName\\ObjectName*. To ensure that the same security settings are applied to open requests for objects in the namespace of a device, set the FILE\_DEVICE\_SECURE\_OPEN device characteristics flag for a device. For more information about secure device access, see [Controlling Device Namespace Access (Windows Drivers)](https://msdn.microsoft.com/library/windows/hardware/ff542068). For information about how to set the FILE\_DEVICE\_SECURE\_OPEN device characteristics flag, See [Specifying Device Characteristics (Windows Drivers)](https://msdn.microsoft.com/library/windows/hardware/ff563818).

The PnP manager sets security values on device objects after it calls a driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. Some WDM drivers can specify a device-specific security descriptor when creating a physical device object (PDO) by calling [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407). For more information, see [Securing Device Objects](https://msdn.microsoft.com/library/windows/hardware/ff563688).

### Security Settings for Driver Files

When copying files by using the [**INF CopyFiles directive**](inf-copyfiles-directive.md), it is possible to specify a *file-list-section*.**security** section. This section specifies a security descriptor for all files that are copied by the **CopyFiles** directive. However, vendors never have to specify a security descriptor for driver files, if the installation destination is one of the system subdirectories of *%SystemRoot%*. (For more information about these subdirectories, see [Using Dirids](using-dirids.md).) The system provides default security descriptors for these subdirectories, and the default descriptors should not be overridden.

### Security Settings for Driver Services

Within a driver INF file's *service-install-section* (see [**INF AddService Directive**](inf-addservice-directive.md)), you can include a **Security** entry. This entry specifies the permissions that are required to perform such operations as starting, stopping, and configuring the driver services that are associated with your device. However, the system provides a default security descriptor for driver services, and this default descriptor generally does not have to be overridden.

### Security Settings for Device and Driver Registry Entries

When specifying registry entries in INF files by using [**INF AddReg directives**](inf-addreg-directive.md), you can include an *add-registry-section*.**Security** section for each *add-registry-section*. The *add-registry-section*.**Security** section specifies access permissions to the created registry entries that are created by the associated *add-registry-section* section. The system provides a default security descriptor for all registry entries created under the **HKR** relative root. Therefore, you do not have to specify a security descriptor when creating registry entries under the relative root.

### Security Settings for WMI Classes

The system assigns default security descriptors to the GUIDs that identify WMI classes. For Windows XP and earlier operating system versions, the default security descriptor for WMI GUIDs allows full access to all users. Starting with Windows Server 2003, the default security descriptor allows access only to administrators.

If your driver defines WMI classes and you do not want to use the system's default security descriptors for these classes, you can supply security descriptors by using an [**INF DDInstall.WMI section**](inf-ddinstall-wmi-section.md) within the device's INF file.

### Using SetupAPI Functions Correctly

If your [driver package](driver-packages.md) includes installers, co-installers, or other installation applications that call SetupAPI functions, you must follow the [guidelines for using SetupAPI](guidelines-for-using-setupapi.md).

### <a href="" id="testing-installation-security-settings-"></a>Testing Installation Security Settings

Use [SetupAPI logging](setupapi-logging--windows-server-2003--windows-xp--and-windows-2000-.md) to verify that security settings that are associated with installing your device have been specified correctly. Set the logging level to verbose (0x0000FFFF), then attempt various installation scenarios.

Such scenarios should include both initial installations and reinstallations, from both user accounts and system administrator accounts. Try plugging in your device before you install software, and vice versa.

If an installation succeeds, view the log to confirm that no errors occurred. If an installation fails, view the log to determine the cause of the failure.

Additionally, after an installation completes you can do the following:

-   Use Registry Editor to view the security settings that are assigned to a registry entry.

-   Use **My Computer** to view the security settings that are assigned to a file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20Secure%20Device%20Installations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




