---
title: Writing an INF File for a Smart Card Reader Driver
description: This article describes required sections for INF file for smart card reader drivers for Microsoft Windows.
keywords:
- smart card drivers WDK , writing INF file
- vendor-supplied drivers WDK smart card , INF file
ms.date: 12/19/2024
---

# Writing an INF file for a smart card reader driver

This article describes required sections for INF file for smart card reader drivers for Microsoft Windows.

Vendors that supply their own reader drivers should make each driver a member of the **SmartCardReader** setup class in the **[INF Version Section](../install/inf-version-section.md)** of the driver's INF file. Vendors must also add a section to properly configure the smartcard services. For example:

```inf
[Version]
...
Class=SmartCardReader
ClassGuid={50DD5230-BA8A-11D1-BF5D-0000F805F530}
...

; ============ Add reg for all readers ===============

[Reader.Install.AddReg]
HKLM, Software\Microsoft\Cryptography\Calais\Readers,,,
HKLM, System\CurrentControlSet\Services\SCardSvr,Start,0x00010001,2
HKLM, System\CurrentControlSet\Services\CertPropSvc,Start,0x00010001,2
```

> [!NOTE]
> Starting with Windows 7, the smartcard subsystem configures the smartcard services. Vendors are no longer required to add the `Reader.Install.AddReg` registry keys listed above.

Vendors that supply their own UMDF reader driver need a registry setting to allow PnP filter drivers to sit on top of the UMDF reflector. Specifically, in the driver INF file, this entry is needed:

```inf
[Install.NT.Wdf]
UmdfKernelModeClientPolicy=AllowKernelModeClients
```

There are no other special requirements that are associated with installing smart card reader drivers.

For general information about device installation in Windows, see [Device and Driver Installation](../install/index.md).
