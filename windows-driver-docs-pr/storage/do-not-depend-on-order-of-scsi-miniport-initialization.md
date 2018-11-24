---
title: Do Not Depend on Order of SCSI Miniport Initialization
description: Do Not Depend on Order of SCSI Miniport Initialization
ms.assetid: 762fa062-4eaa-40f2-acdb-99fc6cafe680
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- converting SCSI miniport drivers
- initializing SCSI miniport drivers
- SCSI miniport drivers WDK storage , initializing
- order-dependent code WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Do Not Depend on Order of SCSI Miniport Initialization


## <span id="ddk_do_not_depend_on_order_of_scsi_miniport_initialization_kg"></span><span id="DDK_DO_NOT_DEPEND_ON_ORDER_OF_SCSI_MINIPORT_INITIALIZATION_KG"></span>


Some miniport drivers support HBAs on several different system buses such as PCI, EISA, and ISA. Under Microsoft Windows NT 4.0, such a miniport driver's *HwScsiFindAdapter* routine(s) were called in the order that the miniport driver called [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645). In several cases, this was used to track the location of a card on one type of bus so the miniport driver could avoid detecting it on another.

For example, assume the Twiddle PCI SCSI HBA is also accessible on the ISA bus. Under Windows NT 4.0, the Twiddle miniport driver would keep track of which PCI HBAs it was called to initialize and the ISA bus locations in which they appeared. The miniport driver could use this information while scanning the ISA bus to determine which I/O ranges to skip.

In Windows 2000 and later, this technique is no longer dependable. Because Plug and Play makes initialization order unpredictable, the Twiddle miniport driver could easily be called to scan for its ISA cards before initializing its PCI cards. The miniport driver would detect each PCI HBA twice, which could lead to a system crash.

In this case, if the Twiddle HBA had a command that could be used to determine the real bus interface of the card, the ISA bus scan could query each card it found. If the card were a PCI card and not an ISA card, then the Twiddle miniport driver would leave it alone until Plug and Play issued requests to pick it up.

If the order-dependent code of a miniport driver cannot be removed it must be run as a legacy driver on Windows 2000 and later platforms.

 

 




