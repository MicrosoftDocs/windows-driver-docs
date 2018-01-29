---
title: HBAFCPBindingEntry2 WMI Class
description: HBAFCPBindingEntry2 WMI Class
ms.assetid: b9423b59-1d55-4487-bebb-e3eb786fc1be
---

# HBAFCPBindingEntry2 WMI Class


## <span id="ddk_hbafcpbindingentry2_wmi_class_kr"></span><span id="DDK_HBAFCPBINDINGENTRY2_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the HBAFCPBindingEntry2 class to define a binding between the information that the operating system uses to identify a logical unit on a SCSI device and the Fibre Channel protocol (FCP) identifier for the logical unit. For an explanation of the FCP, see the T11 committee's *dpANS Fibre Channel Protocol for SCSI* specification. For an explanation of this binding between SCSI and FCP identifiers, see the T11 committee's *Fibre Channel HBA API* specification.

The HBAFCPBindingEntry2 class is defined as follows in *Hbaapi.mof*:

```
class HBAFCPBindingEntry2 {
  [WmiDataId(1), HBA_BIND_TYPE_QUALIFIERS] HBA_BIND_TYPE  Type;
  [HBAType("HBA_FCPSCSIENTRY"), WmiDataId(4)] HBAScsiID  ScsiId;
  [HBAType("HBA_FCID"), WmiDataId(2)] HBAFCPID  FCPId;
  [HBAType("HBA_LUID"), WmiDataId(3)] uint8  Luid[256];
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**HBAFCPBindingEntry2**](https://msdn.microsoft.com/library/windows/hardware/ff556035)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20HBAFCPBindingEntry2%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




