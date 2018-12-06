---
title: Dynamically Configuring MSI-X
description: Dynamically Configuring MSI-X
ms.assetid: 53051239-e00f-41e8-b95d-9618693e696d
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Dynamically Configuring MSI-X


Windows Vista Service Pack 1 (SP1), Windows Server 2008, and later operating systems support dynamically modifying the properties of MSI-X interrupt messages. (The PCI 3.0 specification defined MSI-X.) The PCI bus driver exposes the GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE interface to allow drivers for PCI devices to modify the settings in the bus hardware interrupt table.

Drivers use the interface by sending an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to the bus driver, with the *InterfaceType* parameter equal to GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE. The bus driver supplies a pointer to a [**PCI\_MSIX\_TABLE\_CONFIG\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff558787) structure, which supplies pointers to three routines that modify the interrupt table:

-   [*SetTableEntry*](https://msdn.microsoft.com/library/windows/hardware/gg604857) assigns a message ID to the hardware table entry.

-   [*MaskTableEntry*](https://msdn.microsoft.com/library/windows/hardware/gg604852) masks the interrupt corresponding to a hardware table entry.

-   [*UnmaskTableEntry*](https://msdn.microsoft.com/library/windows/hardware/gg604859) unmasks the interrupt corresponding to a hardware table entry.

By default, the interrupt table is configured so that the first entry has message ID zero, the second entry has message ID one, and so on. If the number of table entries exceeds the number of messages, each additional table entry is assigned message ID zero. (The message ID is the index for the interrupt's entry in the **MessageInfo** member of the [**IO\_INTERRUPT\_MESSAGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550576) structure that describes the driver's message-signaled interrupts. The [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine supplies a pointer to this structure.)

 

 




