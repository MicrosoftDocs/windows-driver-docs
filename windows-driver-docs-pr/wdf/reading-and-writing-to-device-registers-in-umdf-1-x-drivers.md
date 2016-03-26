---
title: Reading and Writing to Device Registers in UMDF 1.x Drivers
description: Reading and Writing to Device Registers in UMDF 1.x Drivers
ms.assetid: A0640E60-B0DF-4CAD-B292-CC1875EF7F7D
---

# Reading and Writing to Device Registers in UMDF 1.x Drivers


\[This topic applies to UMDF 1.*x*.\]

Starting in UMDF version 1.11, the framework provides a set of routines to access registers in memory space and I/O port space. The [UMDF register/port access routines](https://msdn.microsoft.com/library/windows/hardware/hh463975) are very similar to the HAL routines used by kernel-mode drivers. After a driver has mapped registers as described in [Finding and Mapping Hardware Resources in a UMDF Driver](https://msdn.microsoft.com/library/windows/hardware/hh439594), the driver uses the READ/WRITE\_REGISTER\_Xxx routines to read and write to individual registers. For I/O ports, the driver calls the READ/WRITE\_PORT\_Xxx routines.

This example shows how to write to a memory-mapped register.

```
VOID
CMyQueue::WriteToDevice(
    __in IWDFDevice3* pWdfDevice,
    __in UCHAR Value
    )
{
    //
    // Write the UCHAR value at offset 2 from register base
    //
    WRITE_REGISTER_UCHAR(pWdfDevice, 
                      (m_MyDevice->m_RegBase)+2, 
                       Value);
}
```

By default, UMDF internally uses system calls to access the registers mapped either in memory space or in I/O port space. A register in I/O port space is always accessed through a system call. However, when accessing memory-mapped registers, a UMDF driver can cause the framework to map the memory-mapped registers into user-mode address space by setting the INF directive **UmdfRegisterAccessMode** to **RegisterAccessUsingUserModeMapping**. Some drivers may need to do this for performance reasons. See [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md) for a complete list of UMDF INF directives.

The driver should use the READ/WRITE\_REGISTER\_Xxx routines even if it has mapped registers into user-mode. These routines validate driver input and ensure that the driver doesn't request access to invalid locations. Rarely, a driver may need to access user-mode mapped registers directly, without using these routines. To do so, a driver retrieves the user-mode mapped address by calling [**IWDFDevice3::GetHardwareRegisterMappedAddress**](https://msdn.microsoft.com/library/windows/hardware/hh451219) on the mapped base address. Because UMDF doesn't validate read and write accesses performed in this way, this technique is not recommended for register access.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Reading%20and%20Writing%20to%20Device%20Registers%20in%20UMDF%201.x%20Drivers%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




