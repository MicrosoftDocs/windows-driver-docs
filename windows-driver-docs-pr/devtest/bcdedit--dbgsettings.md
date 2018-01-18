---
title: BCDEdit /dbgsettings
description: The /dbgsettings option sets or displays the current global debugger settings for the computer.
ms.assetid: df2fe55c-2752-4e0c-a4c0-004235b85e22
keywords: ["BCDEdit /dbgsettings Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /dbgsettings
api_type:
- NA
---

# BCDEdit /dbgsettings


The **/dbgsettings** option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the [**BCDEdit /debug**](bcdedit--debug.md) option.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

 

``` syntax
bcdedit /dbgsettings SERIAL [DEBUGPORT:port] [BAUDRATE:baud] [/start startpolicy] [/noumex] 

bcdedit /dbgsettings 1394 [CHANNEL:channel] [/start startpolicy] [/noumex] 

bcdedit /dbgsettings USB [TARGETNAME:targetname] [/start startpolicy] [/noumex] 

bcdedit /dbgsettings NET HOSTIP:ip PORT:port [KEY:key] [nodhcp] [newkey] [/start startpolicy] [/noumex] 
```

Parameters
----------

<a href="" id="-------serial------"></a> **SERIAL**   
Specifies that the target machine and the host machine will use a serial connection for debugging. When this option is used, the **DEBUGPORT** and **BAUDRATE** parameters can be included as well. For more information, see [Setting Up Kernel-Mode Debugging over a Serial Cable Manually](https://msdn.microsoft.com/library/windows/hardware/ff556867).

<a href="" id="-------1394------"></a> **1394**   
Specifies that the target machine and the host machine will use an IEEE 1394 (FireWire) connection for debugging. When this option is used, the **CHANNEL** parameter can be included as well. For more information, see [Setting Up Kernel-Mode Debugging over a 1394 Cable Manually](https://msdn.microsoft.com/library/windows/hardware/ff556866).

<a href="" id="-------usb------"></a> **USB**   
Specifies that the target machine and the host machine will use a USB 2.0 or USB 3.0 connection for debugging. When this option is used, the **TARGETNAME** parameter must be included as well. For more information, see:

-   [Setting Up Kernel-Mode Debugging over a USB 3.0 Cable Manually](https://msdn.microsoft.com/library/windows/hardware/hh439372)
-   [Setting Up Kernel-Mode Debugging over a USB 2.0 Cable Manually](https://msdn.microsoft.com/library/windows/hardware/ff556869)

<a href="" id="-------net------"></a> **NET**   
Specifies that the target machine and the host machine will use an Ethernet network connection for debugging. When this option is used, the **HOSTIP** and **PORT** parameters must be included as well. The target computer must have a network adapter that is supported by Debugging Tools for Windows. For more information, see:

-   [Setting Up Kernel-Mode Debugging over a Network Cable Manually](https://msdn.microsoft.com/library/windows/hardware/hh439346)
-   [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](https://msdn.microsoft.com/library/windows/hardware/dn337010)
-   [Supported Ethernet NICs for Network Kernel Debugging in Windows 8](https://msdn.microsoft.com/library/windows/hardware/dn337009)

<a href="" id="-------local------"></a> **LOCAL**   
The **LOCAL** option sets the global debugging option to local debugging. This is kernel-mode debugging on a single computer. In other words, the debugger runs on the same computer that is being debugged. With local debugging you can examine state, but not break into kernel mode processes that would cause the OS to stop running.

For information on setting up local kernel mode debugging manually, see [Setting Up Local Kernel Debugging of a Single Computer Manually](https://msdn.microsoft.com/library/windows/hardware/dn553412).

The LOCAL option is available in Windows 8.0 and Windows Server 2012 and later.

<a href="" id="-------baudrate-baud------"></a> **BAUDRATE:***baud*   
(Only used when the connection type is **SERIAL**.) Specifies the baud rate to use. This parameter is optional. Valid values for *baud* are 9600, 19200, 38400, 57600, and 115200. The default baud rate is 115200 bps.

> [!NOTE]
> If the Windows Special Administration Console (SAC) application is running on a target machine that is configured for kernel mode debug through a serial port, the SAC application may cause the debugger connection to drop. This event occurs because the COM port baud value changes after the debugger connection is established. Either close the SAC application before running the debugger or change the debugger COM port baud value to 9600.

 

<a href="" id="-------channel-channel------"></a> **CHANNEL:***channel*   
(Only used when the connection type is **1394**.) Specifies the 1394 channel to use. The value for *channel* must be a decimal integer between 0 and 62, inclusive, and must match the channel number used by the host computer. The channel specified in this parameter does not depend on the physical 1394 port chosen on the adapter. The default value for *channel* is 0.

<a href="" id="-------debugport-port------"></a> **DEBUGPORT:***port*   
(Only used when the connection type is **SERIAL**.) Specifies the serial port to use as the debugging port. This is an optional setting. The default port is **1** (COM 1).

<a href="" id="-------hostip-ip------"></a> **HOSTIP:***ip*   
(Only used when the connection type is **NET**.) For network debugging, specifies the IPv4 address of the host debugger.

<a href="" id="-------key-key------"></a> **KEY:***key*   
For network debugging, specifies the key with which to encrypt the connection. \[0-9\] and \[a-z\] allowed only. Do not specify this parameter if you have specified the **newkey** parameter.

<a href="" id="-------newkey------"></a> **newkey**   
For network debugging specifies that a new encryption key should be generated for the connection. Do not specify this parameter if you have specified a **KEY** parameter.

<a href="" id="-------nodhcp----------------"></a> **nodhcp**   
For network debugging prevents use of DHCP to obtain the target IP address.

<a href="" id="-------port-port------"></a> **PORT:***port*   
For network debugging, specifies the port to communicate with on the host debugger. Should be 49152 or higher.

<a href="" id="-------targetname-targetname------"></a> **TARGETNAME:***targetname*   
(Only used when the connection type is **USB**.) Specifies a string value to use for the target name. This string can be any value.

<a href="" id="--------start--------startpolicy------"></a> **/start** *startpolicy*   
This option specifies the debugger start policy. The following table shows the options for the *startpolicy*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ACTIVE</strong></p></td>
<td align="left"><p>Specifies that the kernel debugger is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>AUTOENABLE</strong></p></td>
<td align="left"><p>Specifies that the kernel debugger is enabled automatically when an exception or other critical event occurs. Until then, the debugger is active but is disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>DISABLE</strong></p></td>
<td align="left"><p>Specifies that the kernel debugger is enabled when you type <strong>kdbgctrl</strong> to clear the enable block. Until then, the debugger is active but is disabled.</p></td>
</tr>
</tbody>
</table>

 

If a start policy is not specified, ACTIVE is the default.

<a href="" id="--------noumex------"></a> **/noumex**   
Specifies that the kernel debugger ignores user-mode exceptions. By default, the kernel debugger breaks for certain user-mode exceptions, such as STATUS\_BREAKPOINT and STATUS\_SINGLE\_STEP. The **/noumex** parameter is effective only when there is no user-mode debugger attached to the process.

### Comments

The **/dbgsettings** option configures the global debugging settings, but does not enable debugging. You must use the **/debug** option to enable debugging for a specific boot entry. If there are no debugging settings specified for a particular boot entry, the global debug settings are used. To override the global settings, you must use the [**BCDEdit /set**](bcdedit--set.md) command and specify the ID of the boot entry along with the debug parameter and value pair.

The default values for the global settings are serial communications using COM1, at a baud rate of 115,200.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">/dbgsetting parameter</th>
<th align="left">Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Connection type</p></td>
<td align="left"><p>Serial</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>DEBUGPORT:</strong><em>port</em></p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>BAUDRATE:</strong><em>rate</em></p></td>
<td align="left"><p>115200</p></td>
</tr>
</tbody>
</table>

 

For information about Windows debugging tools, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063). For information about setting up and configuring a kernel-mode debugging session, see [Setting Up Kernel-Mode Debugging Manually](https://msdn.microsoft.com/library/windows/hardware/hh439378).

Examples
--------

The following command configures the target computer to use an Ethernet connection for debugging and specifies the IP address of the host computer. The command also specifies a port number that the host computer can use to connect to the target computer. For more information, see [Setting Up Kernel-Mode Debugging over a Network Cable Manually](https://msdn.microsoft.com/library/windows/hardware/hh439346).

``` syntax
bcdedit /dbgsettings net hostip:10.125.5.10 port:50000
```

The following command configures the target computer to use a 1394 connection for debugging. The command also specifies a channel number that the host computer can use to connect to the target computer. For more information, see [Setting Up Kernel-Mode Debugging over a 1394 Cable Manually](https://msdn.microsoft.com/library/windows/hardware/ff556866).

``` syntax
bcdedit /dbgsettings 1394 channel:1
```

The following command configures the target computer to use USB connection for debugging. The command also specifies a target name that the host computer can use to connect to the target computer. For more information, see [Setting Up Kernel-Mode Debugging over a USB 3.0 Cable Manually](https://msdn.microsoft.com/library/windows/hardware/hh439372) and [Setting Up Kernel-Mode Debugging over a USB 2.0 Cable Manually](https://msdn.microsoft.com/library/windows/hardware/ff556869).

``` syntax
bcdedit /dbgsettings usb targetname:myTarget
```

The following command configures the target computer to use a serial connection for debugging. The command also specifies that the debugging connection will use COM2 and a baud rate of 115,200. For more information, see [Setting Up Kernel-Mode Debugging over a Serial Cable Manually](https://msdn.microsoft.com/library/windows/hardware/ff556867).

``` syntax
bcdedit /dbgsettings serial debugport:2 baudrate:115200
```

See also
--------

[Setting Up Kernel-Mode Debugging in Visual Studio](https://msdn.microsoft.com/library/windows/hardware/hh439376)
[Setting Up Kernel-Mode Debugging Manually](https://msdn.microsoft.com/library/windows/hardware/hh439378)
[Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](https://msdn.microsoft.com/library/windows/hardware/dn337010)
[Supported Ethernet NICs for Network Kernel Debugging in Windows 8](https://msdn.microsoft.com/library/windows/hardware/dn337009)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20BCDEdit%20/dbgsettings%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




