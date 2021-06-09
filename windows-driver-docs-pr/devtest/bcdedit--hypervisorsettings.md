---
title: BCDEdit /hypervisorsettings
description: The /hypervisorsettings command sets or displays the hypervisor debugger settings for the system.
ms.date: 10/01/2020
keywords: ["BCDEdit /hypervisorsettings Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /hypervisorsettings
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /hypervisorsettings


The **/hypervisorsettings** command sets or displays the hypervisor debugger settings for the system.

To set an individual hypervisor debugger setting, use "bcdedit /set {hypervisorsettings} <type> <value>". For more information on the set command, see [BCDEdit /set](bcdedit--set.md).

```syntax
bcdedit /hypervisorsettings [ <debugtype> [DEBUGPORT:<port>] [BAUDRATE:<baud>] [CHANNEL:<channel>] [HOSTIP:<ip>] [PORT:<port>] [BUSPARAMS:<Bus.Device.Function>] ]
```

*\<debugtype\>* - Specifies the type of debugger. \<debugtype\> can be one of NET, SERIAL or 1394 as described below.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Network Debugging

\<debugtype\> *NET*  
Specifies an Ethernet network connection for debugging. When this option is used, the **HOSTIP** option must be also be set by specifying the IPv4 address of the host debugger.

**HOSTIP:***\<ip\>*
The IP address is only used when the **hypervisordebugtype** is **Net**. For debugging hypervisor over a network connection, specifies the IPv4 address of the host debugger.

**PORT:***\<port\>*
For network debugging, specifies the port to communicate with on the host debugger. Should be 49152 or higher.

**BUSPARAMS:***\<Bus.Device.Function\>*
Defines the PCI bus, device, and function numbers of the debugging device. For example, 0.25.0 describes the debugging device on bus 0, device 25, function 0. These values are displayed in Device Manager under *Location* on the *General* tab.  

### Network Debugging Example

The following command sets the hypervisor debugger settings to network debugging with a debugger host at 192.168.1.2 communicating on port 50000:

```console
C:\> bcdedit /hypervisorsettings NET HOSTIP:192.168.1.2 PORT:50000 BUSPARAMS:0.25.0
Key=2steg4fzbj2sz.23418vzkd4ko3.1g34ou07z4pev.1sp3yo9yz874p
```

Use the key that is returned to connect to the target.

These network debugging settings can be modified using the [BCDEdit /set](bcdedit--set.md) command.

**hypervisorhostip** *IP address*
(Only used when the **hypervisordebugtype** is **Net**.) For debugging hypervisor over a network connection, specifies the IPv4 address of the host debugger. For information about debugging Hyper-V, see [Create a Virtual Machine with Hyper-V](/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine).

**hypervisorhostport** \[ *port* \]  
(Only used when the **hypervisordebugtype** is **Net**.) For network debugging, specifies the port to communicate with on the host debugger. Should be 49152 or higher.

**hypervisorbusparams** *Bus.Device.Function*  
Defines the PCI bus, device, and function numbers of the debugging device. For example, 0.25.0 describes the debugging device on bus 0, device 25, function 0. These values are displayed in Device Manager under *Location* on the *General* tab.  

**hypervisorusekey**  *\<key\>*
(Only used when the **hypervisordebugtype** is **Net**.) For network debugging specifies the key with which to encrypt the connection. \[0-9\] and \[a-z\] allowed only.

**hypervisordhcp** \[ **yes** | **no** \]  
Controls use of DHCP by the network debugger used with the hypervisor. Setting this to **no** forces the use of Automatic Private IP Addressing (APIPA) to obtain a local link IP address.

## Serial Debugging 

\<debugtype\> *Serial*  
Specifies a serial connection for debugging. When the **Serial** option is specified, you also set the **hypervisordebugport** and **hypervisorbaudrate** options.

**DEBUGPORT:***\<port\>*
 For SERIAL debugging, specifies the serial port to use as the debugging port.

**BAUDRATE:***\<baud\>*
For SERIAL debugging, specifies the baud rate to be used for debugging.

``` syntax
bcdedit /set hypervisordebugtype serial
bcdedit /set hypervisordebugport 1
bcdedit /set hypervisorbaudrate 115200
bcdedit /set hypervisordebug on
bcdedit /set hypervisorlaunchtype auto
```

### Serial Debugging Example

The following command displays the current hypervisor settings.

```console
C:\>bcdedit /hypervisorsettings
isolatedcontext         Yes
hypervisordebugtype     Serial
hypervisordebugport     1
hypervisorbaudrate      115200
The operation completed successfully.
```

The following command sets the hypervisor debugger settings to serial debugging over COM1 at 115,200 baud.

`bcdedit /hypervisorsettings SERIAL DEBUGPORT:1 BAUDRATE:115200`

## 1394 Debugging

> [!IMPORTANT]
> The 1394 transport is available for use in Windows 10, version 1607 and earlier.
> It is not available in later versions of Windows. You should transition your projects to other transports, such as KDNET using Ethernet.

\<debugtype\> *1394*  
Specifies an IEEE 1394 (FireWire) connection for debugging. When this option is used, the *channel* option should also be set.

**CHANNEL:***<channel>*

For 1394 debugging, specifies the 1394 channel to be used for debugging.

The following related option should be set using the [BCDEdit /set](bcdedit--set.md) command.

**hypervisorbusparams** *Bus.Device.Function*  
Defines the PCI bus, device, and function numbers of the debugging device. For example, 1.5.0 describes the debugging device on bus 1, device 5, function 0. These values are displayed in Device Manager under *Location* on the *General* tab.  

## Comments

This command does not enable or disable the hypervisor debugger for any particular OS loader entry. To enable the hypervisor debugger for a particular OS loader entry, use "bcdedit /set <identifier> HYPERVISORDEBUG ON".

For information about identifiers, run "bcdedit /? ID".

## See Also

[BCDEdit /set](bcdedit--set.md) command.

[BCDEdit Options Reference](bcd-boot-options-reference.md)
