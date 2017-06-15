---
title: Dynamically Configuring MSI-X
author: windows-driver-content
description: Dynamically Configuring MSI-X
MS-HAID:
- 'Intrupts\_d4ecc293-3a69-4f7b-8447-0a3f8a9c4970.xml'
- 'kernel.dynamically\_configuring\_msi\_x'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 53051239-e00f-41e8-b95d-9618693e696d
---

# Dynamically Configuring MSI-X


Windows Vista Service Pack 1 (SP1), Windows Server 2008, and later operating systems support dynamically modifying the properties of MSI-X interrupt messages. (The PCI 3.0 specification defined MSI-X.) The PCI bus driver exposes the [GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/ff546563) interface to allow drivers for PCI devices to modify the settings in the bus hardware interrupt table.

Drivers use the interface by sending an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to the bus driver, with the *InterfaceType* parameter equal to GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE. The bus driver supplies a pointer to a [**PCI\_MSIX\_TABLE\_CONFIG\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff558787) structure, which supplies pointers to three routines that modify the interrupt table:

-   [*SetTableEntry*](https://msdn.microsoft.com/library/windows/hardware/gg604857) assigns a message ID to the hardware table entry.

-   [*MaskTableEntry*](https://msdn.microsoft.com/library/windows/hardware/gg604852) masks the interrupt corresponding to a hardware table entry.

-   [*UnmaskTableEntry*](https://msdn.microsoft.com/library/windows/hardware/gg604859) unmasks the interrupt corresponding to a hardware table entry.

By default, the interrupt table is configured so that the first entry has message ID zero, the second entry has message ID one, and so on. If the number of table entries exceeds the number of messages, each additional table entry is assigned message ID zero. (The message ID is the index for the interrupt's entry in the **MessageInfo** member of the [**IO\_INTERRUPT\_MESSAGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550576) structure that describes the driver's message-signaled interrupts. The [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine supplies a pointer to this structure.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Dynamically%20Configuring%20MSI-X%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


