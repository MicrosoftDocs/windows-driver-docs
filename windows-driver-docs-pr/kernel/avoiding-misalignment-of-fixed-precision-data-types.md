---
title: Avoiding Misalignment of Fixed-Precision Data Types
description: Avoiding Misalignment of Fixed-Precision Data Types
ms.assetid: 4e214bd8-b622-447a-b484-bd1d5d239de7
keywords: ["file system control codes WDK 64-bit", "FSCTL WDK 64-bit", "control codes WDK 64-bit", "I/O control codes WDK kernel , 32-bit I/O in 64-bit drivers", "IOCTLs WDK kernel , 32-bit I/O in 64-bit drivers", "pointer precision WDK 64-bit", "fixed-precision data types WDK 64-bit", "misaligned fixed-precision data types"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Avoiding Misalignment of Fixed-Precision Data Types





Unfortunately, it is possible for a data type to have the same size, but different alignment requirements, for 32-bit and 64-bit programming. Thus not all IOCTL/FSCTL buffer misalignment problems can be avoided by changing pointer-precision data types to fixed-precision types. This means that kernel-mode driver IOCTLs and FSCTLs that pass buffers containing certain fixed-precision data types (or pointers to them) may also need to be thunked.

### Which Data Types Are Affected

The problem affects fixed-precision data types that are themselves structures. This is because the rules for determining alignment requirements for structures are platform-specific.

For example, **\_\_int64**, LARGE\_INTEGER, and KFLOATING\_SAVE must be aligned on a 4-byte boundary on x86 platforms. However, on Itanium-based machines, they must be aligned on an 8-byte boundary.

To determine the alignment requirement for a given data type on a particular platform, use the **TYPE\_ALIGNMENT** macro on that platform.

### How To Fix the Problem

In the following example, the IOCTL is a METHOD\_NEITHER IOCTL, so the **Irp-&gt;UserBuffer** pointer is passed directly from the user-mode application to the kernel-mode driver. No validation is performed on buffers used in IOCTLs and FSCTLs. Thus a call to [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) or [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) is required before the buffer pointer can be safely dereferenced.

Assuming that the 32-bit application has passed a valid value for **Irp-&gt;UserBuffer**, the LARGE\_INTEGER structure pointed to by **p-&gt;DeviceTime** will be aligned on a 4-byte boundary. **ProbeForRead** checks this alignment against the value passed in its *Alignment* parameter, which in this case is **TYPE\_ALIGNMENT** (LARGE\_INTEGER). On x86 platforms, this macro expression returns 4 (bytes). However, on Itanium-based machines, it returns 8, causing **ProbeForRead** to raise a STATUS\_DATATYPE\_MISALIGNMENT exception.

**Note**   Removing the **ProbeForRead** call does not fix the problem, but only makes it harder to diagnose.

 

```cpp
typedef struct _IOCTL_PARAMETERS2 {
    LARGE_INTEGER DeviceTime;
} IOCTL_PARAMETERS2, *PIOCTL_PARAMETERS2;

#define SETTIME_FUNCTION 1
#define IOCTL_SETTIME CTL_CODE(FILE_DEVICE_UNKNOWN, \
            SETTIME_FUNCTION, METHOD_NEITHER, FILE_ANY_ACCESS)

...

case IOCTL_SETTIME:
    PIOCTL_PARAMETERS2 p = (PIOCTL_PARAMETERS2)Irp->UserBuffer;

    try {                 
        if (Irp->RequestorMode != KernelMode) { 
            ProbeForRead ( p->DeviceTime,
                      sizeof( LARGE_INTEGER ),
                      TYPE_ALIGNMENT( LARGE_INTEGER ));
    }
    status = DoSomeWork(p->DeviceTime);

 } except( EXCEPTION_EXECUTE_HANDLER ) {
```

The following sections tell how to fix the problem described above. Note that all code snippets have been edited for brevity.

### Solution 1: Copy the Buffer

The safest way to avoid misalignment problems is to make a copy of the buffer before accessing its contents, as in the following example.

```cpp
case IOCTL_SETTIME: {
    PIOCTL_PARAMETERS2 p = (PIOCTL_PARAMETERS2)Irp->UserBuffer;
#if _WIN64
    IOCTL_PARAMETERS2 LocalParams2;

    RtlCopyMemory(&LocalParams2, p, sizeof(IOCTL_PARAMETERS2));
    p = &LocalParams2;
#endif

    status = DoSomeWork(p->DeviceTime);
    break;
}
```

This solution can be optimized for better performance by first checking whether the buffer contents are correctly aligned. If so, the buffer can be used as is. Otherwise, the driver makes a copy of the buffer.

```cpp
case IOCTL_SETTIME: {
    PIOCTL_PARAMETERS2 p = (PIOCTL_PARAMETERS2)Irp->UserBuffer;
#if _WIN64
    IOCTL_PARAMETERS2 LocalParams2;

    if ( (ULONG_PTR)p & (TYPE_ALIGNMENT(IOCTL_PARAMETERS2)-1)) {
        // The buffer contents are not correctly aligned for this 
        // platform, so copy them into a properly aligned local 
        // buffer.
        RtlCopyMemory(&LocalParams2, p, sizeof(IOCTL_PARAMETERS2));
        p = &LocalParams2;
    }
#endif

    status = DoSomeWork(p->DeviceTime);
    break;
}
```

### Solution 2: Use the UNALIGNED Macro

The **UNALIGNED** macro tells the C compiler to generate code that can access the **DeviceTime** field without taking an alignment fault. Note that using this macro on Itanium-based platforms is likely to make your driver significantly larger and slower.

```cpp
typedef struct _IOCTL_PARAMETERS2 {
    LARGE_INTEGER DeviceTime;
} IOCTL_PARAMETERS2;
typedef IOCTL_PARAMETERS2 UNALIGNED *PIOCTL_PARAMETERS2;
```

### Pointers Are Also Affected

The misalignment problem described earlier can also occur in buffered I/O requests. In the following example, the IOCTL buffer contains an embedded pointer to a LARGE\_INTEGER structure.

```cpp
typedef struct _IOCTL_PARAMETERS3 {
    LARGE_INTEGER *pDeviceCount;
} IOCTL_PARAMETERS3, *PIOCTL_PARAMETERS3;0

#define COUNT_FUNCTION 1
#define IOCTL_GETCOUNT CTL_CODE(FILE_DEVICE_UNKNOWN, \
            COUNT_FUNCTION, METHOD_BUFFERED, FILE_ANY_ACCESS)
```

Like the METHOD\_NEITHER IOCTL and FSCTL buffer pointers described earlier, pointers embedded in buffered I/O requests are also passed directly from the user-mode application to the kernel-mode driver. No validation is performed on these pointers. Thus a call to [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) or [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), enclosed in a **try/except** block, is required before the embedded pointer can be safely dereferenced.

As in the earlier example, assuming that the 32-bit application has passed a valid value for **pDeviceCount**, the LARGE\_INTEGER structure pointed to by **pDeviceCount** will be aligned on a 4-byte boundary. **ProbeForRead** and **ProbeForWrite** check this alignment against the value of the *Alignment* parameter, which in this case is TYPE\_ALIGNMENT (LARGE\_INTEGER). On x86 platforms, this macro expression returns 4 (bytes). However, on Itanium-based machines, it returns 8, causing **ProbeForRead** or **ProbeForWrite** to raise a STATUS\_DATATYPE\_MISALIGNMENT exception.

This problem can be fixed either by making a properly aligned copy of the LARGE\_INTEGER structure, as in Solution 1, or by using the UNALIGNED macro as follows:

```cpp
typedef struct _IOCTL_PARAMETERS3 {
    LARGE_INTEGER UNALIGNED *pDeviceCount;
} IOCTL_PARAMETERS3, *PIOCTL_PARAMETERS3;
```

 

 




