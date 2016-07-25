---
title: Compatible ID
description: A compatible ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.assetid: 3d20b43a-9e2b-4a8d-9a1a-eb9217233405
---

# Compatible ID


A compatible ID is a vendor-defined identification string that Windows uses to match a device to an INF file. A device can have associated with it a list of compatible IDs. The compatible IDs should be listed in order of decreasing suitability. If Windows cannot locate an INF file that matches one of a device's hardware IDs, it uses compatible IDs to locate an INF file. Compatible IDs have the same format as [hardware IDs](hardware-ids.md). However, compatible IDs are typically more generic than hardware IDs.

## <a href="" id="ddk-compatible-ids-dg"></a>


If a vendor ships an INF file that specifies a compatible ID for a [*driver node*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-node), the vendor should make sure that their INF file can support all the hardware that matches the compatible ID.

To obtain a list of compatible IDs for a device, call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) with the *DeviceProperty* parameter set to **DevicePropertyCompatibleID**. The list of compatible IDs that this routine retrieves is a REG\_MULTI\_SZ value. The maximum number of characters in a compatible ID list, including a NULL terminator after each compatible ID and a final NULL terminator, is REGSTR\_VAL\_MAX\_HCID\_LEN. The maximum possible number of IDs in a list of compatible IDs is 64.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Compatible%20ID%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




