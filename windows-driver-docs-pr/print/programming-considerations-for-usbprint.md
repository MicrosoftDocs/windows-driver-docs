---
title: Programming Considerations for USBPRINT
author: windows-driver-content
description: Programming Considerations for USBPRINT
ms.assetid: 351b3124-d584-4817-a5ce-09e16b54d41b
keywords:
- printer drivers WDK , USB
- USBPRINT
- USBMON
- USB printers WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Programming Considerations for USBPRINT


## <a href="" id="ddk-programming-considerations-for-usbprint-gg"></a>


Usbprint.sys, together with USBMON, provides an interface very similar to that used by parallel printers. In many cases, it is possible for a single printer driver or language monitor to work correctly on both parallel and USB printers without modification. If a language monitor uses only the [**WritePort**](https://msdn.microsoft.com/library/windows/hardware/ff563792) and [**ReadPort**](https://msdn.microsoft.com/library/windows/hardware/ff561909) functions and the [**IOCTL\_PAR\_QUERY\_DEVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff544076) request, it will be portable between USB and parallel printers.

In some cases, it might be necessary for a language monitor to make vendor-specific requests to a printer in order to take advantage of special printer features. To do this, use [**IOCTL\_USBPRINT\_VENDOR\_SET\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff551817) and [**IOCTL\_USBPRINT\_VENDOR\_GET\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff551815). Note, however, that using these IOCTLs renders a language monitor incompatible with the parallel port monitor.

Language monitors normally do not have access to a device handle for the printer they are managing. Instead, they have a port name provided by the port monitor that sits between the language monitor and the bus driver (Usbprint.sys in this case). See [Language and Port Monitor Interaction](language-and-port-monitor-interaction.md) for more information. The lack of a device handle prevents language monitors from directly calling device bus driver IOCTLs. To overcome this limitation, USBMON implements the [**GetPrinterDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff550506) API, which allows language monitors to issue IOCTLs through USBMON to USBPRINT.

The USB printing stack shares the following APIs and IOCTL with the parallel printing stack:

[**WritePort**](https://msdn.microsoft.com/library/windows/hardware/ff563792)

[**ReadPort**](https://msdn.microsoft.com/library/windows/hardware/ff561909)

[**IOCTL\_PAR\_QUERY\_DEVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff544076)

The following IOCTLs are specific to the USB printing stack:

[**IOCTL\_USBPRINT\_GET\_1284\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551803)

[**IOCTL\_USBPRINT\_GET\_LPT\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff551809)

[**IOCTL\_USBPRINT\_SOFT\_RESET**](https://msdn.microsoft.com/library/windows/hardware/ff551810)

[**IOCTL\_USBPRINT\_VENDOR\_GET\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff551815)

[**IOCTL\_USBPRINT\_VENDOR\_SET\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff551817)

**Note**   Usbprint.sys does not provide a mechanism for obtaining descriptors from the device, nor for directly manipulating USB pipes.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Programming%20Considerations%20for%20USBPRINT%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


