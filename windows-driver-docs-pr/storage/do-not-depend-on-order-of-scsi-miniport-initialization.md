---
title: Do Not Depend on Order of SCSI Miniport Initialization
author: windows-driver-content
description: Do Not Depend on Order of SCSI Miniport Initialization
ms.assetid: 762fa062-4eaa-40f2-acdb-99fc6cafe680
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI", "converting SCSI miniport drivers", "initializing SCSI miniport drivers", "SCSI miniport drivers WDK storage , initializing", "order-dependent code WDK SCSI"]
---

# Do Not Depend on Order of SCSI Miniport Initialization


## <span id="ddk_do_not_depend_on_order_of_scsi_miniport_initialization_kg"></span><span id="DDK_DO_NOT_DEPEND_ON_ORDER_OF_SCSI_MINIPORT_INITIALIZATION_KG"></span>


Some miniport drivers support HBAs on several different system buses such as PCI, EISA, and ISA. Under Microsoft Windows NT 4.0, such a miniport driver's *HwScsiFindAdapter* routine(s) were called in the order that the miniport driver called [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645). In several cases, this was used to track the location of a card on one type of bus so the miniport driver could avoid detecting it on another.

For example, assume the Twiddle PCI SCSI HBA is also accessible on the ISA bus. Under Windows NT 4.0, the Twiddle miniport driver would keep track of which PCI HBAs it was called to initialize and the ISA bus locations in which they appeared. The miniport driver could use this information while scanning the ISA bus to determine which I/O ranges to skip.

In Windows 2000 and later, this technique is no longer dependable. Because Plug and Play makes initialization order unpredictable, the Twiddle miniport driver could easily be called to scan for its ISA cards before initializing its PCI cards. The miniport driver would detect each PCI HBA twice, which could lead to a system crash.

In this case, if the Twiddle HBA had a command that could be used to determine the real bus interface of the card, the ISA bus scan could query each card it found. If the card were a PCI card and not an ISA card, then the Twiddle miniport driver would leave it alone until Plug and Play issued requests to pick it up.

If the order-dependent code of a miniport driver cannot be removed it must be run as a legacy driver on Windows 2000 and later platforms.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Do%20Not%20Depend%20on%20Order%20of%20SCSI%20Miniport%20Initialization%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


