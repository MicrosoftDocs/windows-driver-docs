---
title: MSiSCSI\_QMIPSECStats WMI Class
description: MSiSCSI\_QMIPSECStats WMI Class
ms.assetid: 81a21c25-5f03-4ad0-a892-3947d65975d2
---

# MSiSCSI\_QMIPSECStats WMI Class


## <span id="ddk_msiscsi_qmipsecstats_wmi_class_kr"></span><span id="DDK_MSISCSI_QMIPSECSTATS_WMI_CLASS_KR"></span>


The MSiSCSI\_MMIPSECStats WMI class exposes quick-mode IPsec statistics for iSCSI HBAs.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_MMIPSECStats class is defined in *Iscsiprf.mof*.

```
class MSiSCSI_QMIPSECStats : Win32_PerfRawData {
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [read, WmiDataId(1), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of active IPsec SAs"): amended, 
    cpp_quote(
    "// The number of active IPsec SAs")] 
    uint64  ActiveSA;
  [read, WmiDataId(2), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of IPsec key operations in progress"): amended, 
    cpp_quote("
    // The number of IPsec key operations in progress")] 
    uint64  PendingKeyOperations;
  [read, WmiDataId(3), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of successful IPsec SA negotiations"): amended, 
    cpp_quote(
    "// The total number of successful IPsec SA 
    negotiations")] 
    uint64  KeyAdditions;
  [read, WmiDataId(4), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of key deletions for IPsec SA"): amended, 
    cpp_quote("// The total number of key deletions for 
    IPsec SA")] 
    uint64  KeyDeletions;
  [read, WmiDataId(5), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of rekey operations for IPsec SAs."): amended, 
    cpp_quote("
    // The number of rekey operations for IPsec SAs.")] 
    uint64  ReKeys;
  [read, WmiDataId(6),
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of active IPsec tunnels."): amended, 
    cpp_quote(
    "// The number of active IPsec tunnels.")] 
    uint64  ActiveTunnels;
  [read, WmiDataId(7), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of packets for which the Security Parameters 
    Index (SPI) was incorrect."): amended, 
    cpp_quote(
    "// The total number of packets for which the Security 
    Parameters Index (SPI) was incorrect.")] 
    uint64  BadSPIPackets;
  [read, WmiDataId(8), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of packets that failed decryption."): amended, 
    cpp_quote(
    "// The total number of packets that failed 
    decryption.")] 
    uint64  PacketsNotDecrypted;
  [read, WmiDataId(9), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of packets for which data could not be verified. 
    "): amended, 
    cpp_quote(
    "// The total number of packets for which data could not 
    be verified. ")] 
    uint64  PacketsNotAuthenticated;
  [read, WmiDataId(10), 
    CounterType(PERF_COUNTER_BULK_COUNT),
    DefaultScale(0), 
    PerfDetail(100), Description("The total number of 
    packets that contained a valid Sequence Number field."): 
    amended, 
    cpp_quote(
    "// The total number of packets that contained a valid 
    Sequence Number field.")] 
    uint64  PacketsWithReplayDetection;
  [read, WmiDataId(11), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes sent 
    using the ESP protocol."): amended, 
    cpp_quote(
    "// The number of bytes sent using the ESP protocol.")] 
    uint64  ConfidentialBytesSent;
  [read, WmiDataId(12), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes 
    received using the ESP protocol."): amended, 
    cpp_quote(
    "// The number of bytes received using the ESP 
    rotocol.")] 
    uint64  ConfidentialBytesReceived;
  [read, WmiDataId(13), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes sent 
    using the AH protocol."): amended, 
    cpp_quote(
    "// The number of bytes sent using the AH protocol.")] 
    uint64  AuthenticatedBytesSent;
  [read, WmiDataId(14), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes 
    received using the AH protocol."): amended, cpp_quote(
    "// The number of bytes received using the AH 
    rotocol.")] 
    uint64  AuthenticatedBytesReceived;
  [read, WmiDataId(15), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes sent 
    using the IPsec protocol."): amended, 
    cpp_quote(
    "// The number of bytes sent using the IPsec 
    rotocol.")] 
    uint64  TransportBytesSent;
  [read, WmiDataId(16), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes 
    received using the IPsec protocol."): amended, 
    cpp_quote(
    "// The number of bytes received using the IPsec
    protocol.")] 
    uint64  TransportBytesReceived;
  [read, WmiDataId(17), 
    CounterType(PERF_COUNTER_BULK_COUNT),
    DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes sent 
    using the IPsec tunnel mode."): amended, 
    cpp_quote(
    "// The number of bytes sent using the IPsec tunnel 
    node.")] 
    uint64  TunnelBytesSent;
  [read, WmiDataId(18), 
    CounterType(PERF_COUNTER_BULK_COUNT), DefaultScale(0), 
    PerfDetail(100), Description("The number of bytes 
    received using the IPsec tunnel mode."): amended, 
    cpp_quote(
    "// The number of bytes received using the IPsec tunnel 
    node.")] 
    uint64  TunnelBytesReceived;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_QMIPSECStats**](https://msdn.microsoft.com/library/windows/hardware/ff563102) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_QMIPSECStats%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




