---
title: Framework Interrupt Object
description: Framework Interrupt Object
ms.assetid: FA2B8C11-69D2-4A9E-8F57-C7295DA4EE44
---

# Framework Interrupt Object


\[This topic applies to UMDF 1.*x*.\]

The framework interrupt object is exposed to drivers by the [**IWDFInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451283) interface. It represents a hardware interrupt. Interrupt objects are children of [UMDF device objects](framework-device-object.md). A driver can call the [**IWDFDevice3::CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) method to create an interrupt object.

When drivers create interrupts, they can provide interfaces for callback functions that the framework calls to notify the driver when events related to the interfaces occur. For more information, see [UMDF Interrupt Object Event Callback Functions](https://msdn.microsoft.com/library/windows/hardware/hh463979).

For more information about interrupt objects, see [Handling Interrupts](handling-interrupts.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Interrupt%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




