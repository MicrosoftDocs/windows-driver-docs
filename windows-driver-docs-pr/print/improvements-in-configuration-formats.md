---
title: Improvements in Configuration Formats
description: Configuration formats in v4 printer drivers have been improved to allow control over copy count and punctuation substitutions.
ms.assetid: 66FC6BAF-26DD-4E18-B8C9-0BF494346917
ms.date: 04/20/2017
ms.localizationpriority: medium
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



