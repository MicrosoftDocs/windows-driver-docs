---
title: Why Thunking Is Necessary
description: Why Thunking Is Necessary
ms.assetid: ea73d355-56e8-4f56-b7e8-4dbddcd19124
keywords: ["thunking WDK", "WOW64 thunking layer WDK", "32-bit I/O support WDK 64-bit , thunking", "buffer size WDK kernel", "DRIVER_DATA structure", "pointer precision WDK 64-bit", "fixed-precision data types WDK 64-bit"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Why Thunking Is Necessary





Kernel-mode drivers must validate the size of any I/O buffer passed in from a user-mode application. If a 32-bit application passes a buffer containing pointer-precision data types to a 64-bit driver, and no thunking takes place, the driver will expect the buffer to be larger than it actually is. This is because pointer precision is 32 bits on 32-bit Microsoft Windows and 64 bits on 64-bit Windows. For example, consider the following structure definition:

```cpp
typedef struct _DRIVER_DATA
{
    HANDLE           Event;
    UNICODE_STRING   ObjectName;
} DRIVER_DATA;
```

On 32-bit Windows, the size of the DRIVER\_DATA structure is 12 bytes.

HANDLE **Event**
UNICODE\_STRING **ObjectName**
USHORT Length
USHORT Maximum Length
PWSTR Buffer
32 bits
(4 bytes)
16 bits
(2 bytes)
16 bits
(2 bytes)
32 bits
(4 bytes)
 

On 64-bit Windows, the size of the DRIVER\_DATA structure is 24 bytes. (The 4 bytes of structure padding are required so that the **Buffer** member can be aligned on an 8-byte boundary.)

HANDLE **Event**
UNICODE\_STRING **ObjectName**
USHORT Length
USHORT Maximum Length
Empty (Structure Padding)
PWSTR Buffer
64 bits
(8 bytes)
16 bits
(2 bytes)
16 bits
(2 bytes)
32 bits
(4 bytes)
64 bits
(8 bytes)
 

If a 64-bit driver receives 12 bytes of DRIVER\_DATA when it expected 24 bytes, the size validation will fail. To prevent this, the driver must detect whether a DRIVER\_DATA structure was sent by a 32-bit application, and if so, thunk it appropriately before performing the validation.

For example, a thunked version of the above DRIVER\_DATA structure could be defined as follows:

```cpp
typedef struct _DRIVER_DATA32
{
    VOID *POINTER_32   Event;
    UNICODE_STRING32   ObjectName;
} DRIVER_DATA32;
```

Because it contains only fixed-precision data types, this new structure is the same size on 32-bit Windows and 64-bit Windows.

POINTER\_32 **Event**
UNICODE\_STRING32 **ObjectName**
USHORT Length
USHORT Maximum Length
ULONG Buffer
32 bits
(4 bytes)
16 bits
(2 bytes)
16 bits
(2 bytes)
32 bits
(4 bytes)
 

 

 




