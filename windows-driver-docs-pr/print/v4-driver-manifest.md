---
title: V4 Driver Manifest
description: The v4 print driver manifest contains printer-specific setup directives and is used in conjunction with an INF file.
ms.assetid: 187A10B7-2AAC-46D9-998C-C8724D8E3862
ms.date: 07/13/2018
ms.localizationpriority: medium
---

# V4 Driver Manifest


The v4 print driver manifest is a text file that contains all the printer-specific setup directives. A v4 print driver manifest is used in conjunction with a v4 print driver INF file, as part of the set up for a printer-specific v4 print driver.

The directives in a manifest are organized into sections:

-   [DriverConfig Section](#driverconfig-section)
-   [BidiFiles Section](#bidifiles-section)
-   [DriverRender Section](#driverrender-section)
-   [FileSave Section](#filesave-section)
-   [PrinterExtensions Section](#printerextensions-section)
-   [Related topics](#related-topics)

## DriverConfig Section


The following table shows the directives that are used in the DriverConfig section.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Directive</th>
<th>Restrictions</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>RequiredFiles</strong></p>
<p>Includes files from ntprint.inf or ntprint4.inf.</p>
<p>The RequiredFiles directive will support the following value in Windows 10:</p>
<p>PWGRRenderFilter.dll: Adds the Microsoft PWG Raster rendering filter to the driver&#39;s dependent files list.</p>
<p>The PWG Raster rendering filter render filter requires that the driver use a PrintDeviceCapabilities file for configuration.</p></td>
<td><p>Unidrv.dll, pscript5.dll, and mxdwdrv.dll should be omitted from this list. They will be resolved automatically.</p></td>
<td><p>Examples:</p>
<p>RequiredFiles=</p>
<p>UNIRES.DLL,STDNAMES.GPD,</p>
<p>V3HOSTINGFILTER.DLL</p></td>
</tr>
<tr class="even">
<td><p><strong>RequiredClass</strong></p>
<p>Causes this driver to include all files from a defined class driver using the driver/friendly name of the device and its GUID as key. This is the mechanism for linking a printclass driver to a model specific driver.</p></td>
<td><p>The RequiredClass directive cannot be used by a class driver. When you use RequiredClass, you should avoid file name collisions between the printer driver and the Print Class driver to which you&#39;re linking.</p>
<p>Although files with similar names won&#39;t overwrite each other, it may be difficult during troubleshooting, to distinguish between the class driver package file and the file from the v4 printer driver.</p></td>
<td><p>Example:</p>
<p>RequiredClass=</p>
<p>&quot;Fabrikam PCL5e Class Driver&quot;,{9343720D-B67E-4451-B93F-6F721C439771}</p></td>
</tr>
<tr class="odd">
<td><p><strong>DriverFile</strong></p>
<p>This points to the rendering binary. Mxdwdrv is the default, but class drivers may alternatively specify unidrv.dll or pscript5.dll. This is functionally identical to the same directive in a v3 INF.</p></td>
<td><p>Can only be set in a class driver. Valid choices are unidrv.dll or pscript5.dll. V4 print drivers either inherit from a RequiredClass or default to mxdwdrv.dll</p></td>
<td><p>DriverFile=</p>
<p>unidrv.dll</p></td>
</tr>
<tr class="even">
<td><p><strong>DataFile</strong></p>
<p>This defines the primary GPD or PPD for this driver. This is functionally identical to the same directive in a v3 INF.</p>
<p>In Windows 10, v4 print drivers may continue to specify a GPD or PPD DataFile, however, they may also describe a DataFile which is in the PrintDeviceCapabilities format.</p></td>
<td><p>Required.</p></td>
<td><p>Examples:</p>
<p>DataFile=FAPDL.gpd</p>
<p>DataFile=FAPDL.xml</p></td>
</tr>
<tr class="odd">
<td><p><strong>DataFileType</strong></p>
<p>The DataFileType must be used when describing a PrintDeviceCapabilities file as the DataFile, and may also be used with a GPD or PPD-based DataFile as well.</p></td>
<td><p>Required for PrintDeviceCapabilities file.</p></td>
<td><p>Example:</p>
<p>DataFileType=</p>
<p>&quot;application/vnd.ms-PrintDeviceCapabilities+xml&quot;</p></td>
</tr>
<tr class="even">
<td><p><strong>Flags</strong></p>
<p>This is used to specify additional, optional attributes associated with the driver.</p>
<p></p>
NotShareable:
This flag specifies that the driver is not shareable. This is appropriate for virtual drivers such as the Microsoft XPS Document Writer.
SoftResetOnJobCancellation:
This flag specifies that the device requires a USB soft reset (IOCTL_USBPRINT_SOFT_RESET) on print job cancellation.
ArchiveEnabled
The v4 driver uses this flag to request archive-optimized XPS as a spool file.</td>
<td><p>None.</p></td>
<td><p>Examples:</p>
<p>Flags=</p>
<p>NotShareable,</p>
<p>SoftResetOnJobCancellation</p>
<p>Flags=</p>
<p>ArchiveEnabled,NotShareable</p></td>
</tr>
<tr class="odd">
<td><p><strong>PrinterDriverID</strong></p>
<p>This is a unique ID that describes the print driver. If two drivers specify the same PrinterDriverID, then they must be compatible for sharing and support the same printer extensions.</p></td>
<td><p>Required.</p></td>
<td><p>PrinterDriverID=</p>
<p>{guid}</p></td>
</tr>
<tr class="even">
<td><p><strong>PropertyBag</strong></p>
<p>Specifies a driver property bag for this driver. This is a compiled file generated by DriverPropertyBagTool.exe or Visual Studio.</p></td>
<td><p>None.</p></td>
<td><p>PropertyBag=</p>
<p>FAProperty.dpb</p></td>
</tr>
<tr class="odd">
<td><p><strong>ResourceFile</strong></p>
<p>Defines the name of the driver&#39;s string resource DLL.</p>
<p>In Windows 10, drivers may specify a ResourceFile using .resx format.</p></td>
<td><p>None.</p></td>
<td><p>Examples:</p>
<p>ResourceFile=</p>
<p>FARC.dll</p></td>
</tr>
<tr class="even">
<td><p><strong>ConstraintScript</strong></p>
<p>Defines the name of the driver&#39;s JavaScript constraint file.</p></td>
<td><p>None.</p></td>
<td><p>ConstraintScript=</p>
<p>FAConst.js</p></td>
</tr>
<tr class="odd">
<td><p><strong>DriverCategory</strong></p>
<p>Defines the category of the device between one of several options. Valid options are as follows:</p>
PrintFax.Fax
PrintFax.Printer
PrintFax.Printer.3D
PrintFax.Printer.File
PrintFax.Printer.Service
PrintFax.Printer.Virtual</td>
<td><p>Required.</p></td>
<td><p>DriverCategory=</p>
<p>PrintFax.Printer</p>
<p>For more information about other driver categories, see <a href="printer-inf-file-entries.md" data-raw-source="[Printer INF File Entries](printer-inf-file-entries.md)">Printer INF File Entries</a>.</p></td>
</tr>
<tr class="even">
<td><p><strong>PrinterExtensionUrl</strong></p>
<p>Specifies a URL for the user to obtain a copy of the Printer extension app. Used in printer sharing.</p></td>
<td><p>None.</p></td>
<td><p>PrinterExtensionUrl=</p>
<p>&quot;<a href="http://www.fabrikam.com/files/setup.exe&amp;quot" data-raw-source="http://www.fabrikam.com/files/setup.exe&amp;quot">http://www.fabrikam.com/files/setup.exe&quot</a>;</p></td>
</tr>
<tr class="odd">
<td><p><strong>DevModeMap</strong></p>
<p>Specifies the Devmode mapping file. This is an XML file that is used with PrintTicket to DEVMODE conversion in JavaScript code.</p></td>
<td><p>None.</p></td>
<td><p>DevModeMap=</p>
<p>fadmmap.xml</p></td>
</tr>
<tr class="even">
<td><p><strong>EventFile</strong></p>
<p>Specifies the Driver Event XML file.</p></td>
<td><p>None.</p></td>
<td><p>EventFile=</p>
<p>faevents.xml</p></td>
</tr>
<tr class="odd">
<td><p><strong>QueueProperties</strong></p>
<p>Specifies the format of a queue property bag. This is an XML file and must NOT be compiled.</p></td>
<td><p>None.</p></td>
<td><p>QueueProperties=</p>
<p>faQueueProps.xml</p></td>
</tr>
<tr class="even">
<td><p><strong>BidiUSBStatusInterface</strong></p>
<p>Specifies a list of hardware IDs that match one or more device interfaces to be used for USB Bidi communications.</p></td>
<td><p>None, but should only be supported if status is done over a USB interface that is not the print interface.</p></td>
<td><p>BidiUSBStatusInterface=</p>
<p>”USB\vid_1234&amp;pid_1234”,</p>
<p>”USB\vid_1234&amp;pid_4567”</p></td>
</tr>
<tr class="odd">
<td><p><strong>UserPropertyBagScope</strong></p>
<p>This directive specifies the scope of the user property bag as either Queue or Manufacturer.</p>
<p>If this directive is omitted, then Queue is the default value. Valid options for this directive are as follows:</p>
Queue:
This is the default configuration, and it matches the Windows 8 behavior.
Manufacturer:
All queues which use the same Manufacturer string in the INF use the same user property bag.</td>
<td><p>None.</p></td>
<td><p>UserPropertyBagScope=</p>
<p>Manufacturer</p></td>
</tr>
<tr class="even">
<td><p><strong>RetrievePrintDeviceCapabilitiesFromDevice</strong></p>
<p>v4 drivers may specify that they must retrieve a PrintDeviceCapabilities file from WS-Print v2.0 printers, as long as they set a PrintDeviceCapabilities file as the driver&#39;s DataFile and the DataFileType also indicates that the DataFile is of MIME type &quot;application/vnd.ms-PrintDeviceCapabilities+xml&quot;. Valid options:</p>
<p>Valid options:</p>
<p>True: Allows the driver&#39;s local DataFile to be replaced with the PrintDeviceCapabilities file from the device.</p>
<p>False: The driver&#39;s local DataFile will not be replaced with the PrintDeviceCapabilities file from the device.</p>
<p>If not specified, the default value of this directive is false.</p></td>
<td><p>None.</p></td>
<td><p>Example:</p>
<p>RetrievePrintDeviceCapabilitiesFromDevice=</p>
<p>true</p></td>
</tr>
</tbody>
</table>

 

## BidiFiles Section


The BidiFiles section is used to define Bidi extension files. It is identical to the Windows 7 format for TCP and WSD. The USB keywords are new.

The following table shows the directives that are used in the BidiFiles section.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Directive</th>
<th>Restrictions</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>BidiSPMFile</strong></p>
<p>This defines the Bidi extension file for a TCP/IP-based printer.</p></td>
<td><p>None.</p></td>
<td><p>BidiSPMFile=FaBidiSPM.xml</p></td>
</tr>
<tr class="even">
<td><p><strong>BidiWSDFile</strong></p>
<p>This defines the Bidi extension file for a WSD-based printer.</p></td>
<td><p>None.</p></td>
<td><p>BidiWSDFile=FABidiWSD.xml</p></td>
</tr>
<tr class="odd">
<td><p><strong>BidiUSBFile</strong></p>
<p>This defines the Bidi extension for USB.</p></td>
<td><p>None.</p></td>
<td><p>BidiUSBFile=FABidiUSB.xml</p></td>
</tr>
<tr class="even">
<td><p><strong>BidiUSBJSFile</strong></p>
<p>This defines the JavaScript extension for USB.</p></td>
<td><p>None.</p></td>
<td><p>BidiUSBJSFile=FABidiUSBJS.js</p></td>
</tr>
</tbody>
</table>

 

## DriverRender Section


The following table shows the directives that are used in the DriverRender section.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Directive</th>
<th>Restrictions</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>PageOutputQuality.[OptionName]</strong></p>
<p>Changes the image compression based on the value in the job PrintTicket for PageOutputQuality</p></td>
<td><p>OptionName must be a name specified in the standard PrintSchema namespace.</p></td>
<td><p>PageOutputQuality.Draft=</p>
<p>MxdcImageType.JPEGHigh</p>
<p>PageOutputQuality.Normal=</p>
<p>MxdcImageType.JPEGMedium</p>
<p>PageOutputQuality.High=</p>
<p>MxdcImageType.PNG</p></td>
</tr>
<tr class="even">
<td><p><strong>XpsFormat</strong></p>
<p>Changes the XPS format generated by the print system for this driver. Multiple values may be specified, and the order represents the driver&#39;s preference.</p></td>
<td><p>Not available for use in class drivers that use Unidrv/PScript rendering.</p></td>
<td><p>XpsFormat=XPS</p>
<p>XpsFormat=OpenXPS</p>
<p>XPSFormat=OpenXPS,XPS</p>
<p>XPSFormat=XPS,OpenXPS</p></td>
</tr>
<tr class="odd">
<td><p><strong>OutputFormat</strong></p>
<p>The OutputFormat directive describes a single PDL which is generated by this driver using a MIME type.</p>
<p>This information will be used during the CreateJob or CreateJob2 operation for WSD printers.</p></td>
<td><p>None.</p></td>
<td><p>Valid usage types include:</p>
<p>OutputFormat=</p>
<p>&quot;application/oxps&quot;</p>
<p>OutputFormat=</p>
<p>&quot;application/vnd.ms-xpsdocument&quot;</p>
<p>OutputFormat=</p>
<p>&quot;image/pwg-raster&quot;</p>
<p>OutputFormat=</p>
<p>&quot;application/vnd.ms-3mfdocument&quot;</p>
<p>Any other valid defined MIME type may also be specified here.</p></td>
</tr>
</tbody>
</table>

 

The MxdcImageType keyword for the PageOutputQuality directive has the following allowed values:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>MxdcImageType value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>MxdcImageType.JPEGHigh</strong></p>
<p>High compression JPEG (smaller files)</p></td>
</tr>
<tr class="even">
<td><p><strong>MxdcImageType.JPEGMedium</strong></p>
<p>Medium compression JPEG</p></td>
</tr>
<tr class="odd">
<td><p><strong>MxdcImageType.JPEGLow</strong></p>
<p>Low compression JPEG</p></td>
</tr>
<tr class="even">
<td><p><strong>MxdcImageType.PNG</strong></p>
<p>PNG file type (largest files)</p></td>
</tr>
</tbody>
</table>

 

## FileSave Section


This section supports the file-save scenario. When a v4 print driver is installed against the new PORTPROMPT port type, this section specifies the file extensions to be shown in the **Common File** window, and also specifies the localizable resource strings that support the extensions and the dialog box itself.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Directive</th>
<th>Restrictions</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>&lt;FileExtensionName&gt;</strong></p>
<p>This directive describes the FileExtension to be used when saving a file from this driver using the PORTPROMPT port. The value is a resourceID from the driver&#39;s ResourceFile. For XPS and OXPS only, a resourceID of 0 may be specified and the print spooler will use its internal resources for these.</p></td>
<td><p>None.</p></td>
<td><p>&lt;FileExtensionName&gt;=</p>
<p>&lt;resourceID&gt;</p>
<p>Xps=1234</p></td>
</tr>
<tr class="even">
<td><p><strong>SaveAsTitle</strong></p>
<p>This directive describes the title to be used on the Save File dialog. The value is a resourceID from the driver&#39;s ResourceFile.</p></td>
<td><p>None.</p></td>
<td><p>SaveAsTitle=</p>
<p>&lt;resourceID&gt;</p>
<p>SaveAsTitle=</p>
<p>4321</p></td>
</tr>
</tbody>
</table>

 

## PrinterExtensions Section


The PrinterExtensions section specifies a printer extension and the invocation modes it supports. For both of these entries, the app will automatically be registered with the print system. In addition, the app will be configured with two different parameters, the PrinterDriverID and the ReasonID, in that order. As a result, each entry must use a different PrinterExtensionID GUID.

The following table shows the directives that are used in the PrinterExtensions section.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Directive</th>
<th>Restrictions</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DriverEvent</strong></p>
<p>App servicing the DriverEvent mode.</p></td>
<td><p>None.</p></td>
<td><p>DriverEvent=</p>
<p>app.exe,{extensionID GUID}</p></td>
</tr>
<tr class="even">
<td><p><strong>PrintPreferences</strong></p>
<p>App servicing the PrintPreferences mode.</p></td>
<td><p>None.</p></td>
<td><p>PrintPreferences=</p>
<p>app.exe, {extensionID GUID}</p></td>
</tr>
</tbody>
</table>

 

The following is a sample of a v4 print driver manifest.

```INF
[DriverConfig]
DataFile=FAPDL.xml
RequiredFiles=UNIRES.DLL,STDNAMES.GPD,STDDTYPE.GDL,STDSCHEM.GDL,STDSCHMX.GDL,XPSSVCS.DLL,MSXPSINC.GPD,PWGRRenderFilter.DLL
ResourceFile=FARC.dll
PropertyBag=FAProperty.dpb
PrinterDriverID={GUID}
DriverCategory=PrintFax.Printer
ConstraintScript=faconst.js
EventFile=faevents.xml
PrinterExtensionUrl="http://www.fabrikam.com/download.asp?uiapp=120"
UserPropertyBagScope=Manufacturer
DataFileType="application/vnd.ms-PrintDeviceCapabilities+xml"
RetrievePrintDeviceCapabilitiesFromDevice=true

[BidiFiles]
BidiSPMFile=FABidiSPM.xml
BidiWSDFile=FABidiWSD.xml
BidiUSBFile=FaBidiUSB.xml
BidiUSBJSFile=FABidiUSBJS.js

[DriverRender]
PageOutputQuality.Draft=MxdcImageType.JPEGHigh
PageOutputQuality.Normal=MxdcImageType.JPEGMedium
PageOutputQuality.High=MxdcImageType.PNG
OutputFormat="image/pwg-raster"

[PrinterExtensions]
DriverEvent=FAapp.exe,{GUID}
PrintPreferences=FAapp.exe,{GUID2}
```

## Related topics
[Printer INF File Entries](printer-inf-file-entries.md)  



