---
title: /crashdebug
description: The /crashdebug parameter establishes a kernel debugger connection, but does not enable debugging unless a bug check occurs.
ms.assetid: 671b059d-d6ff-46a8-8d4d-d1c6e1f0739a
keywords: ["/crashdebug Driver Development Tools"]
topic_type:
- apiref
api_name:
- /crashdebug
api_type:
- NA
---

/crashdebug
===========

The **/crashdebug** parameter establishes a kernel debugger connection, but does not enable debugging unless a bug check occurs. Until then, the port that is usually reserved for debugging is free for other uses.

This option is designed for Windows 2000 and Windows XP. For Windows Server 2003, use the **/debug=disable** parameter. For details, see [**/debug**](-debug.md).

``` syntax
    /crashdebug [/debugport=COMx] [/baudrate=BaudRate] 

   
```

## Subparameters


<a href="" id="--------debugport------"></a> **/debugport**   
Specifies the serial port used by the kernel debugger for crash-only debugging.

<a href="" id="-------comx-------------"></a> **COM***x*   
Specifies a communications port on the computer. Valid values for **COM***x* are any valid COM port, such as COM1 or COM2. The default is the highest enumerated port.

<a href="" id="--------baudrate------"></a> **/baudrate**   
Specifies the speed of the kernel debugger connection.

<a href="" id="-------baudrate------"></a> *BaudRate*   
Specifies the speed of the kernel debugger connection in bits per second (BPS). Valid values for *BaudRate* are 9600, 19200, 38400, 57600, and 115200. The default is 19200.

### Comments

This parameter is useful for debugging random kernel errors.

If a boot entry includes both [**/debug**](-debug.md) and **/crashdebug**, the **/debug** parameter is ignored.

### Examples

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /crashdebug

multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /crashdebug /debugport=COM1 /baudrate=57600
```

### Bootcfg Commands

```
bootcfg /raw "/crashdebug" /A /ID 1
bootcfg /raw "crashdebug /debugport=COM1 /baudrate=57600" /A /ID=2
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/crashdebug%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




