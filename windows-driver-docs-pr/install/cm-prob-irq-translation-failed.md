---
title: CM\_PROB\_IRQ\_TRANSLATION\_FAILED
description: CM\_PROB\_IRQ\_TRANSLATION\_FAILED
ms.assetid: fafd40d5-43bf-4243-907a-df523e1b501e
keywords: ["CM_PROB_IRQ_TRANSLATION_FAILED"]
---

# CM\_PROB\_IRQ\_TRANSLATION\_FAILED


## <a href="" id="ddk-cm-prob-irq-translation-failed-dg"></a>


The IRQ translation failed for the device.

### Error Code

36

### Display Message (Windows 2000 and later versions of Windows)

"This device is requesting a PCI interrupt but is configured for an ISA interrupt (or vice versa). Please use the computer's system setup program to reconfigure the interrupt for this device. (Code 36)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

Try using the BIOS setup utility to change settings for IRQ reservations, if such an option exists. (The BIOS might have options to reserve certain IRQs for PCI or ISA devices.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_IRQ_TRANSLATION_FAILED%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




