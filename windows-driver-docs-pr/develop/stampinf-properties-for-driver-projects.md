---
ms.assetid: 18A9ACEF-51F8-4BC0-B305-F58287AD321C
title: Stampinf Properties for Driver Projects
description: Sets the properties for the Stampinf tool. You can use Stampinf to update common INF and INX file directives when you build the driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stampinf Properties for Driver Projects

Sets the properties for the [Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786) tool. You can use Stampinf to update common INF and INX file directives when you build the driver.

## <span id="Setting_Stampinf_properties_for_driver_projects"></span><span id="setting_stampinf_properties_for_driver_projects"></span><span id="SETTING_STAMPINF_PROPERTIES_FOR_DRIVER_PROJECTS"></span>Setting Stampinf properties for driver projects


1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **Stampinf**.
3.  Set the properties for the project.

If you want to add this property page to your project, so that you can run the Stampinf during the build process, see the [WDK and Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286) and the [Stampinf task](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Stampinf option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Enable_Architecture"></span><span id="enable_architecture"></span><span id="ENABLE_ARCHITECTURE"></span><strong>Enable Architecture</strong></p></td>
<td align="left"><p>Enables the replacement of the $ARCH$ variable used in INX files. If enabled, the value specified for <strong>Architecture</strong> is used. If <strong>No</strong> is specified, the $ARCH$ variable is removed. For example, &quot;Standard.NT$ARCH$&quot; becomes &quot;Standard.NT&quot;.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Architecture"></span><span id="architecture"></span><span id="ARCHITECTURE"></span><strong>Architecture</strong></p></td>
<td align="left"><p>Specifies the <em>architecture</em> string to replace the $ARCH$ variable that is used in INX files. The default value is $(InfArch), a macro that selects the current active configuration in Visual Studio. Possible values include <strong>x86</strong>, <strong>x64</strong>. This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-a [</strong><em>architecture</em><strong>]</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_VersionStamp"></span><span id="enable_versionstamp"></span><span id="ENABLE_VERSIONSTAMP"></span><strong>Enable VersionStamp</strong></p></td>
<td align="left"><p>Enables the version time stamp. If enabled, the <strong>Driver Version Number</strong> must not be empty. The <strong>Driver Version Number</strong> specifies the time that is written in the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394)"><strong>INF DriverVer directive</strong></a> for the version number. If not enabled, see the description of the default behavior for this option under <strong>Driver Version Number</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Driver_Version_Number"></span><span id="driver_version_number"></span><span id="DRIVER_VERSION_NUMBER"></span><strong>Driver Version Number</strong></p></td>
<td align="left"><p>Specifies the time that is written in the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394)"><strong>INF DriverVer directive</strong></a> for the version number. The format for the time is <em>hours.minutes.seconds.milliseconds</em> (for example, 11.30.20.15). This option is useful during development because it provides a convenient way to increase the version number of the driver. This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-v [</strong> <em>time</em> <strong>| <em>]</strong>.</p>
<p>To use the current time, specify an asterisk (</em>) with this parameter.</p>
<p><em>Default behavior:</em></p>
<p>If the <strong>Driver Version Number</strong> is not specified, or if <strong>Enable VersionStamp</strong> is <strong>No</strong> or unspecified, Stampinf uses one of the following version number values:</p>
<ul>
<li><p>If the STAMPINF_VERSION environment variable is set, Stampinf uses the version number value that is specified by this environment variable.</p></li>
<li><p>If the STAMPINF_VERSION environment variable is not specified, Stampinf extracts the version number from the ntverp.h file.</p></li>
</ul>
<div class="alert">
<strong>Note</strong>  By default, the STAMPINF_VERSION environment variable is not set when you build a driver unless you set it as a system environment variable. To specify this environment variable within the Visual Studio build environment, see <a href="https://msdn.microsoft.com/Library/Windows/Hardware/ms171459" data-raw-source="[How to: Use Environment Variables in a Build](https://msdn.microsoft.com/Library/Windows/Hardware/ms171459)">How to: Use Environment Variables in a Build</a>.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_DateStamp"></span><span id="enable_datestamp"></span><span id="ENABLE_DATESTAMP"></span><strong>Enable DateStamp</strong></p></td>
<td align="left"><p>Enables the date stamp. If enabled, the <strong>Driver Version Directive Date</strong> must not be empty. If not enabled, see the description of the default behavior for this option under <strong>Driver Version Directive Date</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Driver_Version_Directive_Date"></span><span id="driver_version_directive_date"></span><span id="DRIVER_VERSION_DIRECTIVE_DATE"></span><strong>Driver Version Directive Date</strong></p></td>
<td align="left"><p>Specifies the date that is written in the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394)"><strong>INF DriverVer directive</strong></a>. The format for the date is <em>month</em>/<em>date</em>/<em>year</em> (for example, <strong>10/20/2011</strong>).</p>
<p>To use the current date, specify an asterisk (<strong><em></strong>) with this parameter.</p>
<p><em>Default behavior:</em></p>
<p>If the <strong>Driver Version Directive Date</strong> parameter is not specified, or if <strong>Enable DateStamp</strong> is <strong>No</strong> or unspecified, Stampinf uses one of the following date values:</p>
<ul>
<li><p>If the STAMPINF_DATE environment variable is set, Stampinf uses the date value that is specified by this environment variable.</p></li>
<li><p>If the STAMPINF_DATE environment variable is not specified, Stampinf uses the current date.</p></li>
</ul>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-d [</strong><em>date</em><strong>|</em>]</strong>.</p>
<div class="alert">
<strong>Note</strong>  By default, the STAMPINF_DATE environment variable is not set when you build a driver unless you set it as a system environment variable. To specify this environment variable within the Visual Studio build environment, see <a href="https://msdn.microsoft.com/Library/Windows/Hardware/ms171459" data-raw-source="[How to: Use Environment Variables in a Build](https://msdn.microsoft.com/Library/Windows/Hardware/ms171459)">How to: Use Environment Variables in a Build</a>.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Driver_Version_Directive_Section"></span><span id="driver_version_directive_section"></span><span id="DRIVER_VERSION_DIRECTIVE_SECTION"></span><strong>Driver Version Directive Section</strong></p></td>
<td align="left"><p>Specifies the INF section in which to put the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394)"><strong>INF DriverVer directive</strong></a>. The default location for this directive is the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff547502" data-raw-source="[&lt;strong&gt;INF Version section&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547502)"><strong>INF Version section</strong></a>.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-s</strong> <em>section</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="KMDF_Version_Number"></span><span id="kmdf_version_number"></span><span id="KMDF_VERSION_NUMBER"></span><strong>KMDF Version Number</strong></p></td>
<td align="left"><p>Specifies the version of KMDF that this driver depends on. This is used to customize the KmdfLibraryVersion and KMDF co-installer name in the INF file. This option replaces the $KMDFVERSION$ and $KMDFCOINSTALLERVERSION$ keywords in the INF file. The string has the following format:</p>
<p><em>&lt;major_version&gt;</em>.<em>&lt;minor_version&gt;</em></p>
<p>For example, if you specify 1.5 as the version string, the values 1.5 and 01005 are used for the two keywords (respectively).</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-k</strong> <em>KMDFversion</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="UMDF_Version_Number"></span><span id="umdf_version_number"></span><span id="UMDF_VERSION_NUMBER"></span><strong>UMDF Version Number</strong></p></td>
<td align="left"><p>Specifies the <em>version</em> of UMDF that this driver depends on. This option is used to specify the UmdfLibraryVersion and UMDF co-installer name in the INF file. The <em>version</em> that is specified replaces the $UMDFVERSION$ and $UMDFCOINSTALLERVERSION$ keywords in the INF file. The <em>version</em> string has the following format:</p>
<p><em>&lt;major_version&gt;</em>.<em>&lt;minor_version&gt;</em>.<em>&lt;service_version&gt;</em></p>
<p>(where <em>&lt;service_version&gt;</em> is typically zero).</p>
<p>For example, if you specify 1.5.0 as the version string, the values 1.5.0 and 01005 are used for the major and minor keywords (respectively).</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-u</strong> <em>UMDFversion</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Catalog_File_Name"></span><span id="catalog_file_name"></span><span id="CATALOG_FILE_NAME"></span><strong>Catalog File Name</strong></p></td>
<td align="left"><p>Specifies the value that is written in the <strong>CatalogFile</strong> directive in the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff547502" data-raw-source="[&lt;strong&gt;INF Version section&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547502)"><strong>INF Version section</strong></a>. By default, the <strong>CatalogFile</strong> directive is not written.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-c</strong> <em>catalogfile</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span><strong>Verbose</strong></p></td>
<td align="left"><p>Shows verbose Stampinf output.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-n</strong> .</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Version_Header_Path"></span><span id="version_header_path"></span><span id="VERSION_HEADER_PATH"></span><strong>Version Header Path</strong></p></td>
<td align="left"><p>Specifies the location of Ntverp.h file. The path represent the fully qualified location of the directory containing Ntverp.h.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786" data-raw-source="[Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)">Stampinf</a> option <strong>-i</strong> <em>path</em>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [Stampinf](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786)
* [**INF DriverVer directive**](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547394)
* [**INF Version section**](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547502)
* [WDK and Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286)
* [Stampinf task](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552786_task)
* [How to: Use Environment Variables in a Build](https://msdn.microsoft.com/Library/Windows/Hardware/ms171459)
 

 






