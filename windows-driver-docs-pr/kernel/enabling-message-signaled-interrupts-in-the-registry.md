---
title: Enabling Message-Signaled Interrupts in the Registry
author: windows-driver-content
description: Enabling Message-Signaled Interrupts in the Registry
ms.assetid: 802ad994-51e7-4aef-a0f0-865dfaf4e6ce
keywords: ["message-signaled interrupts WDK kernel , enabling", "enabling message-signaled interrupts WDK kernel", "MSIs WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling Message-Signaled Interrupts in the Registry


To receive message-signaled interrupts (MSIs), a driver's INF file must enable MSIs in the registry during installation. Use the **Interrupt Management\\MessageSignaledInterruptProperties** subkey of the device's hardware key to enable MSI support.

The **MSISupported** entry of **Interrupt Management\\MessageSignaledInterruptProperties** is a REG\_DWORD value that determines whether the device supports MSIs. Set **MSISupported** to 1 to enable MSI support.

You can also use the registry to specify the maximum number of MSIs to allocate for their device. The **MessageNumberLimit** entry of **Interrupt Management\\MessageSignaledInterruptProperties** is a REG\_DWORD value that specifies the maximum number of MSIs to allocate. For PCI 2.2, **MessageNumberLimit** must be 1, 2, 4, 8, or 16. For PCI 3.0, **MessageNumberLimit** can be any number up to 2,048.

Use an [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) in your driver's INF file to set registry keys under the device's hardware key. For more information, see [**INF DDInstall.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330).

The following code example shows how to set the **MSISupported** entry under **Interrupt Management\\MessageSignaledInterruptProperties** for the device. Note that you must first create the **Interrupt Management** and **Interrupt Management\\MessageSignaledInterruptProperties** keys before you can set the **MSISupported** entry.

```
[mydevice.HW]
AddReg = mydevice_addreg

[mydevice_addreg]
HKR,Interrupt Management,,0x00000010
HKR,Interrupt Management\MessageSignaledInterruptProperties,,0x00000010
HKR,Interrupt Management\MessageSignaledInterruptProperties,MSISupported,0x00010001,1
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Enabling%20Message-Signaled%20Interrupts%20in%20the%20Registry%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


