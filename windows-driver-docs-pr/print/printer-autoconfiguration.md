---
title: Printer Autoconfiguration
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Autoconfiguration


In versions of the Windows operating system prior to Windows Vista, the settings of a print queue are set initially to the driver's default settings, rather than to settings appropriate for the device. For Unidrv and Pscript5 drivers, this means that default values specified in the [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) or [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) file are always used for the initial print queue setup. This static set of defaults must represent the minimum configuration that a printer can be shipped with. For instance, if a stapling unit is optional for a device, then such a device cannot have stapling capabilities enabled by default. If stapling capabilities were enabled by default, the user interface for devices without the stapling unit would show stapling as an option; a customer who selected the stapling option but found that it did not work would likely be confused or unhappy.

For any device that comes with features not present in the basic model, a user or administrator must manually configure these features on the print queue after installation. This can, at times, be a confusing and non-intuitive process. The configuration process is easy to get wrong, particularly with regard to internal parameters such as memory and hard disk size, which can significantly affect printing speed and quality.

Autoconfiguration can solve this problem by automatically configuring the print queue according to the installable features of the device, rather than simply using the driver's default settings.

The main target for autoconfiguration is network printers as they are the most likely to have multiple optional features and require more configuration. If autoconfiguration was not used, the user needs to perform this configuration manually.

[Autoconfiguration Details](autoconfiguration-details.md)

[Autoconfiguration Implementation Options](autoconfiguration-implementation-options.md)

 

 




