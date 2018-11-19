---
title: INF Files for Still Image Devices
description: INF Files for Still Image Devices
ms.assetid: f68ba904-9049-4f7e-9903-fdf6f413a1a5
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# INF Files for Still Image Devices

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
<td><p><strong>StillImage</strong></p></td>
<td><p>Required</p></td>
</tr>
<tr class="even">
<td><p><strong>DeviceType</strong></p></td>
<td><p><strong>1</strong> for scanners, <strong>2</strong> for cameras, <strong>3</strong> for Video devices</p></td>
<td><p>Required</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceSubType</strong></p></td>
<td><p>Vendor-defined value.</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p><strong>Connection</strong></p></td>
<td><p>For non-PnP devices connected to serial or parallel ports, this can be <strong>Serial</strong> or <strong>Parallel</strong> to limit the user&#39;s choice of ports during installation.</p></td>
<td><p>Optional. If not specified, the user can select any serial or parallel port.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Capabilities</strong></p></td>
<td><p>Specifies a number that is converted to bit flags identifying device capabilities. These flags are stored in the registry and are available to Microsoft STI components by means of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548380" data-raw-source="[&lt;strong&gt;STI_DEV_CAPS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548380)"><strong>STI_DEV_CAPS</strong></a> structure.</p>
<p>Bit 0 − Sets/clears STI_GENCAP_NOTIFICATIONS in STI_DEV_CAPS.</p>
<p>Bit 1 − Sets/clears STI_GENCAP_POLLING_NEEDED in STI_DEV_CAPS.</p>
<p>Bit 2 − Sets/clears STI_GENCAP_GENERATE_ARRIVALEVENT in STI_DEV_CAPS.</p>
<p>Bit 3 − Sets/clears STI_GENCAP_AUTO_PORTSELECT in STI_DEV_CAPS.</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p><strong>PropertyPages</strong></p></td>
<td><p>Identifies the name and entry point of a DLL that creates customized <a href="property-sheet-pages-for-still-image-devices.md" data-raw-source="[Property Sheet Pages for Still Image Devices](property-sheet-pages-for-still-image-devices.md)">Property Sheet Pages for Still Image Devices</a>.</p>
<p>The following example identifies the DLL, <em>estp2cpl.dll</em>, as well as the <strong>EnumStiPropPages</strong> entry point in this DLL. The entry point name is optional; if omitted, the entry point defaults to <strong>EnumStiPropPages</strong>.</p>
<pre space="preserve"><code>PropertyPages = estp2cpl.dll, EnumStiPropPages</code></pre></td>
<td><p>Optional</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceData</strong></p></td>
<td><p>Identifies a vendor-supplied data section containing information to be stored in the registry, under the <strong>DeviceData</strong> key. For TWAIN-supported devices, the data section must contain a <strong>TwainDS</strong> entry (see <a href="registry-entries-for-still-image-devices.md#ddk-vendor-modifiable-registry-values-si" data-raw-source="[Vendor-Modifiable Registry Values](registry-entries-for-still-image-devices.md#ddk-vendor-modifiable-registry-values-si)">Vendor-Modifiable Registry Values</a>).</p></td>
<td><p>Optional. This entry is required for <a href="creating-push-model-aware-applications.md" data-raw-source="[Creating Push-Model Aware Applications](creating-push-model-aware-applications.md)">Creating Push-Model Aware Applications</a>, however.</p></td>
</tr>
<tr class="even">
<td><p><strong>Events</strong></p></td>
<td><p>Identifies a vendor-supplied data section listing still image device events. Each entry in this section must have the following format:</p>
<p><em>EventName</em><strong>=&quot;</strong><em>String</em><strong>&quot;,{</strong><em>GUID</em><strong>},</strong>App</p>
<p><em>EventName</em> is the event&#39;s internal name, <em>String</em> is the event&#39;s display string, <em>GUID</em> is the event&#39;s GUID (see <a href="still-image-device-events.md" data-raw-source="[Still Image Device Events](still-image-device-events.md)">Still Image Device Events</a>), and <em>App</em> specifies the imaging application to be launched when the event occurs. To launch the currently registered application, use an asterisk (<strong>*</strong>) for <em>App</em>.</p></td>
<td><p>Optional. This entry is required for <a href="creating-push-model-aware-applications.md" data-raw-source="[Creating Push-Model Aware Applications](creating-push-model-aware-applications.md)">Creating Push-Model Aware Applications</a>, however.</p></td>
</tr>
<tr class="odd">
<td><p><strong>UninstallSection</strong></p></td>
<td><p>Points to an INF section typically containing <a href="https://msdn.microsoft.com/library/windows/hardware/ff547363" data-raw-source="[&lt;strong&gt;INF DelFiles directives&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547363)"><strong>INF DelFiles directives</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547374" data-raw-source="[&lt;strong&gt;INF DelReg directives&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547374)"><strong>INF DelReg directives</strong></a>. An entry in this section has the following format:</p>
<p><strong>UninstallSection</strong><em>=UninstallSectionName</em></p>
<p><em>UninstallSectionName</em> is the name of the section containing <strong>Delfiles</strong> or <strong>DelReg</strong> directives. Note that Windows File Protection (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556347#wdkgloss-windows-file-protection--wfp-" data-raw-source="[&lt;em&gt;Windows File Protection (WFP)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556347#wdkgloss-windows-file-protection--wfp-)"><em>Windows File Protection (WFP)</em></a>) might prohibit a user from deleting some files, even though they are specified using <strong>DelFiles</strong> directives.</p></td>
<td><p>Optional. This entry is valid only for Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

The default class installer for still image devices supports the standard [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346). The installer uses an internal reference counter for component files, so files shared by several devices are not removed prematurely during an uninstall operation.

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
    <th>For USB devices</th>
    <th>For SCSI devices</th>
    <th>For serial devices</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre space="preserve"><code>Include=sti.inf</code></pre>
    <pre space="preserve"><code>Needs=STI.USBSection</code></pre></td>
    <td><pre space="preserve"><code>Include=sti.inf</code></pre>
    <p>Needs=STI.SCSISection</p></td>
    <td><pre space="preserve"><code>Include=sti.inf</code></pre>
    <pre space="preserve"><code>Needs=STI.SerialSection</code></pre></td>
    </tr>
    </tbody>
    </table>

     

<!-- -->

-   An [**INF DDInstall.Services Section**](https://msdn.microsoft.com/library/windows/hardware/ff547349), which must be referenced within the *DDInstall*.**Services** section of the vendor-supplied INF file, as shown in the following table.

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>For USB devices</th>
    <th>For SCSI devices</th>
    <th>For serial devices</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre space="preserve"><code>Include=sti.inf</code></pre>
    <pre space="preserve"><code>Needs=STI.USBSection.Services</code></pre></td>
    <td><pre space="preserve"><code>Include=sti.inf</code></pre>
    <pre space="preserve"><code>Needs=STI.SCSISection.Services</code></pre></td>
    <td><pre space="preserve"><code>Include=sti.inf</code></pre>
    <pre space="preserve"><code>Needs=STI.SerialSection.Services</code></pre></td>
    </tr>
    </tbody>
    </table>

     

If you are also [creating device-specific components for image acquisition APIs](creating-device-specific-components-for-image-acquisition-apis.md), you will typically include the file names for these components in the INF file.

For additional guidance in creating INF files for still image devices, you can look at any INF file provided with Windows that contains the entry "Subclass=StillImage".

**Remarks**

When you're developing an INF file for scanners, you can use [Microsoft OS descriptors](https://msdn.microsoft.com/library/windows/hardware/gg463179.aspx) to enable compatibility ID functionality. When you do this, you allow one scanner driver to be compatible with multiple scanner models.

 

 




