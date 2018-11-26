---
title: Specifying WDF Directives in INF Files
description: Specifying WDF Directives in INF Files
ms.assetid: aefc678e-dc81-47dc-a84b-f1a79c16cad9
keywords:
- WDF directives WDK UMDF
- DDInstall section WDK UMDF
- UmdfService INF directive WDK UMDF
- UmdfServiceOrder INF directive WDK UMDF
- UmdfImpersonationLevel INF directive WDK UMDF
- UmdfMethodNeitherAction INF directive WDK UMDF
- UmdfKernelModeClientPolicy INF directive WDK UMDF
- UmdfLibraryVersion INF directive WDK UMDF
- ServiceBinary INF directive WDK UMDF
- DriverCLSID INF directive WDK UMDF
- directives WDK UMDF
- UMDF-specific directives WDK
- UMDF-service-install section WDK
- INF files WDK UMDF , directives
- UmdfDispatcher INF directive WDK UMDF , syntax
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying WDF Directives in INF Files


This topic applies to both User-Mode Driver Framework (UMDF) versions 1 and 2.

An INF file that installs a UMDF driver must contain a Microsoft Windows Driver Frameworks (WDF)-specific *DDInstall* section. The INF file can contain more than one WDF-specific *DDInstall* section if the INF file installs more than one WDF driver. Each WDF-specific *DDInstall* section:

-   Corresponds to the [**DDInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547344) and [**DDInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547349) sections that are associated with a particular WDF driver.

-   Is processed by all the loaded WDF co-installers, which run in arbitrary order.

-   Contains WDF installation directives for a device. UMDF-specific directives begin with the UMDF prefix, and KMDF-specific directives begin with the KMDF prefix.

The following code example shows UMDF-specific directives in a WDF-specific *DDInstall* section.

```cpp
[Skeleton_Install.Wdf]
UmdfService=UMDFSkeleton,UMDFSkeleton_Install
UmdfServiceOrder=UMDFSkeleton
```

Each UMDF-specific directive in the WDF-specific *DDInstall* section is described in the following list:

<a href="" id="umdfservice----servicename----sectionname-"></a>**UmdfService** = &lt;*serviceName*&gt;, &lt;*sectionName*&gt;  
Associates a UMDF driver with a *UMDF-service-install* section that contains information that is required to install the UMDF driver. The *serviceName* parameter specifies the UMDF driver, and is limited to a maximum of 31 characters in length. The *sectionName* parameter references the *UMDF-service-install* section. A valid INF file typically requires at least one **UmdfService** directive. However, if a UMDF driver is part of the operating system, a **UmdfService** directive for the UMDF driver is not required. Therefore, a valid INF file might not have any **UmdfService** directives, although most INF files have one **UmdfService** directive for each UMDF driver.

<a href="" id="umdfhostprocesssharing-------------processsharingdisabled---processsharingenabled-"></a>**UmdfHostProcessSharing** = &lt;**ProcessSharingDisabled** | **ProcessSharingEnabled**&gt;  
Determines whether a device stack is placed into a shared process pool (**ProcessSharingEnabled**) or its own individual process (**ProcessSharingDisabled**). The default is **ProcessSharingEnabled**. This directive is device-specific rather than driver-specific.

For more information about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

UMDF versions 1.11 and later support the **UmdfHostProcessSharing** directive.

<a href="" id="umdfdirecthardwareaccess----allowdirecthardwareaccess---rejectdirecthardwareaccess---"></a>**UmdfDirectHardwareAccess** = &lt;**AllowDirectHardwareAccess** | **RejectDirectHardwareAccess**&gt;   
Indicates whether the framework should allow the driver to use any of the direct hardware access features, such as accessing device registers and ports, scanning hardware resources assigned to the device, handling hardware interrupts, or acquiring connection resources.

If **UmdfDirectHardwareAccess** is set to **AllowDirectHardwareAccess**, the framework allows the driver to use UMDF interfaces that perform direct hardware access.

You must specify **AllowDirectHardwareAccess** if your UMDF driver accesses hardware resources such as registers or ports, interrupts, [general-purpose I/O](https://msdn.microsoft.com/library/windows/hardware/hh439512) (GPIO) pins, or serial bus connections such as I2C, SPI, and serial port. Your driver receives all of these resources through the *ResourcesRaw* and *ResourcesTranslated* parameters of its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function.

**Note**  
Starting with UMDF version 2.15, a UMDF driver does not need to specify **AllowDirectHardwareAccess** in order to receive hardware resource lists in its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback routine. If you don't specify it, the driver does not have the access rights to use these resources, with one exception:

If the device is assigned one or more connection resources (**CmResourceTypeConnection**) and one or more interrupt resources (**CmResourceTypeInterrupt**), the driver can call [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) from its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback routine (but not from [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693)).

 

For information about connecting a UMDF driver to particular types of resources, see:

-   [Connecting a UMDF Driver to GPIO I/O Pins](https://msdn.microsoft.com/library/windows/hardware/hh698244)
-   [Hardware Resources for User-Mode SPB Peripheral Drivers](https://msdn.microsoft.com/library/windows/hardware/hh450837)
-   [Connection IDs for SPB-Connected Peripheral Devices](https://msdn.microsoft.com/library/windows/hardware/hh698216)
-   [Connecting a UMDF Peripheral Driver to a Serial Port](https://msdn.microsoft.com/library/windows/hardware/hh406559)

If **UmdfDirectHardwareAccess** is set to **RejectDirectHardwareAccess**, the framework does not allow drivers to use any direct hardware access features. The default value is **RejectDirectHardwareAccess**.

For information about how a UMDF driver accesses hardware resources, see [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md).

UMDF versions 1.11 and later support the **UmdfDirectHardwareAccess** directive.

<a href="" id="umdfhostpriority----priorityhigh-"></a>**UmdfHostPriority** = &lt;**PriorityHigh**&gt;  
Starting in UMDF version 2.15, a UMDF HID client driver can set **UmdfHostPriority** to **PriorityHigh** to increase its thread priority. This directive should only be used for touch or input drivers that are sensitive to user response time. When a driver specifies **PriorityHigh**, the system puts it in a separate device pool along with other drivers of similar priority. Because the additional device pool uses more memory, you should use this setting with caution. For more information about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

<a href="" id="umdfregisteraccessmode----registeraccessusingsystemcall---registeraccessusingusermodemapping--"></a>**UmdfRegisterAccessMode** = &lt;**RegisterAccessUsingSystemCall** | **RegisterAccessUsingUserModeMapping**&gt;   
Indicates whether the framework should map the registers into user-mode address space (so that a system call is not involved in accessing registers), or use a system call to access registers.

If **UmdfRegisterAccessMode** is set to **RegisterAccessUsingSystemCall**, the framework uses a system call to access registers.

If **UmdfRegisterAccessMode** is set to **RegisterAccessUsingUserModeMapping**, the framework maps the registers into user-mode address space so that a system call is not needed to access registers. The default value is **RegisterAccessUsingSystemCall**.

UMDF versions 1.11 and later support the **UmdfRegisterAccessMode** directive.

<a href="" id="--------umdfserviceorder----servicename1------servicename2------"></a> **UmdfServiceOrder** = &lt;*serviceName1*&gt; \[, &lt;*serviceName2*&gt; ...\]  
Lists the order that the co-installer installs the UMDF drivers on the device stack. Even if the co-installer installs only one UMDF driver on the device stack, the INF file must contain this directive. The *serviceNameXx* parameters correspond to the *serviceName* parameters for each **UmdfService** directive. Because the UMDF drivers are added to the device stack in the order that they are listed, the first parameter specifies the lowest UMDF driver in the device stack.

To ensure that a UMDF co-installer installs the device, only one **UmdfServiceOrder** directive must be present in any given WDF-specific *DDInstall* section. That is, the **UmdfServiceOrder** directive cannot be imported by using the **Include** and **Needs** directives.

<a href="" id="umdfimpersonationlevel----level-"></a>**UmdfImpersonationLevel** = &lt;*level*&gt;  
Informs the framework about the maximum impersonation level that the UMDF driver can have. A **UmdfImpersonationLevel** directive is optional; if an impersonation level is not specified, the default is **Identification**. When an application opens a file handle, the application can grant a greater impersonation level to the driver. However, the driver cannot call the [**IWDFIoRequest::Impersonate**](https://msdn.microsoft.com/library/windows/hardware/ff559136) method to request an impersonation level that is greater than the level that **UmdfImpersonationLevel** specifies. The possible values for this directive are:

-   **Anonymous**

-   **Identification**

-   **Impersonation**

-   **Delegation**

These values correspond to the values that are specified in the [**SECURITY\_IMPERSONATION\_LEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff560499) enumeration.

<a href="" id="umdfmethodneitheraction------------copy---reject-"></a>**UmdfMethodNeitherAction** = &lt;**Copy** | **Reject**&gt;  
Indicates whether the framework will accept (**Copy**) or reject (**Reject**) a device's I/O requests, if the request objects contain I/O control codes that specify the [METHOD\_NEITHER](https://msdn.microsoft.com/library/windows/hardware/ff540663) buffer access method. A **UmdfMethodNeitherAction** directive is optional. If the directive is not specified, the default value is **Reject**.

For more information about supporting the METHOD\_NEITHER buffer access method in UMDF-based drivers, see [Using Neither Buffered I/O nor Direct I/O in UMDF Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554413#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers).

<a href="" id="umdfdispatcher----filehandle---winusb---nativeusb-"></a>**UmdfDispatcher** = &lt;**FileHandle** | **WinUsb** | **NativeUSB**&gt;  
Informs the framework where to send I/O after the I/O goes through the user-mode portion of the device stack. By default, I/O is sent to the reflector (WUDFRd.sys). By setting **UmdfDispatcher** to **WinUsb**, the driver instructs UMDF to send I/O to the WinUsb architecture. Starting in UMDF 2.15, specifying **NativeUSB** causes the reflector to handle USB I/O.

-   If any driver in the stack uses a file-handle-based target, set this directive to **FileHandle**.
-   If the driver uses UMDF 2.15 or later and uses USB I/O targets, set this directive to **NativeUSB**.
-   If the driver is pre-UMDF 2.15 and uses USB I/O targets, set this directive to **WinUsb**.

A **UmdfDispatcher** directive is optional.

The following code example shows the **UmdfDispatcher** directive in a WDF-specific **DDInstall** section.

```cpp
[Xxx_Install.Wdf]
UmdfDispatcher=NativeUSB
```

<a href="" id="umdfkernelmodeclientpolicy------------allowkernelmodeclients---rejectkernelmodeclients-"></a>**UmdfKernelModeClientPolicy** = &lt;**AllowKernelModeClients** | **RejectKernelModeClients**&gt;  
Indicates whether the framework should allow the driver to receive I/O requests from kernel-mode drivers.

If **UmdfKernelModeClientPolicy** is set to **AllowKernelModeClients**, the framework allows kernel-mode drivers to load above a user-mode driver, and it delivers I/O requests from kernel-mode drivers to the user-mode driver.

If **UmdfKernelModeClientPolicy** is set to **RejectKernelModeClients**, the framework does not allow kernel-mode drivers to load above a user-mode driver, and it does not deliver I/O requests from any kernel-mode drivers to the user-mode driver. If a driver's INF file does not contain this directive, the default value is **RejectKernelModeClients**. For more information, see [Supporting Kernel-mode Clients](https://msdn.microsoft.com/library/windows/hardware/ff561214).

UMDF versions 1.9 and later support the **UmdfKernelModeClientPolicy** directive. To allow kernel-mode drivers to load above a user-mode driver in earlier UMDF versions, see [Kernel-mode Client Support in Earlier UMDF Versions](https://msdn.microsoft.com/library/windows/hardware/ff561214#kernel-mode-client-support-in-earlier-umdf-versions).

<a href="" id="umdffileobjectpolicy----rejectnullandunknownfileobjects---allownullandunknownfileobjects--"></a>**UmdfFileObjectPolicy** = &lt;**RejectNullAndUnknownFileObjects** | **AllowNullAndUnknownFileObjects**&gt;   
Indicates whether the framework should allow processing of I/O requests ([IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985)) that are either not associated with a file object ([IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912)) or are associated with an unknown file object (a file object for which a driver has not previously seen a create request).

If **UmdfFileObjectPolicy** is set to **RejectNullAndUnknownFileObjects**, the framework does not allow processing of requests that are associated with a NULL or unknown file object.

If **UmdfFileObjectPolicy** is set to **AllowNullAndUnknownFileObjects**, the framework allows processing of requests that are associated with a NULL or unknown file object.

The default value is **RejectNullAndUnknownFileObjects**.

UMDF versions 1.11 and later support the **UmdfFileObjectPolicy** directive.

<a href="" id="umdffscontextusepolicy----canusefscontext---canusefscontext2----cannotusefscontexts-"></a>**UmdfFsContextUsePolicy** = &lt;**CanUseFsContext** | **CanUseFsContext2** | **CannotUseFsContexts**&gt;  
Indicates whether the framework can store internal information in specific context members of a WDM file object. If a kernel-mode driver in the same stack uses a particular member of the file object, you can use this directive to request that the framework not use the same location.

If **UmdfFsContextUsePolicy** is set to **CanUseFsContext**, the framework stores information in the **FsContext** member of the WDM file object.

If **UmdfFsContextUsePolicy** is set to **CanUseFsContext2**, the framework stores information in the **FsContext2** member of the WDM file object.

If **UmdfFsContextUsePolicy** is set to **CannotUseFsContexts**, the framework does not use either **FsContext** or **FsContext2**.

The default value is **CanUseFsContext**.

UMDF versions 1.11 and later support the **UmdfFsContextUsePolicy** directive.




The following code example shows the required directives in a *UMDF-service-install* section.

```cpp
[UMDFSkeleton_Install]
UmdfLibraryVersion=1.0.0
ServiceBinary=%12%\UMDF\UMDFSkeleton.dll
DriverCLSID={d4112073-d09b-458f-a5aa-35ef21eef5de}
```

Each directive in the *UMDF-service-install* section is described in the following list:

<a href="" id="umdflibraryversion------------version-"></a>**UmdfLibraryVersion** = &lt;*version*&gt;  
Informs the co-installer about the version number of the framework that the UMDF driver will use. The format of the *version* string is &lt;*major*&gt;.&lt;*minor*&gt;.&lt;*service*&gt;. When drivers on the device stack use more than one version of the framework, the INF file copies multiple co-installers--one for each framework version--to the same location on the hard disk drive. However, the INF file adds only the highest version co-installer to the **CoInstallers32** registry value. For more information about copying co-installers, see [Using the UMDF Co-installer](using-the-umdf-co-installer.md).

The co-installer verifies the version string and uses it to locate the version-specific co-installer for the UMDF driver. The co-installer then extracts the framework from the version-specific co-installer.

<a href="" id="servicebinary----binarypath-"></a>**ServiceBinary** = &lt;*binarypath*&gt;  
Informs UMDF about where to place the UMDF driver binary on the hard disk drive.

UMDF drivers should be copied to, and run from, the \\Windows\\System32\\Drivers\\UMDF directory.

<a href="" id="driverclsid-----clsid--"></a>**DriverCLSID** = &lt;{*CLSID*}&gt;  
**Note**  This directive is available in UMDF versions 1.11 and earlier.

Informs UMDF about the class identifier (CLSID) of the UMDF driver. When UMDF loads the UMDF driver, the UMDF host uses the UMDF driver's CLSID to create an instance of the UMDF driver's [IDriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff554885) interface.

<a href="" id=" umdfextensions-----cxservicename--"></a>**UmdfExtensions** = &lt;cxServiceName&gt;
Required for drivers that communicate with class extension drivers provided by Microsoft.  The cxServiceName parameter corresponds to the service associated with the class extension driver binary.

Service names for the class extension drivers could be located as a subkey under the following registry key:
**HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\Services**

On Windows 8.1 and earlier, to avoid a required reboot when you update a UMDF driver, specify the **COPYFLG\_IN\_USE\_RENAME** flag in the [**CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) in your driver's INF file, as shown in this example:

```cpp
[VirtualSerial_Install.NT]
CopyFiles=UMDriverCopy
 
[UMDriverCopy]
Virtualserial.dll,,,0x00004000  ; COPYFLG_IN_USE_RENAME
```

 

 





