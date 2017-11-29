---
title: KSMETHODSETID\_BdaDeviceConfiguration
description: KSMETHODSETID\_BdaDeviceConfiguration
ms.assetid: a0014869-2ea0-4f55-be3a-da1e624ad61c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSMETHODSETID\_BdaDeviceConfiguration


## <span id="ddk_ksmethodsetid_bdadeviceconfiguration_ks"></span><span id="DDK_KSMETHODSETID_BDADEVICECONFIGURATION_KS"></span>


KSMETHODSETID\_BdaDeviceConfiguration is the BDA device configuration method set. It is used to configure a filter for a filter graph.

The following methods are available:

<span id="KSMETHOD_BDA_CREATE_PIN_FACTORY"></span><span id="ksmethod_bda_create_pin_factory"></span>[**KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY**](ksmethod-bda-create-pin-factory.md)  
Triggers a call that creates a pin factory for the filter.

<span id="KSMETHOD_BDA_DELETE_PIN_FACTORY"></span><span id="ksmethod_bda_delete_pin_factory"></span>[**KSMETHOD\_BDA\_DELETE\_PIN\_FACTORY**](ksmethod-bda-delete-pin-factory.md)  
Triggers a call that deletes a pin factory for the filter.

<span id="KSMETHOD_BDA_CREATE_TOPOLOGY"></span><span id="ksmethod_bda_create_topology"></span>[**KSMETHOD\_BDA\_CREATE\_TOPOLOGY**](ksmethod-bda-create-topology.md)  
Creates a topology structure in Ring 3 that reflects the known connections in the filter.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This method set is implemented on filters.

If a BDA minidriver does not define it's own handlers for the methods in this method set, then the BDA support library will add default handlers when the BDA minidriver calls the **BdaInitFilter** function.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**BdaInitFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556464)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHODSETID_BdaDeviceConfiguration%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




