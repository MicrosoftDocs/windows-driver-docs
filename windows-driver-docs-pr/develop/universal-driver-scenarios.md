# Universal Driver Scenarios

This topic describes how the [DCHU universal driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU) applies the DCHU design principles.  You can use it as a model for your own universal driver package.

If you would like a local copy of the sample repo, clone from [Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples).

This sample is intended to be used with Windows 10 Version 1703 and later.

## Prerequisites

Before you read this section, check out the requirements and best practices for universal driver packages described in [Getting Started with Universal Windows drivers](getting-started-with-universal-drivers.md)

## Overview

The DCHU sample provides example scenarios where two hardware partners, Contoso (OEM) and Fabrikam (IHV) are working together to create a Universal Windows Driver for a device in Contoso's upcoming system.  The device in question is an [OSR USB FX2 learning kit](https://store.osr.com/product/osr-usb-fx2-learning-kit-v2/).  In the past, Fabrikam would write a non-universal driver package that was customized to a specific Contoso product line, and then hand it to the OEM to handle servicing.  This resulted in significant maintenance overhead, so Fabrikam decides to refactor the code and create a universal driver package instead.

## Use only declarative sections and directives

First, Fabrikam reviews the [list of INF sections and directives](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file) that are invalid in universal driver packages.  During this exercise, Fabrikam notices that they're using many of these sections and directives in their driver package.  

Their non-universal driver INF registers a co-installer that applies platform-dependent settings and files.  This means that the driver package is larger than it could be, and it is harder to service the driver when a bug affects only a subset of the OEM systems that ship the driver.  Also, most of the OEM-specific modifications are related to branding, so Fabrikam needs to update the driver package every time an OEM is added or a minor issue affects a subset of OEM systems.

Fabrikam removes the non-universal sections and directives and uses the [InfVerif](../devtest/infverif.md) tool to verify that the new driver package's INF file is universal.

## Use extension INFs to componentize a driver package

Next, Fabrikam separates customizations that are specific to OEM partners (such as Contoso) from the primary driver package into an [extension INF](../install/using-an-extension-inf-file.md).

The following snippet, updated from [`osrfx2_DCHU_extension.inx`], specifies the `Extension` class and identifies Contoso as the provider since they will own the extension driver package:

```
[Version]
Class       = Extension
ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
Provider    = Contoso
ExtensionId = {3846ad8c-dd27-433d-ab89-453654cd542a}
```

In [`osrfx2_DCHU_base.inx`], Fabrikam specifies the following entries:

```
[OsrUsbFx2_AddReg]
HKR, OSR, "OperatingMode",, "Default" ; FLG_ADDREG_TYPE_SZ
HKR, OSR, "OperatingParams",, "None" ; FLG_ADDREG_TYPE_SZ
```

In [`osrfx2_DCHU_extension.inx`], Contoso overrides the `OperatingParams` registry key and adds `OperatingExceptions`:

```
[OsrUsbFx2Extension_AddReg]
HKR, OSR, "OperatingParams",, "-Extended"
HKR, OSR, "OperatingExceptions",, "x86"	
```

## Use a component to install a service from a driver package

Fabrikam requires the LEDs on the OSR board to be treated as a child device of the main board.  They control these lights using a Win32 service.

To accomplish this, they encapsulate the LED device in a component and add a separate LED controller driver package to install the service.  Now they have two driver packages in the same Visual Studio solution, which they will provide as one submission in the Windows Hardware Dev Center dashboard.

The following snippet from [`osrfx2_DCHU_base.inx`] specifies the [**AddComponent**](../install/inf-addcomponent-directive.md) directive to make the LED lights a child device to the main board and a [**CopyINF**](../install/inf-copyinf-directive.md) directive to copy the LED driver package to the system:

```
[OsrFx2_Install.NT.Components]
AddComponent = osrfx2_DCHU_usersvc,, OsrFx2_ComponentInstall_UserSvc 

[OsrFx2_ComponentInstall_UserSvc]
ComponentIds = VID_045e&PID_94ac  ; Matches with SWC\VID_045e&PID_94ac 

[OsrFx2_Install.NT]
CopyInf = osrfx2_DCHU_usersvc.inf
```

Use the [**CopyINF**](../install/inf-copyinf-directive.md) directive for multifunction devices when both driver packages are owned by the same organization.  Use extension INFs when different hardware partners own the code.

Then, in the LED controller's INF file [`osrfx2_DCHU_usersvc.inx`], Fabrikam specifies the [**AddService**](../install/inf-addservice-directive.md) directive to add and start the service:

```
[OsrFx2UserSvc_Install.NT.Services]
AddService = , 0x00000002
AddService = osrfx2_DCHU_usersvc, 0x00000800, OsrFx2UserSvc_ServiceInstall
	
[OsrFx2UserSvc_ServiceInstall]
DisplayName = %OsrFx2UserSvcDisplayName%
ServiceType = 0x00000010
StartType = 3
ErrorControl = 1
ServiceBinary = %13%\osrfx2_DCHU_usersvc.exe 

[OsrFx2UserSvc_CopyFiles]
osrfx2_DCHU_usersvc.exe
```

Note that the [**AddService**](../install/inf-addservice-directive.md) directive is not required to be in a separate component.  Fabrikam made this choice to improve componentization of their universal driver package.

## Use a component to install software from a driver package

Fabrikam has an executable file `osrfx2_DCHU_componentsoftware.exe` that they previously installed using a co-installer.  This legacy software displays the registry keys set by the board and is required by the OEM.  This is a GUI-based executable that only runs on Windows for desktop editions.  To install it, Fabrikam creates a separate component driver package.

The following snippet from [`osrfx2_DCHU_base.inx`] uses the [**AddComponent**](../install/inf-addcomponent-directive.md) directive to create a virtual child device:

```
[OsrFx2_Install.NT.Components]
AddComponent = osrfx2_DCHU_component,, OsrFx2_ComponentInstall 

[OsrFx2_ComponentInstall]
ComponentIds = VID_045e&PID_94ab; Matches with SWC\VID_045e&PID_94ab
```

Then, in the component INF [`osrfx2_DCHU_component.inx`], Fabrikam specifies the [**AddSoftware**](../install/inf-addsoftware-directive.md) directive to install the optional executable:

```
[OsrFx2Component_Install.NT.Software]
AddSoftware = osrfx2_DCHU_componentsoftware,, OsrFx2Component_SoftwareInstall
	
[OsrFx2Component_SoftwareInstall]
SoftwareType = 1
SoftwareBinary = osrfx2_DCHU_componentsoftware.exe
SoftwareArguments = <<DeviceInstanceId>>
SoftwareVersion = 1.0.0.0 

[OsrFx2Component_CopyFiles]
osrfx2_DCHU_componentsoftware.exe
```

The [source code for the Win32 app](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU/osrfx2_DCHU_component/osrfx2_DCHU_componentsoftware) is included in the DCHU sample.

Note that the component driver package is only installed on Desktop SKUs due to targeting set in the Windows Hardware Dev Center dashboard.  For more info, see [Publish a driver to Windows Update](https://docs.microsoft.com/windows-hardware/drivers/dashboard/publish-a-driver-to-windows-update).

## Add a hardware support app

Fabrikam would like to provide a GUI-based companion app as part of the universal driver package.  Because Win32-based companion applications cannot be part of a universal driver package, they port their Win32 app to the Universal Windows Platform (UWP) and [pair the app with the device](https://docs.microsoft.com/windows-hardware/drivers/devapps/hardware-access-for-universal-windows-platform-apps).

The following snippet from [`osrfx2_DCHU_base/device.c`](https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_base/device.c) shows how the primary driver package adds a custom capability to the device interface instance:

```cpp
    WDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData = { 0 };
    static const wchar_t customCapabilities[] = L"CompanyName.yourCustomCapabilityNameTBD_YourStorePubId\0";

    WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT(&PropertyData,
                                            &GUID_DEVINTERFACE_OSRUSBFX2,
                                            &DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities);

    Status = WdfDeviceAssignInterfaceProperty(Device,
                                              &PropertyData,
                                              DEVPROP_TYPE_STRING_LIST,
                                              sizeof(customCapabilities),
                                              (PVOID)customCapabilities);
```

The new app (not included in the DCHU sample) is secure and can be updated easily in the Windows Store.   With the UWP application ready, Contoso uses [DISM - Deployment Image Servicing and Management](https://docs.microsoft.com/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows) to pre-load the application on Windows desktop edition images.

## Run from the driver store

To make it easier to update the driver, Fabrikam uses the following snippet in [`osrfx2_DCHU_component.inx`] and [`osrfx2_DCHU_usersvc.inx`] to copy the driver files to the [Driver Store](../install/driver-store.md):

```
[DestinationDirs]
DefaultDestDir = 13 ; copy to driverstore
```

Using a destination directory value of 13 can result in improved stability during the driver update process.

## Summary

The following diagram shows the driver packages that Fabrikam and Contoso created for their Universal Windows Driver.  They will make three submissions on the Windows Hardware Dev Center dashboard.

![Extension, primary, and component driver packages](images/universal-scenarios.png)

## See also

[Getting Started with Universal Windows drivers](getting-started-with-universal-drivers.md)

[`osrfx2_DCHU_base.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_base/osrfx2_DCHU_base.inx
[`osrfx2_DCHU_usersvc.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_usersvc/osrfx2_DCHU_usersvc.inx
[`osrfx2_DCHU_component.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_component/osrfx2_DCHU_component/osrfx2_DCHU_component.inx
[`osrfx2_DCHU_extension.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_extension/osrfx2_DCHU_extension/osrfx2_DCHU_extension.inx
