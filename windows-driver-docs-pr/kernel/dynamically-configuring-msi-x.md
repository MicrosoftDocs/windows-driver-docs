---
title: Dynamically Configuring MSI-X
description: Dynamically Configuring MSI-X
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Dynamically Configuring MSI-X


Windows Vista Service Pack 1 (SP1), Windows Server 2008, and later operating systems support dynamically modifying the properties of MSI-X interrupt messages. (The PCI 3.0 specification defined MSI-X.) The PCI bus driver exposes the GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE interface to allow drivers for PCI devices to modify the settings in the bus hardware interrupt table.

Drivers use the interface by sending an [**IRP\_MN\_QUERY\_INTERFACE**](./irp-mn-query-interface.md) request to the bus driver, with the *InterfaceType* parameter equal to GUID\_MSIX\_TABLE\_CONFIG\_INTERFACE. The bus driver supplies a pointer to a [**PCI\_MSIX\_TABLE\_CONFIG\_INTERFACE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pci_msix_table_config_interface) structure, which supplies pointers to three routines that modify the interrupt table:

-   [*SetTableEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-pci_msix_set_entry) assigns a message ID to the hardware table entry.

-   [*MaskTableEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-pci_msix_maskunmask_entry) masks the interrupt corresponding to a hardware table entry.

-   [*UnmaskTableEntry*](/previous-versions/windows/hardware/drivers/gg604859(v=vs.85)) unmasks the interrupt corresponding to a hardware table entry.

By default, the interrupt table is configured so that the first entry has message ID zero, the second entry has message ID one, and so on. If the number of table entries exceeds the number of messages, each additional table entry is assigned message ID zero. (The message ID is the index for the interrupt's entry in the **MessageInfo** member of the [**IO\_INTERRUPT\_MESSAGE\_INFO**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_interrupt_message_info) structure that describes the driver's message-signaled interrupts. The [**IoConnectInterruptEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterruptex) routine supplies a pointer to this structure.)

 

