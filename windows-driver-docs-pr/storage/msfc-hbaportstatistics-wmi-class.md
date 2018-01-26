---
title: MSFC\_HBAPortStatistics WMI Class
description: MSFC\_HBAPortStatistics WMI Class
ms.assetid: 275e4a50-6500-4a23-a0ae-ddd232da42f0
---

# MSFC\_HBAPortStatistics WMI Class


## <span id="ddk_msfc_hbaportstatistics_wmi_class_kr"></span><span id="DDK_MSFC_HBAPORTSTATISTICS_WMI_CLASS_KR"></span>


A WMI client uses the MSFC\_HBAPortStatistics class to query an HBA miniport driver for statistics related to a port on the HBA.

The MSFC\_HBAPPortStatistics class is defined as follows in *Hbaapi.mof*:

```
class MSFC_HBAPortStatistics
{
  [ WmiDataId(1) ]
  sint64 SecondsSinceLastReset;
  [ WmiDataId(2) ]
  sint64 TxFrames;
  [ WmiDataId(3) ]
  sint64 TxWords;
  [ WmiDataId(4) ]
  sint64 RxFrames;
  [ WmiDataId(5) ]
  sint64 RxWords;
  [ WmiDataId(6) ]
  sint64 LIPCount;
  [ WmiDataId(7) ]
  sint64 NOSCount;
  [ WmiDataId(8) ]
  sint64 ErrorFrames;
  [ WmiDataId(9) ]
  sint64 DumpedFrames;
  [ WmiDataId(10) ]
  sint64 LinkFailureCount;
  [ WmiDataId(11) ]
  sint64 LossOfSyncCount;
  [ WmiDataId(12) ]
  sint64 LossOfSignalCount;
  [ WmiDataId(13) ]
  sint64 PrimitiveSeqProtocolErrCount;
  [ WmiDataId(14) ]
  sint64 InvalidTxWordCount;
  [WmiDataId(15) ]
  sint64 InvalidCRCCount;
};
```

When compiled by the WMI tool suite this class definition produces the following data structure:

[**MSFC\_HBAPortStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff562512)

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_HBAPortStatistics%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




