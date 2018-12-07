---
title: Enabling Message-Signaled Interrupts in the Registry
description: Enabling Message-Signaled Interrupts in the Registry
ms.assetid: 802ad994-51e7-4aef-a0f0-865dfaf4e6ce
keywords: ["message-signaled interrupts WDK kernel , enabling", "enabling message-signaled interrupts WDK kernel", "MSIs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Enabling Message-Signaled Interrupts in the Registry


To receive message-signaled interrupts (MSIs), a driver's INF file must enable MSIs in the registry during installation. Use the **Interrupt Management\\MessageSignaledInterruptProperties** subkey of the device's hardware key to enable MSI support.

The **MSISupported** entry of **Interrupt Management\\MessageSignaledInterruptProperties** is a REG\_DWORD value that determines whether the device supports MSIs. Set **MSISupported** to 1 to enable MSI support.

You can also use the registry to specify the maximum number of MSIs to allocate for their device. The **MessageNumberLimit** entry of **Interrupt Management\\MessageSignaledInterruptProperties** is a REG\_DWORD value that specifies the maximum number of MSIs to allocate. For PCI 2.2, **MessageNumberLimit** must be 1, 2, 4, 8, or 16. For PCI 3.0, **MessageNumberLimit** can be any number up to 2,048.

Use an [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) in your driver's INF file to set registry keys under the device's hardware key. For more information, see [**INF DDInstall.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330).

The following code example shows how to set the **MSISupported** entry under **Interrupt Management\\MessageSignaledInterruptProperties** for the device. Note that you must first create the **Interrupt Management** and **Interrupt Management\\MessageSignaledInterruptProperties** keys before you can set the **MSISupported** entry.

```cpp
[mydevice.HW]
AddReg = mydevice_addreg

[mydevice_addreg]
HKR,Interrupt Management,,0x00000010
HKR,Interrupt Management\MessageSignaledInterruptProperties,,0x00000010
HKR,Interrupt Management\MessageSignaledInterruptProperties,MSISupported,0x00010001,1
```

 

 




