---
title: INF Files for WIA Devices
description: INF files for WIA devices
ms.date: 05/03/2023
---

# INF files for WIA devices

> [!IMPORTANT]
> Some information contained in this article applies to obsolete Windows operating systems.

The default class installer for still image devices, *sti\_ci.dll*, recognizes a special set of INF file entries. Within an INF file, these entries must be placed within a device's [**INF DDInstall Section**](../install/inf-ddinstall-section.md). The entries are described in the following table.

| INF file entry | Value | Comments |
|--|--|--|
| **SubClass** | StillImage | Required |
| **DeviceType** | 1 for scanners<br><br>2 for cameras<br><br>3 for streaming video | Required |
| **DeviceSubType** | Vendor-defined value | Optional |
| **Connection** | For non-Plug and Play devices connected to serial or parallel ports, this can be Serial or Parallel to limit the user's choice of ports during installation. | Optional<br><br>If not specified, the user can select any serial or parallel port. |
| **Capabilities** | Specifies a number that is converted to bit flags identifying device capabilities. These flags are stored in the registry and are available to STI components by means of the STI_DEV_CAPS structure.<br><br>Bit 0 − Sets/clears STI_GENCAP_NOTIFICATIONS in STI_DEV_CAPS.<br><br>Bit 1 − Sets/clears STI_GENCAP_POLLING_NEEDED in STI_DEV_CAPS.<br><br>Bit 2 − Sets/clears STI_GENCAP_GENERATE_ARRIVALEVENT in STI_DEV_CAPS.<br><br>Bit 3 − Sets/clears STI_GENCAP_AUTO_PORTSELECT in STI_DEV_CAPS.<br><br>Bit 4 − Sets/clears STI_GENCAP_WIA in STI_DEV_CAPS.<br><br>Bit 5 − Sets/clears STI_GENCAP_SUBSET in STI_DEV_CAPS. | Optional<br><br>Bit 5 is currently not used.<br><br>Set this entry in your INF file to 0x33 to support push-button events with your scanner. |
| **PropertyPages** | For Windows 98 and Windows 2000 only<br><br>Identifies the name and entry point of a DLL that creates customized property sheet pages for still image devices.<br><br>For more information about the **PropertyPages** entry, see [INF Files for Still Image Devices](inf-files-for-still-image-devices.md). | Optional<br><br>This entry is for use only by STI drivers, and is obsolete for WIA drivers.<br><br>For information about property pages relevant to WIA driver developers, see the **Note** on PropertyPages following this table. |
| **DeviceData** | Identifies a vendor-supplied data section containing information to be stored in the registry, under the **DeviceData** key. For TWAIN-supported devices, the data section must contain a TwainDS entry (see [Registry Entries for WIA Drivers](registry-entries-for-wia-drivers.md)) | Optional |
| **Events** | Identifies a vendor-supplied data section listing still image device events. Each entry in this section must have the following format:<br><br>*EventName*="*String*",{*GUID*},App<br><br>*EventName* is the event's internal name, *String* is the event's display string, *GUID* is the event's GUID, and *App* specifies the imaging application to be launched when the event occurs. To launch the currently registered application, use an asterisk (*) for*App*. | Required |
| **PortSelect** | If the device installation does not require a port selection page, a value of "no" causes that page to be skipped. This value also causes the **CreateFileName** entry value (see the **Note** on **CreateFileName** and **PortSelect** following this table) to be automatically set to AUTO.<br><br>A value of Message1 causes a system-supplied message to be displayed, and sets the **CreateFileName** entry value to AUTO.<br><br>Applies to both scanners and cameras that require manual installation. | Optional<br><br>Note that for Plug and Play devices, **PortSelect** is ignored, but the device still must have the **CreateFileName** entry value set to AUTO in order for WIA to load the device. Use the [**INF AddReg Directive**](../install/inf-addreg-directive.md) to add this entry to the [**INF DDInstall Section**](../install/inf-ddinstall-section.md) of the device's INF file. |

> [!NOTE]
> In order to communicate with a device, a user-mode client (a minidriver) must ask the WIA service for the device's file name and a string that specifies the name of the object to create or open. (The file name does not have to be the name of a disk file.) Responding to such a query, the WIA service obtains the device's file name from the **CreateFileName** registry entry. (The *usbscan.sys* and *scsiscan.sys* kernel-mode drivers create this entry, as does the class installer.) The minidriver receives this file name by calling the [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname) method. The minidriver can then use this file name when it calls the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function to open a handle to the device. If the device is installed manually, the class installer creates the **CreateFileName** entry, setting its value to one that depends on the user's selection on the port selection page: COM*X*, LPT*X*, or AUTO. Some devices (network scanners, for example) that are installed manually do not require a port. In such cases, the resulting port selection dialog can confuse users. You can prevent this dialog from appearing by adding the following entry in the [**INF DDInstall Section**](../install/inf-ddinstall-section.md) of your device's INF file.

```INF
PortSelect=NO
```

> [!NOTE]
> A side effect of this entry value is that the **CreateFileName** entry is set to AUTO. Be advised that if the minidriver receives AUTO for the file name, it must be able to determine on its own which device it should communicate with.

> [!NOTE]
> For PropertyPages, A WIA driver must use a different extensibility mechanism in order to add property pages. It must also add its own GUID to the **UI Class ID** entry in its INF files, and must provide specific UI extensibility registration (see [User Interface Extension Registry Entries](user-interface-extension-registry-entries.md)) for the UI components being replaced, such as common dialogs, or added, such as context menus and property pages. A WIA driver must also provide UI extensibility registration for the component itself.

## Additional INF File Entries

The entries in the following table must be placed within the section pointed to by the device's [**INF AddReg Directive**](../install/inf-addreg-directive.md):

| INF file entry | Value | Comments |
|---------|---------|---------|
|**HardwareConfig**     |    Indicates the type of connection the device is using.<br><br>1,1 − generic WDM device<br><br>1,2 − SCSI device<br><br>1,4 − USB device<br><br>1,8 − serial device<br><br>1,16 − parallel device     |     Optional    |
|**USDClass**     |     Indicates the GUID for the minidriver.    |      Optional.<br><br>The GUID in the **USDClass** and **CLSID** entries must match the GUID that is used in the **DllGetClassObject** function of the minidriver. If you are writing a microdriver, the value should be BB6CF8E2-1511-40bd-91BA-80D43C53064E. Otherwise, you must generate a new GUID, using, for example, *genguid.exe*.   |
|**CLSID**     |     Indicates the GUID for the minidriver.    |   Optional.<br><br>See the immediately preceding comments for the **USDClass** entry.      |

The default class installer for still image devices supports the standard [**INF CopyFiles Directive**](../install/inf-copyfiles-directive.md).

The default INF file for still image devices, *sti.inf*, defines two installation sections for each device type, as follows:

- An [**INF DDInstall Section**](../install/inf-ddinstall-section.md), which must be referenced within the *DDInstall* section of the vendor-supplied INF file, as shown in the following table.

    | Device Type | Include | Needs |
    |--|--|--|
    | IEEE 1394/SBP2 | Include=sti.inf | Needs=STI.SBP2Section |
    | USB | Include=sti.inf | Needs=STI.USBSection |
    | SCSI | Include=sti.inf | Needs=STI.SCSISection |
    | Serial | Include=sti.inf | Needs=STI.SerialSection |

- An INF DDInstall Services section, which must be referenced within the [**INF DDInstall.Services Section**](../install/inf-ddinstall-services-section.md) of the vendor-supplied INF file, as shown in the following table.

    | Device Type | Include | Needs |
    |--|--|--|
    | 1394/SBP2 | Include=sti.inf | Needs=STI.SBP2Section.Services |
    | USB | Include=sti.inf | Needs=STI.USBSection.Services |
    | SCSI | Include=sti.inf | Needs=STI.SCSISection.Services |
    | Serial | Include=sti.inf | Needs=STI.SerialSection.Services |

For additional guidance in creating INF files for still image devices, you can look at any INF file provided with Windows that contains the entry SubClass=StillImage.

To designate the device as a WIA device, the minidriver INF file must contain the following values placed within the *DeviceData* section of the vendor-supplied INF file.

| INF File Entry | Value | Comments |
|--|--|--|
| **Server** | Local | Designates the device as a local device. This is optional and if a vendor does not specify an entry value, the device is assumed to be local. That is, the WIA_DIP_SERVER_NAME property is set to Local. |
| **MicroDriver** | Vendor-supplied *.dll* file name | This entry should be set to the name of the vendor-supplied DLL that implements the WIA microdriver. |
| **UI DLL** | Vendor-supplied *.dll* file name | Obsolete and never used. Formerly, this entry indicated the name of the vendor-supplied user interface DLL file. |
| **UI Class ID** | Vendor-supplied device class identifier | Indicates the device class the vendor-supplied user interface is capable of supporting. This is optional and if a vendor does not specify an entry value, WIA sets the WIA_DIP_UI_CLSID property to GUID_NULL and the default WIA UI is used. |
| **ICMProfiles** | Vendor-supplied color profile value | Specifies a value to put in the WIA_IPA_ICM_PROFILE_NAME property. If no value is specified, the standard sRGB profile *sRGB Color Space Profile.icm* is used. |

The **MicroDriver** entry is required only if the vendor supplies a WIA microdriver.

The user interface (UI) entries are required only if the vendor supplies a custom user interface for the imaging device.

## Remarks

When you're developing an INF file for scanners, you can use [Microsoft OS descriptors](/previous-versions/gg463179(v=msdn.10)) to enable compatibility ID functionality. When you do this, you allow one scanner driver to be compatible with multiple scanner models.
