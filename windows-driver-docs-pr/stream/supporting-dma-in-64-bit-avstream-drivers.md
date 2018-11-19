---
title: Supporting DMA in 64-Bit AVStream Drivers
description: Supporting DMA in 64-Bit AVStream Drivers
ms.assetid: 1173a83f-8d9e-4678-bfb5-f2fb91e827be
keywords:
- AVStream WDK , hardware
- hardware WDK AVStream
- DMA services WDK AVStream
- Direct Memory Access WDK AVStream
- 64-bit WDK AVStream
- 32-bit addressable devices WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting DMA in 64-Bit AVStream Drivers





AVStream supports DMA on 32-bit and 64-bit addressable devices.

All drivers compiled for Win64 platforms should use [**IKsDeviceFunctions::RegisterAdapterObjectEx**](https://msdn.microsoft.com/library/windows/hardware/ff559852) instead of [**KsDeviceRegisterAdapterObject**](https://msdn.microsoft.com/library/windows/hardware/ff561687).

**IKsDeviceFunctions::RegisterAdapterObjectEx** is only available in Microsoft Windows Server 2003 SP1 and later.

The following code example illustrates how to support DMA on both the x64-based client release and 32-bit platforms:

```cpp
NTSTATUS MyDeviceStart (...) {
// Get the DMA adapter object and store it in the Context member of the I/O stack location.
Context -> AdapterObject = IoGetDmaAdapter (
Device -> PhysicalDeviceObject,
&DeviceDesc,
&Context -> NumberOfMapRegisters
);

PUNKNOWN DeviceUnk =
KsDeviceGetOuterUnknown (
Device
);

// Register the DMA adapter with AVStream
IKsDeviceFunctions *DeviceFunctions;
NTSTATUS Status = DeviceUnk -> QueryInterface (
__uuidof (IKsDeviceFunctions),
(PVOID *)&DeviceFunctions
);

// Conditionally, call IksDeviceFunctions::RegisterAdapterObjectEx, 
// which will not break downlevel load compatibility.

if (NT_SUCCESS (Status)) {
DeviceFunctions -> RegisterAdapterObjectEx (
Context -> AdapterObject,
&DeviceDesc,
Context -> NumMapRegisters,
MAX_MAPPING,
sizeof (KSMAPPING)
);
DeviceFunctions -> Release ();
}

// If this call fails, call KsDeviceRegisterAdapterObject to
// preserve downlevel load compatibility.
else {
KsDeviceRegisterAdapterObject (
Device,
Context -> AdapterObject,
MAX_MAPPING,
sizeof (KSMAPPING)
);
}
...
```

This code example works on 64-bit as well as 32-bit platforms. If the driver does not find **IKsDeviceFunctions::RegisterAdapterObjectEx**, it still calls **KsDeviceRegisterAdapter**.

In addition, when authoring a 64-bit AVStream driver, minimize the number of concurrent frame locks held. Since AVStream generates scatter/gather mappings when the minidriver first locks frames, your driver might run out of resources if it does not follow this guideline. In particular, if you are writing a driver to run on a Win64 platform with a 32-bit card, increasing the number of simultaneous locks increases the chance that a lock will fail because low memory buffers are a limited resource.

 

 




