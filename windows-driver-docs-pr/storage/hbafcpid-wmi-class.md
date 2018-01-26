---
title: HBAFCPID WMI Class
description: HBAFCPID WMI Class
ms.assetid: 6b0d0f79-a7a8-4341-955b-2c3068936a1d
---

# HBAFCPID WMI Class


## <span id="ddk_hbafcpid_wmi_class_kr"></span><span id="DDK_HBAFCPID_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the HBAFCPID class to define a Fibre Channel protocol (FCP) identifier for a logical unit. The FCP identifier specifies the name of the machine the logical unit is located on and the HBA port through which it can be accessed.

The miniport driver uses this identifier to construct a binding between the information that the operating system uses to identify a logical unit and the FCP identifier for the logical unit. For information about this kind of binding, see [**HBAFCPBindingEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556034). For an explanation of the Fibre Channel protocol, see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* specification.

The HBAFCPID class is defined as follows in *Hbaapi.mof*:

```
class HBAFCPID {
  [WmiDataId(1)] uint32  Fcid;
  [HBAType("HBA_WWN"), WmiDataId(2)] uint8  NodeWWN[8];
  [HBAType("HBA_WWN"), WmiDataId(3)] uint8  PortWWN[8];
  [WmiDataId(4)] uint64  FcpLun;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**HBAFCPID**](https://msdn.microsoft.com/library/windows/hardware/ff556038)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20HBAFCPID%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




