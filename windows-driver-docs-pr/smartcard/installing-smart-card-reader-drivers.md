---
title: Installing Smart Card Reader Drivers
description: Installing Smart Card Reader Drivers
ms.assetid: 6e641718-d6d0-4f09-8935-6b381ad0c085
keywords:
- smart card drivers WDK , installing
- vendor-supplied drivers WDK smart card , installing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing Smart Card Reader Drivers


## <span id="_ntovr_installing_smart_card_reader_drivers"></span><span id="_NTOVR_INSTALLING_SMART_CARD_READER_DRIVERS"></span>


This section provides installation information that is specific to smart card reader drivers for Microsoft Windows 2000 and later versions of the operating system.

Vendors that supply their own reader drivers should make each driver a member of the **SmartCardReader** setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. Vendors must also add a section to properly configure the smartcard services. For example:

```
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

```
[Install.NT.Wdf]
UmdfKernelModeClientPolicy=AllowKernelModeClients
```

There are no other special requirements that are associated with installing smart card reader drivers.

For general information about device installation in Windows 2000 and later versions of the operating system, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Installing%20Smart%20Card%20Reader%20Drivers%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




