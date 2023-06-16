---
title: HFP device removal
description: Learn about the process and consequences of removing a Bluetooth hands-free profile (HFP) device from an audio system.
ms.date: 04/20/2017
---

# HFP device removal

This article discusses what how the audio driver should respond when when a Bluetooth hands-free profile (HFP) device is removed from (leaves) the audio system.

To remove the registered device interface for a paired HFP device, follow these steps:

1. Cancel any pending IOCTL_BTHHFP_SPEAKER_GET_VOLUME_STATUS_UPDATE IOCTLs.
2. Cancel any pending IOCTL_BTHHFP_STREAM_GET_STATUS_UPDATE IOCTLs.
3. Cancel any pending IOCTL_BTHHFP_DEVICE_GET_CONNECTION_STATUS_UPDATE IOCTLs.
4. De-reference the HFP FileObject (which also de-references the DeviceObject).
5. Select KsDeleteFilterFactory to remove the filter factory representing the HFP device associated with the removed interface.

## Related topics

[Theory of Bluetooth bypass audio streaming](theory-of-operation.md)
