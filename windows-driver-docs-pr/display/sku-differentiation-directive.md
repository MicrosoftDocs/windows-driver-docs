---
title: SKU differentiation directive
description: With Windows Server 2008 and Windows Vista SP1, the in-box display driver INFs were modified to include a new value that represented the drivers as Client Only, meaning that the drivers would not install on server SKUs of Windows.
ms.assetid: 9E31BD57-41B6-40DF-AF27-8EAC66BDFE09
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SKU differentiation directive


With Windows Server 2008 and Windows Vista SP1, the in-box display driver INFs were modified to include a new value that represented the drivers as *Client Only*, meaning that the drivers would not install on server SKUs of Windows. This directive is required for all display drivers in Windows 8.

In Windows Vista before SP1, the following values were used:

``` syntax
X86:
[Manufacturer]
%ATI% = ATI.Mfg

[ATI.Mfg]

In Vista SP1\Server 2008 the following values were used; 
X86:
[Manufacturer]
%ATI% = ATI.Mfg,NTx86...1

[ATI.Mfg.NTx86...1]

X64:
[Manufacturer]
%ATI% = ATI.Mfg,NTamd64...1

[ATI.Mfg.NTamd64...1]
```

For Windows 8, the same values that were used for Windows Vista SP1 and Windows Server 2008 are used.

## <span id="SKU_differentiation_for_device_drivers__"></span><span id="sku_differentiation_for_device_drivers__"></span><span id="SKU_DIFFERENTIATION_FOR_DEVICE_DRIVERS__"></span>SKU differentiation for device drivers


independent hardware vendors (IHVs) can use ProductType INF values to indicate that a given INF is valid for server or client platforms only. This works on Windows XP and later operating systems, and the changes are relatively simple to implement.

Therefore, even if a client-only driver package exists in the driver store of a server system, that driver is not installable.

The [**INF Manufacturer Section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) topic shows how to add *TargetOSVersion* to filter device installations based on various criteria. One of these criteria is *ProductType*, which can be used to specify a category of SKUs on which the package can be installed. The following values are defined for *ProductType*:

``` syntax
0x0000001 (VER_NT_WORKSTATION)
0x0000002 (VER_NT_DOMAIN_CONTROLLER)
0x0000003 (VER_NT_SERVER) 
```

For any given architecture, a typical INF is decorated to install on any SKU in the following way:

``` syntax
[Manufacturer]
%MSFT%=Models,amd64

[Models.NTamd64]
<models entries>

In order to restrict this INF to install on client only, you need to add a ProductType of â€œ1â€ to the decoration. The number may be expressed as decimal or hexadecimalâ€¦ the documentation shows hexadecimal, but I will use decimal in the example for simplicity.

[Manufacturer]
%MSFT%=Models,amd64...1

; models section for workstation
[Models.NTamd64...1]
<models entries>

For server, the syntax breaks it down to install on a client and a plain server. Each of these has its own product typeâ€¦ unfortunately the INF syntax needs you to specify both to cover both cases. Thus you need to duplicate the entire models section to really cover the server SKU:

[Manufacturer]
%MSFT%=Models,amd64...1amd64...3

; models section for client
[Models.NTamd64...1]
IHV_DeviceName.XXX = â€œFoo Generic Device Name (Microsoft Corporation â€“ WDDM v1.2)â€
IHV_DeviceName.YYY = â€œFoo Enthusiast Device Name (Microsoft Corporation â€“ WDDM v1.2)â€
<models entries>

; models section for Server
[Models.NTamd64...3]
IHV_DeviceName.XXX = â€œFoo Generic Name (Microsoft Corporation â€“ WDDM v1.2)â€
IHV_DeviceName.ZZZ = â€œFoo Datacenter Name (Microsoft Corporation â€“ WDDM v1.2)â€
<models entries>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20SKU%20differentiation%20directive%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




