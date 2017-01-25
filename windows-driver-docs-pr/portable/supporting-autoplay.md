---
Description: Supporting AutoPlay
MS-HAID: 'wpddk.supporting\_autoplay'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting AutoPlay
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Supporting%20AutoPlay%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



