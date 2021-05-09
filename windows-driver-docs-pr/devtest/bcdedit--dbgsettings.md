---
title: BCDEdit /dbgsettings
description: The /dbgsettings option sets or displays the current global debugger settings for the computer.
ms.date: 04/23/2019
keywords: ["BCDEdit /dbgsettings Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /dbgsettings
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /dbgsettings


The **/dbgsettings** option sets or displays the current global debugger settings for the computer. To enable or disable the kernel debugger, use the [**BCDEdit /debug**](bcdedit--debug.md) option.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.


``` syntax
bcdedit /dbgsettings NET HOSTIP:ip PORT:port [KEY:key] [nodhcp] [newkey] [/start startpolicy] [/noumex] 

bcdedit /dbgsettings LOCAL [/start startpolicy] [/noumex] 

bcdedit /dbgsettings SERIAL [DEBUGPORT:port] [BAUDRATE:baud] [/start startpolicy] [/noumex] 

bcdedit /dbgsettings USB [TARGETNAME:targetname] [/start startpolicy] [/noumex] 

bcdedit /dbgsettings 1394 [CHANNEL:channel] [/start startpolicy] [/noumex] NOTE: The 1394 TRANSPORT IS DEPRECATED
```

## Parameters

## NET

Specifies that the target machine and the host machine will use an Ethernet network connection for debugging. When this option is used, the **HOSTIP** and **PORT** parameters must be included as well. The target computer must have a network adapter that is supported by Debugging Tools for Windows. 

**HOSTIP:**<em>ip</em>   
For network debugging, specifies the IP address of the host debugger.

**KEY:**<em>key</em>   
For network debugging, specifies the key with which to encrypt the connection. \[0-9\] and \[a-z\] allowed only. Do not specify this parameter if you have specified the **newkey** parameter.

**PORT:**<em>port</em>  
For network debugging, specifies the port to communicate with on the host debugger. Should be 49152 or higher.

**newkey**   
For network debugging specifies that a new encryption key should be generated for the connection. Do not specify this parameter if you have specified a **KEY** parameter.

**nodhcp**

Setting *nodhcp* prevents use of DHCP to obtain the target IP address. This option is rarely required as even small routers provide support for DHCP. The *nodhcp* option should only be used if you know that there are no DHCP servers on the network.  In most situations, the KDNET transport works best when this option is not set, and DHCP is enabled.

**busparams**=*Bus.Device.Function*
Specifies the target controller. *Bus* specifies the bus number, *Device* specifies the device number, and *Function* specifies the function number.  

To specify the bus parameters, Open Device Manager, and locate the network adapter that you want to use for debugging. Open the property page for the network adapter, and make a note of the bus number, device number, and function number. These values are displayed in Device Manager under *Location* on the *General* tab. In an elevated Command Prompt Window, enter the following command, where b, d, and f are the bus, device and function numbers in decimal format:

```console
bcdedit /set "{dbgsettings}" busparams b.d.f
```

If you are manually configuring a debugger connection, you must specify the bus parameters. For more information, see [Setting Up KDNET Network Kernel Debugging Manually](../debugger/setting-up-a-network-debugging-connection.md) and [Setting Up Kernel-Mode Debugging over a USB 3.0 Cable Manually](../debugger/setting-up-a-usb-3-0-debug-cable-connection.md).

## Examples

The following command configures the target computer to use an Ethernet connection for debugging and specifies the IP address of the host computer. The command also specifies a port number that the host computer can use to connect to the target computer. 

``` console
bcdedit /dbgsettings net hostip:10.125.5.10 port:50000
```

The following command sets the global debugger settings to network debugging
using IPv6 with a debugger host at 2001:48:d8:2f:5e:c0:42:28:4f5b
communicating on port 50000:

``` console
bcdedit /dbgsettings NET HOSTIPV6:2001:48:d8:2f:5e:c0:42:28:4f5b PORT:50000
```

 > [!IMPORTANT]
> Setting up a network debugging manually is a complex and error prone process.
> To set up network debugging automatically, see [Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md). Using the KDNET utility is **strongly** recommended for all debugger users.

For more information on manual setup, see [Setting Up Kernel-Mode Debugging over a Network Cable Manually](../debugger/setting-up-a-network-debugging-connection.md).


## LOCAL

The **LOCAL** option sets the global debugging option to local debugging. This is kernel-mode debugging on a single computer. In other words, the debugger runs on the same computer that is being debugged. With local debugging you can examine state, but not break into kernel mode processes that would cause the OS to stop running.

### Example

The following command sets the global debugger settings to local debugging.

``` console
bcdedit /dbgsettings LOCAL
```

The LOCAL option is available in Windows 8.0 and Windows Server 2012 and later.

For information on setting up local kernel mode debugging manually, see [Setting Up Local Kernel Debugging of a Single Computer Manually](../debugger/setting-up-local-kernel-debugging-of-a-single-computer-manually.md).

## SERIAL

Specifies that the target machine and the host machine will use a serial connection for debugging. When this option is used, the **DEBUGPORT** and **BAUDRATE** parameters should be specified.

**BAUDRATE:**<em>baud</em>   
Specifies the baud rate to use. This parameter is optional. Valid values for *baud* are 9600, 19200, 38400, 57600, and 115200. The default baud rate is 115200 bps.

**DEBUGPORT:**<em>port</em>   
 Specifies the serial port to use as the debugging port. This is an optional setting. The default port is **1** (COM 1).

### Example

The following command configures the target computer to use a serial connection for debugging. The command also specifies that the debugging connection will use COM1 and a baud rate of 115,200. 

``` console
bcdedit /dbgsettings serial debugport:1 baudrate:115200
```
For more information, see [Setting Up Kernel-Mode Debugging over a Serial Cable Manually](../debugger/setting-up-a-null-modem-cable-connection.md).

## USB   
Specifies that the target machine and the host machine will use a USB 2.0 or USB 3.0 connection for debugging. When this option is used, the **TARGETNAME** parameter must be included as well. 

**TARGETNAME:** <em>targetname</em>   
Specifies a string value to use for the target name. Note that TargetName does not have to be the official name of the target computer; it can be any string that you create as long as it meets these restrictions:

- The string must not contain “debug” anywhere in the TargetName in any combination of upper or lower case. For example if you use “DeBuG” or "DEBUG" anywhere in your targetname, debugging will not work correctly.
- The only characters in the string are the hyphen (-), the underscore(_), the digits 0 through 9, and the letters A through Z (upper or lower case).
- The maximum length of the string is 24 characters.


### Example

The following command configures the target computer to use USB connection for debugging. The command also specifies a target name that the host computer can use to connect to the target computer. 

``` console
bcdedit /dbgsettings usb targetname:myTarget
```

For more information, see:

- [Setting Up Kernel-Mode Debugging over a USB 3.0 Cable Manually](../debugger/setting-up-a-usb-3-0-debug-cable-connection.md)
- [Setting Up Kernel-Mode Debugging over a USB 2.0 Cable Manually](../debugger/setting-up-a-usb-2-0-debug-cable-connection.md)



## 1394   

> [!IMPORTANT]
> The 1394 transport is available for use in Windows 10, version 1607 and earlier. 
> It is not available in later versions of Windows. You should transition your projects to other transports, such as KDNET using Ethernet. 
> For more information about that transport, see [Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md).
>

Specifies that the target machine and the host machine will use an IEEE 1394 (FireWire) connection for debugging. When this option is used, the **CHANNEL** parameter can be included as well. 

**CHANNEL:**<em>channel</em>   
(Only used when the connection type is **1394**.) Specifies the 1394 channel to use. The value for *channel* must be a decimal integer between 0 and 62, inclusive, and must match the channel number used by the host computer. The channel specified in this parameter does not depend on the physical 1394 port chosen on the adapter. The default value for *channel* is 0.

For more information, see [Setting Up Kernel-Mode Debugging over a 1394 Cable Manually](../debugger/setting-up-a-1394-cable-connection.md).

## General Debugger Settings

**/start** <em>startpolicy</em>   
This option specifies the debugger start policy. The following table shows the options for the *startpolicy*.

|Option|Description|
|--- |--- |
|ACTIVE|Specifies that the kernel debugger is active.|
|AUTOENABLE|Specifies that the kernel debugger is enabled automatically when an exception or other critical event occurs. Until then, the debugger is active but is disabled.|
|DISABLE|Specifies that the kernel debugger is enabled when you type kdbgctrl to clear the enable block. Until then, the debugger is active but is disabled.|
 

If a start policy is not specified, ACTIVE is the default.

**/noumex**   
Specifies that the kernel debugger ignores user-mode exceptions. By default, the kernel debugger breaks for certain user-mode exceptions, such as STATUS\_BREAKPOINT and STATUS\_SINGLE\_STEP. The **/noumex** parameter is effective only when there is no user-mode debugger attached to the process.

### Comments

The **/dbgsettings** option configures the debugging settings, but does not enable debugging. You must use the **/debug** option to enable debugging for a specific boot entry. If there are no debugging settings specified for a particular boot entry, the default debug settings are used. 

The default values for the dbgsettings are shown in the following table.

|dbgsetting parameter|Default value|
|--- |--- |
|debugtype|Local|
|debugstart|Active|
|noumex|Yes|


## See also

For information about Windows debugging tools, see [Windows Debugging](../debugger/index.md). 

For information about setting up and configuring a kernel-mode debugging session, see [Setting Up Kernel-Mode Debugging Manually](../debugger/setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md) and [Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md).



