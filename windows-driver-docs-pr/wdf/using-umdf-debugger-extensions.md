---
title: Summary of Debugger Extensions in Wudfext.dll
description: The Windows Driver Kit (WDK) includes a debugger extension library, named WudfExt.dll, which is located in the DDKROOT \\bin subdirectory.
ms.assetid: af84ed3a-33a1-4736-9080-c43e87052064
keywords: ["UMDF debugger extensions WDK", "debugger extensions WDK UMDF", "extensions WDK debuggers"]
---

# Summary of Debugger Extensions in Wudfext.dll


\[This topic applies to UMDF 1.*x*.\]

The Windows Driver Kit (WDK) includes a debugger extension library, named *WudfExt.dll*, which is located in the %DDKROOT%\\bin subdirectory. This topic describes the debugger extension commands in *WudfExt.dll*, which you can use to debug User-Mode Driver Framework (UMDF) version 1.*x* drivers.

To debug UMDF drivers starting in UMDF version 2.0, you must instead use the *Wdfkd.dll* debugger extension library. For more info, see [**Windows Driver Framework Extensions (Wdfkd.dll)**](https://msdn.microsoft.com/library/windows/hardware/ff551876).

For a complete description of each command in *WudfExt.dll*, see [User-Mode Driver Framework Extensions (Wudfext.dll)](https://msdn.microsoft.com/library/windows/hardware/ff560030). For more information about all available debugger extension libraries, see the documentation that is supplied with the [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) package.

To load the *WudfExt.dll* debugger extension library, enter the following command at the debugger's command prompt:

**!load WudfExt.dll**

The following table summarizes the extension commands that the WudfExt.dll extension library provides.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Extension</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>!help</strong></p></td>
<td align="left"><p>Shows all debugger extensions that WudfExt.dll supports</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!umdevstacks</strong></p></td>
<td align="left"><p>Shows all the device stacks in the host process</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!umdevstack</strong></p></td>
<td align="left"><p>Shows information about a device stack in the host process</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!umirps</strong></p></td>
<td align="left"><p>Shows the list of pending I/O request packets in the host process</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!umirp</strong></p></td>
<td align="left"><p>Shows information about a user-mode I/O request packet</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudfdriverinfo</strong></p></td>
<td align="left"><p>Shows information about a UMDF driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!wudfdevicequeues</strong></p></td>
<td align="left"><p>Shows all the I/O queues for a device</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudfqueue</strong></p></td>
<td align="left"><p>Shows information about an I/O queue</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!wudfrequest</strong></p></td>
<td align="left"><p>Shows information about an I/O request</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudfobject</strong></p></td>
<td align="left"><p>Shows information about a WDF object as well as its parent and child relationships</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!wudfdevice</strong></p></td>
<td align="left"><p>Shows Plug and Play (PnP) and power-management state systems for a device</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudfdumpobjects</strong></p></td>
<td align="left"><p>Shows the list of outstanding WDF objects; used to determine any leaked objects when the driver unloads</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!wudfiotarget</strong></p></td>
<td align="left"><p>Shows information about an I/O target, including its state and list of sent requests</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudffile</strong></p></td>
<td align="left"><p>Shows information about a framework file</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!umfile</strong></p></td>
<td align="left"><p>Shows information about a UMDF [intra-stack file](creating-a-file-object-to-handle-i-o.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudffilehandletarget</strong></p></td>
<td align="left"><p>Shows information about a file-handle-based I/O target</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!wudfusbtarget</strong></p></td>
<td align="left"><p>Shows information about a USB I/O target</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudfusbinterface</strong></p></td>
<td align="left"><p>Shows information about a USB interface object</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>!wudfusbpipe</strong></p></td>
<td align="left"><p>Shows information about a USB pipe object</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>!wudfrefhist</strong></p></td>
<td align="left"><p>Shows reference count history for a framework object</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Summary%20of%20Debugger%20Extensions%20in%20Wudfext.dll%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




