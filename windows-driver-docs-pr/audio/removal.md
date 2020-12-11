---
title: HFP Device Removal
description: The HFP device removal topic discusses what happens when a Bluetooth hands-free profile (HFP) device is removed from (leaves) the audio system.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HFP Device Removal


The HFP device removal topic discusses what happens when a Bluetooth hands-free profile (HFP) device is removed from (leaves) the audio system.

To remove the registered device interface for a paired HFP device, the audio driver:

1. Cancels any pending IOCTL\_BTHHFP\_SPEAKER\_GET\_VOLUME\_STATUS\_UPDATE IOCTLs.

2. Cancels any pending IOCTL\_BTHHFP\_STREAM\_GET\_STATUS\_UPDATE IOCTLs.

3. Cancels any pending IOCTL\_BTHHFP\_DEVICE\_GET\_CONNECTION\_STATUS\_UPDATE IOCTLs.

4. De-references the HFP FileObject (which also de-references the DeviceObject).

5. Calls KsDeleteFilterFactory to remove the filter factory that represents the HFP device associated with the removed interface.

## <span id="related_topics"></span>Related topics
[Theory of Operation](theory-of-operation.md)  



