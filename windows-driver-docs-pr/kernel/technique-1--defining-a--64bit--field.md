---
title: Technique 1 Defining a "64Bit" Field
author: windows-driver-content
description: Defining a "64Bit" Field for drivers
ms.assetid: 6498e66c-145e-4f7e-a065-cbd781e142cc
keywords: ["32-bit I/O support WDK 64-bit , 64Bit field defined", "64Bit field defined WDK kernel", "bitfields WDK 64-bit", "separate control codes WDK 64-bit", "control codes WDK 64-bit", "file system control codes WDK 64-bit", "FSCTL WDK 64-bit", "I/O control codes WDK kernel , 32-bit I/O in 64-bit drivers", "IOCTLs WDK kernel , 32-bit I/O in 64-bit drivers"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Technique 1: Defining a "64Bit" Field


## <a href="" id="ddk-technique-1-defining-a-64bit-field-kg"></a>


The "64Bit" field is defined in the IOCTL or FSCTL control code. This field contains a bit flag that is always set for 64-bit callers, but is always clear for 32-bit. Which bit in the control code is chosen as the "64Bit" field is driver-specific, but it must be a bit that is never set for 32-bit callers. A good choice for most drivers is the most significant bit (MSB) in the Function field.

For example, the IOCTL (FSCTL) control codes used in 32-bit drivers contain four bitfields:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Device type</th>
<th>Access</th>
<th>Function</th>
<th>Method</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>16 bits</p></td>
<td><p>2 bits</p></td>
<td><p>12 bits</p></td>
<td><p>2 bits</p></td>
</tr>
</tbody>
</table>

 

As long as none of the existing driver-defined control codes set the MSB in the Function field, these control codes can continue to be used by 32-bit user-mode applications.

To accommodate 64-bit callers, the driver defines a Function field that is shorter by one bit. This bit is redefined as a "64Bit" field:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Device type</th>
<th>Access</th>
<th>64Bit</th>
<th>Function</th>
<th>Method</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>16 bits</p></td>
<td><p>2 bits</p></td>
<td><p>1 bit</p></td>
<td><p>11 bits</p></td>
<td><p>2 bits</p></td>
</tr>
</tbody>
</table>

 

The following code example shows how to define a "64Bit" field in a driver header file:

```
#define REGISTER_FUNCTION 0     // Define the IOCTL function code

#ifdef  _WIN64
#define CLIENT_64BIT   0x800
#define REGISTER_FUNCTION 0
#define IOCTL_REGISTER   CTL_CODE(FILE_DEVICE_UNKNOWN, \
  CLIENT_64BIT|REGISTER_FUNCTION, METHOD_BUFFERED, FILE_ANY_ACCESS)
#else
#define IOCTL_REGISTER   CTL_CODE(FILE_DEVICE_UNKNOWN, \
  REGISTER_FUNCTION, METHOD_BUFFERED, FILE_ANY_ACCESS)
#endif

typedef struct _IOCTL_PARAMETERS {
    PVOID   Addr;
    SIZE_T  Length;
    HANDLE  Handle;
} IOCTL_PARAMETERS, *PIOCTL_PARAMETERS;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Technique%201:%20Defining%20a%20%2264Bit%22%20Field%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


