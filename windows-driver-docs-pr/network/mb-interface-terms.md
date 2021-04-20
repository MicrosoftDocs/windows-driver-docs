---
title: MB interface terms
description: Provides a list of mobile broadband terminology used in the MB interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Interface Terms


The following terminology is used throughout the Mobile Broadband (MB)documentation:

|Term|Description|
|--- |--- |
|MBIM|Mobile Broadband Interface Model, a USB Device Working Group (DWG) specification for mobile broadband devices.|
|MBIM function|A USB function within a USB device that is compliant with the MBIM specification.|
|Mobile broadband device|A USB device that is either single function or multi-functional. In the single function case, the function should be an MBIM function. In the multi-function case, one of the functions is the MBIM function. This may also be a multi-configuration device in which at least one of the configurations contains the MBIM function.|
|NCM2|The earlier name for the MBIM specification. Some diagrams still refer to the MBIM functions as NCM2 functions.|
|Virtual CD-ROM|A CD-ROM function that does not have a physical CD-ROM drive.|
|IAD|Interface association descriptors (IADs) used to group interfaces into functions.|
|WMC UFD|Union function descriptors (UFDs) described in the Wireless Mobile Communication (WMC) specifications. UFDs are used to group interfaces into functions. This is an alternative to using IADs.|
|Morphing|The ability of a USB device to expose a different set of USB functions than what is currently exposed.|
|Driver|Software required by Windows to work with a USB function.|
|Inbox driver|A driver supplied by Microsoft for USB functions. These drivers are present in Windows.|
|IHV driver|A driver supplied by the independent hardware vendor (IHV) for USB functions that do not have inbox drivers.|
|IHV driver package|A collection of all IHV drivers supplied by the IHV.|
|USBHUB|A Microsoft USB hub driver.|
|USBCCGP|A Microsoft driver for USB composite devices.|
|MBCD|Mobile Broadband Class Driver, the inbox driver in Windows 8 for USB functions that conform to the MBIM specification.|

