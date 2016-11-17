---
title: Supporting DMA in 64-Bit AVStream Drivers
author: windows-driver-content
description: Supporting DMA in 64-Bit AVStream Drivers
MS-HAID:
- 'avsover\_29f43ebf-2694-40c2-b4d4-a04f98b4f87e.xml'
- 'stream.supporting\_dma\_in\_64\_bit\_avstream\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1173a83f-8d9e-4678-bfb5-f2fb91e827be
keywords: ["AVStream WDK , hardware", "hardware WDK AVStream", "DMA services WDK AVStream", "Direct Memory Access WDK AVStream", "64-bit WDK AVStream", "32-bit addressable devices WDK AVStream"]
---

# Supporting DMA in 64-Bit AVStream Drivers


## <a href="" id="ddk-supporting-dma-in-64-bit-avstream-drivers-ksg"></a>


AVStream supports DMA on 32-bit and 64-bit addressable devices.

All drivers compiled for Win64 platforms should use [**IKsDeviceFunctions::RegisterAdapterObjectEx**](https://msdn.microsoft.com/library/windows/hardware/ff559852) instead of [**KsDeviceRegisterAdapterObject**](https://msdn.microsoft.com/library/windows/hardware/ff561687).

**IKsDeviceFunctions::RegisterAdapterObjectEx** is only available in Microsoft Windows Server 2003 SP1 and later.

The following code example illustrates how to support DMA on both the x64-based client release and 32-bit platforms:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Supporting%20DMA%20in%2064-Bit%20AVStream%20Drivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


