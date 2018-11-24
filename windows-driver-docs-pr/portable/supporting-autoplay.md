---
Description: Supporting AutoPlay
title: Supporting AutoPlay
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting AutoPlay


AutoPlay is a feature of the Shell that detects content on portable devices. Depending on the current AutoPlay settings, this feature will perform one of several actions, such as presenting a list of available handler applications, displaying a standard folder view of files, and so on.

In Windows Vista, the AutoPlay feature was extended so that a WPD device can provide a list of content types that it supports. Similarly, WPD applications can register content types that they support. (For more information about registering an application, see the WPD SDK.)

## <span id="The_WPD_AutoPlay_Scheme"></span><span id="the_wpd_autoplay_scheme"></span><span id="THE_WPD_AUTOPLAY_SCHEME"></span>The WPD AutoPlay Scheme


The WPD AutoPlay scheme integrates with the Windows Vista AutoPlay feature. It does so by supporting three AutoPlay categories, which are described in the following table.

| Category | Description                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------|
| Source   | A WPD device can be treated as a source of content, that is, the content can be transferred from the device.        |
| Sink     | A WPD device can be treated as a destination for content, that is, the content can be transferred to the device.    |
| Function | A WPD device supports a programmable or controllable capability, for example, it can send and receive SMS messages. |

 

Devices that support these categories should set the appropriate entries in the Device\_AddReg section of the setup information (.inf) file. The following table lists the two AutoPlay directives that are supported by the WPD Class Installer.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Section</th>
<th align="left">Directive or Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Device_AddReg</td>
<td align="left">AutoPlaySourceOnly</td>
<td align="left">This directive is required for devices that act only as an AutoPlay source.
<ul>
<li>The reg root must be &quot;HKR&quot;.</li>
<li>The type must be 0x10001.</li>
<li>A value of 1 must be set.</li>
</ul>
<p>Example:</p>
<p><code>[Device_AddReg]</code></p>
<p><code>HKR,,&quot;AutoPlaySourceOnly&quot;,0x10001,1</code></p></td>
</tr>
<tr class="even">
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
</tbody>
</table>

 

Most devices will specify the EnableDefaultAutoPlaySupport directive in their setup information files. The AutoPlaySourceOnly directive is provided only for legacy devices that do not support bi-directional transfers.

If you do not want your device to participate in AutoPlay, either set the EnableAutoPlaySupport directive to 0 or omit this directive from your driver's setup information (.inf) file. If you explicitly need to disable any AutoPlay functionality for a given WPD device, you can do so by creating a false DeviceHandlers value in the Device\_Parameters section of the .inf file.

If you need to create a custom AutoPlay scheme, you can do so by creating a private DeviceHandlers value in the Device\_Parameters section of the setup information (.inf) file.

 

 




