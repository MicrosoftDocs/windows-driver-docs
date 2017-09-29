---
title:  Controlling driver access
description: This article describes steps you can take to help control access to your driver.
ms.assetid: 7908AC6E-93EA-4EF1-8086-701F76160DFE
ms.author: windowsdriverdev
ms.date: 09/29/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling driver access

This article describes steps you can take to help control access to your driver.

The drivers for a device are responsible for ensuring that unauthorized users do not have access to the device. Complete the following tasks to help control access:

-   [Create secure device objects](#create-secure-device-objects)
-   [Secure the device namespace](#secure-the-device-namespace)
-   [Specify device characteristics and security settings in INF files](#specify-device-characteristics-and-security-settings-in-inf-files)
-   [Define and handle IOCTLs securely](#define-and-handle-ioctls-securely)

## <span id="Create-secure-device-objects"></span><span id="create-secure-device-objects"></span><span id="CREATE-SECURE-DEVICE-OBJECTS"></span>Create secure device objects


Every device object has a security descriptor, which contains an ACL that controls access to the device. In general, the security descriptor is created at the same time as the device object, and the ACL is specified in the INF file for the device, but the details vary depending on the position of the driver in the device stack and the type of device it controls. The following sections describe the specific requirements for:

-   Bus drivers
-   Other Plug and Play and Windows Driver Model (WDM) drivers
-   Legacy devices

### <span id="bus"></span><span id="BUS"></span>Bus drivers

A WDM bus driver for a device that can be run in raw mode must use the **IoCreateDeviceSecure** routine to create its physical device object (PDO) and set a strong default ACL. For example, the ACL for a raw-mode device PDO might set SDDL\_DEVOBJ\_SYS\_ALL, which allows access for the System (SY) but denies access for everyone else: “D:P(A;;GA;;;SY)”.

This ACL blocks even the Administrator from accessing the device. However, the INF file for the device can loosen the ACL to allow access by the Administrator or other valid users. Because a raw-mode device can be started without an INF file, specifying a strong default ACL when creating the device object is critical. Otherwise, if the device has no INF file, a user could gain access to the device without any security checks whatsoever.

If the device cannot be used in raw mode, the driver can call either the **IoCreateDevice** or the **IoCreateDeviceSecure** routine to create the device object. If the driver uses **IoCreateDevice**, the PnP Manager applies a default security descriptor just as it does for other WDM device objects. However, if the PDO requires stricter security settings than the default provides, the INF file should supply a security descriptor.

### <span id="Plug_and_Play_and_WDM_drivers"></span><span id="plug_and_play_and_wdm_drivers"></span><span id="PLUG_AND_PLAY_AND_WDM_DRIVERS"></span>Plug and Play and WDM drivers

Plug and Play (PnP) and WDM drivers (except for bus drivers, as described in “[Bus drivers](#bus)”) call the **IoCreateDevice** routine to create an unnamed device object. The PnP Manager applies a default security descriptor to each such unnamed device object.

The INF file for the device should specify the device-specific ACL. The PnP Manager ensures that the ACL is applied to all device objects in the device stack, thereby securing the entire stack before allowing other processes any access to the device.

In the INF file, ACLs are specified in SDDL and appear in an AddReg section. The AddReg section can also set device characteristics, such as FILE\_DEVICE\_SECURE\_OPEN.

Plug and Play and WDM drivers must not use the **IoCreateDeviceSecure** routine to create device objects that attach to the device stack. However, some Plug and Play drivers create named control device objects, which do not attach to the device stacks. Such control device objects must be created with the **IoCreateDeviceSecure** routine.

### <span id="Legacy_devices"></span><span id="legacy_devices"></span><span id="LEGACY_DEVICES"></span>Legacy devices

A legacy device is a device that is not controlled by the PnP Manager. Legacy drivers must create at least one named device object in the \\Device object directory to receive I/O requests.

To secure the device object for a legacy device, its driver must call the **IoCreateDeviceSecure** routine to create a named device object and to set the default security descriptor and class GUID for the device. The security descriptor should specify a strong default ACL, such as SDDL\_DEVOBJ\_SYS\_ALL. This setting allows kernel-mode code and user-mode code running as System to access the device object. At run time, the driver’s service (running as System) can open the device to individual users by using the **SetFileSecurity** user-mode function.


## <span id="Secure-the-device-namespace"></span><span id="secure-the-device-namespace"></span><span id="SECURE-THE-DEVICE-NAMESPACE"></span>Secure the device namespace


The driver is responsible for checking security when a caller tries to open an object in the device namespace. A caller can specify an object in any of the following formats.

| Path                       | Description                       |
|----------------------------|-----------------------------------|
| \\Device\\DeviceName       | Device object for DeviceName      |
| \\Device\\DeviceName\\     | Top-level directory on DeviceName |
| \\Device\\DeviceName\\File | File on DeviceName                |

 

The I/O Manager is considered the type owner for device objects; thus, the I/O Manager is responsible for checking security whenever a caller specifies a name in the form \\Device\\DeviceName.

The driver is considered the type owner for objects in its namespace. The namespace includes the top-level directory for the device (\\Device\\DeviceName\) and any objects subordinate to this directory (\\Device\\DeviceName\\File).

### <span id="Open_devices_securely"></span><span id="open_devices_securely"></span><span id="OPEN_DEVICES_SECURELY"></span>Open devices securely

A user opens a device by specifying the device name. For example:

``` 
\Device\Serial0
```

When the I/O Manager receives an open request, it parses the target device name and checks the rights in the process’s access token against the ACL of the target device object. By denying traversal rights to its device object, a driver can deny all access to its device.

If a device stack has two named device objects, a process can use either of them to open the device stack. In this case, IRPs intended for either device object are sent to the same stack, so the ACLs for the two device objects must agree.

As a general rule, the PDO should be the only named device object in a stack. Drivers should not name FDOs unless necessary, but there are a few exceptions. For example, the FDO for a storage device that has a Volume Parameter Block (VPB) must have a name.

An *exclusive device* is a device for which only one handle can be open at a time. WDM drivers designate a device as exclusive in an AddReg directive in the INF file. As a result of the AddReg directive, the system sets the DO\_EXCLUSIVE bit in the Flags field of the device object. If DO\_EXCLUSIVE is set, the I/O Manager enforces exclusivity by checking open requests against the device namespace. If DO\_EXCLUSIVE is not set, the I/O manager does not check open requests against the device namespace; instead, the driver must do so.

Even if the DO\_EXCLUSIVE bit is set for a device object, an application that has a handle to the device stack nevertheless might be able to obtain additional handles by opening “” relative to the existing handle. To prevent this problem, the driver should fail any IRP\_MJ\_CREATE requests for related file objects. The driver should check the value of the **RelatedFileObject** field in the IRP\_MJ\_CREATE request as follows:

```
if ( IrpSp->FileObject->RelatedFileObject != NULL)
```

A non-NULL value in the **RelatedFileObject** field indicates that another handle is already open. The driver must fail the request if this value is not NULL.

## Control Device Namespace Access

The I/O Manager can protect your device's namespace from unprivileged access if you set the FILE\_DEVICE\_SECURE\_OPEN device characteristic. Setting the FILE\_DEVICE\_SECURE\_OPEN device characteristic directs the I/O Manager to apply the security descriptor of the device object to all open requests, including file-open requests into the device's namespace. Essentially, the I/O Manager performs access checks and fails requests that don't have the privileges you established for the device object. 

A client usually opens a driver's named device objects ("\\Device\\MyDevice") in order to access the device. However, a client can also attempt to open files on a device by appending a file path to the device object name ("\\Device\\MyDevice\\Some\\Arbitrary\\Path\\To\\A\\File"). When this happens, the file object has a FileName equal to the trailing portion of the name ("\\Some\\Arbitrary\\Path\\To\\A\\File"). Unless the device driver watches for this case and either fails the create request or applies a security check, this can create a security hole in the system, because an unprivileged user could bypass security and obtain handles with read and write access simply by opening a file in the device's namespace.

Your driver is always responsible for managing its namespace, and using FILE\_DEVICE\_SECURE\_OPEN makes that easier by having the I/O Manager perform security checks for your driver. Setting FILE\_DEVICE\_SECURE\_OPEN closes potential security holes because the security descriptor for the device is applied to all open attempts, including those with trailing names, no matter how deep into the namespace they go. (To be absolutely sure of preventing a caller from opening files, make sure that **IrpSp-&gt;FileObject-&gt;FileName.Length** is 0 in every create IRP your driver receives).

### What should you do?

Almost all drivers that create device objects should set FILE\_DEVICE\_SECURE\_OPEN when the device object is created. The only drivers that shouldn't are those that implement their own security checking, such as file systems.

-   Set FILE\_DEVICE\_SECURE\_OPEN when calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create a device object.
-   For Plug and Play drivers use the INF file to assign FILE\_DEVICE\_SECURE\_OPEN to the DeviceCharacteristics value name in the registry.
-   If your driver cannot use FILE\_DEVICE\_SECURE\_OPEN for some reason, perform your own access checks or reject I/O requests from unprivileged callers.
-   If your driver does not support opening files or supports exclusive opens, fail any IRP\_MJ\_CREATE requests that specify an **IrpSp-&gt;FileObject-&gt;FileName** parameter with a nonzero length.

For more information, see [Controlling Device Namespace Access](https://msdn.microsoft.com/library/windows/hardware/ff542068).


### <span id="Open_files_securely"></span><span id="open_files_securely"></span><span id="OPEN_FILES_SECURELY"></span>Open files securely

Open requests in the following forms specify files or other objects in the device namespace:

``` 
\Device\Floppy0\Readme.txt
\Device\Mup\Server\Share\File.txt
\Device\Serial0\
```

**Note**  The trailing backslash in \\Device\\Serial0\\ denotes the top-level directory on the device Serial0.

 
By default, the driver is responsible for checking security for objects within its device namespace. If the driver does not support a device namespace, it should simply set the FILE\_DEVICE\_SECURE\_OPEN characteristic in the device object. If this flag is set, the operating system applies the security descriptor of the device object to all open requests in the device namespace. If the ACL for the device object does not allow access, the I/O Manager will fail the request.

Any driver that does not support a device namespace, and does not set the FILE\_DEVICE\_SECURE\_OPEN flag must fail any IRP\_MJ\_CREATE requests for objects within the object’s namespace. The driver should check the file name length in the IRP\_MJ\_CREATE request as follows:

```
if ( IrpSp->FileObject->Filename.Length != 0 )
```

If the length is nonzero, the driver must fail the request with a status indicating that the device does not support file opens

In general, drivers that support a device namespace should also set the FILE\_DEVICE\_SECURE\_OPEN characteristic. The only exception occurs when the device namespace requires different security from the device object; a volume device object of a file system is one such exception. Drivers that support a namespace but do not set this flag must check the ACL of the target file against the access token for the requesting process.

A driver can set the FILE\_DEVICE\_SECURE\_OPEN flag in its call to the **IoCreateDevice** or **IoCreateDeviceSecure** routine or in the INF file for the device. The I/O Manager checks this field at the top of the device stack. Therefore, filter drivers must copy the **Characteristics** field from the next lower driver when they attach to the stack.


## <span id="Specify-device-characteristics-and-security-settings-in-INF_files"></span><span id="specify-device-characteristics-and-security-settings-in-inf-files"></span><span id="SPECIFY-DEVICE-CHARACTERISTICS-AND-SECURITY-SETTINGS-IN-INF-FILES"></span>Specify device characteristics and security settings in INF files


Most drivers should specify device characteristics and security settings in the device INF file. The values in the INF file override the defaults for the security descriptor for the device class. For WDM drivers, specifying security settings in the INF file is the preferred method. Before starting a WDM device stack, the PnP Manager propagates the security settings specified in the INF file to the security descriptors for the drivers in the stack.

The following sample, part of an INF file, shows how to set device characteristics and security:

```
[MyDevice.NTx86]
CopyFiles = ...
[MyDevice.NTx86.Services]
AddService = ...
[MyDevice.NTx86.HW]
AddReg = MyDevice.Security
[MyDevice.Security]
HKR,,DeviceCharacteristics,0x10001,0x100
HKR,,Security,,”D:P(A;;GA;;;SY)”
```

In the preceding sample, the AddReg directive in the **MyDevice.NTx86.HW** section specifies the Security section named **MyDevice.Security**. In the **MyDevice.Security** section, the **DeviceCharacteristics** entry specifies the flag 0x10001 to indicate that the next value is a DWORD, and sets 0x100, which specifies the FILE\_DEVICE\_SECURE\_OPEN characteristic. The **Security** entry, formatted in SDDL, allows system-only access. Such a security string is appropriate for a bus driver that creates a raw PDO.


## <span id="Define-and-handle-IOCTLs-securely"></span><span id="define-and-handle-ioctls-securely"></span><span id="DEFINE-AND-HANDLE-IOCTLS-SECURELY"></span>Define and handle IOCTLs securely

Drivers must properly define IOCTL control codes and must properly handle and validate I/O requests received in IOCTLs.

An IOCTL control code has the following format:

![ioctl control code format](images/wsm-ioctl.gif)

Bits 15 and 14 of the I/O control code contain a mask describing the requested access. The access mask can specify the following rights:

-   FILE\_ANY\_ACCESS: Allows access to any caller that has a handle to the file object specified in the request.
-   FILE\_READ\_DATA: Allows the caller to request data from the file object.
-   FILE\_WRITE\_DATA: Allows the caller to write data to the file object.
-   FILE\_READ\_DATA OR’ed with FILE\_WRITE\_DATA: Allows the caller to read and write data to the object.

When a caller sends an IOCTL, the I/O Manager checks the required access specified in the control code against the rights granted to the caller, which are stored in the object handle. If the caller has adequate rights, the I/O Manager forwards the IRP to the device stack. If the caller has insufficient rights, the I/O Manager fails the IRP.

### Define secure IOCTLs

When defining an IOCTL for user-mode callers, a driver should always specify a required access value in the CTL\_CODE macro. In the past, many drivers specified FILE\_ANY\_ACCESS as the required access value. However, this value allows virtually unrestricted access to the device. Unless you are absolutely certain that allowing unrestricted access to your device does not leave the system vulnerable to a malicious user, do not specify FILE\_ANY\_ACCESS in the **RequiredAccess** field. Instead, specify FILE\_READ\_DATA or FILE\_WRITE\_DATA or the union of these two values, as appropriate.

### Handle IOCTLs securely

The I/O Manager checks access rights for all IRPs that contain IOCTLs. Rights granted to the caller are stored in the object handle, which is opaque to drivers. If the caller has insufficient rights, the I/O Manager does not send the IOCTL to the device stack.

Some system-defined and many driver-defined IOCTLs are defined with FILE\_ANY\_ACCESS as the required access value. To tighten security when such IOCTLs are sent by user-mode callers, a driver should use the [IoValidateDeviceIoControlAccess routine](https://msdn.microsoft.com/library/windows/hardware/ff550418.aspx) function. This function allows a driver to check access rights. 

Upon receiving an IOCTL, a driver can call [IoValidateDeviceIoControlAccess routine](https://msdn.microsoft.com/en-us/library/windows/hardware/ff550418.aspx), specifying FILE\_READ\_ACCESS, FILE\_WRITE\_ACCESS, or both. In response, the I/O Manager checks the access rights granted to the caller. If the caller does not have the specified rights, the driver can fail the IRP with an appropriate status.

A driver can also check system-wide privileges. For example, a driver can test the Load/Unload Driver privilege before it forwards an IRP down the device stack. Drivers should check privileges when passing an IRP down the device stack. When the IRP is returning back up the device stack, checking privilege is not effective because the I/O is already complete.

FILE\_ANY\_ACCESS authorizes the I/O Manager to send an IRP for any caller that has a handle to the device, creating a possible path for malicious users to compromise the system. The the alternative is to use the *RequiredAccess* bits in an IOCTL definition indicate the type of access that a caller must request when opening the file object that represents the device. The system-defined constant FILE\_ANY\_ACCESS, commonly used for driver IOCTLs and FSCTLs, authorizes the I/O Manager to send an IRP for any caller that has a handle to the device (that is, a handle to the file object that represents the target device object). FILE\_ANY\_ACCESS essentially allows unrestricted access to the target device.

Although FILE\_ANY\_ACCESS makes life easy for callers, it's risky for drivers because it can create a possible path for malicious users to compromise the system. For example, an IOCTL might put the device in a particular state that should only be in effect for legitimate reads and writes to the device. If the IOCTL's RequiredAccess is set to FILE\_ANY\_ACCESS, any caller could issue the IOCTL.

Don't specify FILE\_ANY\_ACCESS, most requests need only FILE\_READ\_ACCESS or FILE\_WRITE\_ACCESS (or both—they can be OR'd together).


 
## See Also

[Kernel-Mode Drivers: Fixing Common Driver Reliability Issues](http://download.microsoft.com/download/5/7/7/577a5684-8a83-43ae-9272-ff260a9c20e2/drvqa.doc)
 
---

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Driver%20security%20responsibility%20%28Windows%20security%20model%29%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




