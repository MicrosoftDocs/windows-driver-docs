---
title: /debug
description: The /debug parameter establishes a kernel debugging connection.
ms.assetid: 12e9488d-762e-4bee-aa7e-f285040d800b
keywords: ["/debug Driver Development Tools"]
topic_type:
- apiref
api_name:
- /debug
api_type:
- NA
---

/debug
======

The **/debug** parameter establishes a kernel debugging connection.

**Syntax for Microsoft Windows 2000 and Windows XP only.**

``` syntax
    /debug

   
```

``` syntax
    /debug /debugport=COMx [ /baudrate=BaudRate ] 

   
```

``` syntax
    /debug /debugport=1394 [/channel=Channel ] 

   
```

``` syntax
    /debug /debugport=usb /targetname=String

   
```

**Syntax for Microsoft Windows Server 2003 only.**

``` syntax
    /debug

   
```

``` syntax
    /debug[={autoenable | disable | noumex},...] /debugport=COMx [ /baudrate=BaudRate ]

   
```

``` syntax
    /debug[={autoenable | disable | noumex},...] /debugport=1394 [/channel=Channel ]

   
```

``` syntax
    /debug[={autoenable | disable | noumex},...] /debugport=usb /targetname=String

   
```

## Subparameters


<a href="" id="--------debugport------"></a> **/debugport**   
Specifies the serial port used by the kernel debugger.

With **COM***x*, **/debugport** enables debugging with a debug (null modem) cable.

With **1394**, **/debugport** enables debugging with an IEEE 1394 cable.

With **usb**, **/debugport** enables debugging with a USB 2.0 debugging cable.

<a href="" id="-------comx-------------"></a> **COM***x*   
Specifies the communications port used for kernel debugging with a null modem cable. Valid values are any valid COM port, such as COM1 or COM2.

<a href="" id="--------baudrate------"></a> **/baudrate**   
Specifies the speed of a kernel debugger connection when using the **/debugport=COM***x* parameter.

<a href="" id="-------baudrate------"></a> *BaudRate*   
Specifies the speed of a kernel debugger connection in BPS. Valid values for *BaudRate* are 9600, 19200, 38400, 57600, and 115200. The default is 19200.

<a href="" id="-------1394------"></a> **1394**   
Specifies debugging with an IEEE 1394 (FireWire) cable. This feature is supported only if your target computer and your host computer are both running Windows XP or a later version of Windows.

> \[!Note\]
> To perform kernel debugging with a 1394 cable when the target computer is running Windows Server 2003 (with no service packs installed) or Windows XP with Service Pack 1 (SP1), you must disable the 1394 host controller on the target computer and install the 1394 virtual driver that is included in the Debugging Tools for Windows package on the host computer. For instructions, see the [Disabling the 1394 Host Controller](http://go.microsoft.com/fwlink/p/?linkid=113154) and [Installing the 1394 Virtual Driver](http://go.microsoft.com/fwlink/p/?linkid=113153) topics in the Debugging Tools for Windows documentation on MSDN.

 

<a href="" id="-channel"></a>**/channel**  
Specifies the 1394 bus channel used when debugging with an IEEE 1394 cable. The default value is 0.

<a href="" id="-------channel------"></a> *Channel*   
Specifies the 1394 channel. The default value is 0. The value of *Channel* must be a decimal integer between 0 and 62, inclusive, and must match the channel number used by the host computer. The channel specified in this parameter does not depend on the physical 1394 port chosen on the adapter.

<a href="" id="-------usb------"></a> **usb**   
Specifies debugging with a USB 2.0 debugging cable. This feature is supported only if your host computer is running Windows 2000 or later, and your target computer is running Windows Vista or later.

> \[!Note\]
> Before you perform kernel debugging over a USB 2.0 cable, additional configuration is required. For more information, see the [Setting Up a USB 2.0 Debug Cable Connection](http://go.microsoft.com/fwlink/p/?linkid=113153) topic in Debugging Tools for Windows documentation on MSDN.

 

<a href="" id="--------targetname------"></a> **/targetname**   
Specifies a string to use as the identification for the USB 2.0 connection. This string can be any value.

<a href="" id="-------string------"></a> *String*   
Specifies a string to use as the identification for the USB 2.0 connection. *String* can be any value.

<a href="" id="-------autoenable------"></a> **autoenable**   
Specifies that the kernel debugger is enabled automatically when an exception or other critical event occurs. Until then, the debugger is active but is disabled.

<a href="" id="-------disable------"></a> **disable**   
Specifies that the kernel debugger is enabled when you type **kdbgctrl** to clear the enable block. Until then, the debugger is active but is disabled.

The **/debug=disable** parameter is designed to be a preferred alternative to [**/crashdebug**](-crashdebug.md). For more information about the KDbgCtrl tool, see the Debugging Tools for Windows documentation.

<a href="" id="-------noumex------"></a> **noumex**   
Specifies that the kernel debugger does not break for user-mode exceptions. By default, the kernel debugger breaks for particular user-mode exceptions, such as STATUS\_BREAKPOINT and STATUS\_SINGLE\_STEP. The **/debug=noumex** parameter is effective only when there is no user-mode debugger attached to the process.

### Comments

The **/debug** parameter is supported only on Windows Server 2003, Windows XP, and Windows 2000. In Windows Vista and later versions of Windows, use BCDEdit and the **/dbgsettings** parameter and its subparameters to establish debugger settings for all boot entries. Then, use the **/debug** parameter to enable debugging for a particular boot entry.

To enable local (one computer) debugging, use only the **/debug** parameter.

To enable debugging with a debug (null-modem) cable, use the **/debug** parameter with the **/debugport=COM***x* and **/baudrate** subparameter.

To enable debugging with an IEEE 1394 (FireWire) cable, use the **/debug** parameter with the **/debugport=1394** and **/channel** subparameters.

Because the **/debugport** subparameter reserves the specified port, do not use it unless you plan to debug the computer.

When you enable kernel debugging on a serial port, Windows removes the specified port from the system device list. As a result, on computers with an [ACPI BIOS](https://msdn.microsoft.com/library/windows/hardware/ff540487), the port does not appear in any device lists, such as the one in Device Manager. On computers that do no have an ACPI BIOS, the port appears with an error message, such as "Not enough resources to use this port." These messages indicate that the port is under the control of the host debugging computer; they do not indicate a malfunction.

To test a cable connection, start your test after connecting the cable, but before enabling debugging.

When you configure a boot entry for debugging, the boot loader appends a bracketed phrase, **\[debugger enabled\]**, to the friendly name that appears in the boot menu. However, the boot loader omits the bracketed phrase from the boot menu when the friendly name and the bracketed phrase together exceed 70 characters. To restore the bracketed phrase, shorten the friendly name.

On Windows Server 2003, you can use the **autoenable**, **disable**, and **noumex** subparameters of **/debug** to enable the debugger only when you need it. You can use more than one subparameter at a time. To use multiple subparameters, separate each subparameter with a comma. (Do not type **/debug** more than once. If you do, Windows uses the first instance and ignores all others.)

For example, **/debug=autoenable, noumex** enables the kernel debugger on an exception or critical event, but not for user-mode events.

For detailed examples of the use of the **/debug** parameter and its variations, see [Boot Parameters to Enable Debugging](https://msdn.microsoft.com/library/windows/hardware/ff542279).

### Examples

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /debug

multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /debug /debugport=COM1 /baudrate=115200

multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /debug /debugport=1394 /channel=44

multi(0)disk(0)rdisk(0)partition(1)\WINNT="Windows Server 2003, Standard" /noexecute=optout /fastdetect /debug=autoenable /debugport=1394 /channel=44

multi(0)disk(0)rdisk(0)partition(1)\WINNT="Windows Server 2003, Standard" /noexecute=optout /fastdetect /debug=disable,noumex /debugport=COM1 /baudrate=115200
```

### Bootcfg Commands

```
bootcfg /debug ON /ID 1
bootcfg /debug ON /port=COMx [/baud=115200] /ID 2
bootcfg /dbg1394 ON /channel=44 /ID 3
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/debug%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




