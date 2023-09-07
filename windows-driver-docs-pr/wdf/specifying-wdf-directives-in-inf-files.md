---
title: Specifying WDF Directives in INF Files
description: Specifying WDF Directives in INF Files
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
ms.date: 09/07/2023
---

# Specifying WDF Directives in INF Files

An INF file that installs a WDF driver must contain two WDF-specific sections:

 - [DDInstall.wdf] section for each [DDInstall] section
 - [wdf-service-install] section, with name specified in a KmdfService or UmdfService directive in [DDInstall.wdf]

These sections contain WDF-specific directives. UMDF-specific directives begin with the UMDF prefix, and KMDF-specific directives begin with the KMDF prefix.

The following code example shows UMDF-specific directives:

```inf
[ECHO_Device.NT.Wdf]
UmdfService = Echo, Echo_service_wdfsect
UmdfServiceOrder = Echo

[Echo_service_wdfsect]
UmdfLibraryVersion = $UMDFVERSION$
ServiceBinary = %13%\echo.dll
```

The following code example shows KMDF-specific directives:

```inf
[ECHO_Device.NT.Wdf]
KmdfService =  Echo, Echo_service_wdfsect

[Echo_service_wdfsect]
KmdfLibraryVersion = $KMDFVERSION$
```

## [UMDF Directives for DDInstall.WDF sections]

The following is a code example. Each UMDF-specific directive in the DDInstall.WDF section is described below.

```inf
[ECHO_Device.NT.Wdf]
UmdfService = Echo, Echo_service_wdfsect
UmdfServiceOrder = Echo
```

## UmdfService

`**UmdfService** = <*serviceName*>, <*sectionName*>

Associates a UMDF driver with a *UMDF-service-install* section that contains information that is required to install the UMDF driver. The *serviceName* parameter specifies the UMDF driver, and is limited to a maximum of 31 characters in length. The *sectionName* parameter references the *UMDF-service-install* section. A valid INF file typically requires at least one **UmdfService** directive. However, if a UMDF driver is part of the operating system, a **UmdfService** directive for the UMDF driver is not required. Therefore, a valid INF file might not have any **UmdfService** directives, although most INF files have one **UmdfService** directive for each UMDF driver.

## UmdfHostProcessSharing

*This directive is supported in UMDF versions 1.11 and later.*

**UmdfHostProcessSharing** = <**ProcessSharingDisabled** | **ProcessSharingEnabled**>


Determines whether a device stack is placed into a shared process pool (**ProcessSharingEnabled**) or its own individual process (**ProcessSharingDisabled**). The default is **ProcessSharingEnabled**. This directive is device-specific rather than driver-specific.

For more information about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).


## UmdfDirectHardwareAccess

*This directive is supported in UMDF versions 1.11 and later.*

**UmdfDirectHardwareAccess** = <**AllowDirectHardwareAccess** | **RejectDirectHardwareAccess**> 

Indicates whether the framework should allow the driver to use any of the direct hardware access features, such as accessing device registers and ports, scanning hardware resources assigned to the device, handling hardware interrupts, or acquiring connection resources.

If **UmdfDirectHardwareAccess** is set to **AllowDirectHardwareAccess**, the framework allows the driver to use UMDF interfaces that perform direct hardware access.

You must specify **AllowDirectHardwareAccess** if your UMDF driver accesses hardware resources such as registers or ports, interrupts, [general-purpose I/O](../gpio/gpio-driver-support-overview.md) (GPIO) pins, or serial bus connections such as I2C, SPI, and serial port. Your driver receives all of these resources through the *ResourcesRaw* and *ResourcesTranslated* parameters of its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function.

> [!NOTE]
> Starting with UMDF version 2.15, a UMDF driver does not need to specify **AllowDirectHardwareAccess** in order to receive hardware resource lists in its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback routine. If you don't specify it, the driver does not have the access rights to use these resources, with one exception:
> If the device is assigned one or more connection resources (**CmResourceTypeConnection**) and one or more interrupt resources (**CmResourceTypeInterrupt**), the driver can call [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) from its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback routine (but not from [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)).

 

For information about connecting a UMDF driver to particular types of resources, see:

-   [Hardware Resources for User-Mode SPB Peripheral Drivers](../spb/hardware-resources-for-user-mode-spb-peripheral-drivers.md)
-   [Connection IDs for SPB-Connected Peripheral Devices](../spb/connection-ids-for-spb-connected-peripheral-devices.md)
-   [Connecting a UMDF Peripheral Driver to a Serial Port](/previous-versions/hh406559(v=vs.85))

If **UmdfDirectHardwareAccess** is set to **RejectDirectHardwareAccess**, the framework does not allow drivers to use any direct hardware access features. The default value is **RejectDirectHardwareAccess**.

For information about how a UMDF driver accesses hardware resources, see [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md).


## UmdfHostPriority

*This directive is supported in UMDF versions 2.15 and later.*

**UmdfHostPriority** = <**PriorityHigh**>  

A UMDF HID client driver can set **UmdfHostPriority** to **PriorityHigh** to increase its thread priority. This directive should only be used for touch or input drivers that are sensitive to user response time. When a driver specifies **PriorityHigh**, the system puts it in a separate device pool along with other drivers of similar priority. Because the additional device pool uses more memory, you should use this setting with caution. For more information about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

## UmdfRegisterAccessMode

*This directive is supported in UMDF versions 1.11 and later.*

**UmdfRegisterAccessMode** = <**RegisterAccessUsingSystemCall** | **RegisterAccessUsingUserModeMapping**>   

Indicates whether the framework should map the registers into user-mode address space (so that a system call is not involved in accessing registers), or use a system call to access registers.

If **UmdfRegisterAccessMode** is set to **RegisterAccessUsingSystemCall**, the framework uses a system call to access registers.

If **UmdfRegisterAccessMode** is set to **RegisterAccessUsingUserModeMapping**, the framework maps the registers into user-mode address space so that a system call is not needed to access registers. The default value is **RegisterAccessUsingSystemCall**.


##  UmdfServiceOrder

**UmdfServiceOrder** = <*serviceName1*> \[, <*serviceName2*> ...\]  

Lists the order that the co-installer installs the UMDF drivers on the device stack. Even if the co-installer installs only one UMDF driver on the device stack, the INF file must contain this directive. The *serviceNameXx* parameters correspond to the *serviceName* parameters for each **UmdfService** directive. Because the UMDF drivers are added to the device stack in the order that they are listed, the first parameter specifies the lowest UMDF driver in the device stack.

To ensure that a UMDF co-installer installs the device, only one **UmdfServiceOrder** directive must be present in any given WDF-specific *DDInstall* section. That is, the **UmdfServiceOrder** directive cannot be imported by using the **Include** and **Needs** directives.

## UmdfImpersonationLevel

**UmdfImpersonationLevel** = <*level*>  

Informs the framework about the maximum impersonation level that the UMDF driver can have. A **UmdfImpersonationLevel** directive is optional; if an impersonation level is not specified, the default is **Identification**. When an application opens a file handle, the application can grant a greater impersonation level to the driver. However, the driver cannot call the [**IWDFIoRequest::Impersonate**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-impersonate) method to request an impersonation level that is greater than the level that **UmdfImpersonationLevel** specifies. The possible values for this directive are:

-   **Anonymous**

-   **Identification**

-   **Impersonation**

-   **Delegation**

These values correspond to the values that are specified in the [**SECURITY\_IMPERSONATION\_LEVEL**](/windows-hardware/drivers/ddi/wudfddi/ne-wudfddi-_security_impersonation_level) enumeration.

## UmdfMethodNeitherAction

**UmdfMethodNeitherAction** = <**Copy** | **Reject**>  

Indicates whether the framework will accept (**Copy**) or reject (**Reject**) a device's I/O requests, if the request objects contain I/O control codes that specify the [METHOD\_NEITHER](../kernel/buffer-descriptions-for-i-o-control-codes.md) buffer access method. A **UmdfMethodNeitherAction** directive is optional. If the directive is not specified, the default value is **Reject**.

For more information about supporting the METHOD\_NEITHER buffer access method in UMDF-based drivers, see [Using Neither Buffered I/O nor Direct I/O in UMDF Drivers](./accessing-data-buffers-in-umdf-1-x-drivers.md#using-neither-buffered-i-o-nor-direct-i-o-in-umdf-drivers).

## UmdfDispatcher

**UmdfDispatcher** = <**FileHandle** | **WinUsb** | **NativeUSB**>  

Informs the framework where to send I/O after the I/O goes through the user-mode portion of the device stack. By default, I/O is sent to the reflector (WUDFRd.sys). By setting **UmdfDispatcher** to **WinUsb**, the driver instructs UMDF to send I/O to the WinUsb architecture. Starting in UMDF 2.15, specifying **NativeUSB** causes the reflector to handle USB I/O.

-   If any driver in the stack uses a file-handle-based target, set this directive to **FileHandle**.
-   If the driver uses UMDF 2.15 or later and uses USB I/O targets, set this directive to **NativeUSB**.
-   If the driver is pre-UMDF 2.15 and uses USB I/O targets, set this directive to **WinUsb**.

A **UmdfDispatcher** directive is optional.

The following code example shows the **UmdfDispatcher** directive in a WDF-specific **DDInstall** section.

```inf
[Xxx_Install.Wdf]
UmdfDispatcher=NativeUSB
```

## UmdfKernelModeClientPolicy

*This directive is supported in UMDF versions 1.9 and later.*

**UmdfKernelModeClientPolicy** = <**AllowKernelModeClients** | **RejectKernelModeClients**>  

To allow kernel-mode drivers to load above a user-mode driver in earlier UMDF versions, see [Kernel-mode Client Support in Earlier UMDF Versions](./supporting-kernel-mode-clients-in-umdf-1-x-drivers.md#kernel-mode-client-support-in-earlier-umdf-versions).

Indicates whether the framework should allow the driver to receive I/O requests from kernel-mode drivers.

If **UmdfKernelModeClientPolicy** is set to **AllowKernelModeClients**, the framework allows kernel-mode drivers to load above a user-mode driver, and it delivers I/O requests from kernel-mode drivers to the user-mode driver.

If **UmdfKernelModeClientPolicy** is set to **RejectKernelModeClients**, the framework does not allow kernel-mode drivers to load above a user-mode driver, and it does not deliver I/O requests from any kernel-mode drivers to the user-mode driver. If a driver's INF file does not contain this directive, the default value is **RejectKernelModeClients**. For more information, see [Supporting Kernel-mode Clients](./supporting-kernel-mode-clients-in-umdf-1-x-drivers.md).


## UmdfFileObjectPolicy

*This directive is supported in UMDF versions 1.11 and later.*

**UmdfFileObjectPolicy** = <**RejectNullAndUnknownFileObjects** | **AllowNullAndUnknownFileObjects**>   

Indicates whether the framework should allow processing of I/O requests ([IWDFIoRequest](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest)) that are either not associated with a file object ([IWDFFile](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile)) or are associated with an unknown file object (a file object for which a driver has not previously seen a create request).

If **UmdfFileObjectPolicy** is set to **RejectNullAndUnknownFileObjects**, the framework does not allow processing of requests that are associated with a NULL or unknown file object.

If **UmdfFileObjectPolicy** is set to **AllowNullAndUnknownFileObjects**, the framework allows processing of requests that are associated with a NULL or unknown file object.

The default value is **RejectNullAndUnknownFileObjects**.


## UmdfFsContextUsePolicy

*This directive is supported in UMDF versions 1.11 and later.*

**UmdfFsContextUsePolicy** = <**CanUseFsContext** | **CanUseFsContext2** | **CannotUseFsContexts**> 

Indicates whether the framework can store internal information in specific context members of a WDM file object. If a kernel-mode driver in the same stack uses a particular member of the file object, you can use this directive to request that the framework not use the same location.

If **UmdfFsContextUsePolicy** is set to **CanUseFsContext**, the framework stores information in the **FsContext** member of the WDM file object.

If **UmdfFsContextUsePolicy** is set to **CanUseFsContext2**, the framework stores information in the **FsContext2** member of the WDM file object.

If **UmdfFsContextUsePolicy** is set to **CannotUseFsContexts**, the framework does not use either **FsContext** or **FsContext2**.

The default value is **CanUseFsContext**.

## [UMDF Directives for wdf-service-install section]

The following is a code example. Each UMDF-specific directive in the wdf-service-install section is described below. The section name is specified in a UmdfService directive in the DDInstall.wdf section.

```inf
[Echo_service_wdfsect]
UmdfLibraryVersion = $UMDFVERSION$
ServiceBinary = %13%\echo.dll
```

## UmdfLibraryVersion

**UmdfLibraryVersion** = <*version*>  

Informs the co-installer about the version number of the framework that the UMDF driver will use. The format of the *version* string is <*major*>.<*minor*>.<*service*>. When drivers on the device stack use more than one version of the framework, the INF file copies multiple co-installers--one for each framework version--to the same location on the hard disk drive. However, the INF file adds only the highest version co-installer to the **CoInstallers32** registry value. For more information about copying co-installers, see [Using the UMDF Co-installer](using-the-umdf-co-installer.md).

The co-installer verifies the version string and uses it to locate the version-specific co-installer for the UMDF driver. The co-installer then extracts the framework from the version-specific co-installer.

## ServiceBinary

**ServiceBinary** = <*binarypath*>  

Informs UMDF about where to place the UMDF driver binary on the hard disk drive.

UMDF drivers should be copied to, and run from, the `Windows\System32\Drivers\UMDF` directory.

## DriverCLSID

**Note**  This directive is only supported in UMDF 1.x, which is deprecated. For more info, see [UMDF 1.x Design Guide](./user-mode-driver-framework-design-guide.md).

**DriverCLSID** = <{*CLSID*}>  

Informs UMDF about the class identifier (CLSID) of the UMDF driver. When UMDF loads the UMDF driver, the UMDF host uses the UMDF driver's CLSID to create an instance of the UMDF driver's [IDriverEntry](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-idriverentry) interface.

## UmdfExtensions

**UmdfExtensions** = <*cxServiceName*>  

Required for drivers that communicate with class extension drivers provided by Microsoft.  The cxServiceName parameter corresponds to the service associated with the class extension driver binary.

Service names for the class extension drivers could be located as a subkey under the following registry key:
**HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WUDF\Services**

The following code example shows the required directives in a KMDF-service-install section.

```inf
[Echo_service_wdfsect]
KmdfLibraryVersion = $KMDFVERSION$
```

## [KMDF Directives for DDInstall.WDF sections]

The following is a code example. Each KMDF-specific directive in the DDInstall.WDF section is described below.

```inf
[ECHO_Device.NT.Wdf]
KmdfService =  Echo, Echo_service_wdfsect
```

## KmdfService

`**KmdfService** = <*serviceName*>, <*sectionName*>

Associates a KMDF driver with a *KMDF-service-install* section that contains information that is required to install the KMDF driver. The *serviceName* parameter specifies the KMDF driver, and is limited to a maximum of 31 characters in length. The *sectionName* parameter references the *KMDF-service-install* section. A valid INF file typically requires at least one **KmdfService** directive. However, if a KMDF driver is part of the operating system, a **KmdfService** directive for the KMDF driver is not required. Therefore, a valid INF file might not have any **KmdfService** directives, although most INF files have one **KmdfService** directive for each KMDF driver.

## [KMDF Directives for wdf-service-install section]

The following is a code example. Each KMDF-specific directive in the wdf-service-install section is described below.  The section name comes from KmdfService directive in DDInstall.wdf section.

```inf
[Echo_service_wdfsect]
KmdfLibraryVersion = $KMDFVERSION$
```

## KmdfLibraryVersion

```inf
KmdfLibraryVersion = <version>
```
 
The format of the version string is `major.minor`. Normally you should specify `$KMDFVERSION$` and then the WDK build process will replace it with the correct version number.
