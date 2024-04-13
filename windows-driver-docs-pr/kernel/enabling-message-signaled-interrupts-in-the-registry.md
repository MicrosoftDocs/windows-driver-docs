---
title: Enabling Message-Signaled Interrupts in the Registry
description: Enabling Message-Signaled Interrupts in the Registry
keywords: ["message-signaled interrupts WDK kernel , enabling", "enabling message-signaled interrupts WDK kernel", "MSIs WDK kernel"]
ms.date: 06/16/2017
---

# Enabling Message-Signaled Interrupts in the Registry


To receive message-signaled interrupts (MSIs), a driver's INF file must enable MSIs in the registry during installation. Use the **Interrupt Management\\MessageSignaledInterruptProperties** subkey of the device's hardware key to enable MSI support.

The **MSISupported** entry of **Interrupt Management\\MessageSignaledInterruptProperties** is a REG\_DWORD value that determines whether the device supports MSIs. Set **MSISupported** to 1 to enable MSI support.

You can also use the registry to specify the maximum number of MSIs to allocate for their device. The **MessageNumberLimit** entry of **Interrupt Management\\MessageSignaledInterruptProperties** is a REG\_DWORD value that specifies the maximum number of MSIs to allocate.

For multi-message MSI (available starting with PCI 2.2), **MessageNumberLimit** must be 1, 2, 4, 8, or 16. For MSI-X devices (available starting with PCI 3.0), **MessageNumberLimit** can be any number up to 2,048.

Use an [**INF AddReg Directive**](../install/inf-addreg-directive.md) in your driver's INF file to set registry keys under the device's hardware key. For more information, see [**INF DDInstall.HW Section**](../install/inf-ddinstall-hw-section.md).

The following code example shows how to set the **MSISupported** entry under **Interrupt Management\\MessageSignaledInterruptProperties** for the device. Note that **Interrupt Management** and **Interrupt Management\\MessageSignaledInterruptProperties** keys are automatically created by the **AddReg** directive when adding the **MSISupported** value.

```cpp
[mydevice.HW]
AddReg = mydevice_addreg

[mydevice_addreg]
HKR,Interrupt Management\MessageSignaledInterruptProperties,MSISupported,0x00010001,1
```

 

