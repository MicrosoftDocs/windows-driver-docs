---
title: In-Box Support for Autoconfiguration
author: windows-driver-content
description: In-Box Support for Autoconfiguration
MS-HAID:
- 'autocfg\_124e7bcd-5b91-43f6-8953-5d3bf20fabab.xml'
- 'print.in\_box\_support\_for\_autoconfiguration'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cd2faef4-96ba-4d11-99f6-90e41ae2e283
keywords: ["autoconfiguration WDK printer , in-box support", "printer autoconfiguration WDK printer , in-box support", "in-box autoconfiguration support WDK printer", "in-box autoconfiguration support WDK printer , about in-box autoconfiguration support"]
---

# In-Box Support for Autoconfiguration


In Windows Vista, Unidrv-based and Pscript5-based drivers using the standard TCP/IP port monitor or the Web Services for Devices (WSD) port monitor provide support for autoconfiguration. Note that autoconfiguration support in Windows Vista is provided only for queries about installable features, such as those concerned with the duplex unit or the font cartridge. For a given feature, the response to the query can concern only one option of the feature. A query about whether the duplex unit is installed would elicit one of two responses: that the duplex unit was installed or that it was not. A query about which font cartridge is installed would generate a response indicating either that font cartridge *A* was installed or that font cartridge *B* was installed.

The current (version 1) implementation of autoconfiguration does not allow for multiple responses. A query is limited to a single option of a feature. This means, for example, that a response to a query cannot provide information about both the media size and media color in an input tray.

The following topics describe how to take advantage of the in-box support for autoconfiguration in Windows Vista:

[Printer Minidriver Changes](printer-minidriver-changes.md)

[Customizing the Printer Port Monitors](customizing-the-printer-port-monitors.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20In-Box%20Support%20for%20Autoconfiguration%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


