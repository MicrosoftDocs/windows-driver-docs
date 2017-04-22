---
title: Probing and Locking of Configurations
description: Probing and Locking of Configurations
ms.assetid: 6f68db48-ed4b-487c-b425-43c610651c16
keywords:
- video decoding WDK DirectX VA , configuration probing and locking
- decoding video WDK DirectX VA , configuration probing and locking
- picture decoding WDK DirectX VA , configuration probing and locking
- minimal interoperability configuration set WDK DirectX VA
- locking configurations WDK DirectX VA
- probing configurations WDK DirectX VA
- configuration probing and locking WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Probing and Locking of Configurations


## <span id="ddk_probing_and_locking_of_configurations_gg"></span><span id="DDK_PROBING_AND_LOCKING_OF_CONFIGURATIONS_GG"></span>


The process for establishing the configuration for each DirectX VA function (a specific value of [bDXVA\_Func](bdxva-func-variable.md)) that needs a configuration (for example, compressed picture decoding, alpha-blending data loading, and alpha-blending combination) can be performed by:

1.  Probing (if needed) to determine whether a configuration is accepted by the accelerator.

2.  Locking in a specific configuration, if it is supported.

To determine if a specific configuration is supported, a probing command is sent to the accelerator for the particular *bDXVA\_Func* value to be probed, along with a configuration. In addition to the probing command, a configuration structure (for the value in *bDXVA\_Func*) is sent that describes the configuration being probed to determine whether the configuration is supported. The accelerator then returns a value of S\_OK or S\_FALSE, indicating whether the specified configuration is supported by the accelerator. The accelerator can also return a suggested alternative configuration.

To lock in a specific configuration, a locking command is sent to the accelerator for the particular *bDXVA\_Func* to be locked. Along with the locking command, a configuration structure (for the value in *bDXVA\_Func*) is sent that describes the configuration to be locked in, if the configuration is supported. The accelerator returns an S\_OK or S\_FALSE indicating whether the specified configuration is supported by the accelerator. If the return value is S\_OK, the specified configuration is locked in for use. If the return value is S\_FALSE, a suggested alternative configuration is returned.

The decoder may send a locking command without first sending a probing command for the specified configuration. If the accelerator returns an S\_OK in a probing command for a specific configuration, it returns an S\_OK to a locking command for that same configuration, unless otherwise noted. After a locking command has been sent and the accelerator returns S\_OK, the specified configuration is locked in and no additional probing or locking commands are sent by the decoder for the same value of *bDXVA\_Func*.

To ensure that all DirectX VA software decoders can operate with all DirectX VA accelerators, a [minimal interoperability configuration set](minimal-interoperability-configuration-sets.md) is defined as a set of configurations that must be supported by any decoder using a particular value for *bDXVA\_Func*. Every accelerator that indicates support for the *bDXVA\_Func* variable by exposing an associated video accelerator GUID must support at least one member of this interoperability configuration set. In some cases, an [additional encouraged configuration set](additional-encouraged-configuration-set.md) may also be defined.

The following figure shows the control flow of probing and locking commands sent by the decoder.

![flowchart illustrating probing and locking to set driver configuration](images/probe-lock.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Probing%20and%20Locking%20of%20Configurations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




