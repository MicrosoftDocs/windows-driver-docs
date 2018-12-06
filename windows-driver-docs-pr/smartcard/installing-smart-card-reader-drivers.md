---
title: Installing Smart Card Reader Drivers
description: Installing Smart Card Reader Drivers
ms.assetid: 6e641718-d6d0-4f09-8935-6b381ad0c085
keywords:
- smart card drivers WDK , installing
- vendor-supplied drivers WDK smart card , installing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Smart Card Reader Drivers


## <span id="_ntovr_installing_smart_card_reader_drivers"></span><span id="_NTOVR_INSTALLING_SMART_CARD_READER_DRIVERS"></span>


This section provides installation information that is specific to smart card reader drivers for Microsoft Windows 2000 and later versions of the operating system.

Vendors that supply their own reader drivers should make each driver a member of the **SmartCardReader** setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. Vendors must also add a section to properly configure the smartcard services. For example:

```cpp
[Version]
Signature="$Windows NT$"
Class=SmartCardReader
ClassGuid={50DD5230-BA8A-11D1-BF5D-0000F805F530}

; ============ Add reg for all readers ===============

[Reader.Install.AddReg]
HKLM, Software\Microsoft\Cryptography\Calais\Readers,,,
HKLM, System\CurrentControlSet\Services\SCardSvr,Start,0x00010001,2
HKLM, System\CurrentControlSet\Services\CertPropSvc,Start,0x00010001,2
```

Vendors that supply their own UMDF reader driver need a registry setting to allow PnP filter drivers to sit on top of the UMDF reflector. Specifically, in the driver INF file, this entry is needed:

```cpp
[Install.NT.Wdf]
UmdfKernelModeClientPolicy=AllowKernelModeClients
```

There are no other special requirements that are associated with installing smart card reader drivers.

For general information about device installation in Windows 2000 and later versions of the operating system, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).









