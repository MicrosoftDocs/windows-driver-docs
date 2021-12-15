---
title: INF Files for Still Image Devices
description: INF Files for Still Image Devices
ms.date: 03/21/2019
---

# INF Files for Still Image Devices

The default class installer for still image devices, *sti\_ci.dll*, recognizes a special set of INF file entries. Within an INF file, these entries must be placed within a device's [**INF DDInstall Section**](../install/inf-ddinstall-section.md). The entries are described in the following table.

| INF File Entry | Value | Comments |
| --- | --- | --- |
| SubClass | StillImage | Required |
| DeviceType | 1 for scanners, 2 for cameras, 3 for video devices | Required |
| DeviceSubType | Vendor-defined value | Optional |
| Connection | For non-PnP devices connected to serial or parallel ports, this can be Serial or Parallel to limit the user's choice of ports during installation. | Optional.<br>If not specified, the user can select any serial or parallel port. |
| Capabilities | Specifies a number that is converted to bit flags identifying device capabilities. These flags are stored in the registry and are available to Microsoft STI components by means of the [STI_DEV_CAPS](/windows-hardware/drivers/ddi/sti/ns-sti-_sti_dev_caps) structure.<br><br>Bit 0 − Sets/clears STI_GENCAP_NOTIFICATIONS in STI_DEV_CAPS<br>Bit 1 − Sets/clears STI_GENCAP_POLLING_NEEDED in STI_DEV_CAPS<br>Bit 2 − Sets/clears STI_GENCAP_GENERATE_ARRIVALEVENT in STI_DEV_CAPS<br>Bit 3 − Sets/clears STI_GENCAP_AUTO_PORTSELECT in STI_DEV_CAPS | Optional |
| PropertyPages | Identifies the name and entry point of a DLL that creates customized [Property Sheet Pages for Still Image Devices](property-sheet-pages-for-still-image-devices.md).<br>The following example identifies the DLL, *estp2cpl.dll*, as well as the **EnumStiPropPages** entry point in this DLL. The entry point name is optional; if omitted, the entry point defaults to **EnumStiPropPages**.<br><br>`PropertyPages = estp2cpl.dll, EnumStiPropPages`<br><br> | Optional |
| DeviceData | Identifies a vendor-supplied data section containing information to be stored in the registry, under the **DeviceData** key. For TWAIN-supported devices, the data section must contain a **TwainDS** entry. For more information, see [Vendor-Modifiable Registry Values](registry-entries-for-still-image-devices.md#ddk-vendor-modifiable-registry-values-si) | Optional.<br>However, this entry is required for [Creating Push-Model Aware Applications](creating-push-model-aware-applications.md). |
| Events | Identifies a vendor-supplied data section listing still image device events. Each entry in this section must have the following format:<br><br>`EventName="String",{GUID},App`<br><br>*EventName* is the event's internal name, *String* is the event's display string, *GUID* is the event's GUID, see [Still Image Device Events](still-image-device-events.md), and *App* specifies the imaging application to be launched when the event occurs. To launch the currently registered application, use an asterisk (*) for *App*. | Optional.<br>However, this entry is required for [Creating Push-Model Aware Applications](creating-push-model-aware-applications.md). |
| UninstallSection | Points to an INF section typically containing [INF DelFiles directives](../install/inf-delfiles-directive.md) and [INF DelReg directives](../install/inf-delreg-directive.md). An entry in this section has the following format:<br><br>`UninstallSection=UninstallSectionName`<br><br>*UninstallSectionName* is the name of the section containing **Delfiles** or **DelReg** directives. Note that **Windows File Protection** might prohibit a user from deleting some files, even though they are specified using **DelFiles** directives. | Optional.<br>This entry is valid only for Windows 2000. |

The default class installer for still image devices supports the standard [INF CopyFiles directive](../install/inf-copyfiles-directive.md). The installer uses an internal reference counter for component files, so files shared by several devices are not removed prematurely during an uninstall operation.

The default INF file for still image devices, *sti.inf*, defines two installation sections for each device type, as follows:

- An [INF DDInstall Section](../install/inf-ddinstall-section.md), which must be referenced within the *DDInstall* section of the vendor-supplied INF file, as shown in the following table.

| USB devices | SCSI devices | Serial devices |
| --- | --- | --- |
| `Include=sti.inf`<br><br>`Needs=STI.USBSection` | `Include=sti.inf`<br><br>`Needs=STI.SCSISection`  | `Include=sti.inf`<br><br>`Needs=STI.SerialSection` |

- An [INF DDInstall.Services Section](../install/inf-ddinstall-services-section.md), which must be referenced within the *DDInstall*.**Services** section of the vendor-supplied INF file, as shown in the following table.

| USB devices | SCSI devices | Serial devices |
| --- | --- | --- |
| `Include=sti.inf`<br><br>`Needs=STI.USBSection.Services` | `Include=sti.inf`<br><br>`Needs=STI.SCSISection.Services`  | `Include=sti.inf`<br><br>`Needs=STI.SerialSection.Services` |

If you are also [creating device-specific components for image acquisition APIs](creating-device-specific-components-for-image-acquisition-apis.md), you will typically include the file names for these components in the INF file.

For additional guidance in creating INF files for still image devices, you can look at any INF file provided with Windows that contains the entry "Subclass=StillImage".

## Remarks

When you're developing an INF file for scanners, you can use [Microsoft OS descriptors](/previous-versions/gg463179(v=msdn.10)) to enable compatibility ID functionality. When you do this, you allow one scanner driver to be compatible with multiple scanner models.
