---
title: Configurability
author: windows-driver-content
description: In addition to extensibility points available to the NFC client driver, the NFC CX also enables the client driver to configure the parameters of many of its operations. The following configurations can be customized by the NFC client driver.
ms.assetid: 29C6C96E-9F20-4750-ABDD-103871B405FA
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# Configurability


In addition to extensibility points available to the NFC client driver, the NFC CX also enables the client driver to configure the parameters of many of its operations. The following configurations can be customized by the NFC client driver.

-   Driver Flags
-   RF Discovery Configuration
-   LLCP Configuration

## Driver Flags


The NFC CX allows the NFC client driver to provide [**driver flags**](https://msdn.microsoft.com/library/windows/hardware/dn905542) to configure the run-time implementation of the class extension. These flags allow the NFC CX to implement certain standard NCI operation slightly differently, due to different firmware implementations due to ambiguities in the NCI specification.

## RF Discovery Configuration


The RF discovery configuration can be set by the NFC client driver through the [**NfcCxSetRfDiscoveryConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905616) method. The RF discovery configuration should be done during initialization after calling [**NfcCxDeviceInitialize**](https://msdn.microsoft.com/library/windows/hardware/dn905611), otherwise an error is returned.

## LLCP Configuration


The LLCP configuration can be set by the NFC client driver through the [**NfcCxSetLlcpConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905615) method provided by the NFC CX. The LLCP configuration should be done during initialization after [**NfcCxDeviceInitialize**](https://msdn.microsoft.com/library/windows/hardware/dn905611), otherwise an error is returned.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Configurability%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
