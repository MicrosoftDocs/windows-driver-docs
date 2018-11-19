---
title: Technique 1 Defining a "64Bit" Field
description: Defining a "64Bit" Field for drivers
ms.assetid: 6498e66c-145e-4f7e-a065-cbd781e142cc
keywords: ["32-bit I/O support WDK 64-bit , 64Bit field defined", "64Bit field defined WDK kernel", "bitfields WDK 64-bit", "separate control codes WDK 64-bit", "control codes WDK 64-bit", "file system control codes WDK 64-bit", "FSCTL WDK 64-bit", "I/O control codes WDK kernel , 32-bit I/O in 64-bit drivers", "IOCTLs WDK kernel , 32-bit I/O in 64-bit drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Technique 1: Defining a "64Bit" Field





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

```cpp
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

 

 




