---
title: SetCHAPSharedSecret
description: SetCHAPSharedSecret
ms.assetid: d1f1d6f2-154e-4e41-8ebf-4071de4ceafe
---

# SetCHAPSharedSecret


The **SetCHAPSharedSecret** method establishes the shared secret for the initiator to use when it verifies the target's response to the initiator's challenge.

The initiator uses two different shared secrets to implement the challenge handshake authentication protocol (CHAP):

-   The **SetCHAPSharedSecret** method establishes the shared secret that the initiator uses to verify the target's response to the initiator's challenge.

-   The [LoginToTarget](logintotarget.md) method establishes the shared secret that the initiator uses to generate the CHAP response to a target's challenge.

The **SetCHAPSharedSecret** WMI method belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **SetCHAPSharedSecret** method, see the member descriptions for the [**SetCHAPSharedSecret\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565595) and [**SetCHAPSharedSecret\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565600) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class are not required to support **SetCHAPSharedSecret**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SetCHAPSharedSecret%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




