---
title: Printer Autoconfiguration
author: windows-driver-content
description: Printer Autoconfiguration
ms.assetid: bbe5e58b-4ca2-4ec2-867e-27765d4f59ab
keywords:
- autoconfiguration WDK printer
- printer autoconfiguration WDK printer
- autoconfiguration WDK printer , about printer autoconfiguration
- printer autoconfiguration WDK printer , about printer autoconfiguration
- print queues WDK , autoconfiguration
- queues WDK printer , autoconfiguration
- automatic printer configuration WDK
- printer configuration WDK , autoconfiguration
- queues WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer Autoconfiguration


In versions of the Windows operating system prior to Windows Vista, the settings of a print queue are set initially to the driver's default settings, rather than to settings appropriate for the device. For Unidrv and Pscript5 drivers, this means that default values specified in the [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) or [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) file are always used for the initial print queue setup. This static set of defaults must represent the minimum configuration that a printer can be shipped with. For instance, if a stapling unit is optional for a device, then such a device cannot have stapling capabilities enabled by default. If stapling capabilities were enabled by default, the user interface for devices without the stapling unit would show stapling as an option; a customer who selected the stapling option but found that it did not work would likely be confused or unhappy.

For any device that comes with features not present in the basic model, a user or administrator must manually configure these features on the print queue after installation. This can, at times, be a confusing and non-intuitive process. The configuration process is easy to get wrong, particularly with regard to internal parameters such as memory and hard disk size, which can significantly affect printing speed and quality.

Autoconfiguration can solve this problem by automatically configuring the print queue according to the installable features of the device, rather than simply using the driver's default settings.

The main target for autoconfiguration is network printers as they are the most likely to have multiple optional features and require more configuration. If autoconfiguration was not used, the user needs to perform this configuration manually.

[Autoconfiguration Details](autoconfiguration-details.md)

[Autoconfiguration Implementation Options](autoconfiguration-implementation-options.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Autoconfiguration%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


