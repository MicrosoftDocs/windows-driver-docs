---
title: MSiSCSI\_MMIPSECStats WMI Class
description: MSiSCSI\_MMIPSECStats WMI Class
ms.assetid: fda67ca5-58b6-4338-a7c2-b1058bd11a57
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_MMIPSECStats WMI Class


## <span id="ddk_msiscsi_mmipsecstats_wmi_class_kr"></span><span id="DDK_MSISCSI_MMIPSECSTATS_WMI_CLASS_KR"></span>


The MSiSCSI\_MMIPSECStats WMI class exposes the main mode IPsec statistics.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_MMIPSECStats class is defined in *Iscsiprf.mof*.

```cpp
class MSiSCSI_MMIPSECStats : Win32_PerfRawData {
  // instance name is pnp id
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [read, WmiDataId(1),
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("An 
  acquire is a request by the IPsec driver to have internet
    key exchange (IKE) perform a task. The active acquire
    statistic includes the outstanding request and the number
    of any queued requests. Typically, the number of active
    acquires is 1. 
    Under a heavy load, the number of active acquires is 1 
    plus the number of requests that are queued by IKE for 
    processing."): amended, 
    cpp_quote(
    "// An acquire is a request by the IPsec driver to have 
    IKE perform a task. The active acquire statistic 
    includes the outstanding request and the number of any 
    queued requests. Typically, the number of active 
    acquires is 1. Under a heavy load, the number of active 
    acquires is 1 plus the number of requests that are queued 
    by IKE for processing.")] 
    uint64  ActiveAcquire;
  [read, WmiDataId(2), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of IKE messages received that are queued for 
    processing.") : amended, 
    cpp_quote("// The number of IKE messages received that 
    are queued for processing.")] 
    uint64  ActiveReceive;
  [read, WmiDataId(3), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of times that an acquire has failed.") : amended,
    cpp_quote(
    "// The number of times that an acquire has failed.")] 
    uint64  AcquireFailures;
  [read, WmiDataId(4),
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of times that the TCP stack has failed when 
    receiving IKE messages.") : amended,
    cpp_quote(
    "// The number of times that the TCP stack has failed 
    when receiving IKE messages.")] 
    uint64  ReceiveFailures;
  [read, WmiDataId(5), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of times that the TCP/IP stack has failed when 
    sending IKE messages.") : amended, 
    cpp_quote(
    "// The number of times that the TCP/IP stack has failed 
    when sending IKE messages.")] 
    uint64  SendFailures;
  [read, WmiDataId(6), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of entries in the acquire heap, which stores 
    active acquires. This number increases under a heavy 
    load and then gradually decreases over time, as the 
    acquire heap is cleared.") : amended,
    cpp_quote(
    "// The number of entries in the acquire heap, which 
    stores active acquires. This number increases under a 
    heavy load and then gradually decreases over time, as 
    the acquire heap is cleared.")] 
    uint64  AcquireHeapSize;
  [read, WmiDataId(7), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of entries in the IKE receive buffers for 
    incoming IKE messages.") : amended, 
    cpp_quote(
    "// The number of entries in the IKE receive buffers for 
    incoming IKE messages.")] 
    uint64  ReceiveHeapSize;
  [read, WmiDataId(8), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of negotiation failures that occurred during main 
    mode (also known as Phase I) or quick mode (also known 
    as Phase II) negotiation.") : amended, 
    cpp_quote(
    "// The total number of negotiation failures that 
    occurred during main mode (also known as Phase I) or 
    quick mode (also known as Phase II) negotiation.")] 
    uint64  NegotiationFailures;
  [read, WmiDataId(9), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of identity authentication failures (Kerberos, 
    certificate, and preshared key) that occurred during 
    main mode negotiation.") : amended, 
    cpp_quote(
    "// The total number of identity authentication failures 
    (Kerberos, certificate, and preshared key) that occurred 
    during main mode negotiation.")] 
    uint64  AuthenticationFailures;
  [read, WmiDataId(10), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("A cookie 
    is a value contained in a received IKE message that is 
    used by IKE to find the state of an active main mode. A 
    cookie in a received IKE message that cannot be matched 
    with an active main mode is invalid.") : amended,
    cpp_quote(
    "// A cookie is a value contained in a received IKE 
    message that is used by IKE to find the state of an 
    active main mode. A cookie in a received IKE message 
    that cannot be matched with an active main mode is 
    invalid.")] 
    uint64  InvalidCookiesReceived;
  [read, WmiDataId(11), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of requests submitted by IKE to obtain a unique 
    Security Parameters Index (SPI).") : amended,
    cpp_quote(
    "// The total number of requests submitted by IKE to 
    obtain a unique Security Parameters Index (SPI).")] 
    uint64  TotalGetSPI;
  [read, WmiDataId(12), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of outbound quick mode security associations 
    (SAs) added by IKE ") : amended,
    cpp_quote(
    "// The number of outbound quick mode security 
    associations (SAs) added by IKE ")] 
    uint64  KeyAdditions;
  [read, WmiDataId(13), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of inbound quick mode security associations (SAs) 
    added by IKE ") : amended, 
    cpp_quote(
    "// The number of inbound quick mode security 
    associations (SAs) added by IKE ")] 
    uint64  KeyUpdates;
  [read, WmiDataId(14), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of requests submitted by IKE to obtain a unique 
    Security Parameters Index (SPI) that failed.") : 
    amended, 
    cpp_quote(
    "// The total number of requests submitted by IKE to 
    obtain a unique Security Parameters Index (SPI) that 
    failed.")] 
    uint64  GetSPIFailures;
  [read, WmiDataId(15), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of outbound quick mode security associations 
    (SAs) submitted by IKE that failed") : amended,
    cpp_quote(
    "// The number of outbound quick mode security 
    associations (SAs) submitted by IKE that failed")] 
    uint64  KeyAdditionFailures;
  [read, WmiDataId(16), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of inbound quick mode security associations (SAs) 
    added by IKE ") : amended,
    cpp_quote(
    "// The number of inbound quick mode security 
    associations (SAs) added by IKE ")] 
    uint64  KeyUpdateFailures;
  [read, WmiDataId(17), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of quick mode state entries.") : amended,
    cpp_quote(
    "// The number of quick mode state entries.")] 
    uint64  ConnectionListSize;
  [read, WmiDataId(18), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of successful SAs created during main mode 
    negotiations.") : amended, 
    cpp_quote(
    "// The total number of successful SAs created during 
    main mode negotiations.")] 
    uint64  OakleyMainMode;
  [read, WmiDataId(19), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of successful SAs created during quick mode 
    negotiations") : amended, 
    cpp_quote(
    "// The total number of successful SAs created during 
    quick mode negotiations")] 
    uint64  OakleyQuickMode;
  [read, WmiDataId(20), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The 
    number of received IKE messages that are invalid, 
    including IKE messages with invalid header fields, 
    incorrect payload lengths, and incorrect values for the 
    responder cookie (when it should be set to 0). ") : 
    amended, 
    cpp_quote(
    "// The number of received IKE messages that are 
    invalid, including IKE messages with invalid header 
    fields, incorrect payload lengths, and incorrect values 
    for the responder cookie (when it should be set to 
    0).")] 
    uint64  InvalidPackets;
  [read, WmiDataId(21), 
    CounterType(PERF_COUNTER_LARGE_RAWCOUNT), 
    DefaultScale(0), PerfDetail(100), Description("The total 
    number of negotiations that resulted in the use of 
    plaintext (also known as soft SAs). This typically 
    reflects the number of associations formed with 
    computers that did not respond to main mode negotiation 
    attempts. This can include both non-IPsec-aware 
  computers and IPsec-aware computers that do not have 
    IPsec policy to negotiate security with this IPsec 
    peer.") : amended, 
    cpp_quote(
    "// The total number of negotiations that resulted in 
    the use of plaintext (also known as soft SAs). This 
    typically reflects the number of associations formed 
    with computers that did not respond to main mode 
    negotiation attempts. This can include both non-IPsec-
    aware computers and IPsec-aware computers that do not 
    have IPsec policy to negotiate security with this IPsec 
    peer.")] 
    uint64  SoftAssociations;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_MMIPSECStats**](https://msdn.microsoft.com/library/windows/hardware/ff563073) data structure.

 

 





