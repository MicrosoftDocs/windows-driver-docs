---
Description: The MTP Setup Information (.inf) File
title: The MTP Setup Information (.inf) File
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The MTP Setup Information (.inf) File


Microsoft provides a set of class drivers to support the Media Transfer Protocol (MTP). If your device supports MTP, you can use one of these drivers. In addition to the class drivers, Microsoft provides a setup information (.inf) file to install a class driver. This file is named *WpdMtp.inf*.

If your MTP device has unique requirements, create a new setup information (.inf) file that is based on the original version of *WpdMtp.inf*. (You cannot modify *WpdMtp.inf* directly.)

The following table describes specific Needs directives that are found in *WpdMtp.inf* and possible modifications that you can make to the sections that are identified by a given directive.

The entries in the following table can support any of three transports (USB, IP, or Bluetooth). Be aware that each transport requires a unique installation section. Also be aware that the Bluetooth transport is only supported in Windows 7.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Needs directive</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Needs = WPD.MTP, WINUSB.NT</td>
<td align="left">The WPD.MTP section identifies the driver files that will be copied and registered. The following applies to Windows Vista and Windows Media Player 11.
<pre space="preserve"><code>;;[DDInstall]
;;Include = wpdmtp.inf
;;Needs = WPD.MTP</code></pre>
<p>Starting with Windows 7, <em>WinUsb.sys</em> replaces <em>WpdUsb.sys</em> as the lower filter driver for MTP devices that connect to the computer by using USB. The following directive is required for a vendor’s INF to include <em>WinUsb.inf</em> and a specific WinUSB section:</p>
<pre space="preserve"><code>;;[DDInstall]
;;Include = wpdmtp.inf, WINUSB.INF
;;Needs = WPD.MTP, WINUSB.NT</code></pre></td>
</tr>
<tr class="even">
<td align="left">Needs = WPD.MTP.Registration</td>
<td align="left">The WPD.MTP.Registration section accomplishes four tasks:
<ol>
<li>Registers the kernel-mode driver (including <em>WPDUSB.sys</em> as the lower filter driver if you are installing the device on Windows Vista or Windows XP).</li>
<li>Enables default MTP AutoPlay support.</li>
<li>Enables legacy application compatibility support (the default value 0xFFFFFFFF allows the WPD class installer to query the device&#39;s capabilities).</li>
<li>Sets the transport driver&#39;s class identifier.</li>
</ol>
<pre space="preserve"><code>;;[DDInstall.hw]
;;Include = wpdmtp.inf
;;Needs = WPD.MTP.Registration</code></pre></td>
</tr>
<tr class="odd">
<td align="left">Needs = WPD.MTP.Registration.Basic</td>
<td align="left">The WPD.MTP.Registration.Basic section lets you customize tasks 2 and 3 in the previous list. For example, you can set the application compatibility to support Windows Image Acquisition (WIA) by using a value of 0x01 or Windows Media Device Manager (WMDM) by using a value of 0x02.
<pre space="preserve"><code>;;[DDInstall.hw]
;;Include = wpdmtp.inf
;;Needs = WPD.MTP.Registration.Basic</code></pre></td>
</tr>
<tr class="even">
<td align="left">Needs = WPD.MTP.Services</td>
<td align="left">The WPD.MTP.Services section adds driver services (and default service parameters). This includes WUDF and <em>WPDUSB.sys</em> (for Windows Vista and Windows XP only).
<pre space="preserve"><code>;;[DDInstall.Services]
;;Include = wpdmtp.inf
;;Needs = WPD.MTP.Services</code></pre></td>
</tr>
<tr class="odd">
<td align="left">Needs = WPD.MTP.CoInstallers</td>
<td align="left">The WPD.MTP.CoInstallers section identifies the co-installer. (To install an MTP device, a Windows user-mode driver framework (UMDF) co-installer is used.)
<p>This section is required for Windows 7, Windows Vista, and Windows Media Player 11. (It was not required for an MTP driver that supported Windows Media Player 10.)</p>
<pre space="preserve"><code>;;[DDInstall.CoInstallers]
;;Include = wpdmtp.inf
;;Needs = WPD.MTP.CoInstallers</code></pre></td>
</tr>
<tr class="even">
<td align="left">Needs = WPD.MTP.Wdf</td>
<td align="left">The WPD.MTP.Wdf section identifies the Windows user-mode driver framework (UMDF) service and its binary (<em>WPDMTPDR.dll</em>).
<p>This section is required for Windows 7, Windows Vista, and Windows Media Player 11. (It was not required for an MTP driver that supported Windows Media Player 10.)</p>
<pre space="preserve"><code>;;[DDInstall.CoInstallers]
;;Include = wpdmtp.inf
;;Needs = WPD.MTP.Wdf</code></pre></td>
</tr>
</tbody>
</table>

 

 

 




