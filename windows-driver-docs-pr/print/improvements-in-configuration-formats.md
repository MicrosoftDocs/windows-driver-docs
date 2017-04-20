---
title: Improvements in Configuration Formats
author: windows-driver-content
description: Configuration formats in v4 printer drivers have been improved to allow control over copy count and punctuation substitutions.
ms.assetid: 66FC6BAF-26DD-4E18-B8C9-0BF494346917
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Improvements in Configuration Formats


Configuration formats in v4 printer drivers have been improved to allow control over copy count and punctuation substitutions.

**Copy count**

If a GPD-based printer driver uses an XPS-to-PCL6 rendering filter but does not support hardware copies, it must specify the **\*HardwareCopies** directive to implement control over copy count. If the directive is set to ON, or not specified, this instructs the filter to send the appropriate PCL6 commands for hardware copies to the device, to handle multiple copies. Otherwise, if the directive is set to OFF, the filter will generate software copies.

**No punctuation substitutions**

Due to historical implementations using v3 printer drivers, some devices may require punctuation characters such as a period (.) or a hyphen (-) to be used in PrintCapabilities and PrintTicket implementations. The default behavior is that character substitutions will continue to occur. To configure punctuation character substitution, specify the following, root level attributes:

| File type | Directive                      | Required value |
|-----------|--------------------------------|----------------|
| GPD       | \*NoPunctuationCharSubstitute? | True           |
| PPD       | \*MSPunctuationCharSubstitute  | True           |

 

## Related topics
[V4 Driver Configuration](v4-driver-configuration.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Improvements%20in%20Configuration%20Formats%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


