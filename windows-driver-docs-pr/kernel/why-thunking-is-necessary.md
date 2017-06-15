---
title: Why Thunking Is Necessary
author: windows-driver-content
description: Why Thunking Is Necessary
MS-HAID:
- 'Other\_ef58e0a3-148f-44fb-ae93-8bd04a8dc735.xml'
- 'kernel.why\_thunking\_is\_necessary'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ea73d355-56e8-4f56-b7e8-4dbddcd19124
keywords: ["thunking WDK", "WOW64 thunking layer WDK", "32-bit I/O support WDK 64-bit , thunking", "buffer size WDK kernel", "DRIVER_DATA structure", "pointer precision WDK 64-bit", "fixed-precision data types WDK 64-bit"]
---

# Why Thunking Is Necessary


## <a href="" id="ddk-why-thunking-is-necessary-kg"></a>


Kernel-mode drivers must validate the size of any I/O buffer passed in from a user-mode application. If a 32-bit application passes a buffer containing pointer-precision data types to a 64-bit driver, and no thunking takes place, the driver will expect the buffer to be larger than it actually is. This is because pointer precision is 32 bits on 32-bit Microsoft Windows and 64 bits on 64-bit Windows. For example, consider the following structure definition:

```
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

```
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
 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Why%20Thunking%20Is%20Necessary%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


