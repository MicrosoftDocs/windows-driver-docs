---
title: WDI_TLV_OFFLOAD_SCOPE
description: WDI_TLV_OFFLOAD_SCOPE is a TLV that contains Rx coalesce offload capabilities.
ms.assetid: 2E00659F-4A41-4907-AEA6-92EAFBFF2149
ms.author: windowsdriverdev 
ms.date: 10/05/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_OFFLOAD_SCOPE Network Drivers Starting with Windows Vista
---

# WDI_TLV_OFFLOAD_SCOPE


WDI_TLV_OFFLOAD_SCOPE is a TLV that contains the scope for network offloads.

## TLV Type


0x143

## Length


The size (in bytes) of the below values.

## Values

| Type | Description |
| --- | --- |
| UINT8 | Specifies whether checksum offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
| UINT8 | Specifies whether LsoV1 offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
| UINT8 | Specifies whether LsoV2 offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
| UINT8 | Specifies whether RSC offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
 

## Requirements

| | |
| --- | --- |
| Minimum supported client | Windows 10, version 1709 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_OFFLOAD_SCOPE%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


