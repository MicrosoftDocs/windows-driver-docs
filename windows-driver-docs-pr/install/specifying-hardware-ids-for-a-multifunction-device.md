---
title: Specifying Hardware IDs for a Multifunction Device
description: Specifying Hardware IDs for a multifunction device
ms.date: 06/19/2025
ms.topic: concept-article
---

# Specifying Hardware IDs for a multifunction device

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](windows-hardware/drivers/install/driver-package-container-metadata)**.

You can specify more than one **[HardwareID]**(/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) element for a physical device. This is done by specifying multiple **HardwareID** element values within the parent **[HardwareIDList]**(/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) element. Each value must specify a unique [hardware ID](hardware-ids.md) for the device.

For example, consider a single-function USB printer from the company Contoso, Ltd. The following **HardwareID** elements can be used to define the device:

```xml
<HardwareIDList>
  <HardwareID>DOID:USB\VID_1234&PID_1234&REV_0000</HardwareID>
  <HardwareID>DOID:USB\VID_1234&PID_1234</HardwareID>
  <HardwareID>DOID:USBPRINT\Contoso_Ltd_Co9999/HardwareID>
</HardwareIDList>
```

If the device is a multifunction device, a device container combines all the [hardware IDs](hardware-ids.md) from the device nodes (*devnodes*) for each hardware function on the device. For more information about device containers and container IDs, see [Container IDs](container-ids.md).

The following figure shows the relationship between a multifunction device's devnodes and device container.

:::image type="content" source="images/hardwareid.png" alt-text="Diagram illustrating combining hardware IDs from multiple devnodes into a single device container.":::

Depending on your multifunction device, you can decide which [hardware ID](hardware-ids.md) values are specified by using separate **[HardwareID]**(/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) elements in the **[HardwareIDList]**(/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) element. Multiple hardware IDs can be specified in any order in the **HardwareIDList** element. However, you should be aware of the following points:

- Within a given devnode, the ranking of hardware IDs by the operating system is deterministic. For example, in the previous figure, *HardwareID1-1* is always ranked higher than *HardwareID1-2* and *HardwareID1-3*.

- The operating system doesn't consistently rank a hardware ID from one devnode higher than a hardware ID from another devnode. For example, in the previous figure, the operating system might not always rank *HardwareID1-1* higher than *HardwareID2-1*.

Therefore, make sure that your metadata package doesn't rely on the order or ranking of [hardware IDs](hardware-ids.md) across the devnodes for a device. You should use all relevant hardware IDs for your multifunction device in the **[HardwareIDList]**(/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) element of your device metadata package. This guarantees that the operating system selects your metadata package regardless of the ranking of hardware IDs.

Based on the *devnode* topology shown in the previous figure, consider the following suggestions:

- Specify *HardwareID1-1*, *HardwareID2-1*, and *HardwareID3-1* in a new device metadata package if another metadata package that specifies *HardwareID2-1* already exists.

    If the operating system ranks *HardwareID2-1* higher than *HardwareID1-1* and finds that*HardwareID2-1* is specified in both the old and new metadata package, the operating system selects the metadata package based on the value of the **[LastModifiedDate]**(/previous-versions/windows/hardware/metadata/ff548624(v=vs.85)) XML element. In this case, the operating system selects the new metadata package.

- If your new metadata package lists only *HardwareID1-1*, the operating system doesn't select the new package if *HardwareID2-1* is ranked higher than *HardwareID1-1.*

For more information about metadata package selection and ranking, see [How the DMRC Selects a Device Metadata Package](how-the-dmrc-selects-a-device-metadata-package.md).
