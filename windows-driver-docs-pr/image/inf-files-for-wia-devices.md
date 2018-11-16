---
title: INF Files for WIA Devices
description: INF Files for WIA Devices
ms.assetid: 65eac8b5-35d2-4537-8646-a35a1cf9aced
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# INF Files for WIA Devices


The default class installer for still image devices, *sti\_ci.dll*, recognizes a special set of INF file entries. Within an INF file, these entries must be placed within a device's [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344). The entries are described in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>INF File Entry</th>
<th>Value</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>SubClass</strong></p></td>
<td><p>StillImage</p></td>
<td><p>Required</p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceType</strong></p></td>
<td><p>1 for scanners</p>
<p>2 for cameras</p>
<p>3 for streaming video</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceSubType</strong></p></td>
<td><p>Vendor-defined value</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p><strong>Connection</strong></p></td>
<td><p>For non-Plug and Play devices connected to serial or parallel ports, this can be Serial or Parallel to limit the user&#39;s choice of ports during installation.</p></td>
<td><p>Optional</p>
<p>If not specified, the user can select any serial or parallel port.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Capabilities</strong></p></td>
<td><p>Specifies a number that is converted to bit flags identifying device capabilities. These flags are stored in the registry and are available to STI components by means of the STI_DEV_CAPS structure.</p>
<p>Bit 0 − Sets/clears STI_GENCAP_NOTIFICATIONS in STI_DEV_CAPS.</p>
<p>Bit 1 − Sets/clears STI_GENCAP_POLLING_NEEDED in STI_DEV_CAPS.</p>
<p>Bit 2 − Sets/clears STI_GENCAP_GENERATE_ARRIVALEVENT in STI_DEV_CAPS.</p>
<p>Bit 3 − Sets/clears STI_GENCAP_AUTO_PORTSELECT in STI_DEV_CAPS.</p>
<p>Bit 4 − Sets/clears STI_GENCAP_WIA in STI_DEV_CAPS.</p>
<p>Bit 5 − Sets/clears STI_GENCAP_SUBSET in STI_DEV_CAPS.</p></td>
<td><p>Optional</p>
<p>Bit 5 is currently not used.</p>
<p>Set this entry in your INF file to 0x33 to support push-button events with your scanner.</p></td>
</tr>
<tr class="even">
<td><p><strong>PropertyPages</strong></p></td>
<td><p>For Windows 98 and Windows 2000 only</p>
<p>Identifies the name and entry point of a DLL that creates customized property sheet pages for still image devices.</p>
<p>For more information about the <strong>PropertyPages</strong> entry, see <a href="inf-files-for-still-image-devices.md" data-raw-source="[INF Files for Still Image Devices](inf-files-for-still-image-devices.md)">INF Files for Still Image Devices</a>.</p></td>
<td><p>Optional</p>
<p>This entry is for use only by STI drivers, and is obsolete for WIA drivers.</p>
<p>For information about property pages relevant to WIA driver developers, see the <strong>Note</strong> on PropertyPages following this table.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceData</strong></p></td>
<td><p>Identifies a vendor-supplied data section containing information to be stored in the registry, under the <strong>DeviceData</strong> key. For TWAIN-supported devices, the data section must contain a TwainDS entry (see <a href="registry-entries-for-wia-drivers.md" data-raw-source="[Registry Entries for WIA Drivers](registry-entries-for-wia-drivers.md)">Registry Entries for WIA Drivers</a>).</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p><strong>Events</strong></p></td>
<td><p>Identifies a vendor-supplied data section listing still image device events. Each entry in this section must have the following format:</p>
<p><em>EventName</em><strong>=&quot;</strong><em>String</em><strong>&quot;,{</strong><em>GUID</em><strong>},</strong>App</p>
<p><em>EventName</em> is the event&#39;s internal name, <em>String</em> is the event&#39;s display string, <em>GUID</em> is the event&#39;s GUID, and <em>App</em> specifies the imaging application to be launched when the event occurs. To launch the currently registered application, use an asterisk (<strong>*</strong>) for <em>App</em>.</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p><strong>PortSelect</strong></p></td>
<td><p>If the device installation does not require a port selection page, a value of &quot;no&quot; causes that page to be skipped. This value also causes the <strong>CreateFileName</strong> entry value (see the <strong>Note</strong> on <strong>CreateFileName</strong> and <strong>PortSelect</strong> following this table) to be automatically set to AUTO.</p>
<p>A value of Message1 causes a system-supplied message to be displayed, and sets the <strong>CreateFileName</strong> entry value to AUTO.</p>
<p>Applies to both scanners and cameras that require manual installation.</p></td>
<td><p>Optional</p>
<p>Note that for Plug and Play devices, <strong>PortSelect</strong> is ignored, but the device still must have the <strong>CreateFileName</strong> entry value set to AUTO in order for WIA to load the device. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546320" data-raw-source="[&lt;strong&gt;INF AddReg Directive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546320)"><strong>INF AddReg Directive</strong></a> to add this entry to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547344" data-raw-source="[&lt;strong&gt;INF DDInstall Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547344)"><strong>INF DDInstall Section</strong></a> of the device&#39;s INF file.</p></td>
</tr>
</tbody>
</table>

 

**Note**   In order to communicate with a device, a user-mode client (a minidriver) must ask the WIA service for the device's file name and a string that specifies the name of the object to create or open. (The file name does not have to be the name of a disk file.) Responding to such a query, the WIA service obtains the device's file name from the **CreateFileName** registry entry. (The *usbscan.sys* and *scsiscan.sys* kernel-mode drivers create this entry, as does the class installer.) The minidriver receives this file name by calling the [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944) method. The minidriver can then use this file name when it calls the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function (described in the Microsoft Windows SDK documentation) to open a handle to the device.
If the device is installed manually, the class installer creates the **CreateFileName** entry, setting its value to one that depends on the user's selection on the port selection page: COM*X*, LPT*X*, or AUTO. Some devices (network scanners, for example) that are installed manually do not require a port. In such cases, the resulting port selection dialog can confuse users. You can prevent this dialog from appearing by adding the following entry in the [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of your device's INF file:

 

```INF
     PortSelect=NO
```

**Note**  A side effect of this entry value is that the **CreateFileName** entry is set to AUTO. Be advised that if the minidriver receives AUTO for the file name, it must be able to determine on its own which device it should communicate with.

**Note**  For PropertyPages, A WIA driver must use a different extensibility mechanism in order to add property pages. It must also add its own GUID to the **UI Class ID** entry in its INF files, and must provide specific UI extensibility registration (see [User Interface Extension Registry Entries](user-interface-extension-registry-entries.md)) for the UI components being replaced, such as common dialogs, or added, such as context menus and property pages. A WIA driver must also provide UI extensibility registration for the component itself.

 

 

### Additional INF File Entries

The entries in the following table must be placed within the section pointed to by the device's [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320):

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>INF File Entry</th>
<th>Value</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>HardwareConfig</strong></p></td>
<td><p>Indicates the type of connection the device is using.</p>
<p>1,1 − generic WDM device</p>
<p>1,2 − SCSI device</p>
<p>1,4 − USB device</p>
<p>1,8 − serial device</p>
<p>1,16 − parallel device</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p><strong>USDClass</strong></p></td>
<td><p>Indicates the GUID for the minidriver.</p></td>
<td><p>Optional.</p>
<p>The GUID in the <strong>USDClass</strong> and <strong>CLSID</strong> entries must match the GUID that is used in the <strong>DllGetClassObject</strong> function of the minidriver. If you are writing a microdriver, the value should be BB6CF8E2-1511-40bd-91BA-80D43C53064E. Otherwise, you must generate a new GUID, using, for example, <em>genguid.exe</em>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CLSID</strong></p></td>
<td><p>Indicates the GUID for the minidriver.</p></td>
<td><p>Optional.</p>
<p>See the immediately preceding comments for the <strong>USDClass</strong> entry.</p></td>
</tr>
</tbody>
</table>

 

The default class installer for still image devices supports the standard [**INF CopyFiles Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346).

The default INF file for still image devices, *sti.inf*, defines two installation sections for each device type, as follows:

-   An [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344), which must be referenced within the *DDInstall* section of the vendor-supplied INF file, as shown in the following table.

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Device Type</th>
    <th>Include</th>
    <th>Needs</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>IEEE 1394/SBP2</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.SBP2Section</p></td>
    </tr>
    <tr class="even">
    <td><p>USB</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.USBSection</p></td>
    </tr>
    <tr class="odd">
    <td><p>SCSI</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.SCSISection</p></td>
    </tr>
    <tr class="even">
    <td><p>Serial</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.SerialSection</p></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   An INF DDInstall Services section, which must be referenced within the [**INF DDInstall.Services Section**](https://msdn.microsoft.com/library/windows/hardware/ff547349) of the vendor-supplied INF file, as shown in the following table.

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Device Type</th>
    <th>Include</th>
    <th>Needs</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>1394/SBP2</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.SBP2Section.Services</p></td>
    </tr>
    <tr class="even">
    <td><p>USB</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.USBSection.Services</p></td>
    </tr>
    <tr class="odd">
    <td><p>SCSI</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.SCSISection.Services</p></td>
    </tr>
    <tr class="even">
    <td><p>Serial</p></td>
    <td><p>Include=sti.inf</p></td>
    <td><p>Needs=STI.SerialSection.Services</p></td>
    </tr>
    </tbody>
    </table>

     

For additional guidance in creating INF files for still image devices, you can look at any INF file provided with Windows that contains the entry SubClass=StillImage.

To designate the device as a WIA device, the minidriver INF file must contain the following values placed within the *DeviceData* section of the vendor-supplied INF file.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>INF File Entry</th>
<th>Value</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Server</strong></p></td>
<td><p>Local</p></td>
<td><p>Designates the device as a local device. This is optional and if a vendor does not specify an entry value, the device is assumed to be local. That is, the WIA_DIP_SERVER_NAME property is set to Local.</p></td>
</tr>
<tr class="even">
<td><p><strong>MicroDriver</strong></p></td>
<td><p>Vendor-supplied <em>.dll</em> file name</p></td>
<td><p>This entry should be set to the name of the vendor-supplied DLL that implements the WIA microdriver.</p></td>
</tr>
<tr class="odd">
<td><p><strong>UI DLL</strong></p></td>
<td><p>Vendor-supplied <em>.dll</em> file name</p></td>
<td><p>Obsolete and never used. Formerly, this entry indicated the name of the vendor-supplied user interface DLL file.</p></td>
</tr>
<tr class="even">
<td><p><strong>UI Class ID</strong></p></td>
<td><p>Vendor-supplied device class identifier</p></td>
<td><p>Indicates the device class the vendor-supplied user interface is capable of supporting. This is optional and if a vendor does not specify an entry value, WIA sets the WIA_DIP_UI_CLSID property to GUID_NULL and the default WIA UI is used.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ICMProfiles</strong></p></td>
<td><p>Vendor-supplied color profile value</p></td>
<td><p>Specifies a value to put in the WIA_IPA_ICM_PROFILE_NAME property. If no value is specified, the standard sRGB profile <em>sRGB Color Space Profile.icm</em> is used.</p></td>
</tr>
</tbody>
</table>

 

The **MicroDriver** entry is required only if the vendor supplies a WIA microdriver.

The user interface (UI) entries are required only if the vendor supplies a custom user interface for the imaging device.

**Remarks**

When you're developing an INF file for scanners, you can use [Microsoft OS descriptors](https://msdn.microsoft.com/library/windows/hardware/gg463179.aspx) to enable compatibility ID functionality. When you do this, you allow one scanner driver to be compatible with multiple scanner models.

 

 




