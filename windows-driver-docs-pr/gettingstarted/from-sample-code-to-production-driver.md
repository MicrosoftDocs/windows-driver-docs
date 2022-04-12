---
title: From Sample Code to Production Driver - What to Change in the Samples
description: This topic provides information for developers about how to change WDK sample drivers before releasing device drivers based on these samples.
keywords:
- WDK Windows Driver Kit Sample Drivers Tips
- From Sample Code to Production Driver
- What to Change in the WDK Samples
ms.date: 03/24/2022
---

# From Sample Code to Production Driver - What to Change in the Samples

This topic describes important changes that need to be made to the WDK sample drivers before releasing device drivers based on the sample code.

In addition to the changes described here, all drivers should make use of the best practices described in [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md) and in [Surface Team Driver Development Best Practices](../kernel/surface-team-driver-development-best-practices.md).  All drivers should also adhere to the guidelines provided in [Driver Security Guidance](../driversecurity/index.md). 

## WDK Driver Samples - Unique Identifiers

The Windows Driver Kit (WDK) contains a wide variety of sample drivers that demonstrate useful techniques for driver development. You can use these samples as a basis for your own drivers, but before you release the driver, you must change certain device-specific aspects of the sample - beyond the obvious operational code - to uniquely apply to your own device and driver. Driver writers sometimes overlook these details.

The exact items that you must change vary from one sample to the next, but in general, they identify a specific device, interface, or driver. For example, if the sample driver contains any of the following items, you must change them to apply to your driver and device:

- Globally unique identifiers (GUIDs)

- Symbolic link names

- Device object name

- Pool tags

- I/O control code (IOCTL) definitions

- Names of any files that are copied to the system folder

- Plug and Play device ID, hardware ID, and compatible IDs

- Driver service name

- Device description

- Resource file

Forgetting to make these changes can result in failed installation, conflicts with other devices and drivers on the system, and difficulties in debugging, along with other errors. 

For example if you receive an error such as `...\toastDrv\kmdf\toastmon\wdftoastmon.inx(18-18): error 1284: Class "Sample" is reserved for use by Microsoft.` this indicates that the "Sample" name must be changed to a unique name for your sample driver.

## GUIDs

Drivers use GUIDs to identify device setup classes, device interface classes, custom PnP events, custom Windows Management Instrumentation (WMI) events, and Windows PreProcessor (WPP) trace providers. Some GUIDs are defined by Microsoft, and others are defined by device and driver vendors.

Device setup class GUIDs, device interface class GUIDs, and WMI GUIDs for common devices and WMI data are defined in the WDK or in public header files for use by any driver. You should not change these GUIDs. 

For example, if you are implementing a mouse, you would continue to use GUID_DEVINTERFACE_MOUSE, which is defined in the WDK Ntddmou.h header file, as the device interface class.However, if you define a new device setup class, you must generate a new device setup class GUID and setup class name, and possibly a new device interface class GUID as well. The setup class GUID and the device interface class GUID must be unique values; they cannot share a GUID.

For most sample-based drivers, you should change only the GUIDs that are defined in a sample's local header or source file and are thus specific to the sample. Such GUIDs might include the following:

- Custom PnP events

- Custom WMI events

- Device interface classes for new or custom devices

- WPP trace providers

Using a GUID that has been defined for another driver can cause conflicts if both drivers are loaded on the same system. For example, if two different drivers use the same GUID to register a device interface, clients that try to open the device interface might inadvertently open the wrong device.

The following excerpt is from the Driver.h file that is included in all of the Toaster driver samples. It defines the device interface GUID for Toaster devices:

<pre class="codeSample">
DEFINE_GUID(GUID_TOASTER_INTERFACE_STANDARD, \
            <b><i>0xe0b27630, 0x5434, 0x11d3, 0xb8, 0x90, 0x0, 0xc0,</i></b> \
            <b><i>0x4f, 0xad, 0x51, 0x71</i></b>);
// {E0B27630-5434-11d3-B890-00C04FAD5171}
</pre>

If you use this file in your own driver, make sure that you replace the sample GUID (shown above as bold text) with the interface GUID for your own device. To create a GUID, use the Create GUID tool in Microsoft Visual Studio or Guidgen.exe, both of which are included in the Microsoft Windows Software Development Kit (SDK). You can then associate the GUID with a symbolic constant in the driver header file, as the example shows.

You might also be required to create new GUIDs for the driver's WMI events. The Toaster driver samples define the following GUID for notification of toaster device arrival:

<pre class="codeSample">

DEFINE_GUID (TOASTER_NOTIFY_DEVICE_ARRIVAL_EVENT, \
             <b><i>0x1cdaff1, 0xc901, 0x45b4, 0xb3, 0x59, 0xb5, 0x54,</i></b> \
             <b><i>0x27, 0x25, 0xe2, 0x9c</i></b>);
// {01CDAFF1-C901-45b4-B359-B5542725E29C}
</pre>

You should create a new GUID for each WMI event in your driver.

If the sample driver uses WPP software tracing, generate a new trace provider GUID for any drivers that you base on the sample. For example, the Osrusbfx2 sample's Trace.h header file in %WinDDK%\Src\Kmdf\Osrusbfx2\Final defines a control GUID as follows:

<pre class="codeSample">
#define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID( \
           <b><i>OsrUsbFxTraceGuid</i></b>,(<b><i>d23a0c5a,d307,4f0e,ae8e,E2A355AD5DAB</i></b>), \
        WPP_DEFINE_BIT(DBG_INIT)          /* bit  0 = 0x00000001 */ \
        WPP_DEFINE_BIT(DBG_PNP)           /* bit  1 = 0x00000002 */ \
        WPP_DEFINE_BIT(DBG_POWER)         /* bit  2 = 0x00000004 */ \
        WPP_DEFINE_BIT(DBG_WMI)           /* bit  3 = 0x00000008 */ \
        WPP_DEFINE_BIT(DBG_CREATE_CLOSE)  /* bit  4 = 0x00000010 */ \
        WPP_DEFINE_BIT(DBG_IOCTL)         /* bit  5 = 0x00000020 */ \
        WPP_DEFINE_BIT(DBG_WRITE)         /* bit  6 = 0x00000040 */ \
        WPP_DEFINE_BIT(DBG_READ)          /* bit  7 = 0x00000080 */ \
       )
</pre>

In your own driver, you would replace the boldfaced text with a driver-specific name and the GUID that you created.

## Symbolic Link Names

If the sample defines a symbolic link name, replace the name in the sample with a name that applies to your own driver. However, do not change well-known link names such as \DosDevices\COM1. In general, if the link name is quite similar to the sample name (such as \DosDevices\CancelSamp)you should change it. 

Using the same symbolic link as another driver has the same effect as using the wrong device interface GUID, because device interfaces are essentially symbolic links.

The KMDF Toaster Filter driver in %WinDDK\Src\Kmdf\Toaster\Filter creates a symbolic link name that uses a string defined as follows in the Filter.h header file:

<pre class="codeSample">
#define SYMBOLIC_NAME_STRING     L"\\DosDevices\\<b><i>ToasterFilter</i></b>"
</pre>

Change the bolded string to more accurately describe your own driver.

## Device Object Name 

If the sample creates a name for the device object, you must change the name when you adapt the sample code.

The KMDF Toaster Filter driver names its device object in the Filter.h header file as follows:

<pre class="codeSample">
#define NTDEVICE_NAME_STRING      L\\Device\\<b><i>ToasterFilter</i></b>
</pre>

As with the symbolic link name, you should change the string to describe your driver.

Remember that named device objects can represent a security risk. Physical device objects (PDOs) must have names, and most such names are system generated instead of explicitly assigned by a driver. Other device objects should be named only if they represent control device objects, which are used for sideband communication between an application and a driver. Both the kernel-mode driver framework (KMDF) and the Windows Driver Model (WDM) enable you to let Windows generate the name. This approach ensures that the name of the device object is unique and that unprivileged users cannot access it. For details, see [Controlling Device Namespace Access](../kernel/controlling-device-namespace-access.md) and [Controlling Device Access in KMDF Drivers](../wdf/controlling-device-access-in-kmdf-drivers.md).

## Pool Tags

A pool tag is a one- to four-character literal that identifies a specific memory allocation and can aid in debugging.

Many of the sample drivers define a pool tag in the driver header file, as in the following line from Toaster.h:

<pre class="codeSample">
#define TOASTER_POOL_TAG (ULONG) '<b><i>saoT</i></b>'
</pre>

The driver defines the tag backward because the debugger displays it in reverse order. Thus, this tag appears as *Toas* in debugger output. Instead of using the tag that the sample defines, change the string to uniquely identify your own code.

The <i>Pooltag.txt</i> file lists the pool tags used by kernel-mode components and drivers that are supplied with Windows. <i>Pooltag.txt</i> is installed with the WDK in %winddk%\Tools\Other\<i>platform</i>\Poolmon, where <i>platform</i> is amd64, i386, or ia64. Do not use any of the tags that appear in this list.

## IOCTL Definitions

Change any sample-defined I/O control codes to use a name, device type, function code, transfer type, and access type that are appropriate for your device and driver.

For example, the Osrusbfx2 sample includes the following definition for IOCTL_OSRUSBFX2_READ_SWITCHES:

<pre class="codeSample">
#define IOCTL_OSRUSBFX2_READ_SWITCHES   
                    CTL_CODE(FILE_DEVICE_OSRUSBFX2, \
                             IOCTL_INDEX + 6, \
                             METHOD_BUFFERED, \
                             FILE_READ_ACCESS)
</pre>

A sample-based driver for a different device would require modifications to this definition.

## File Names

In the INF or INX, change the names of the driver, the vendor-supplied co-installer, and any other files that the installation procedure copies to the system folder. These file names typically appear in the <b>[SourceDisksFiles]</b> and <b>[ClassInstall32]</b> sections of the INF and in <b>CopyFiles</b> entries.

The following example is from the INX file for the KMDF Featured Toaster sample, which is available in %WinDDK%\src\kmdf\Toaster\Func\Featured. The file names that must be changed are shown in bold:

<pre class="codeSample">
[ClassInstall32]
Addreg=ToasterClassReg
CopyFiles=ToasterClassInstallerCopyFileshighlight

[ToasterClassReg]
...
HKR,,Installer32,,"<b><i>tostrcls.dll,ToasterClassInstaller</i></b>"
...

[ToasterClassInstallerCopyFiles]
<b><i>tostrcls.dll</i></b>									    
...
</pre>

To adapt this part of the file for a different driver, you would change "tostrcls.dll" to the file name of your class installer and change the "ToasterClassInstaller" string to describe your own installer. These changes ensure that the installation procedure copies the correct co-installer file and that the registry key records the correct file name.

Do not change the name of co-installers that are supplied in the WDK or with Windows, such as the KMDF, UMDF, and WinUSB co-installers.

Additional changes are required later in the file's <b>Device Install</b> section, as shown in this example:

<pre class="codeSample">
[Toaster_Device.NT]
CopyFiles=Toaster_Device.NT.Copy

[Toaster_Device.NT.Copy]
<b><i>wdffeatured.sys</i></b>
</pre>

In this example, you would change the bolded file name to the name of your generated driver file.

When Setup copies the INF and driver catalog files, it renames them, so you are not strictly required to change their names in your driver package. However, it's generally a good idea to ensure that the INF and catalog file names are similar to the driver file name.

## PnP Device ID, Hardware ID, and Compatible IDs

Setup uses the device ID along with hardware IDs and compatible IDs to select the INF to use for device installation.

The device ID is a vendor-defined string that uniquely identifies a specific device. Every device has exactly one device ID. The bus driver reports the device ID during enumeration, and Setup uses it to match the device with the correct INF file. The device ID is defined in the <b>[Manufacturer]</b> section of the INF.

The following example shows the device ID for the OSR USB Fx2 device, as specified in the Osrusbfx2.inx file:

<pre class="codeSample">
[Manufacturer]
%MfgName%=Microsoft,NT$ARCH$

; For Win2K
[Microsoft]
%USB\VID_045E&amp;PID_930A.DeviceDesc%=osrusbfx2.Dev, 
        <b><i>USB\VID_0547&amp;PID_1002</i></b>
...

; For XP and later
[Microsoft.NT$ARCH$]
%USB\VID_045E&amp;PID_930A.DeviceDesc%=osrusbfx2.Dev, 
        <b><i>USB\VID_0547&amp;PID_1002</i></b>
</pre>

To adapt this INF directive for your own driver, replace the device ID shown in bold with the device ID for your own device. You should also change the manufacturer name to the name of your company. 

The hardware ID and compatible ID are less specific IDs that Setup uses if it cannot match the device ID to an INF. If your INF can support other devices, you should change these values in addition to the device ID. The following example from the KMDF Featured Toaster driver shows a hardware ID:
<pre class="codeSample">

[Manufacturer]
%StdMfg%=Standard,NT$ARCH$

; For Win2K
[Standard]
; DisplayName                   Section           DeviceId
; -----------                   -------           --------
%ToasterDevice.DeviceDesc%=Toaster_Device, 
         {<b><i>b85b7c50-6a01-11d2-b841-00c04fad5171</i></b>}\<b><i>MsToaster</i></b>

; For XP and later
[Standard.NT$ARCH$]
%ToasterDevice.DeviceDesc%=Toaster_Device, 
         {<b><i>b85b7c50-6a01-11d2-b841-00c04fad5171</i></b>}\<b><i>MsToaster</i></b>
</pre>

To adapt this INF directive for your own driver, replace the hardware ID with the device ID of your driver and change "MsToaster" to a more descriptive string.

## Driver Service Name

Update the service name in the <b>AddService</b> directive in the INF to a value that is appropriate for your driver. If the driver service name conflicts with that of another driver on the system, the driver will not install or load.

The KMDF Featured Toaster driver names its service as follows:

<pre class="codeSample">

[Toaster_Device.NT.Services]
AddService = <b><i>wdffeatured</i></b>, %SPSVCINST_ASSOCSERVICE%,
     wdffeatured_Service_Inst
      
</pre>

The service name is the first entry in the <b>AddService</b> directive. To adapt the Featured Toaster's INF, you would change the bolded string to a string more suitable for your driver. In the example, the wdffeatured_Service_Inst entry merely references an INF-defined section, so changing it is not critical.

## Device Description

The device description consists of several strings that are typically defined in the <b>[Strings]</b> section of the INF and are used in various places throughout the INF. For example, the KMDF Featured Toaster sample defines the following strings in the WdfFeatured.inx file:

<pre class="codeSample">
[Strings]
SPSVCINST_ASSOCSERVICE   = 0x00000002
MSFT                     = "<b><i>Microsoft</i></b>"
StdMfg                   = "(<b><i>Standard system devices</i></b>)"
ClassName                = "<b><i>Toaster</i></b>"
DiskId1                  = "<b><i>Toaster Device Installation Disk #1</i></b>"
ToasterDevice.DeviceDesc = "<b><i>Microsoft WDF Featured Toaster</i></b>"
Toaster.SVCDESC          = "<b><i>Microsoft WDF Toaster Featured Device Driver</i></b>"
</pre>

To modify this file to install your own driver, you should change the bolded strings to reflect information about your company, device, and driver.

If the company name also appears in a [Manufacturer] section in the INF, you must change the name there, too.

## Resource File

Drivers and other components such as sample-specific co-installers also have resource (.rc) files, which define driver-specific strings, including the product name, file version, and company name. Change these strings to appropriate values for your driver package.

## Summary - What should you do?

Before you release a driver that is based on a WDK sample, replace any sample-specific information in the source files, the INF, and any other resources that you used to create your own driver. The required changes vary from one sample to another, but generally include any information that uniquely identifies the sample driver or its device. The following are typical of the changes you must make:

- Generate and use GUIDs that are specific to your driver where appropriate.

- Update the symbolic link name.

- Update the name of the device object or use an autogenerated name.

- Use pool tags that identify your driver and do not conflict with any known tags.

- Define IOCTL codes that are appropriate for your driver and device.

- Update the names of any files that are copied to the system folder.

- Insert the correct Plug and Play device ID, hardware IDs, and compatible IDs in the INF.

- Update the service name of the driver in the INF.

- Change the device description.

- Modify any driver-specific strings in the resource file.
 
- Adhere to best practices for security and reliability

## Additional Information

### Books

*Developing Drivers with the Windows Driver Foundation*, by Penny Orwick and Guy Smith

### WDK Topics

[Defining and Exporting New GUIDs](../kernel/defining-and-exporting-new-guids.md) 

[Controlling Device Access in  KMDF Drivers](../wdf/controlling-device-access-in-kmdf-drivers.md) 

[Developing, Testing, and Deploying Drivers](../develop/index.md)

[Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md) 

[Surface Team Driver Development Best Practices](../kernel/surface-team-driver-development-best-practices.md) 

[Driver Security Guidance](../driversecurity/index.md)

[Write your first driver](writing-your-first-driver.md)