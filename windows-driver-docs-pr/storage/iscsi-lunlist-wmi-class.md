---
title: ISCSI\_LUNList WMI Class
description: ISCSI\_LUNList WMI Class
ms.assetid: 2ad0dabe-54b3-4075-966b-491e078f2c8b
---

# ISCSI\_LUNList WMI Class


## <span id="ddk_iscsi_lunlist_wmi_class_kr"></span><span id="DDK_ISCSI_LUNLIST_WMI_CLASS_KR"></span>


The ISCSI\_LUNList WMI class describes a mapping from a logical unit number (LUN) that the operating system defines locally to be a 64-bit number that, together with the name of the target that the logical unit belongs to, uniquely identifies the logical unit and is globally valid anywhere in the network. This class is defined as follows in *Common.mof*.

```
class ISCSI_LUNList {
  [WmiDataId(1), description("Target LUN") : amended]
    uint64  TargetLUN;
  [WmiDataId(2), description("OS Scsi bus number target
  is mapped to") : amended]
    uint32  OSLUN;
  [WmiDataId(3), description("Reserved") : amended]
    uint32  Reserved;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**ISCSI\_LUNList**](https://msdn.microsoft.com/library/windows/hardware/ff561544) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ISCSI_LUNList%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




