---
title: HFP Device Removal
description: The HFP device removal topic discusses what happens when a Bluetooth hands-free profile (HFP) device is removed from (leaves) the audio system.
ms.assetid: 99B6C09E-2467-4124-9F9A-5116586BB38C
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20HFP%20Device%20Removal%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





