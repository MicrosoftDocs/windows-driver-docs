---
title: Storage Kernel Debugger Extensions
description: The storage kernel debugger extensions (storagekd) are used for debugging the storage drivers on Windows 8 and above operating system (OS) targets.
ms.assetid: 8EF83BC8-6ABB-496C-98A6-EF0298D78F76
---

# Storage Kernel Debugger Extensions


The storage kernel debugger extensions (storagekd) are used for debugging the storage drivers on Windows 8 and above operating system (OS) targets.

Extension commands that are useful for debugging storage drivers, via classpnp managed storage class drivers and Storport managed storage miniport drivers, can be found in **Storagekd.dll**.

Please refer to [SCSI Miniport Extensions (Scsikd.dll and Minipkd.dll)](scsi-miniport-extensions--scsikd-dll-and-minipkd-dll-.md) for debugging needs for Windows 7 and below version of OS targets.

**Important**  You need special symbols to use this extension. For more information, see [Debugging Tools for Windows](index.md).

 

## <span id="Storage_kernel_debugger_extension_commands"></span><span id="storage_kernel_debugger_extension_commands"></span><span id="STORAGE_KERNEL_DEBUGGER_EXTENSION_COMMANDS"></span>Storage kernel debugger extension commands


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storhelp"></span><span id="_STORAGEKD.STORHELP"></span><strong>[!storagekd.storhelp](-storagekd-storhelp.md)</strong></p></td>
<td align="left"><p>Displays help text for <strong>Storagekd.dll</strong> extension commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storclass"></span><span id="_STORAGEKD.STORCLASS"></span><strong>[!storagekd.storclass](-storagekd-storclass.md)</strong></p></td>
<td align="left"><p>Displays information about the specified <em>classpnp</em> device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storadapter"></span><span id="_STORAGEKD.STORADAPTER"></span><strong>[!storagekd.storadapter](-storagekd-storadapter.md)</strong></p></td>
<td align="left"><p>Displays information about the specified <em>Storport</em> adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storunit"></span><span id="_STORAGEKD.STORUNIT"></span><strong>[!storagekd.storunit](-storagekd-storunit.md)</strong></p></td>
<td align="left"><p>Displays information about the specified <em>Storport</em> logical unit.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storloglist"></span><span id="_STORAGEKD.STORLOGLIST"></span><strong>[!storagekd.storloglist](-storagekd-storloglist.md)</strong></p></td>
<td align="left"><p>Displays the <em>Storport</em> adapter’s internal log entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storlogirp"></span><span id="_STORAGEKD.STORLOGIRP"></span><strong>[!storagekd.storlogirp](-storagekd-storlogirp.md)</strong></p></td>
<td align="left"><p>Displays the <em>Storport’s</em> internal log entries for the adapter filtered for the IRP provided.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="_storagekd.storlogsrb"></span><span id="_STORAGEKD.STORLOGSRB"></span><strong>[!storagekd.storlogsrb](-storagekd-storlogsrb.md)</strong></p></td>
<td align="left"><p>Displays the <em>Storport’s</em> internal log entries for the adapter filtered for the Storage (or SCSI) Request Block (SRB) provided.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_storagekd.storsrb"></span><span id="_STORAGEKD.STORSRB"></span><strong>[!storagekd.storsrb](-storagekd-storsrb.md)</strong></p></td>
<td align="left"><p>Displays information about the specified Storage (or SCSI) Request Block (SRB).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Storage%20Kernel%20Debugger%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




