---
title: SKU differentiation directive
description: With Windows Server 2008 and Windows Vista SP1, the in-box display driver INFs were modified to include a new value that represented the drivers as Client Only, meaning that the drivers would not install on server SKUs of Windows.
ms.assetid: 9E31BD57-41B6-40DF-AF27-8EAC66BDFE09
ms.date: 04/20/2017
ms.localizationpriority: medium
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
```

In order to restrict this INF to install on client only, you need to add a ProductType of "1" to the decoration. The number may be expressed as decimal or hexadecimal. The documentation shows hexadecimal, but I will use decimal in the example for simplicity.

``` syntax
[Manufacturer]
%MSFT%=Models,amd64...1

; models section for workstation
[Models.NTamd64...1]
<models entries>
```

For server, the syntax breaks it down to install on a client and a plain server. Each of these has its own product type. Unfortunately the INF syntax needs you to specify both to cover both cases. Thus you need to duplicate the entire models section to really cover the server SKU:

``` syntax
[Manufacturer]
%MSFT%=Models,amd64...1amd64...3

; models section for client
[Models.NTamd64...1]
IHV_DeviceName.XXX = "Foo Generic Device Name (Microsoft Corporation - WDDM v1.2)"
IHV_DeviceName.YYY = "Foo Enthusiast Device Name (Microsoft Corporation - WDDM v1.2)"
<models entries>

; models section for Server
[Models.NTamd64...3]
IHV_DeviceName.XXX = "Foo Generic Name (Microsoft Corporation - WDDM v1.2)"
IHV_DeviceName.ZZZ = "Foo Datacenter Name (Microsoft Corporation - WDDM v1.2)"
<models entries>
```

 

 





