---
Description: 'The Sample Driver Setup Information (.inf) File'
MS-HAID: 'wpddk.the\_sample\_driver\_setup\_information\_\_\_inf\_\_file'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'The Sample Driver Setup Information (.inf) File'
---

# The Sample Driver Setup Information (.inf) File


The WpdHelloWorldDriver project contains a setup information (.inf) file named *WpdHelloWorldDriver.inf*. This file contains the UMDF parameters and directives that are required by the WUDF co-installer. However, this file also contains parameters and directives that are exclusive to WPD. The following table lists these WPD-specific parameters, directives, and sections.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Section</th>
<th align="left">Directive or parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Basic_Install.CoInstaller_AddReg</td>
<td align="left"></td>
<td align="left">This section is required.
<ul>
<li><em>WudfCoInstaller.dll</em> must be listed as a co-installer.</li>
<li>The reg root must be &quot;HKR&quot;.</li>
<li>The type must be 0x10000.</li>
<li>The registry directive must be present.</li>
</ul>
<p>Example: <code>[Basic_Install.CoInstallers_AddReg]</code></p>
<p><code>HKR,,CoInstallers32,0x00010000,&quot;WUDFCoInstaller.dll&quot;</code></p></td>
</tr>
<tr class="even">
<td align="left">Basic_Install.wdf</td>
<td align="left">UmdfService directive</td>
<td align="left">This directive is required.
<ul>
<li>This directive is of the form: &quot;UmdfService=ServiceName, ServiceInstallSection&quot;.</li>
<li>The referenced section (&quot;ServiceInstallSection&quot;) must exist.</li>
<li>The specified service name (&quot;ServiceName&quot;) must be used by the UmdfServiceOrder directive.</li>
</ul>
<p>Example: <code>[Basic_Install.Wdf]</code></p>
<p><code>UmdfService=WpdHelloWorldDriver, WpdHelloWorldDriver_Install</code></p>
<p><code>UmdfServiceOrder=WpdHelloWorldDriver</code></p></td>
</tr>
<tr class="odd">
<td align="left">DDInstall.Services</td>
<td align="left">Includes directive</td>
<td align="left">This directive is required if the driver reuses the MTP class driver components. Otherwise, it should not appear.
<p>The necessary system files must be referenced by using the appropriate Includes or Needs directives. (These files are WpdMtpDr.dll, <em>WpdMtp.dll</em>, <em>WpdMtpUs.dll</em>, <em>WpdConns.dll,</em> and <em>WpdUsb.sys</em>). The necessary service files must also be referenced. (The single service file that requires reference is <em>WpdUsb.sys</em> (for Windows Vista) or <em>WinUSB.sys</em> (for Windows 7).)</p></td>
</tr>
<tr class="even">
<td align="left">DDInstall.Services</td>
<td align="left">Needs directive</td>
<td align="left">This directive is required if the driver reuses the MTP class driver components. Otherwise, it should not appear.
<p>The necessary system files must be referenced by using the appropriate Includes or Needs directives. (These files are: <em>WpdMtpDr.dll</em>, <em>WpdMtp.dll,WpdMtpUs.dll</em>, <em>WpdConns.dll</em>, and <em>WpdUsb.sys</em>). The necessary service files must also be referenced. (The single service file that requires reference is <em>WpdUsb.sys</em> (for Windows Vista) or <em>WinUSB.sys</em> (for Windows 7).)</p></td>
</tr>
<tr class="odd">
<td align="left">Device_AddReg</td>
<td align="left">EnableDefaultAutoPlaySupport directive</td>
<td align="left">This directive is required.
<ul>
<li>The reg root must be &quot;HKR&quot;.</li>
<li>The type must be 0x10001.</li>
<li>A valid value (0 or 1) must be set.</li>
</ul>
<p>Example:</p>
<p><code>[Device_AddReg]</code></p>
<p><code>HKR,,&quot;EnableDefaultAutoPlaySupport&quot;,0x10001,1</code></p></td>
</tr>
<tr class="even">
<td align="left">Device_AddReg</td>
<td align="left">EnableLegacySupport directive</td>
<td align="left">This directive is required.
<ul>
<li>The reg root must be &quot;HKR&quot;.</li>
<li>The type must be 0x10001.</li>
<li>A valid value (0, 1, 2, or 3) must be set.</li>
</ul>
<p>Example:</p>
<p><code>[Device_AddReg]</code></p>
<p><code>HKR,,&quot;EnableLegacySupport&quot;,0x10001,1</code></p></td>
</tr>
<tr class="odd">
<td align="left">Device_AddReg</td>
<td align="left">UseWiaAutoPlay directive</td>
<td align="left">This directive is optional.
<ul>
<li>The reg root must be &quot;HKR&quot;.</li>
<li>The type must be 0x10001.</li>
<li>A valid value (0 or 1) must be set.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left">Install</td>
<td align="left">UmdfLibraryVersion directive</td>
<td align="left">This directive is required.
<p>This directive must be of the form: n.n.n</p>
<p>Example: <code>[WpdHelloWorldDriver_Install]</code></p>
<p><code>UmdfLibraryVersion=1.0.0</code></p></td>
</tr>
<tr class="odd">
<td align="left">ServiceInstall</td>
<td align="left">ErrorControl directive</td>
<td align="left">This directive is required.
<p>This directive must specify a value of 1.</p>
<p>Example: <code>[WUDFRD_ServiceInstall]</code></p>
<p><code>ErrorControl=1</code></p></td>
</tr>
<tr class="even">
<td align="left">ServiceInstall</td>
<td align="left">ServiceType directive</td>
<td align="left">This directive is required.
<p>This directive must specify a value of 1.</p>
<p>Example:</p>
<p><code>[WUDFRD_ServiceInstall]</code></p>
<p><code>ServiceType=1</code></p></td>
</tr>
<tr class="odd">
<td align="left">ServiceInstall</td>
<td align="left">StartType directive</td>
<td align="left">This directive is required.
<p>This directive must specify a value of 3.</p>
<p>Example:</p>
<p><code>[WUDFRD_ServiceInstall]</code></p>
<p><code>StartType=3</code></p></td>
</tr>
<tr class="even">
<td align="left">Version</td>
<td align="left">Class parameter</td>
<td align="left">This parameter is required. Must be set to &quot;WPD&quot;.
<p>Example:</p>
<pre space="preserve"><code>[Version]
Class=WPD</code></pre></td>
</tr>
<tr class="odd">
<td align="left">Version</td>
<td align="left">ClassGuid parameter</td>
<td align="left">This parameter is required. Must be set to a valid GUID.
<p>Example:</p>
<pre space="preserve"><code>[Version]
ClassGuid={EEC5AD98-8080-425f-922A-DABF3DE3F69A}</code></pre></td>
</tr>
<tr class="even">
<td align="left">WpdHelloWorldDriver_Install</td>
<td align="left">DriverCLSID directive</td>
<td align="left">This directive is required.
<p>This directive must specify a well-formed GUID.</p>
<p>Example:</p>
<pre space="preserve"><code>[WpdHelloWorldDriver_Install]
DriverCLSID=&quot;{EC7445EE-BC00-4CED-AFE7-A52849F10239}&quot;</code></pre></td>
</tr>
<tr class="odd">
<td align="left">WpdHelloWorldDriver_Install</td>
<td align="left">ServiceBinary directive</td>
<td align="left">This directive is required.
<p>This directive must specify a path of the form: &quot;%12%\wudfrd.sys&quot;</p>
<p>Example:</p>
<p><code>[WUDFRD_ServiceInstall]</code></p>
<p><code>ServiceBinary=%12%\WUDFRd.sys</code></p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20Sample%20Driver%20Setup%20Information%20%28.inf%29%20File%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



