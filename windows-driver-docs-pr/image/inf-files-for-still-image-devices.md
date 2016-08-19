---
title: INF Files for Still Image Devices
author: windows-driver-content
description: INF Files for Still Image Devices
MS-HAID:
- 'stillimg\_d4b9463b-e568-4d78-ab61-8288ffaad713.xml'
- 'image.inf\_files\_for\_still\_image\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f68ba904-9049-4f7e-9903-fdf6f413a1a5
---

# INF Files for Still Image Devices


## <a href="" id="ddk-inf-files-for-still-image-devices-si"></a>


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
<td><p>For non-PnP devices connected to serial or parallel ports, this can be <strong>Serial</strong> or <strong>Parallel</strong> to limit the user's choice of ports during installation.</p></td>
<td><p>Optional. If not specified, the user can select any serial or parallel port.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Capabilities</strong></p></td>
<td><p>Specifies a number that is converted to bit flags identifying device capabilities. These flags are stored in the registry and are available to Microsoft STI components by means of the [<strong>STI_DEV_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548380) structure.</p>
<p>Bit 0 − Sets/clears STI_GENCAP_NOTIFICATIONS in STI_DEV_CAPS.</p>
<p>Bit 1 − Sets/clears STI_GENCAP_POLLING_NEEDED in STI_DEV_CAPS.</p>
<p>Bit 2 − Sets/clears STI_GENCAP_GENERATE_ARRIVALEVENT in STI_DEV_CAPS.</p>
<p>Bit 3 − Sets/clears STI_GENCAP_AUTO_PORTSELECT in STI_DEV_CAPS.</p></td>
<td><p>Optional</p></td>
</tr>
<tr class="even">
<td><p><strong>PropertyPages</strong></p></td>
<td><p>Identifies the name and entry point of a DLL that creates customized [Property Sheet Pages for Still Image Devices](property-sheet-pages-for-still-image-devices.md).</p>
<p>The following example identifies the DLL, <em>estp2cpl.dll</em>, as well as the <strong>EnumStiPropPages</strong> entry point in this DLL. The entry point name is optional; if omitted, the entry point defaults to <strong>EnumStiPropPages</strong>.</p>
<pre space="preserve"><code>PropertyPages = estp2cpl.dll, EnumStiPropPages</code></pre></td>
<td><p>Optional</p></td>
</tr>
<tr class="odd">
<td><p><strong>DeviceData</strong></p></td>
<td><p>Identifies a vendor-supplied data section containing information to be stored in the registry, under the <strong>DeviceData</strong> key. For TWAIN-supported devices, the data section must contain a <strong>TwainDS</strong> entry (see [Vendor-Modifiable Registry Values](registry-entries-for-still-image-devices.md#ddk-vendor-modifiable-registry-values-si)).</p></td>
<td><p>Optional. This entry is required for [Creating Push-Model Aware Applications](creating-push-model-aware-applications.md), however.</p></td>
</tr>
<tr class="even">
<td><p><strong>Events</strong></p></td>
<td><p>Identifies a vendor-supplied data section listing still image device events. Each entry in this section must have the following format:</p>
<p><em>EventName</em><strong>=&quot;</strong><em>String</em><strong>&quot;,{</strong><em>GUID</em><strong>},</strong>App</p>
<p><em>EventName</em> is the event's internal name, <em>String</em> is the event's display string, <em>GUID</em> is the event's GUID (see [Still Image Device Events](still-image-device-events.md)), and <em>App</em> specifies the imaging application to be launched when the event occurs. To launch the currently registered application, use an asterisk (<strong>*</strong>) for <em>App</em>.</p></td>
<td><p>Optional. This entry is required for [Creating Push-Model Aware Applications](creating-push-model-aware-applications.md), however.</p></td>
</tr>
<tr class="odd">
<td><p><strong>UninstallSection</strong></p></td>
<td><p>Points to an INF section typically containing [<strong>INF DelFiles directives</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547363) and [<strong>INF DelReg directives</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547374). An entry in this section has the following format:</p>
<p><strong>UninstallSection</strong><em>=UninstallSectionName</em></p>
<p><em>UninstallSectionName</em> is the name of the section containing <strong>Delfiles</strong> or <strong>DelReg</strong> directives. Note that Windows File Protection ([<em>Windows File Protection (WFP)</em>](https://msdn.microsoft.com/library/windows/hardware/ff556347#wdkgloss-windows-file-protection--wfp-)) might prohibit a user from deleting some files, even though they are specified using <strong>DelFiles</strong> directives.</p></td>
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

For additional guidance in creating INF files for still image devices, you can look at any INF file provided with Windows 2000 or later that contains the entry "Subclass=StillImage".

**Remarks**

When you're developing an INF file for scanners, you can use [Microsoft OS descriptors](http://msdn.microsoft.com/library/windows/hardware/gg463179.aspx) to enable compatibility ID functionality. When you do this, you allow one scanner driver to be compatible with multiple scanner models.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20INF%20Files%20for%20Still%20Image%20Devices%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


