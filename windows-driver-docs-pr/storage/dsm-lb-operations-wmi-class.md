---
title: DSM\_LB\_Operations WMI Class
description: DSM\_LB\_Operations WMI Class
ms.assetid: 67f040ea-4be6-49b7-8476-abb39ad90548
---

# DSM\_LB\_Operations WMI Class


An MPIO driver uses the MPIO\_WMI\_METHODS WMI class to provide various services to WMI clients. MPIO publishes the MPIO\_WMI\_METHODS WMI class but expects the DSM to register the GUID and handle its implementation.

This WMI class has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following sections describe these methods and their accompanying structures:

[**DsmSetLoadBalancePolicy**](dsmsetloadbalancepolicy.md)

[**DsmSetLoadBalancePolicyALUA**](dsmsetloadbalancepolicyalua.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DSM_LB_Operations%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




