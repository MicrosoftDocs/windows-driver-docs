---
title: ACX reference documentation
description: This topic provides a high level overview of the ACX reference documentation.
ms.date: 04/19/2023
ms.localizationpriority: medium
---

# ACX reference documentation

>[!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This topic describes the header level reference documentation for the ACX audio class extensions.

For a general overview of ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md). ACX is based on the Windows Driver Framework (WDF) and WDF reference topics can also be useful when looking at the functions and callbacks in ACX. For more information about WDF see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

The following ACX headers have reference documentation available.

Just like WDF drivers, DEVICE and DRIVER are used to initialize the base driver.

- [acxdevice.h](/windows-hardware/drivers/ddi/acxdevice/)
- [acxdriver.h](/windows-hardware/drivers/ddi/acxdriver/)

Pins, streams and circuits are used to route audio signals.

- [acxpin.h](/windows-hardware/drivers/ddi/acxpin/)
- [acxstreams.h](/windows-hardware/drivers/ddi/acxstreams/)
- [acxcircuit.h](/windows-hardware/drivers/ddi/acxcircuit/)
- [acxtargets.h](/windows-hardware/drivers/ddi/acxtargets/)

The data formats are controlled using this header.

- [acxdataformat.h](/windows-hardware/drivers/ddi/acxdataformat/)

The acxelements header provides access to specific audio system elements, such as volume, mute, peakmeter and the keyword spotter.

- [acxelements.h](/windows-hardware/drivers/ddi/acxelements/)

Events and requests allow for notification.

- [acxevents.h](/windows-hardware/drivers/ddi/acxevents/)
- [acxrequest.h](/windows-hardware/drivers/ddi/acxrequest/)

An object bag, which can be used to store and retrieve configuration information and is defined in acxmisc.

- [acxmisc.h](/windows-hardware/drivers/ddi/acxmisc/)

The ACX manager is used for supporting composite audio endpoints. 

- [acxmanager.h](/windows-hardware/drivers/ddi/acxmanager/)

## See also

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[Summary of ACX objects](acx-summary-of-objects.md)

[ACX version information](acx-version-overview.md)

[ACX logging and debugging](acx-logging-and-debugging.md)

[ACX targets and driver synchronization](acx-targets.md)

[ACX IO request packet IRPs](acx-irps.md)

[ACX device enumeration](acx-device-enumeration.md)

[ACX power management](acx-power-management.md)

[ACX multi stack cross driver communications](acx-multi-stack.md)

[ACX streaming](acx-streaming.md)
